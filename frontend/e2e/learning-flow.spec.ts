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
    page.getByText(/Four short lessons do not constitute a semester course/),
  ).toBeVisible();
  await expect(
    page.getByText("partial", { exact: true }).first(),
  ).toBeVisible();
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
