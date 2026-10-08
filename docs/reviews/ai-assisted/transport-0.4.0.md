# AI-assisted check: Thermodynamics & Transport in Bioengineering 0.4.0

**This is not a human review.** It was run on 2026-10-08 by an AI coding assistant (Claude Sonnet 5.5 in
Claude Code) on material that the same kind of system had just written, so it is not independent and may
share that material's blind spots. It changes no maturity or review label. The package remains `partial`,
unreviewed and formative-only.

- **Version checked:** the working tree that became 0.4.0.
- **Scope:** lessons 7 to 13 (transient diffusion and the error function; advection, diffusion and the Péclet
  number; oxygen in a spheroid with an anoxic core; Michaelis–Menten uptake and the limits of zero order; lumped
  heat transfer and the Biot number; residence time and tanks in series; a perfused construct with a hypoxic
  center), the oxygen depth-profile lab (reading, dataset and eight items), the schedule, the learner-facing
  limitations and the syllabus. It also covers the numerical keys of the earlier lessons 1 to 6. All 62 new
  items were checked.
- **Not checked:** teaching depth and sequencing, Bloom labels, accessibility, the text of the earlier lessons 5
  and 6, and the textbook-level statements listed below, which cite no source.

## Method

1. Every numerical key in the package (all 67 numeric items, old and new) was recomputed independently from the
   numbers in its prompt, with constants written out. The calculations are kept as tests in
   `tests/content/test_ai_assisted_checks.py`, which also asserts that every numeric item is covered.
2. Numbers that the lessons quote but no item asks for were recomputed too, by writing the expected sentence
   fragments from independent formulas and requiring them in the rendered text. This includes the
   complementary error function table and its inverse (by bisection), the anoxic-core radii of spheres (by
   bisection on the cubic that fixes them, which the stated values are checked to satisfy), the table of
   Michaelis–Menten slab minima (by a separate Runge–Kutta shooting solver, against the library solver used to
   write the table), the lumped heat-transfer and Biot numbers, the tanks-in-series response, and every
   worked example. The Krogh-cylinder radial drop was also checked by integrating the stated concentration
   gradient numerically.
3. The lab keys were recomputed from the lab CSV with separate code, and every reading in the CSV was checked
   against the zero-order profile it was built from to within the stated noise. The fit recovers the consumption
   rate (0.020 mol/(m³·s)) and the critical thickness (200 μm) that the data were built from.
4. All 62 new items were graded with the real grader using a correct response: 62 of 62 earned full credit on the
   first run. Units that the grader does not support (kPa, minutes as a rate) were avoided by asking for a number
   only.
5. Each lesson was read as rendered, for accuracy, internal consistency and overclaiming.

## Results

No answer key in the package was wrong, including the 17 older numeric keys. Five drafting problems were found
and fixed before the version was committed:

| # | Where | Severity | Finding | Status |
|---|---|---|---|---|
| 1 | Lesson 9, worked example | error | It asked for the central concentration at 250 μm, which is above that example's own critical radius (212 μm), so the answer was negative. | Radius changed to 180 μm |
| 2 | Lesson 9 | unclear | The explanation of why the living rim is thicker than the slab's critical thickness ("converging geometry concentrates the supply") was imprecise and omitted that the rim thins toward 200 μm as the sphere grows. | Rewritten, with the value at 600 μm |
| 3 | Lesson 8 | cosmetic | One sentence printed `2e+05 cells/cm²` in raw exponent notation, which the repository's formatting guard rejects. | Written as 2.0 × 10⁵ |
| 4 | Lesson 13 | unclear | "The center of the cylinder is well supplied" is ambiguous, since the axis of the cylinder is the channel. | "The tissue farthest from the channel" |
| 5 | Lesson 10 | cosmetic | "Below about 180 μm" understated the range over which the two kinetics models agree. | "Up to about 180 μm" |

## Statements without a cited source

The package adds no references. These statements and values are at textbook level, and a reviewer should confirm
that each is acceptable as stated: the order-of-magnitude diffusion time and the error-function solution for a
semi-infinite medium (lesson 7); the Sherwood number of 3.66 for fully developed laminar tube flow, the Schmidt
number scaling of the concentration boundary layer, and the statement that the mass-transfer coefficient of
fully developed laminar flow does not depend on the flow rate (lesson 8); the zero-order solution for a sphere
with an anoxic core and the rim thicknesses derived from it (lesson 9); Michaelis–Menten kinetics with an
illustrative K_m of 5 μM, and the statement that cells lose function at oxygen levels well above K_m (lesson
10); the lumped-capacitance model, the rule of thumb of 0.1 for the Biot number, the heat-transfer coefficients
of 10 and 500 W/(m²·K), and the internal time constant R²/(π²α) of a sphere (lesson 11); the tanks-in-series
model of imperfect mixing (lesson 12); and the Krogh-cylinder model with a uniform channel concentration at each
axial position (lesson 13).

## For a human reviewer

- Lesson 13 models the course case (a perfused construct with a hypoxic center) as one channel and its Krogh
  cylinder with radial and axial losses. A transport engineer should judge whether this is a sound outline, in
  particular the neglect of axial diffusion, of consumption in the lumen and of saturable uptake.
- The table in lesson 10 comes from a numerical solution of a one-dimensional steady model; check the
  interpretation that the zero-order critical thickness is a first estimate.
- In the lab, oxygen readings below 0.03 mol/m³ carry no noise, so the replicates coincide there. Real
  microsensor readings would scatter at all depths; check that this simplification is acceptable.
- Prototype units 1 to 4 are still 70 to 80 words each, and their eight objectives are linked to no course
  outcome. The earlier lessons 5 and 6 were not re-read in this pass.
