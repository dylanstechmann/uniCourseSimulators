import { expect, test, type Page } from "@playwright/test";
import AxeBuilder from "@axe-core/playwright";

// Runs only against the throwaway QA deployment described in docs/QA_PROTECTED_GRADED.md:
// a copy of the content with genetics switched to a graded, protected policy and three QA
// assignments whose keys live in a private store. The committed packages are formative-only,
// so the default Compose stack has nothing for this file to test and it is skipped there.
const enabled = process.env.E2E_PROTECTED_FIXTURE === "1";
const SENTINEL = "QA_PRIVATE_KEY_SENTINEL";
const LEAK_MARKERS = [SENTINEL, "solution_spec", "private://"];

test.skip(
  !enabled,
  "Needs the protected QA fixture (tools/qa/build_protected_fixture.py).",
);

test.afterEach(async ({ page }) => {
  if (!page.url().startsWith("http")) return;
  const deletionStatus = await page.evaluate(async () => {
    const sessionResponse = await fetch("/api/v1/auth/session");
    if (!sessionResponse.ok) return null;
    const session = await sessionResponse.json();
    if (!session.user || !session.csrf_token) return null;
    const deletion = await fetch("/api/v1/learner", {
      method: "DELETE",
      headers: { "X-CSRF-Token": session.csrf_token },
    });
    return deletion.status;
  });
  if (deletionStatus !== null) expect(deletionStatus).toBe(204);
});

function watchForLeaks(page: Page) {
  const leaks: string[] = [];
  page.on("response", async (response) => {
    if (!response.url().includes("/api/")) return;
    let body: string;
    try {
      body = await response.text();
    } catch {
      return;
    }
    for (const marker of LEAK_MARKERS) {
      if (body.includes(marker)) leaks.push(`${marker} in ${response.url()}`);
    }
  });
  return leaks;
}

async function enrollInGradedGenetics(page: Page) {
  await page.goto("/#/account");
  await page.getByRole("button", { name: "Start guest session" }).click();
  await page.getByRole("link", { name: "Course catalog", exact: true }).click();
  await page.getByRole("link", { name: /Genetics & Genomics/ }).click();
  await page.getByRole("button", { name: "Enroll in partial course" }).click();
  await page.getByRole("link", { name: "Practice gradebook" }).click();
}

async function apiCall(
  page: Page,
  path: string,
  method: "GET" | "POST" = "GET",
  body?: unknown,
) {
  return page.evaluate(
    async ({ path, method, body }) => {
      const session = await (await fetch("/api/v1/auth/session")).json();
      const response = await fetch(path, {
        method,
        headers: {
          "Content-Type": "application/json",
          "X-CSRF-Token": session.csrf_token,
        },
        body: body === undefined ? undefined : JSON.stringify(body),
      });
      return { status: response.status, text: await response.text() };
    },
    { path, method, body },
  );
}

