# AI-assisted check: Biomaterials & Tissue Engineering 0.3.0

**This is not a human review.** It was run on 2026-10-08 by an AI coding assistant (Claude Sonnet 5.5 in
Claude Code) on material that the same kind of system had just written, so it is not independent and may
share that material's blind spots. It changes no maturity or review label. The package remains `partial`,
unreviewed and formative-only.

- **Version checked:** the working tree that became 0.3.0.
- **Scope:** lessons 7 to 13 (protein adsorption and wettability; hydrogel networks, modulus and mesh size;
  polymer chain scission and erosion mode; vascular scaffold wall stress, collapse and wall shear; biocompatibility
  evidence and the unit of analysis; cells for a scaffold, seeding and expansion; reading a failure in a degrading
  vascular scaffold), the degradation time-course lab (reading, dataset and eight items), the schedule, the
  learner-facing limitations and the syllabus. It also covers the numerical keys of the earlier lessons 2, 5 and
  6. All 63 new items were checked.
- **Not checked:** teaching depth and sequencing, Bloom labels, accessibility, the text of the earlier lessons 5
  and 6, and the textbook-level statements listed below, which cite no source.

## Method

1. Every numerical key in the package (all 59 numeric items, old and new, and the numeric field of the lab's
   data-interpretation item) was recomputed independently from the numbers in its prompt, with constants written
   out. The calculations are kept as tests in `tests/content/test_ai_assisted_checks.py`, which also asserts that
   every numeric item is covered.
2. Numbers that the lessons quote but no item asks for were recomputed too, by writing the expected sentence
   fragments from independent formulas and requiring them in the rendered text: contact angles and work of
   adhesion, adsorbed amounts and arrival times, mesh sizes and diffusion ratios, the chain-scission table and
   the onset of mass loss, buckling pressures, flow and shear factors, the animal-level t statistic and its
   p-value and interval (with a t distribution that shares no code with the generator), the cell-number and
   passage arithmetic, the local pH, and every worked example.
3. The lab keys were recomputed from the lab CSV with separate code: the replicate means, the fraction of bonds
   cleaved, the scission rate constant, the modulus half-time, the time to a modulus threshold and the first
   sampled day with mass loss. The data recover the rate constants they were built from (0.0002 per bond per day
   and 0.02 per day) to within 0.1%.
4. All 63 new items were graded with the real grader using a correct response: 63 of 63 earned full credit on the
   first run. Units that the grader does not support (kPa, mmHg, kDa, mN/m, degrees, days) were avoided by asking
   for a number only.
5. Each lesson was read as rendered, for accuracy, internal consistency and overclaiming.

## Results

No answer key in the package was wrong, including the 10 older numeric keys. Seven drafting problems were found
and fixed before the version was committed:

| # | Where | Severity | Finding | Status |
|---|---|---|---|---|
| 1 | Lesson 9 | misleading | A first choice of rate constant (0.0005 per bond per day) halved the molar mass in 1.4 days and began mass loss at 28 days, which would give a wrong sense of scale for a design meant to last about ten weeks. | Lowered to 0.0002 per day, so mass loss begins at 69 days |
| 2 | Lesson 7, worked example | unclear | Step 3 contained a placeholder phrase and an expression in raw exponent notation. | Written out in full with superscripts |
| 3 | Lessons 7 and 8 | unclear | Some expressions put a product in a denominator without brackets (`/ 8.0 × 10⁻¹¹`). | Bracketed |
| 4 | Lesson 10 | unclear | The pulse-strain line carried a confusing unit factor. | Rewritten with units |
| 5 | Lesson 11 | cosmetic | Per-animal data were printed as Python lists, and a reference to "the lesson on variability" did not say that it is in the statistics course. | Plain lists, course named |
| 6 | Lab | misleading | Mean mass values above 100% appeared without explanation. | A note says the values reflect weighing variability |
| 7 | Lab item `supported-conclusions` | error | Its prompt duplicated the prompt of the biochemistry lab, which the validator rejects. | Reworded |

Two mistakes in the new test code itself (a per-100 mmHg conversion and a bold marker) were also found and fixed;
neither involved a key.

## Statements without a cited source

The package adds no references. These statements and values are at textbook level, and a reviewer should
confirm that each is acceptable as stated: Young's equation and the work of adhesion, the Langmuir isotherm,
typical protein sizes and diffusion coefficients, and the illustrative plasma-like concentrations (lesson 7);
ideal rubber elasticity, E ≈ 3G, the mesh-size scaling (k_B T/G)^(1/3) and the Stokes–Einstein relation
(lesson 8); the random-scission relation 1/Mn = 1/Mn0 + p/M_u, the lag model for mass loss and the critical
thickness √(D/k), which is a heuristic (lesson 9); Laplace's law, the buckling pressure of a long thin tube and
Poiseuille flow, with a native artery described as typically more distensible than a synthetic tube (lesson 10);
the description of the host response and of ISO 10993 as the series on biological evaluation of medical devices
(lesson 11); cell volume, the finite division of primary cells and phenotype change with expansion (lesson 12);
and the statement that polyester degradation products are acids that can lower local pH (lesson 13).

## For a human reviewer

- Lesson 13 models the course case (a degradable vascular scaffold that narrows) with three hypotheses and a
  list of separating measurements. A biomaterials scientist should judge whether the list is the right minimum
  and whether the first-order models are acceptable for the purpose; it is explicitly not a protocol.
- The lab's modulus decays exponentially and its mass follows a lag model, both constructed. Real polymers show
  crystallinity and autocatalysis effects that this does not. Check that the pedagogy is acceptable.
- Lesson 11 uses a synthetic acceptance criterion of 70% viability as an example. Check that it is not read as
  a standard.
- Prototype units 1 to 4 are still 70 to 80 words each, and their eight objectives are linked to no course
  outcome. The earlier lessons 5 and 6 were not re-read in this pass.
