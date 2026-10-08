# AI-assisted check: Genetics & Genomics 0.5.0 (new material)

**This is not a human review.** It was run on 2026-10-08 by an AI coding assistant (Claude Sonnet 5.5 in
Claude Code) on material that the same kind of system had just written, so it is not independent and may
share that material's blind spots. It changes no maturity or review label. The package remains `partial`,
unreviewed and formative-only. The earlier check of the version 0.4.1 content is in
[genetics-0.4.1.md](genetics-0.4.1.md).

- **Version checked:** the working tree that became 0.5.0.
- **Scope:** lessons 10 to 15, the association lab (reading, dataset and seven items), the added
  "Common mistakes" sections of lessons 5 to 8, the schedule, the learner-facing limitations and the
  syllabus. The 43 new items and their keys were checked.
- **Not checked:** teaching depth and sequencing, Bloom labels, accessibility and rendering in the app,
  whether the synthetic numbers are realistic, and the references beyond the records and abstracts named
  below.

## Method

1. Every new numerical key (24 numeric items, plus the 12 cells of the lab summary upload and the 2 numeric
   fields of the lab's interpretation items) was recomputed independently, from the numbers stated in the
   prompt or from the lab CSV, and compared with the stored answer. The calculations are kept as tests in
   `tests/content/test_ai_assisted_checks.py` and `tests/content/test_new_geroscience_and_statistics_lessons.py`.
   The Benjamini–Hochberg and credible-set computations use separate step-up and cumulative-sum code.
2. All 43 new items were graded with the real grader using a correct response: 43 of 43 earned full
   credit.
3. The lab's claim that genotypes are close to Hardy–Weinberg proportions inside each stratum was tested:
   the worst of 12 strata has a chi-square of 1.41, below the 3.84 cutoff for one degree of freedom.
4. Each reading was read twice, once after drafting and once as rendered, for factual accuracy,
   overclaiming and consistency with its items and cards.
5. The four new references were resolved with the citation-check script (all four records exist). The
   abstracts of Kenyon 1993, Hassold and Hunt 2001, and Blokzijl 2016 were read for the sentence each
   supports. Luria and Delbrück 1943 has no abstract in PubMed and its scanned text was not read, so the
   lesson describes the experiment in standard textbook terms and says so.

## Results

No answer key was wrong. Seven problems were found in the drafts and fixed before the version was committed:

| # | Where | Severity | Finding | Status |
|---|---|---|---|---|
| 1 | Lesson 12, "Frequencies from error rates" | error | The draft said the per-product fractions equal the chance that an egg is disomic. In oogenesis only one product becomes the egg, so this is false for meiosis II errors. | Rewritten: per-product bookkeeping is separated from the per-egg argument |
| 2 | Lesson 10, worm longevity example | misleading | The draft attached the identity of daf-2 as an insulin/IGF-1-like receptor to the 1993 paper, which does not report it. | Now attributed to later work not part of the cited paper |
| 3 | Lesson 14, Benjamini–Hochberg example | misleading | The first example would not have shown that BH takes the largest passing rank, so ranks that miss their own threshold can still be called. | Example replaced; the step-up behaviour is explained and added to the common mistakes |
| 4 | Lesson 13, solution text of the rate item | unclear | "0.821/2 × 10⁸ × 10⁹" is ambiguous. | Grouped as 0.821/(2 × 10⁸) × 10⁹ |
| 5 | Lesson 11 | unclear | The X-inactivation sentence ("favour the variant X") was ambiguous; the father-to-son rule lacked its pseudoautosomal exception; one sentence pointed to lessons that do not exist. | Reworded or removed |
| 6 | Lesson 12 | unclear | A promise of a topic "covered in the mutation lesson" that lesson 13 does not cover. | Removed |
| 7 | Lab item `genetics-lab1:stratum-summary` | error | Row ids with capital letters violate the content schema, which made the whole question bank fail to load. Found by the validator. | Stratum labels are lowercase (a-case, a-control, b-case, b-control) |

## For a human reviewer

- Lesson 15 teaches fine-mapping as PIP = BF(i) / Σ BF(j) under a single causal variant and equal priors, and
  allele-specific expression with a normal approximation. Please judge whether this level of
  simplification is acceptable as a first exposure and whether the stated caveats are enough.
- The oogenesis paragraph of lesson 12 and the description of the fluctuation test in lesson 13 deserve a
  check by a geneticist against the primary sources (the 1943 paper was not read here).
- The lab uses an allelic test and a Mantel–Haenszel odds ratio on allele counts from 100 people. That
  treats the two alleles of a person as independent, which the lab says is acceptable only because
  genotypes are near Hardy–Weinberg proportions; a genotype-based test is the usual choice.
- Prototype units 1 to 4 are still 60 to 80 words each, and their eight objectives are linked to no
  course outcome.