test("a learner completes a protected graded assignment without ever receiving its key", async ({
  page,
}) => {
  const leaks = watchForLeaks(page);
  await enrollInGradedGenetics(page);

  const plan = page.getByRole("region", { name: "Course assessment plan" });
  await expect(plan).toContainText("Graded policy configured");
  await plan.getByText("Assessment policies").click();
  await expect(plan).toContainText(
    "Graded questions and keys are kept outside the public repository.",
  );
  const openRow = page.getByRole("row", {
    name: /QA protected homework \(open\)/,
  });
  await expect(openRow).toContainText("open");
  await expect(
    page
      .getByRole("row", { name: /QA protected homework \(past deadline\)/ })
      .getByRole("button", { name: "Open assignment" }),
  ).toBeDisabled();
  await expect(
    page
      .getByRole("row", { name: /QA protected homework \(not yet released\)/ })
      .getByRole("button", { name: "Open assignment" }),
  ).toBeDisabled();

  await openRow.getByRole("button", { name: "Open assignment" }).click();
  const assignment = page.getByRole("region", { name: "Graded assignment" });
  await expect(
    assignment.getByRole("heading", { name: "QA protected homework (open)" }),
  ).toBeVisible();
  await expect(assignment).toContainText("attempts used: 0 of 2");
  const accessibility = await new AxeBuilder({ page })
    .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
    .analyze();
  expect(accessibility.violations).toEqual([]);

  // An incomplete attempt is stopped in the browser and costs no attempt.
  await assignment.getByRole("button", { name: "Submit assignment" }).click();
  await expect(assignment.getByRole("alert")).toContainText(
    "Enter a response for",
  );
  await expect(assignment).toContainText("attempts used: 0 of 2");

  // Attempt 1: wrong control, a number without its unit, and an overclaim.
  await assignment
    .getByRole("radio", {
      name: "Cells given twice the amount of the targeting guide.",
    })
    .check();
  await assignment.getByLabel("Numerical answer").fill("75");
  await assignment
    .getByRole("checkbox", { name: /removed all of the target protein/ })
    .check();
  await assignment.getByRole("button", { name: "Submit assignment" }).click();
  const first = assignment.getByRole("region", { name: "Attempt 1 results" });
  await expect(first.getByRole("heading")).toContainText(
    "Attempt 1: 0 / 6 points",
  );
  await expect(assignment).toContainText("attempts used: 1 of 2");

  // Attempt 2: all correct, with the unit.
  await assignment
    .getByRole("radio", {
      name: "Cells given a non-targeting guide delivered the same way.",
    })
    .check();
  await assignment.getByLabel("Numerical answer").fill("75");
  await assignment.getByLabel("Unit").fill("%");
  await assignment
    .getByRole("checkbox", { name: /depends on loss of the target/ })
    .check();
  await assignment
    .getByRole("checkbox", { name: /argues against an off-target/ })
    .check();
  await assignment.getByRole("button", { name: "Submit assignment" }).click();
  const second = assignment.getByRole("region", { name: "Attempt 2 results" });
  await expect(second.getByRole("heading")).toContainText(
    "Attempt 2: 6 / 6 points",
  );
  await expect(assignment).toContainText("attempts used: 2 of 2");
  await expect(assignment).toContainText(
    "The configured attempt limit has been reached.",
  );
  await expect(
    assignment.getByRole("button", { name: "Submit assignment" }),
  ).toHaveCount(0);

  // The highest attempt (6/6) counts. The past-deadline assignment was never submitted, so it
  // enters the homework category as zero; the unreleased one is excluded: (6 + 0) / 12 = 50%.
  const grade = page.getByRole("region", {
    name: "Current weighted course grade",
  });
  await expect(grade).toContainText("50% under the configured");
  await expect(grade).toContainText("homework: 50%");

  // A learner can ask for one human review of a saved attempt.
  await first
    .getByLabel("Request human review")
    .fill("QA check: I would like a person to look at the unit rule.");
  await first.getByRole("button", { name: "Send for human review" }).click();
  await expect(first.getByLabel("Assignment review status")).toContainText(
    "Human review · open",
  );

  // Everything persists across a reload, and the server still refuses a third attempt.
  await page.reload();
  await page
    .getByRole("row", { name: /QA protected homework \(open\)/ })
    .getByRole("button", { name: "Open assignment" })
    .click();
  const reloaded = page.getByRole("region", { name: "Graded assignment" });
  await expect(reloaded).toContainText("attempts used: 2 of 2");
  await expect(
    reloaded.getByRole("region", { name: "Attempt 2 results" }),
  ).toContainText("6 / 6 points");
  const third = await apiCall(
    page,
    "/api/v1/assessments/genetics/qa-protected-open/submissions",
    "POST",
    {
      responses: {
        "qa-protected-open:control-choice": { response: 1 },
        "qa-protected-open:knockdown-percent": { response: "75", unit: "%" },
        "qa-protected-open:supported-claims": { response: [0, 1] },
      },
    },
  );
  expect(third.status).toBe(409);

  await expect(page.locator("body")).not.toContainText(SENTINEL);
  expect(leaks).toEqual([]);
});

test("past-deadline and unreleased protected assignments refuse questions and submissions", async ({
  page,
}) => {
  const leaks = watchForLeaks(page);
  await enrollInGradedGenetics(page);
  await expect(
    page.getByRole("region", { name: "Course assessment plan" }),
  ).toBeVisible();

  const answers = (prefix: string) => ({
    responses: {
      [`${prefix}:control-choice`]: { response: 1 },
      [`${prefix}:knockdown-percent`]: { response: "75", unit: "%" },
      [`${prefix}:supported-claims`]: { response: [0, 1] },
    },
  });
  const closedSubmission = await apiCall(
    page,
    "/api/v1/assessments/genetics/qa-protected-closed/submissions",
    "POST",
    answers("qa-protected-closed"),
  );
  expect(closedSubmission.status).toBe(409);
  const scheduledQuestions = await apiCall(
    page,
    "/api/v1/assessments/genetics/qa-protected-scheduled/questions",
  );
  expect(scheduledQuestions.status).toBeGreaterThanOrEqual(400);
  const scheduledSubmission = await apiCall(
    page,
    "/api/v1/assessments/genetics/qa-protected-scheduled/submissions",
    "POST",
    answers("qa-protected-scheduled"),
  );
  expect(scheduledSubmission.status).toBeGreaterThanOrEqual(400);
  for (const response of [
    closedSubmission,
    scheduledQuestions,
    scheduledSubmission,
  ]) {
    for (const marker of LEAK_MARKERS)
      expect(response.text).not.toContain(marker);
  }
  const exported = await apiCall(page, "/api/v1/learner/export");
  expect(exported.status).toBe(200);
  for (const marker of LEAK_MARKERS)
    expect(exported.text).not.toContain(marker);
  expect(leaks).toEqual([]);
});
