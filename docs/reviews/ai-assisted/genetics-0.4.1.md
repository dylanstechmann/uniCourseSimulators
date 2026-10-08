# AI-assisted check: Genetics & Genomics 0.4.1

**This is not a human review.** It was run on 2026-10-08 by an AI coding assistant (Claude Opus 5.5 in
Claude Code). The same kind of system wrote lessons 5 to 9, so the check is not independent and may
share their blind spots. It changes no maturity or review label. The package remains `partial`,
unreviewed and formative-only.

- **Version checked:** 0.4.1 (commit `1317222`). Fixes are in 0.4.2.
- **Scope:** all nine readings (four short prototype units and five original lessons), all 39 practice
  items and their keys, the worked-example summaries, the retrieval cards that state formulas, and the
  course-level text shown to learners (limitations and syllabus).
- **Not checked:** the link-only source comparators, Bloom levels and prerequisite edges, accessibility
  and rendering in the app, and whether the items test the outcomes at a suitable depth.

## Method

1. Every numerical key (23) was recomputed from the data stated in its prompt, independently of the
   stored answer, and compared within the item's tolerance. The recalculations are kept as tests in
   `tests/content/test_ai_assisted_checks.py`. The suite also grades every stored key with the real
   grader (`backend/tests/test_authored_items.py`).
2. Every number in the five original readings was recalculated: allele frequencies, χ², F, carrier
   frequency, the Wahlund example, Falconer estimates, the polygenic score, R² to r, the three-point
   cross, coincidence and interference, the Haldane and Kosambi distances, ΔΔCt, sample size by the normal
   approximation, exact two-sample t-test power (noncentral t), the Wald ratio, its standard error,
   intervals and odds ratios, and the F-statistic.
3. Each reading was checked for scientific accuracy, overclaiming, and consistency with its items and
   cards. The 16 choice and multiple-select keys were checked by reasoning.
4. The course-level text was compared with the package's actual contents.

## Results

No answer key was wrong: all 23 numerical keys agree with the recalculation, and the 16 choice keys
are defensible. The prototype units are accurate but very short.

| # | Where | Severity | Finding | Status |
|---|---|---|---|---|
| 1 | Lesson 8, "Replication and sample size" and worked example; item `genetics-8:sample-size` solution; card | misleading | The lesson recommended at least 4 replicates per group right after saying the normal approximation runs low. Exact t-test power at n = 4 (σ = 0.5, δ = 1.0) is about 66%, and 6 per group are needed for 80%. | Fixed in 0.4.2: reading, worked example, item solution, card and lesson summary |
| 2 | Lesson 8, σ = 0.8 case | unclear | "Gives 10.0, so 11 per group": the value is 10.05, and the exact t-test needs 12. | Fixed in 0.4.2 |
| 3 | Lesson 7, map functions | unclear | "Kosambi's function ... gives intermediate values" gave no number. | Fixed in 0.4.2: 22.4 cM, close to the 22.6 cM interval sum |
| 4 | Item `genetics-7:outer-underestimate`; lesson 7 summary | unclear | Used 0.23 where the reading uses the unrounded 0.226. | Fixed in 0.4.2 |
| 5 | Lesson 6, twin and SNP heritability | suggestion | Called the twin versus SNP-based gap "missing heritability" without qualification. | Reworded in 0.4.2 ("part of what is called") |
| 6 | Lesson 8 | typo | "a 80% knockdown" | Fixed in 0.4.2 |
| 7 | Course limitations shown to learners | misleading | Described "a single formative check per lesson" and the prototype's numerical rules. Similar stale text was in every other package; geroscience, for example, still said it had no 14-week schedule. | Fixed in every affected package (x.y.1 versions) |

## For a human reviewer

- Units 1 to 4 are 60- to 80-word prototype readings. Their eight objectives are not linked to any
  course outcome.
- Lessons 5 to 8 have no "Common mistakes" section, unlike the later lessons.
- Outcome 4 ("Design a controlled gene-expression experiment") is assessed only by choice and numeric
  items. A design task with a rubric would test it more directly.
- Judgements left to a geneticist: whether the cautions in the heritability and polygenic-score lesson
  are balanced, whether the Mendelian-randomization sensitivity methods named are the right ones to
  teach first, and whether the synthetic numbers are realistic enough.
