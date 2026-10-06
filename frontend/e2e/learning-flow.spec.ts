import { expect, test } from "@playwright/test";
import AxeBuilder from "@axe-core/playwright";

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

test("catalog communicates maturity and has no automated accessibility violations", async ({
  page,
}) => {
  await page.goto("/");
  await expect(page).toHaveTitle("uniStemCourseSimulators");
  await expect(
    page.getByRole("link", {
      name: "uniStemCourseSimulators Think · Model · Practice",
      exact: true,
    }),
  ).toBeVisible();
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
    page.getByRole("region", { name: "Course assessment plan" }),
  ).toContainText("No course grade is configured");
  await expect(
    page.getByRole("heading", { name: "Attempt and feedback history" }),
  ).toBeVisible();
  await expect(
    page
      .getByRole("region", { name: "Practice gradebook" })
      .getByRole("table")
      .first()
      .getByText("insufficient evidence")
      .first(),
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
    "uni-stem-course-simulators-learner-data.json",
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

test("the developed cell-biology weeks expose original lessons and deterministic practice", async ({
  page,
}) => {
  await page.goto("/#/account");
  await page.getByRole("button", { name: "Start guest session" }).click();
  await page.getByRole("link", { name: "Course catalog", exact: true }).click();
  await page.getByRole("link", { name: /Foundations of Cell/ }).click();
  await page.getByRole("button", { name: "Enroll in partial course" }).click();

  const lessons = page.getByRole("navigation", { name: "Lessons" });
  await lessons
    .getByRole("link", { name: /Water, pH, and noncovalent interactions/ })
    .click();
  await expect(
    page.getByRole("heading", {
      name: "Water, pH, and noncovalent interactions",
      level: 1,
    }),
  ).toBeVisible();
  const protonation = page.locator(
    '[data-question-id="cell-biology-5:protonation-state"]',
  );
  await protonation.getByRole("radio").first().check();
  await protonation
    .getByRole("button", { name: "Submit practice response" })
    .click();
  await expect(
    protonation.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("1 / 1 practice points");

  await lessons
    .getByRole("link", {
      name: /Protein sequence, structure, and variant evidence/,
    })
    .click();
  const variant = page.locator(
    '[data-question-id="cell-biology-6:variant-inference"]',
  );
  await variant.getByLabel(/Mechanistic prediction/).selectOption("0");
  await variant.getByLabel(/Discriminating evidence/).selectOption("0");
  await variant.getByLabel(/Inference scope/).selectOption("0");
  await variant
    .getByRole("button", { name: "Submit practice response" })
    .click();
  await expect(
    variant.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("3 / 3 practice points");

  await lessons
    .getByRole("link", {
      name: /Membranes, transport, and electrochemical gradients/,
    })
    .click();
  const transport = page.locator(
    '[data-question-id="cell-biology-2:transport-classification"]',
  );
  await transport.getByRole("radio").first().check();
  await transport
    .getByRole("button", { name: "Submit practice response" })
    .click();
  await expect(
    transport.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("1 / 1 practice points");

  await lessons
    .getByRole("link", {
      name: /Organelle compartments, membrane topology, and protein targeting/,
    })
    .click();
  await expect(
    page.getByRole("heading", {
      name: "Organelle compartments, membrane topology, and protein targeting",
      level: 1,
    }),
  ).toBeVisible();
  const route = page.locator(
    '[data-question-id="cell-biology-7:secretory-route"]',
  );
  await route.getByRole("radio").first().check();
  await route.getByRole("button", { name: "Submit practice response" }).click();
  await expect(
    route.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("1 / 1 practice points");

  const protection = page.locator(
    '[data-question-id="cell-biology-7:protease-protection"]',
  );
  await protection.getByLabel(/Membrane-enclosure inference/).selectOption("0");
  await protection.getByLabel(/Membrane-integrity control/).selectOption("0");
  await protection.getByLabel(/Inference boundary/).selectOption("0");
  await protection
    .getByRole("button", { name: "Submit practice response" })
    .click();
  await expect(
    protection.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("3 / 3 practice points");

  await lessons
    .getByRole("link", { name: /Protein sorting, vesicle traffic/ })
    .click();
  await expect(
    page.getByRole("heading", {
      name: "Protein sorting, vesicle traffic, and experimental inference",
      level: 1,
    }),
  ).toBeVisible();
  const lysosome = page.locator(
    '[data-question-id="cell-biology-8:m6p-sorting"]',
  );
  await lysosome.getByRole("radio").first().check();
  await lysosome
    .getByRole("button", { name: "Submit practice response" })
    .click();
  await expect(
    lysosome.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("1 / 1 practice points");

  const kdel = page.locator(
    '[data-question-id="cell-biology-8:kdel-retrieval"]',
  );
  await kdel.getByRole("radio").first().check();
  await kdel.getByRole("button", { name: "Submit practice response" }).click();
  await expect(
    kdel.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("1 / 1 practice points");

  await lessons
    .getByRole("link", {
      name: /Enzyme catalysis, reaction mechanisms, and free energy/,
    })
    .click();
  await expect(
    page.getByRole("heading", {
      name: "Enzyme catalysis, reaction mechanisms, and free energy",
      level: 1,
    }),
  ).toBeVisible();
  const equilibrium = page.locator(
    '[data-question-id="cell-biology-9:equilibrium"]',
  );
  await equilibrium.getByRole("radio").first().check();
  await equilibrium
    .getByRole("button", { name: "Submit practice response" })
    .click();
  await expect(
    equilibrium.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("1 / 1 practice points");

  const coupling = page.locator(
    '[data-question-id="cell-biology-9:coupling-energy"]',
  );
  await coupling.getByLabel("Numerical value").fill("-9.0");
  await coupling.getByLabel("Unit").fill("kJ/mol");
  await coupling
    .getByRole("button", { name: "Submit practice response" })
    .click();
  await expect(
    coupling.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("1 / 1 practice points");

  await lessons
    .getByRole("link", {
      name: /Initial-rate evidence and reversible enzyme inhibition/,
    })
    .click();
  await expect(
    page.getByRole("heading", {
      name: "Initial-rate evidence and reversible enzyme inhibition",
      level: 1,
    }),
  ).toBeVisible();
  const rate = page.locator(
    '[data-question-id="cell-biology-10:rate-prediction"]',
  );
  await rate.getByLabel("Numerical value").fill("80");
  await rate.getByLabel("Unit").fill("nM/s");
  await rate.getByRole("button", { name: "Submit practice response" }).click();
  await expect(
    rate.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("1 / 1 practice points");

  const inference = page.locator(
    '[data-question-id="cell-biology-10:kinetic-inference"]',
  );
  await inference.getByLabel(/Kinetic pattern/).selectOption("0");
  await inference.getByLabel(/Detector control/).selectOption("0");
  await inference.getByLabel(/Inference boundary/).selectOption("0");
  await inference
    .getByRole("button", { name: "Submit practice response" })
    .click();
  await expect(
    inference.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("3 / 3 practice points");

  await lessons
    .getByRole("link", { name: /Cell imaging: resolution, contrast/ })
    .click();
  await expect(
    page.getByRole("heading", {
      name: "Cell imaging: resolution, contrast, and quantitative limits",
      level: 1,
    }),
  ).toBeVisible();
  const resolution = page.locator(
    '[data-question-id="cell-biology-11:resolution-estimate"]',
  );
  await resolution.getByLabel("Numerical value").fill("244");
  await resolution.getByLabel("Unit").fill("nm");
  await resolution
    .getByRole("button", { name: "Submit practice response" })
    .click();
  await expect(
    resolution.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("1 / 1 practice points");

  const confocal = page.locator(
    '[data-question-id="cell-biology-11:confocal-contrast"]',
  );
  await confocal.getByRole("radio").first().check();
  await confocal
    .getByRole("button", { name: "Submit practice response" })
    .click();
  await expect(
    confocal.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("1 / 1 practice points");

  const colocalization = page.locator(
    '[data-question-id="cell-biology-11:colocalization-limit"]',
  );
  await colocalization.getByRole("radio").first().check();
  await colocalization
    .getByRole("button", { name: "Submit practice response" })
    .click();
  await expect(
    colocalization.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("1 / 1 practice points");

  await lessons
    .getByRole("link", { name: /Cell fractionation: enrichment/ })
    .click();
  await expect(
    page.getByRole("heading", {
      name: "Cell fractionation: enrichment, contamination, and recovery",
      level: 1,
    }),
  ).toBeVisible();
  const recovery = page.locator(
    '[data-question-id="cell-biology-12:er-marker-recovery"]',
  );
  await recovery.getByLabel("Numerical value").fill("95");
  await recovery.getByLabel("Unit").fill("%");
  await recovery
    .getByRole("button", { name: "Submit practice response" })
    .click();
  await expect(
    recovery.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("1 / 1 practice points");

  const fractions = page.locator(
    '[data-question-id="cell-biology-12:fraction-analysis"]',
  );
  await fractions.getByLabel(/Fraction interpretation/).selectOption("0");
  await fractions.getByLabel(/Recovery accounting/).selectOption("0");
  await fractions.getByLabel(/Inference boundary/).selectOption("0");
  await fractions
    .getByRole("button", { name: "Submit practice response" })
    .click();
  await expect(
    fractions.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("3 / 3 practice points");

  const markerPanel = page.locator(
    '[data-question-id="cell-biology-12:marker-panel"]',
  );
  await markerPanel.getByRole("radio").first().check();
  await markerPanel
    .getByRole("button", { name: "Submit practice response" })
    .click();
  await expect(
    markerPanel.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("1 / 1 practice points");

  await lessons
    .getByRole("link", { name: /DNA structure, genome organization/ })
    .click();
  await expect(
    page.getByRole("heading", {
      name: "DNA structure, genome organization, and semiconservative replication",
      level: 1,
    }),
  ).toBeVisible();
  const complement = page.locator(
    '[data-question-id="cell-biology-13:strand-complement"]',
  );
  await complement.getByRole("radio").first().check();
  await complement
    .getByRole("button", { name: "Submit practice response" })
    .click();
  await expect(
    complement.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("1 / 1 practice points");

  const hybridFraction = page.locator(
    '[data-question-id="cell-biology-13:hybrid-fraction"]',
  );
  await hybridFraction.getByLabel("Numerical value").fill("50");
  await hybridFraction.getByLabel("Unit").fill("%");
  await hybridFraction
    .getByRole("button", { name: "Submit practice response" })
    .click();
  await expect(
    hybridFraction.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("1 / 1 practice points");

  await lessons
    .getByRole("link", { name: /DNA damage, repair pathways/ })
    .click();
  await expect(
    page.getByRole("heading", {
      name: "DNA damage, repair pathways, and evidence of lesion removal",
      level: 1,
    }),
  ).toBeVisible();
  const pathways = page.locator(
    '[data-question-id="cell-biology-14:repair-pathway-match"]',
  );
  await pathways.getByLabel(/Bulky lesion/).selectOption("0");
  await pathways.getByLabel(/Small base lesion/).selectOption("0");
  await pathways.getByLabel(/Escaped replication error/).selectOption("0");
  await pathways
    .getByRole("button", { name: "Submit practice response" })
    .click();
  await expect(
    pathways.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("3 / 3 practice points");

  const lesionData = page.locator(
    '[data-question-id="cell-biology-14:lesion-removal-data"]',
  );
  await lesionData.getByLabel(/Starting burden/).selectOption("0");
  await lesionData.getByLabel(/Perturbation evidence/).selectOption("0");
  await lesionData.getByLabel(/Claim boundary/).selectOption("0");
  await lesionData
    .getByRole("button", { name: "Submit practice response" })
    .click();
  await expect(
    lesionData.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("3 / 3 practice points");

  await lessons
    .getByRole("link", { name: /Chromatin accessibility and regulatory DNA/ })
    .click();
  await expect(
    page.getByRole("heading", {
      name: "Chromatin accessibility and regulatory DNA",
      level: 1,
    }),
  ).toBeVisible();
  const chromatinData = page.locator(
    '[data-question-id="cell-biology-15:cell-state-data"]',
  );
  await chromatinData.getByLabel(/Accessibility pattern/).selectOption("0");
  await chromatinData.getByLabel(/RNA pattern/).selectOption("0");
  await chromatinData.getByLabel(/Causal boundary/).selectOption("0");
  await chromatinData
    .getByRole("button", { name: "Submit practice response" })
    .click();
  await expect(
    chromatinData.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("3 / 3 practice points");

  await lessons
    .getByRole("link", {
      name: /Transcription-factor occupancy and reporter evidence/,
    })
    .click();
  await expect(
    page.getByRole("heading", {
      name: "Transcription-factor occupancy and reporter evidence",
      level: 1,
    }),
  ).toBeVisible();
  const percentInput = page.locator(
    '[data-question-id="cell-biology-16:chip-percent-input"]',
  );
  await percentInput.getByLabel("Numerical value").fill("8");
  await percentInput.getByLabel("Unit").fill("%");
  await percentInput
    .getByRole("button", { name: "Submit practice response" })
    .click();
  await expect(
    percentInput.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("1 / 1 practice points");

  const chipControls = page.locator(
    '[data-question-id="cell-biology-16:chip-controls"]',
  );
  await chipControls.getByLabel(/Starting material/).selectOption("0");
  await chipControls.getByLabel(/Nonspecific pull-down/).selectOption("0");
  await chipControls.getByLabel(/Locus\/PCR specificity/).selectOption("0");
  await chipControls
    .getByRole("button", { name: "Submit practice response" })
    .click();
  await expect(
    chipControls.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("3 / 3 practice points");

  const reporter = page.locator(
    '[data-question-id="cell-biology-16:reporter-interpretation"]',
  );
  await reporter.getByLabel(/Sequence contribution/).selectOption("0");
  await reporter.getByLabel(/Normalization/).selectOption("0");
  await reporter.getByLabel(/Endogenous limit/).selectOption("0");
  await reporter
    .getByRole("button", { name: "Submit practice response" })
    .click();
  await expect(
    reporter.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("3 / 3 practice points");
});

test("week 8 cumulative review is interactive, ungraded practice and persists feedback", async ({
  page,
}) => {
  await page.goto("/#/account");
  await page.getByRole("button", { name: "Start guest session" }).click();
  await page.getByRole("link", { name: "Course catalog", exact: true }).click();
  await page.getByRole("link", { name: /Foundations of Cell/ }).click();
  await page.getByRole("button", { name: "Enroll in partial course" }).click();
  await page.getByRole("link", { name: "Practice gradebook" }).click();

  const row = page.getByRole("row", {
    name: /Week 8 cumulative review practice \(ungraded; not a midterm\)/,
  });
  await row.getByRole("button", { name: "Open practice set" }).click();
  await expect(
    page.getByRole("heading", {
      name: "Week 8 cumulative review practice (ungraded; not a midterm)",
    }),
  ).toBeVisible();
  await expect(
    page.getByText(/not a midterm or other summative exam/i),
  ).toBeVisible();
  const accessibility = await new AxeBuilder({ page })
    .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
    .analyze();
  expect(accessibility.violations).toEqual([]);

  const question = page.locator(
    '[data-question-id="cell-biology-1:check-all"]',
  );
  await question.getByRole("checkbox").first().check();
  await question
    .getByRole("button", { name: "Submit practice response" })
    .click();
  await expect(
    question.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("practice points");

  await page.reload();
  const reloadedRow = page.getByRole("row", {
    name: /Week 8 cumulative review practice \(ungraded; not a midterm\)/,
  });
  await reloadedRow.getByRole("button", { name: "Open practice set" }).click();
  await expect(
    page
      .locator('[data-question-id="cell-biology-1:check-all"]')
      .getByRole("region", { name: "Submission feedback" }),
  ).toContainText("practice points");
  await expect(
    page.getByRole("button", { name: "Close practice set" }),
  ).toBeVisible();
});

test("week 9 RNA and protein practice loads and grades version-pinned content", async ({
  page,
}) => {
  await page.goto("/#/account");
  await page.getByRole("button", { name: "Start guest session" }).click();
  await page.getByRole("link", { name: "Course catalog", exact: true }).click();
  await page.getByRole("link", { name: /Foundations of Cell/ }).click();
  await page.getByRole("button", { name: "Enroll in partial course" }).click();
  await page.getByRole("link", { name: "Practice gradebook" }).click();

  const row = page.getByRole("row", {
    name: /Week 9: RNA processing, translation, and protein-turnover practice/,
  });
  await row.getByRole("button", { name: "Open practice set" }).click();
  await expect(
    page.getByRole("heading", {
      name: "Week 9: RNA processing, translation, and protein-turnover practice",
    }),
  ).toBeVisible();
  await expect(
    page.getByText(/8 questions · 14 practice points/),
  ).toBeVisible();

  const isoform = page.locator(
    '[data-question-id="cell-biology-17:isoform-fraction"]',
  );
  await isoform.getByLabel("Numerical value").fill("66.7");
  await isoform.getByLabel("Unit").fill("%");
  await isoform
    .getByRole("button", { name: "Submit practice response" })
    .click();
  await expect(
    isoform.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("1 / 1 practice points");

  const turnover = page.locator(
    '[data-question-id="cell-biology-18:synthesis-vs-turnover-data"]',
  );
  await turnover.getByLabel(/Mechanistic inference/).selectOption("0");
  await turnover.getByLabel(/Follow-up/).selectOption("0");
  await turnover.getByLabel(/Claim boundary/).selectOption("0");
  await turnover
    .getByRole("button", { name: "Submit practice response" })
    .click();
  await expect(
    turnover.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("3 / 3 practice points");
});

test("week 10 inheritance and variant practice separates transmission and phenotype", async ({
  page,
}) => {
  await page.goto("/#/account");
  await page.getByRole("button", { name: "Start guest session" }).click();
  await page.getByRole("link", { name: "Course catalog", exact: true }).click();
  await page.getByRole("link", { name: /Foundations of Cell/ }).click();
  await page.getByRole("button", { name: "Enroll in partial course" }).click();
  await page.getByRole("link", { name: "Practice gradebook" }).click();

  const row = page.getByRole("row", {
    name: /Week 10: inheritance and genotype-to-phenotype practice/,
  });
  await row.getByRole("button", { name: "Open practice set" }).click();
  await expect(
    page.getByRole("heading", {
      name: "Week 10: inheritance and genotype-to-phenotype practice",
    }),
  ).toBeVisible();
  await expect(
    page.getByText(/7 questions · 13 practice points/),
  ).toBeVisible();

  const risk = page.locator(
    '[data-question-id="cell-biology-19:affected-child-risk"]',
  );
  await risk.getByLabel("Numerical value").fill("40.0");
  await risk.getByLabel("Unit").fill("%");
  await risk.getByRole("button", { name: "Submit practice response" }).click();
  await expect(
    risk.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("1 / 1 practice points");

  const isogenic = page.locator(
    '[data-question-id="cell-biology-20:isogenic-data"]',
  );
  await isogenic.getByLabel(/Data interpretation/).selectOption("0");
  await isogenic.getByLabel(/Reversibility/).selectOption("0");
  await isogenic.getByLabel(/Next mechanism test/).selectOption("0");
  await isogenic
    .getByRole("button", { name: "Submit practice response" })
    .click();
  await expect(
    isogenic.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("3 / 3 practice points");
});

test("week 11 signaling practice separates occupancy, response dynamics, and feedback evidence", async ({
  page,
}) => {
  await page.goto("/#/account");
  await page.getByRole("button", { name: "Start guest session" }).click();
  await page.getByRole("link", { name: "Course catalog", exact: true }).click();
  await page.getByRole("link", { name: /Foundations of Cell/ }).click();
  await page.getByRole("button", { name: "Enroll in partial course" }).click();
  await page.getByRole("link", { name: "Practice gradebook" }).click();

  const row = page.getByRole("row", {
    name: /Week 11: receptor signaling and perturbation practice/,
  });
  await row.getByRole("button", { name: "Open practice set" }).click();
  await expect(
    page.getByRole("heading", {
      name: "Week 11: receptor signaling and perturbation practice",
    }),
  ).toBeVisible();
  await expect(
    page.getByText(/7 questions · 13 practice points/),
  ).toBeVisible();

  const occupancy = page.locator(
    '[data-question-id="cell-biology-21:occupancy-model"]',
  );
  await occupancy.getByLabel("Numerical value").fill("0.20");
  await occupancy
    .getByRole("button", { name: "Submit practice response" })
    .click();
  await expect(
    occupancy.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("1 / 1 practice points");

  const trajectory = page.locator(
    '[data-question-id="cell-biology-22:dynamic-trajectory"]',
  );
  await trajectory.getByLabel(/Time-course shape/).selectOption("1");
  await trajectory.getByLabel(/Early peak/).selectOption("0");
  await trajectory.getByLabel(/Claim boundary/).selectOption("0");
  await trajectory
    .getByRole("button", { name: "Submit practice response" })
    .click();
  await expect(
    trajectory.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("3 / 3 practice points");

  const feedback = page.locator(
    '[data-question-id="cell-biology-22:feedback-alternatives"]',
  );
  await feedback.getByLabel(/Ligand-depletion test/).selectOption("1");
  await feedback.getByLabel(/Receptor-adaptation test/).selectOption("0");
  await feedback.getByLabel(/Induced-feedback test/).selectOption("2");
  await feedback.getByLabel(/Alternative explanation/).selectOption("1");
  await feedback
    .getByRole("button", { name: "Submit practice response" })
    .click();
  await expect(
    feedback.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("4 / 4 practice points");
});

test("week 12 mechanics practice separates modulus, matrix controls, and cell outcome", async ({
  page,
}) => {
  await page.goto("/#/account");
  await page.getByRole("button", { name: "Start guest session" }).click();
  await page.getByRole("link", { name: "Course catalog", exact: true }).click();
  await page.getByRole("link", { name: /Foundations of Cell/ }).click();
  await page.getByRole("button", { name: "Enroll in partial course" }).click();
  await page.getByRole("link", { name: "Practice gradebook" }).click();

  const row = page.getByRole("row", {
    name: /Week 12: cytoskeleton, matrix, and mechanobiology practice/,
  });
  await row.getByRole("button", { name: "Open practice set" }).click();
  await expect(
    page.getByRole("heading", {
      name: "Week 12: cytoskeleton, matrix, and mechanobiology practice",
    }),
  ).toBeVisible();
  await expect(
    page.getByText(/7 questions · 13 practice points/),
  ).toBeVisible();

  const stress = page.locator(
    '[data-question-id="cell-biology-24:uniform-stress"]',
  );
  await stress.getByLabel("Numerical value").fill("4000");
  await stress.getByLabel("Unit").fill("Pa");
  await stress
    .getByRole("button", { name: "Submit practice response" })
    .click();
  await expect(
    stress.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("1 / 1 practice points");

  const stiffness = page.locator(
    '[data-question-id="cell-biology-24:synthetic-stiffness-data"]',
  );
  await stiffness.getByLabel(/Measured trend/).selectOption("0");
  await stiffness.getByLabel(/Replicate interpretation/).selectOption("2");
  await stiffness.getByLabel(/Inference boundary/).selectOption("1");
  await stiffness
    .getByRole("button", { name: "Submit practice response" })
    .click();
  await expect(
    stiffness.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("3 / 3 practice points");

  const controls = page.locator(
    '[data-question-id="cell-biology-24:matrix-mechanics-controls"]',
  );
  await controls.getByLabel(/Matrix control/).selectOption("1");
  await controls.getByLabel(/Cell-state control/).selectOption("0");
  await controls.getByLabel(/Force-route test/).selectOption("0");
  await controls.getByLabel(/Outcome boundary/).selectOption("2");
  await controls
    .getByRole("button", { name: "Submit practice response" })
    .click();
  await expect(
    controls.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("4 / 4 practice points");
});

test("week 13 cell-cycle and cell-fate practice separates arrest, senescence, and apoptosis evidence", async ({
  page,
}) => {
  await page.goto("/#/account");
  await page.getByRole("button", { name: "Start guest session" }).click();
  await page.getByRole("link", { name: "Course catalog", exact: true }).click();
  await page.getByRole("link", { name: /Foundations of Cell/ }).click();
  await page.getByRole("button", { name: "Enroll in partial course" }).click();
  await page.getByRole("link", { name: "Practice gradebook" }).click();

  const row = page.getByRole("row", {
    name: /Week 13: cell-cycle control, senescence, and cell death practice/,
  });
  await row.getByRole("button", { name: "Open practice set" }).click();
  await expect(
    page.getByRole("heading", {
      name: "Week 13: cell-cycle control, senescence, and cell death practice",
    }),
  ).toBeVisible();
  await expect(
    page.getByText(/7 questions · 13 practice points/),
  ).toBeVisible();

  const phase = page.locator(
    '[data-question-id="cell-biology-25:phase-snapshot"]',
  );
  await phase.getByLabel("Numerical value").fill("25");
  await phase.getByLabel("Unit").fill("%");
  await phase.getByRole("button", { name: "Submit practice response" }).click();
  await expect(
    phase.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("1 / 1 practice points");

  const damage = page.locator(
    '[data-question-id="cell-biology-25:damage-time-course"]',
  );
  await damage.getByLabel(/Measured pattern/).selectOption("0");
  await damage.getByLabel(/Inference boundary/).selectOption("1");
  await damage.getByLabel(/Next experiment/).selectOption("2");
  await damage
    .getByRole("button", { name: "Submit practice response" })
    .click();
  await expect(
    damage.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("3 / 3 practice points");

  const senescence = page.locator(
    '[data-question-id="cell-biology-26:senescence-marker-panel"]',
  );
  await senescence.getByLabel(/State interpretation/).selectOption("0");
  await senescence.getByLabel(/Marker limitation/).selectOption("2");
  await senescence.getByLabel(/Follow-up/).selectOption("1");
  await senescence
    .getByRole("button", { name: "Submit practice response" })
    .click();
  await expect(
    senescence.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("3 / 3 practice points");
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

  const experimentLesson = await request.get(
    "/api/v1/courses/cell-biology/lessons/cell-biology-4",
  );
  expect(experimentLesson.ok()).toBeTruthy();
  const uploadQuestion = (await experimentLesson.json()).questions.find(
    (question: { type: string }) => question.type === "file_upload",
  );
  expect(uploadQuestion.accepted_media_types).toEqual(["text/csv"]);
  expect(uploadQuestion.max_upload_bytes).toBe(32768);
  expect(uploadQuestion).not.toHaveProperty("validation_spec");
  expect(uploadQuestion).not.toHaveProperty("rubric");
  expect(uploadQuestion).not.toHaveProperty("solution_spec");
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

test("self-registration cannot receive human-review access for a learner appeal", async ({
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
    const session = await reviewerPage.evaluate(async () => {
      const response = await fetch("/api/v1/auth/session");
      return response.json();
    });
    expect(session.can_review).toBe(false);
    expect(
      await reviewerPage.evaluate(
        async () => (await fetch("/api/v1/instructor/appeals")).status,
      ),
    ).toBe(403);
    await page.reload();
    await expect(
      page.getByRole("heading", { name: "Human review · open" }),
    ).toBeVisible();

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

  const graph = page.locator(
    '[data-question-id="statistics-5:concentration-graph"]',
  );
  await expect(graph.getByRole("table")).toContainText("4.8, 5, 5.2");
  await expect(graph.getByRole("img", { name: /Graph preview/ })).toBeVisible();
  const vehicle = graph.getByRole("group", { name: "Vehicle" });
  await vehicle.getByLabel("Concentration (μM) coordinate").fill("0");
  await vehicle
    .getByLabel("Mean signal (arbitrary fluorescence units) coordinate")
    .fill("4.7");
  const lowDose = graph.getByRole("group", { name: "2 μM" });
  await lowDose.getByLabel("Concentration (μM) coordinate").fill("2");
  await lowDose
    .getByLabel("Mean signal (arbitrary fluorescence units) coordinate")
    .fill("10");
  const highDose = graph.getByRole("group", { name: "4 μM" });
  await highDose.getByLabel("Concentration (μM) coordinate").fill("4");
  await highDose
    .getByLabel("Mean signal (arbitrary fluorescence units) coordinate")
    .fill("15");
  await graph.getByRole("button", { name: "Submit practice response" }).click();
  await expect(
    graph.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("2.5 / 3 practice points");
  await expect(graph.getByLabel("Field-level scoring")).toContainText(
    "Vehicle sample mean coordinate",
  );
  await expect(graph.getByLabel("Field-level scoring")).toContainText(
    "0 / 0.5 point",
  );
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
  await expect(
    page
      .locator('[data-question-id="statistics-5:concentration-graph"]')
      .getByRole("region", { name: "Submission feedback" }),
  ).toContainText("2.5 / 3 practice points");
});

test("CSV analysis upload receives cell-level partial credit and persists safely", async ({
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
    '[data-question-id="cell-biology-4:csv-summary-table"]',
  );
  await expect(practice).toContainText("Upload a UTF-8 CSV");
  await practice.getByLabel("CSV file upload").setInputFiles({
    name: "summary.csv",
    mimeType: "text/csv",
    buffer: Buffer.from(
      "condition,replicate_count,mean_signal\nvehicle,4,5.00\ninhibitor,4,100\n",
    ),
  });
  await practice
    .getByRole("button", { name: "Submit practice response" })
    .click();
  await expect(
    practice.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("3 / 4 practice points");
  await expect(practice.getByLabel("Field-level scoring")).toContainText(
    "Vehicle mean signal",
  );
  await expect(
    practice.getByRole("region", { name: "Submission feedback" }),
  ).toContainText("Some uploaded CSV results met");
  await expect(practice).toContainText("uploaded content is never executed");
  const accessibility = await new AxeBuilder({ page })
    .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
    .analyze();
  expect(accessibility.violations).toEqual([]);

  await page.reload();
  await expect(
    page
      .locator('[data-question-id="cell-biology-4:csv-summary-table"]')
      .getByRole("region", { name: "Submission feedback" }),
  ).toContainText("3 / 4 practice points");
});
