# AI-assisted check: Human Physiology for Engineers 0.4.0

**This is not a human review.** It was run on 2026-10-08 by an AI coding assistant (Claude Sonnet 5.5 in
Claude Code) on material that the same kind of system had just written, so it is not independent and may
share that material's blind spots. It changes no maturity or review label. The package remains `partial`,
unreviewed and formative-only.

- **Version checked:** the working tree that became 0.4.0.
- **Scope:** lessons 8 to 14 (balance and feedback gain; membrane potential; hemodynamics; respiratory mechanics
  and gas exchange; muscle mechanics; tissue repair; compensation and reserve), the scratch-assay lab (reading,
  dataset and seven items), the schedule, the learner-facing limitations and the syllabus. It also covers the
  numerical keys of the earlier lessons 1, 2, 4, 5, 6 and 7. All 56 new items were checked.
- **Not checked:** teaching depth and sequencing, Bloom labels, accessibility, whether the synthetic values are
  realistic for any particular person or tissue, and the textbook-level statements listed below, which cite no
  source.

## Method

1. Every numerical key in the package (all 57 numeric items, old and new) was recomputed independently from the
   numbers in its prompt, with constants written out (R, T, F for the Nernst and Goldman–Hodgkin–Katz values,
   and series or parallel combinations for resistance and compliance). The calculations are kept as tests in
   `tests/content/test_ai_assisted_checks.py`. A test also asserts that every numeric item in the package is
   covered.
2. The lab keys (the 9-cell summary upload and the interpretation, ratio and edge-speed items) were recomputed
   from the lab CSV in `tests/content/test_new_geroscience_and_statistics_lessons.py`.
3. The closed-form load of maximum muscle power (about 0.31 of maximum force for Hill's a/F₀ = 0.25) was
   checked against a grid search over force: both give 154.5 N and 19.1 W.
4. All 56 new items were graded with the real grader using a correct response: 56 of 56 earned full credit.
5. Each lesson was read twice, once after drafting and once as rendered, for accuracy, internal consistency and
   overclaiming.

## Results

No answer key in the package was wrong, including the 17 older numeric keys. Five problems were found in the
drafts and fixed before the version was committed:

| # | Where | Severity | Finding | Status |
|---|---|---|---|---|
| 1 | Lesson 8, exercise example | misleading | Heat loss at the start of exercise was called "resting-like" at 8 kJ/min, but resting heat production in the same lesson is 5 kJ/min. | Set to the resting value (5 kJ/min); the temperature-rise item and its key were recomputed |
| 2 | Lesson 13 | error | The first learning objective (ordering the healing phases) had no practice item. Found by the lesson-structure test. | Added a multi-select item on the phases |
| 3 | Lesson 10, item `bed-flow` | error | A hint of 9 characters violated the content schema, which made the whole question bank fail to load. Found by the validator. | Hint lengthened |
| 4 | Lesson 14 | unclear | Decimal formatting ("90 to 45.0") was inconsistent. | Fixed |
| 5 | Several items | design | The grader cannot parse some units (mmHg, °C, compliance and resistance units). | Those answers are entered as bare numbers and the prompt says so |

## Statements without a cited source

The package cites no papers. These general statements are at textbook level and a reviewer should confirm that
each is acceptable as stated: the phases and time scales of skin wound healing and the cell types in each
(lesson 13); that healing is on average slower in older adults and that several chronic conditions are
associated with slower healing (lesson 13); that arterial stiffness, muscle mass and maximum organ capacities
decline on average with age (lessons 10, 12 and 14); that power often declines faster than strength with age
(lesson 12); and that about 25 N/cm² is a representative specific tension (lesson 12, labelled synthetic).

## For a human reviewer

- Lesson 14 models the course case (pressure held, renal perfusion reduced, sympathetic activity raised) with
  parallel beds and a capped output. A physiologist should judge whether "weaker pump compensated by
  vasoconstriction" is a fair simple model for the case and whether the stated measurements are the right ones
  to name.
- Lesson 9 omits chloride from the Goldman–Hodgkin–Katz example and gives a conductance-weighted version with
  arbitrary relative conductances. Check that the two are not presented as equivalent.
- The lab is idealized (straight gap, four tidy experiments, a clean division block). It teaches reasoning, not
  analysis of real images.
- Prototype units 1 to 4 are still 60 to 80 words each, and their eight objectives are linked to no course
  outcome.
