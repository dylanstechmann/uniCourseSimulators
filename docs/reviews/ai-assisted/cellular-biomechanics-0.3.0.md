# AI-assisted check: Cellular Biomechanics & Mechanobiology 0.3.0

**This is not a human review.** It was run on 2026-10-08 by an AI coding assistant (Claude Sonnet 5.5 in
Claude Code) on material that the same kind of system had just written, so it is not independent and may
share that material's blind spots. It changes no maturity or review label. The package remains `partial`,
unreviewed and formative-only.

- **Version checked:** the working tree that became 0.3.0.
- **Scope:** lessons 7 to 13 (oscillatory rheology; micropillar traction forces; bonds under force and the
  molecular clutch; cortical tension and micropipette aspiration; the Hill function and stiffness
  dose–response; applying strain to cells; decoupling stiffness from ligand density), the stiffness and
  ligand-density lab (reading, dataset and eight items), the schedule, the learner-facing limitations and the
  syllabus. It also covers the numerical keys of the earlier lessons 5 and 6. All 64 new items were checked.
- **Not checked:** teaching depth and sequencing, Bloom labels, accessibility, the text of the earlier lessons 5
  and 6, and the textbook-level statements listed below, which cite no source.

## Method

1. Every numerical key in the package (all 61 numeric items, old and new, and the numeric field of the lab's
   data-interpretation item) was recomputed independently from the numbers in its prompt, with constants written
   out. The calculations are kept as tests in `tests/content/test_ai_assisted_checks.py`, which also asserts that
   every numeric item is covered. The midpoint slope of the Hill curve was checked by numerical differentiation
   and the stiffness for a given response by bisection.
2. Numbers that the lessons quote but no item asks for were recomputed too, by writing the expected sentence
   fragments from independent formulas and requiring them in the rendered text: the storage and loss moduli
   table, the pillar stiffness and forces, the bond lifetimes and critical stiffness, the aspiration pressures,
   the Hill responses, the strain measures and the variance-inflation and standard-error arithmetic, together
   with every worked example.
3. The lab keys were recomputed from the lab CSV with separate code: the gel means and counts, the main effect,
   the ligand effect, the interaction, and both standard errors. The CSV was also checked to carry the condition
   means and the between-gel spread that it was built from.
4. All 64 new items were graded with the real grader using a correct response: 64 of 64 earned full credit on the
   first run. Units that the grader does not support (kPa, nN/μm, pN·nm, mN/m) were avoided by asking for a
   number only.
5. Each lesson was read as rendered, for accuracy, internal consistency and overclaiming.

## Results

No answer key in the package was wrong, including the 9 older numeric keys. Four drafting problems were found
and fixed before the version was committed:

| # | Where | Severity | Finding | Status |
|---|---|---|---|---|
| 1 | Lab | error | The first dataset had a between-gel spread much smaller than the cell-to-cell noise, so the cell-level standard error came out larger than the gel-level one (1.98 against 1.63), which contradicted the lab's point, and the generated explanation said "about 0.8 times smaller". | Between-gel spread raised to ±6 units; the gel-level error is 4.90 and the cell-level error 2.32, which is 2.1 times too small |
| 2 | Lesson 10 | cosmetic | The tension was printed as `4.0e-04 N/m` in raw exponent notation. | Written as 4.0 × 10⁻⁴ N/m |
| 3 | Lesson 11 | cosmetic | A sentence read "a fourfold increase in stiffness (4-fold)". | Duplicate removed |
| 4 | Lesson 8 | cosmetic | The modulus was printed as 2000000 in the stiffness formula. | Written as 2.0 × 10⁶ |

Two mistakes in the new test code itself (a typed expectation that rounded one response differently and a bold
marker around a whole expression) were also found and fixed; neither involved a key.

## Statements without a cited source

The package adds no references. These statements and values are at textbook level, and a reviewer should confirm
that each is acceptable as stated: the definitions of the storage and loss moduli, the Maxwell element and the
relation E = 2(1 + ν)G (lesson 7); the Euler–Bernoulli stiffness of a cylindrical cantilever and the PDMS-like
modulus (lesson 8); the Bell relation for slip bonds, the constant-loading-rate picture and the resulting critical
stiffness, which is an illustration (lesson 9); the liquid-drop (Laplace) model of micropipette aspiration and the
order of magnitude of cortical tension (lesson 10); the Hill function as an empirical description (lesson 11);
engineering and true strain, the Poisson contraction of an incompressible elastomer and the strain rate of a
sinusoid (lesson 12); and the variance inflation factor and the photobleaching relation D ≈ 0.224 w²/t½ for a
circular spot (lesson 13).

## For a human reviewer

- Lesson 13 models the course case (a stiffness change confounded with ligand mobility) with a variance
  inflation calculation, a photobleaching measurement of mobility and a crossed design. A biomechanics or
  materials scientist should judge whether independent control of stiffness, ligand density and mobility is
  realistic and whether the outline of the characterization is complete.
- Lesson 9 gives a critical stiffness from a deliberately simple clutch model. Check that it is read as an
  illustration of the logic, as the lesson says.
- The lab's gel means are constructed with a fixed spread of −6, 0 and +6 units and cell offsets from a fixed
  pattern; real data are skewed and noisier. Check that the pedagogy is acceptable.
- Prototype units 1 to 4 are still 70 to 75 words each, and their eight objectives are linked to no course
  outcome. The earlier lessons 5 and 6 were not re-read in this pass.
