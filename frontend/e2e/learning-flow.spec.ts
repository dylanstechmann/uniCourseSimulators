import { expect, test } from "@playwright/test";
import AxeBuilder from "@axe-core/playwright";

test("catalog communicates maturity and has no automated accessibility violations", async ({
  page,
}) => {
  await page.goto("/");
  await expect(
    page.getByRole("heading", { name: "Course catalog", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText(/prototype material with uneven depth/),
  ).toBeVisible();
  await expect(
    page.locator(".course-grid .maturity-partial").first(),
  ).toBeVisible();
  const accessibility = await new AxeBuilder({ page })
    .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
    .analyze();
  expect(accessibility.violations).toEqual([]);
});

test("curriculum explorer exposes prerequisite chains and the JHU topic map honestly", async ({
  page,
}) => {
  await page.goto("/");
  const summary = page.getByText(
    "Johns Hopkins regenerative/stem-cell prerequisite knowledge map",
    { exact: true },
  );
  await expect(summary).toBeVisible();
  await summary.click();
  const openPathway = page.locator(".pathway-card[open]");
  await expect(
    openPathway.getByRole("heading", {
      name: "Molecular Biology",
      exact: true,
    }),
  ).toBeVisible();
  await expect(
    openPathway.getByText("catalog-only", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    openPathway
      .getByText(/Original lessons and assessments have not been authored/)
      .first(),
  ).toBeVisible();
  await expect(
    page.getByRole("link", {
      name: /Regenerative and Stem Cell Technologies.*Academic Catalogue/,
    }),
  ).toHaveAttribute("href", /e-catalogue\.jhu\.edu/);
  await expect(
    page.getByRole("link", {
      name: /Open available partial package: Organic Chemistry I for Life Sciences/,
    }),
  ).toHaveAttribute("href", "#/course/organic-chemistry");
  const accessibility = await new AxeBuilder({ page })
    .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
    .analyze();
  expect(accessibility.violations).toEqual([]);
});

test("guest enrollment, feedback, notes, progress, account upgrade and deletion persist correctly", async ({
  page,
}) => {
  await page.goto("/#/account");
  await page.getByRole("button", { name: "Start guest session" }).click();
  await expect(
    page.getByRole("heading", { name: "Guest session", exact: true }),
  ).toBeVisible();
  await page.getByRole("link", { name: "Course catalog", exact: true }).click();
  await page.getByRole("link", { name: /Foundations of Cell/ }).click();
  await page.getByRole("button", { name: "Enroll in partial course" }).click();
  await expect(page.getByText("Enrolled", { exact: true })).toBeVisible();
  const lessonLink = page
    .getByRole("navigation", { name: "Lessons" })
    .getByRole("link")
    .first();
  await lessonLink.click();
  const bilayerPractice = page
    .getByRole("region", { name: "Formative practice" })
    .filter({
      hasText: "Which statements best explain how amphipathic phospholipids",
    });
  await bilayerPractice
    .getByRole("checkbox", { name: /Nonpolar acyl chains/ })
    .check();
  await bilayerPractice
    .getByRole("checkbox", { name: /Polar headgroups/ })
    .check();
  await bilayerPractice
    .getByRole("button", { name: "Submit practice response" })
    .click();
  await expect(
    bilayerPractice.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("2 / 3 practice points");
  const structurePractice = page.locator(
    '[data-question-id="cell-biology-1:check"]',
  );
  await structurePractice.getByRole("radio").first().check();
  await structurePractice
    .getByRole("button", { name: "Submit practice response" })
    .click();
  await expect(
    structurePractice.getByRole("region", { name: "Submission feedback" }),
  ).toBeVisible();
  await expect(
    structurePractice.getByText(
      /does not establish sound reasoning or learning mastery/,
    ),
  ).toBeVisible();
  await page
    .getByLabel("Your private note")
    .fill(
      "A control tests an alternative explanation; a correct numerical result alone does not establish mechanism.",
    );
  await page.getByRole("button", { name: "Save note", exact: true }).click();
  await expect(page.getByText("Note saved.", { exact: true })).toBeVisible();
  await page.getByRole("button", { name: "Mark as read", exact: true }).click();
  await page
    .getByRole("button", { name: "Bookmark course", exact: true })
    .click();
  await page.reload();
  await expect(page.getByLabel("Your private note")).toHaveValue(
    /A control tests an alternative explanation/,
  );
  await expect(
    page.getByRole("button", { name: "Marked as read — undo" }),
  ).toBeVisible();
  await expect(
    page.getByRole("button", { name: "Remove bookmark" }),
  ).toBeVisible();
  const savedFeedback = page.getByRole("region", {
    name: "Submission feedback",
  });
  expect(await savedFeedback.count()).toBeGreaterThanOrEqual(1);
  await expect(
    savedFeedback.filter({ hasText: "2 / 3 practice points" }),
  ).toBeVisible();
  const lessonAccessibility = await new AxeBuilder({ page })
    .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
    .analyze();
  expect(lessonAccessibility.violations).toEqual([]);
  await page
    .getByRole("link", { name: "Practice gradebook", exact: true })
    .click();
  await expect(
    page.getByRole("heading", { name: "Attempt and feedback history" }),
  ).toBeVisible();
  await expect(
    page.getByRole("table").first().getByText("insufficient evidence").first(),
  ).toBeVisible();
  const gradebookAccessibility = await new AxeBuilder({ page })
    .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
    .analyze();
  expect(gradebookAccessibility.violations).toEqual([]);
  await expect(page.getByRole("table").last().getByRole("row")).toHaveCount(3);
  await expect(
    page
      .getByRole("table")
      .last()
      .getByRole("rowheader", {
        name: /Variant: (base|surface-residue-substitution|surface-area-prediction)/,
      }),
  ).toBeVisible();
  await expect(
    page.getByRole("table").last().getByText("Feedback details").first(),
  ).toBeVisible();
  await page
    .getByRole("link", { name: "Account and data", exact: true })
    .click();
  const unique = crypto.randomUUID();
  await page
    .getByLabel("Email address")
    .fill(`courselab-e2e-${unique}@example.invalid`);
  await page.getByLabel("Password", { exact: true }).fill(crypto.randomUUID());
  await page
    .getByRole("button", { name: "Create account", exact: true })
    .click();
  await expect(
    page.getByRole("heading", { name: "Signed in", exact: true }),
  ).toBeVisible();
  await page.getByRole("link", { name: "My learning" }).click();
  await expect(
    page.getByRole("link", { name: /Foundations of Cell/ }),
  ).toBeVisible();
  await page
    .getByRole("link", { name: "Account and data", exact: true })
    .click();
  const downloadPromise = page.waitForEvent("download");
  await page.getByRole("button", { name: "Export learner data" }).click();
  expect((await downloadPromise).suggestedFilename()).toBe(
    "lattice-courselab-learner-data.json",
  );
  await expect(
    page.getByRole("button", { name: "Delete account and saved data" }),
  ).toBeDisabled();
  await page.getByLabel("Type DELETE to confirm").fill("DELETE");
  await page
    .getByRole("button", { name: "Delete account and saved data" })
    .click();
  await expect(
    page.getByText("Account and saved learner data deleted.", { exact: true }),
  ).toBeVisible();
  await page.reload();
  await expect(
    page.getByRole("button", { name: "Start guest session" }),
  ).toBeVisible();
});

test("structured experimental criteria receive deterministic partial credit and persist", async ({
  page,
}) => {
  await page.goto("/#/account");
  await page.getByRole("button", { name: "Start guest session" }).click();
  await page.getByRole("link", { name: "Course catalog", exact: true }).click();
  await page.getByRole("link", { name: /Foundations of Cell/ }).click();
  await page.getByRole("button", { name: "Enroll in partial course" }).click();
  await page
    .getByRole("navigation", { name: "Lessons" })
    .getByRole("link", { name: /Gene expression and experimental logic/ })
    .click();

  const practice = page.locator(
    '[data-question-id="cell-biology-4:experimental-logic-structured"]',
  );
  await expect(practice).toContainText(
    "Each analytic criterion is scored separately",
  );
  await practice.getByLabel(/Control fidelity/).selectOption("0");
  await practice.getByLabel(/Direct occupancy/).selectOption("0");
  await practice.getByLabel(/Cis-regulatory test/).selectOption("1");
  await practice.getByLabel(/Inference boundary/).selectOption("0");
  await practice
    .getByRole("button", { name: "Submit practice response" })
    .click();
  await expect(
    practice.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("3 / 4 practice points");
  await expect(practice.getByLabel("Field-level scoring")).toContainText(
    "Direct promoter occupancy",
  );
  await expect(
    practice.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("Some structured analytic criteria met");
  await expect(
    practice.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("free-form reasoning is not scored");
  const accessibility = await new AxeBuilder({ page })
    .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
    .analyze();
  expect(accessibility.violations).toEqual([]);

  await page.reload();
  await expect(
    page
      .locator(
        '[data-question-id="cell-biology-4:experimental-logic-structured"]',
      )
      .getByRole("region", { name: "Submission feedback" }),
  ).toContainText("3 / 4 practice points");
});

test("public lesson DTOs contain no answer specifications or solution fields", async ({
  request,
}) => {
  const course = await request.get("/api/v1/courses/cell-biology");
  expect(course.ok()).toBeTruthy();
  const detail = await course.json();
  const lesson = await request.get(
    `/api/v1/courses/cell-biology/lessons/${detail.modules[0].lessons[0].id}`,
  );
  expect(lesson.ok()).toBeTruthy();
  const dto = await lesson.json();
  const seededPractice = dto.questions.find(
    (question: { id: string }) => question.id === "cell-biology-1:check",
  );
  expect(seededPractice.variant_id).toBeTruthy();
  expect(seededPractice.variant_token).toBeTruthy();
  for (const question of dto.questions) {
    expect(question).not.toHaveProperty("answer");
    expect(question).not.toHaveProperty("solution");
    expect(question).not.toHaveProperty("answer_specification");
    expect(question).not.toHaveProperty("solution_spec");
  }
  expect(
    (
      await request.get(
        "/content/courses/cell-biology/question-banks/practice.json",
      )
    ).status(),
  ).toBe(404);
  expect((await request.get("/legacy/src/data/courses.js")).status()).toBe(404);
  expect((await request.get("/.env")).status()).toBe(404);
});

test("symbolic calculus practice accepts an equivalent expression and saves feedback", async ({
  page,
}) => {
  await page.goto("/#/account");
  await page.getByRole("button", { name: "Start guest session" }).click();
  await page.getByRole("link", { name: "Course catalog", exact: true }).click();
  await page.getByRole("link", { name: /Calculus I:/ }).click();
  await page.getByRole("button", { name: "Enroll in partial course" }).click();

  const lessons = page.getByRole("navigation", { name: "Lessons" });
  await lessons.getByRole("link").nth(1).click();
  const practice = page.locator(
    '[data-question-id="calculus-1-2:symbolic-quotient-derivative"]',
  );
  await practice
    .getByLabel("Algebraic expression")
    .fill("((2*x)*(x + 1) - (x^2 + 1))/(x + 1)^2");
  await practice
    .getByRole("button", { name: "Submit practice response" })
    .click();
  await expect(
    practice.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("1 / 1 practice points");
  await expect(
    practice.getByText(/Reasoning has not been assessed/),
  ).toBeVisible();
});

test("learner appeal receives an audited manual adjustment", async ({
  page,
  browser,
}) => {
  const reason = `Please reconsider the control comparison in my response. ${crypto.randomUUID()}`;
  await page.goto("/#/account");
  await page.getByRole("button", { name: "Start guest session" }).click();
  await page.getByRole("link", { name: "Course catalog", exact: true }).click();
  await page.getByRole("link", { name: /Foundations of Cell/ }).click();
  await page.getByRole("button", { name: "Enroll in partial course" }).click();
  await page
    .getByRole("navigation", { name: "Lessons" })
    .getByRole("link")
    .first()
    .click();

  const practice = page.locator('[data-question-id="cell-biology-1:check"]');
  await practice.getByRole("radio").last().check();
  await practice
    .getByRole("button", { name: "Submit practice response" })
    .click();
  await practice.getByLabel("Reason for review").fill(reason);
  await practice.getByRole("button", { name: "Send for human review" }).click();
  await expect(
    practice.getByRole("heading", { name: "Human review · open" }),
  ).toBeVisible();

  const reviewerContext = await browser.newContext();
  const reviewerPage = await reviewerContext.newPage();
  try {
    await reviewerPage.goto("/#/account");
    await reviewerPage
      .getByLabel("Email address")
      .fill("courselab-reviewer@example.invalid");
    await reviewerPage
      .getByLabel("Password", { exact: true })
      .fill("courselab-reviewer-password");
    const registration = reviewerPage.waitForResponse((response) =>
      response.url().endsWith("/api/v1/auth/register"),
    );
    await reviewerPage.getByRole("button", { name: "Create account" }).click();
    if ((await registration).status() === 409) {
      await reviewerPage
        .getByRole("button", { name: "Use an existing account" })
        .click();
      await reviewerPage
        .getByRole("button", { name: "Sign in", exact: true })
        .click();
    }
    await expect(
      reviewerPage.getByRole("heading", { name: "Signed in", exact: true }),
    ).toBeVisible();
    await reviewerPage
      .getByRole("link", { name: "Instructor review", exact: true })
      .click();
    await expect(
      reviewerPage.getByRole("heading", { name: "Human review requests" }),
    ).toBeVisible();
    const reviewCard = reviewerPage
      .locator(".instructor-appeal")
      .filter({ hasText: reason });
    await expect(reviewCard).toBeVisible();
    const accessibility = await new AxeBuilder({ page: reviewerPage })
      .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
      .analyze();
    expect(accessibility.violations).toEqual([]);
    await reviewCard
      .getByRole("radio", { name: "Adjust practice score" })
      .check();
    await reviewCard.getByLabel(/Reviewed practice score/).fill("1");
    await reviewCard
      .getByLabel("Review note (visible to the learner)")
      .fill(
        "The alternate control is supported by the written practice rubric.",
      );
    await reviewCard
      .getByRole("button", { name: "Record review decision" })
      .click();
    await expect(reviewCard).toHaveCount(0);

    const attemptsResponse = page.waitForResponse((response) =>
      response.url().includes("/api/v1/attempts?course_id=cell-biology"),
    );
    await page.reload();
    const refreshedAttempts = await (await attemptsResponse).json();
    expect(
      refreshedAttempts.some(
        (attempt: { appeal?: { status?: string; reason?: string } | null }) =>
          attempt.appeal?.reason === reason &&
          attempt.appeal.status === "adjusted",
      ),
    ).toBeTruthy();
    await page
      .getByRole("link", { name: "Practice gradebook", exact: true })
      .click();
    await expect(
      page.getByText("1 / 1 (manual review; automatic 0)"),
    ).toBeVisible();
    await expect(
      page.getByRole("row").filter({ hasText: "cell-biology-1:check" }),
    ).toContainText("Review: adjusted");

    await reviewerPage
      .getByRole("link", { name: "Account and data", exact: true })
      .click();
    await reviewerPage.getByLabel("Type DELETE to confirm").fill("DELETE");
    await reviewerPage
      .getByRole("button", { name: "Delete account and saved data" })
      .click();
    await expect(
      reviewerPage.getByText("Account and saved learner data deleted.", {
        exact: true,
      }),
    ).toBeVisible();
  } finally {
    await reviewerContext.close();
  }
});

test("data interpretation awards transparent field credit and reloads saved feedback", async ({
  page,
}) => {
  await page.goto("/#/account");
  await page.getByRole("button", { name: "Start guest session" }).click();
  await page.getByRole("link", { name: "Course catalog", exact: true }).click();
  await page.getByRole("link", { name: /Probability, Biostatistics/ }).click();
  await page.getByRole("button", { name: "Enroll in partial course" }).click();

  await page
    .getByRole("navigation", { name: "Lessons" })
    .getByRole("link", {
      name: /Descriptive differences and inferential limits/,
    })
    .click();
  const retrieval = page.getByRole("region", { name: "Retrieval practice" });
  await expect(retrieval).toContainText(
    "compound-minus-vehicle sample contrast",
  );
  const firstCard = retrieval.locator("details").first();
  await expect(firstCard).not.toHaveAttribute("open", "");
  await firstCard.getByText("Reveal answer").click();
  await expect(firstCard).toHaveAttribute("open", "");
  await expect(firstCard).toContainText(
    "does not imply that every compound replicate was higher",
  );
  const practice = page.locator(
    '[data-question-id="statistics-5:group-summary"]',
  );
  await practice.getByLabel(/Calculate compound minus vehicle/).fill("4.0 μM");
  await practice
    .getByLabel(/Which conclusion is best supported/)
    .selectOption("1");
  await practice
    .getByRole("button", { name: "Submit practice response" })
    .click();
  await expect(
    practice.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("1 / 2 practice points");
  await expect(practice.getByLabel("Field-level scoring")).toContainText(
    "1 / 1 point",
  );
  await expect(practice.getByLabel("Field-level scoring")).toContainText(
    "0 / 1 point",
  );
  await expect(practice.getByText(/Some fields are correct/)).toBeVisible();
  const accessibility = await new AxeBuilder({ page })
    .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
    .analyze();
  expect(accessibility.violations).toEqual([]);

  await page.reload();
  await expect(
    page
      .locator('[data-question-id="statistics-5:group-summary"]')
      .getByRole("region", { name: "Submission feedback" }),
  ).toContainText("1 / 2 practice points");
});
