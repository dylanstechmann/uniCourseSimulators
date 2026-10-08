# AI-assisted check: Bioreactors & Tissue Culture Engineering 0.4.0

**This is not a human review.** It was run on 2026-10-08 by an AI coding assistant (Claude Sonnet 5.5 in
Claude Code) on material that the same kind of system had just written, so it is not independent and may
share that material's blind spots. It changes no maturity or review label. The package remains `partial`,
unreviewed and formative-only.

- **Version checked:** the working tree that became 0.4.0.
- **Scope:** lessons 7 to 13 (Monod growth and yield; chemostat washout and cell-specific perfusion; mixing and
  scale-up; shear, eddies and the Kolmogorov scale; dissolved-oxygen control and the capacity limit; factorial
  design of experiments; designing a scale-down experiment), the kLa gassing-out lab (reading, dataset and eight
  items), the schedule, the learner-facing limitations and the syllabus. It also covers the numerical keys of the
  earlier lessons 1, 2, 5 and 6. All 65 new items were checked.
- **Not checked:** teaching depth and sequencing, Bloom labels, accessibility, the text of the earlier lessons 5
  and 6, and the textbook-level statements listed below, which cite no source.

## Method

1. Every numerical key in the package (all 65 numeric items, old and new, and the numeric field of the lab's
   data-interpretation item) was recomputed independently from the numbers in its prompt, with constants written
   out. The calculations are kept as tests in `tests/content/test_ai_assisted_checks.py`, which also asserts that
   every numeric item is covered.
2. Numbers that the lessons quote but no item asks for were recomputed too, by writing the expected sentence
   fragments from independent formulas and requiring them in the rendered text: Monod rates and yield limits, the
   chemostat steady states and optimum, the stirred-vessel power, Reynolds number, tip speeds and mixing times
   under three scale-up criteria (including the scaling table), the Kolmogorov scales and stresses, the required
   kLa and the time to reach the ceiling, every effect, interaction and standard error of the factorial design, the
   oxygen excursions of the capstone, the power at 4, 5 and 6 cultures per group (with a t distribution that
   shares no code with the generator), and every worked example.
3. The lab keys were recomputed from the lab CSV with separate code: the replicate means, the kLa at each speed from
   the logarithmic form, the speed exponent, and the supportable density. The curves were built from
   kLa = 2.0 (N/200)^1.5 per hour and the fits recover it to within 0.1%.
4. All 65 new items were graded with the real grader using a correct response: 65 of 65 earned full credit on the
   first run. Units that the grader may not support (cells/mL, pL/(cell·day), W/kg, W/m³) were avoided by asking
   for a number only.
5. Each lesson was read as rendered, for accuracy, internal consistency and overclaiming.

## Results

No answer key in the package was wrong, including the 12 older numeric keys. Seven drafting problems were found
and fixed before the version was committed:

| # | Where | Severity | Finding | Status |
|---|---|---|---|---|
| 1 | Lesson 7 | misleading | The text and a multiple-select item said that doubling the starting glucose does not double the maximum density, although the lesson's own numbers give 6.05 against 3.05 (1.98-fold). | Now stated as roughly doubling the yield limit, with the caution that another factor can stop growth first; the false statement is "always doubles" |
| 2 | Lesson 8 | cosmetic | Steady-state symbols were written with asterisks (S*, X*) that a markdown renderer shows as `S\*`. | Renamed S_ss and X_ss |
| 3 | Lessons 9 and 10 | unclear | Cross-references to "the previous lesson" and "the next lesson" did not name the lessons they meant. | Named |
| 4 | Lesson 10 | unclear | The Kolmogorov expression had an unbalanced bracket, and a stress expression put a product in a denominator without brackets. | Rewritten |
| 5 | Lesson 11 | unclear | The lower-setpoint arithmetic mixed units, and a sentence cited "the critical level assumed in this package". | Written with units; "used in this lesson" |
| 6 | Lesson 13 | error | A sentence said that "the same fall takes 15 s" in the small vessel, which has the opposite meaning (the cell stays about 15 s, so the fall is smaller). | Corrected |
| 7 | Lab | misleading | A supportable density of exactly 4.245 was printed as 4.25 in the text but compared as 4.24 by an independent calculation, a rounding-boundary mismatch. | Printed with three decimals |

One mistake in the test helper itself was found too: the numerical integral used for Student's t is inaccurate at
2 degrees of freedom, which made the minimum significant effect of the factorial design come out as 0.32 against
the correct 0.30. The test now uses the exact closed form at 2 degrees of freedom. No content was affected.

## Statements without a cited source

The package adds no references. These statements and values are at textbook level, and a reviewer should confirm
that each is acceptable as stated: Monod kinetics and a constant yield, and the chemostat steady states and
washout condition (lessons 7 and 8); the cell-specific perfusion rate as a design quantity (lesson 8); the power
number of a pitched-blade impeller, the turbulent scaling laws for geometrically similar vessels and the
dimensionless mixing time, which is an illustrative value (lesson 9); the Kolmogorov scale and the stress at
that scale, the local dissipation factor of 100, which is illustrative, the proportionality of the maximum local
dissipation to power per volume in geometric similarity, and the empirical rule that damage becomes likely
when eddies are smaller than the particle or a fraction of it (lesson 10); air-saturation concentration, the
first-order oxygen time constant and the cascade ordering (lesson 11); two-level factorial analysis, aliasing
and the standard error of an effect (lesson 12); the zero-order oxygen fall in an unsupplied zone and the
dimensionless ratio of consumption to bulk oxygen over one mixing time (lesson 13); and the gassing-out
method (lab).

## For a human reviewer

- Lesson 13 models the course case (a viability gradient in a scaled-up perfusion culture) with a two-by-two
  scale-down comparison of environment and passage. A bioprocess engineer should judge whether the design is a
  sound outline and whether the zero-order excursion model is acceptable for the purpose; it is explicitly not a
  protocol or a validation plan.
- Lesson 10 uses an illustrative local dissipation factor of 100 and states that damage thresholds are empirical.
  Check that no threshold is read as a standard.
- The lab's curves are constructed from an exact exponential with a small additive noise; real curves also show
  gas-phase dynamics and probe lag. Check that the pedagogy is acceptable.
- Prototype units 1 to 4 are still 60 to 80 words each, and their eight objectives are linked to no course
  outcome. The earlier lessons 5 and 6 were not re-read in this pass.
