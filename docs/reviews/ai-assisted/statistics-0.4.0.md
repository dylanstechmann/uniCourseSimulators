# AI-assisted check: Probability, Biostatistics & Experimental Design 0.4.0

**This is not a human review.** It was run on 2026-10-08 by an AI coding assistant (Claude Sonnet 5.5 in
Claude Code) on material that the same kind of system had just written, so it is not independent and may
share that material's blind spots. It changes no maturity or review label. The package remains `partial`,
unreviewed and formative-only.

- **Version checked:** the working tree that became 0.4.0.
- **Scope:** lessons 9 to 15 (sources of variability and pseudoreplication; comparing two groups; power and
  sample size; regression and calibration; resampling and rank-based methods; base rates and replication;
  planning a confirmatory study), the nested-design lab (reading, dataset and seven items), the schedule, the
  learner-facing limitations and the syllabus. It also covers the numerical keys of the earlier lessons 1, 3, 5,
  6, 7 and 8. All 58 new items were checked.
- **Not checked:** teaching depth and sequencing, Bloom labels, accessibility, the text of the earlier lessons
  5 to 8, and the textbook-level statements listed below, which cite no source.

## Method

1. Every numerical key in the package (all 57 numeric items, old and new, and the numeric field of the older
   statistics-5 item and of the lab's two data-interpretation items) was recomputed independently from the
   numbers in its prompt, with constants written out. Student's t is evaluated by integrating over the
   chi-square mixing distribution, which shares no code with the scipy routines that produced the stored keys.
   The calculations are kept as tests in `tests/content/test_ai_assisted_checks.py`, which also asserts that
   every numeric item is covered.
2. Numbers that the lessons quote but no item asks for were recomputed too: quoted p-values and critical
   values; the exact power of the t test (0.51 at six per group, 11 per group needed for the planning effect, 52
   per group in the capstone, 0.14 for the pilot); the standard error and interval for the inverse prediction;
   the residuals of the saturating-response example; every worked example, including counting 14 of 70
   permutations by enumeration; and the natural-frequency table.
3. The lab keys were recomputed from the lab CSV with separate code: animal means and counts, the pooled
   technical SD, the intraclass correlation and the two t statistics, together with the identity between the
   F statistic of a balanced nested analysis of variance and the square of the animal-level t statistic.
4. All 58 new items were graded with the real grader using a correct response. Two failed on the first run (see
   the table) and all 58 earned full credit after the fix.
5. Each lesson and the lab were read once as rendered, for accuracy, internal consistency and overclaiming.

## Results

No answer key in the package was wrong, including the 17 older numeric keys. Six drafting problems were found
and fixed before the version was committed:

| # | Where | Severity | Finding | Status |
|---|---|---|---|---|
| 1 | Lab items `animal-summary` and `technical-sd` | error | They asked for answers in "au" (arbitrary units), a unit the real grader does not support, so a correct answer could not be graded. | The prompts now say "arbitrary units" and take a number only |
| 2 | Lab item `supported-conclusions` | error | Its prompt duplicated the prompt of the biochemistry lab, which the validator rejects. | Reworded |
| 3 | Lesson 14, item `ppv-high-power` | misleading | An answer explanation printed 0.08 as 0.08000000000000002. The number-formatting guard caught it. | Formatted to two decimals |
| 4 | Lessons 9 to 15 | cosmetic | Negative numbers such as (-0.05, 5.65) used a hyphen where the rest of the package uses a minus sign. | The build step now typesets a minus sign before a digit. One older lesson (8) still has a hyphen in an interval, and was left unchanged |
| 5 | Lesson 15, step 3 | unclear | The statement that a result must exceed 11.5 units to be significant did not say that it applies when animals, not readings, are the units. | Stated |
| 6 | Syllabus | omission | The syllabus listed four of the package's five authored outcomes; the graph outcome was missing. | Regenerated from the manifest |

Two mistakes in the new test code itself (an expected string that did not match the lesson, and a back-derived
rather than computed nested F statistic) were also found and fixed; neither involved a key.

## Statements without a cited source

The package adds no references. These statements are at textbook level, and a reviewer should confirm that each
is acceptable as stated: the normal-approximation sample-size formula with z = 1.96, 0.8416 and 2.99, and that it
is optimistic for small samples compared with the exact t calculation (lessons 11 and 15); the formula for the
share of significant findings that are true, from a prior probability, power and α, which ignores bias and the
distribution of effect sizes (lesson 14); the approximate standard error of an inverse prediction (lesson 12);
that the Mann–Whitney test is a permutation test on ranks when there are no ties (lesson 13); the cost-optimal
number of readings per unit, √(σ_t² c_unit / (σ_b² c_reading)) (lesson 15); and that a balanced nested analysis
of variance gives the same test as the animal-level t test (lab).

## For a human reviewer

- Lesson 15 models the course case (a pilot with p = 0.04 for one of 18 biomarkers) with synthetic variance
  components. A statistician should judge whether the list of what to write down before the data exist is the
  right minimum, and whether the smallest-effect-of-interest framing is clear.
- Lesson 14 uses the simple model of a prior probability, power and α. Some statisticians dispute using it to
  estimate a field's rate of false findings, and the lesson says that it is an illustration; check the wording.
- The lab uses the pooled-variance t statistic for equal group sizes and a balanced layout. Real nested data
  are rarely balanced, and the lab says so. Check that the pedagogy is acceptable.
- Prototype units 1 to 4 are still 70 to 80 words each, and their eight objectives are linked to no course
  outcome. The earlier lessons 5 to 8 were not re-read in this pass.
