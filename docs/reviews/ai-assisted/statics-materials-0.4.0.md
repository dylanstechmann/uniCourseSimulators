# AI-assisted check: Statics & Mechanics of Materials 0.4.0

**This is not a human review.** It was run on 2026-10-08 by an AI coding assistant (Claude Sonnet 5.5 in
Claude Code) on material that the same kind of system had just written, so it is not independent and may
share that material's blind spots. It changes no maturity or review label. The package remains `partial`,
unreviewed and formative-only.

- **Version checked:** the working tree that became 0.4.0.
- **Scope:** lessons 7 to 13 (stress concentrations; fatigue, S–N curves and cumulative damage; buckling of
  slender struts; principal stresses, Mohr's circle and yield criteria; beam deflection and the flexural
  modulus; brittle strength and the Weibull distribution; a failure analysis and accelerated test plan for a
  scaffold that collapses under cyclic perfusion), the fatigue-lives lab (reading, dataset and eight items),
  the schedule, the learner-facing limitations and the syllabus. It also covers the numerical keys of the
  earlier lessons 1 to 6. All 68 new items were checked.
- **Not checked:** teaching depth and sequencing, Bloom labels, accessibility, the text of the earlier lessons 1
  to 6, and the textbook-level statements listed below, which cite no source.

## Method

1. Every numerical key in the package (all 74 numeric items, old and new, and the numeric field of the lab's
   data-interpretation item) was recomputed independently from the numbers in its prompt, with constants written
   out. The calculations are kept as tests in `tests/content/test_ai_assisted_checks.py`, which also asserts that
   every numeric item is covered. The design diameter of a strut, the 1% stresses of the Weibull distribution
   and the fitted line of the lab were found by bisection or least squares, not by the closed forms that the
   lessons print.
2. Numbers that the lessons quote but no item asks for were recomputed too, by writing the expected sentence
   fragments from independent formulas and requiring them in the rendered text: the net-section stress and the
   notch factors, the cycle table and Miner's sum, the Euler loads for doubled length and fixed ends, the
   transition slenderness, the shear stress and the three-dimensional maximum shear on the Mohr's circle
   example, the Tresca factor of safety, the beam deflections under a tip load and a uniform load, the span-to-
   thickness ratios, the flaw-size strengths, the six-specimen Weibull fit, the days a test takes at 10 Hz, the
   heating bounds at 1 and 10 Hz and the life factor for a 25% higher amplitude, together with every worked
   example.
3. The lab keys were recomputed from the lab CSV with separate code: the specimen and failure counts, the mean
   log life of the failures at each level, the standard deviation at 260 MPa, the fitted slope and exponent, the
   predicted life at 160 MPa and the mean with the run-outs counted at the cutoff. The CSV was also checked to
   follow the Basquin line it was built from (level means within 0.05 in log10 life, spread between 0.1 and
   0.25), to have exactly two run-outs, both at the cutoff, and no failure at or above the cutoff.
4. All 68 new items were graded with the real grader using a correct response: 68 of 68 earned full credit on
   the first run. Units that the grader does not support (N/mm, mm⁴, mK/s, degrees) were avoided by asking for a
   number only.
5. Each lesson and the lab were read once as rendered, for accuracy, internal consistency and overclaiming, and
   the stored item prompts were read once for ambiguity.

## Results

No answer key in the package was wrong, including the 17 older numeric keys. Eleven drafting problems were found
and fixed before the version was committed:

| # | Where | Severity | Finding | Status |
|---|---|---|---|---|
| 1 | Lesson 7 | error | It said that sharper notches have a notch sensitivity closer to 1. Notch sensitivity falls as the root radius shrinks, so the statement was reversed. | Replaced by the correct trends (stronger materials and larger radii give q nearer 1; a very sharp notch in a ductile metal has a lower q) |
| 2 | Lesson 8, worked example | error | The blocks of 20,000 and 300,000 cycles gave a Miner sum of 8.2, and the last step reported 824% of the life used and a remaining life of −724%. | Blocks of 2,000 and 15,000 cycles (sum 0.535, 54% used) |
| 3 | Lesson 8, scatter paragraph | error | It said that counting a run-out as a failure at the cutoff biases the life upward. The true life is longer than the cutoff, so that treatment biases it downward, as dropping the run-outs does. | Corrected, and now consistent with the lab |
| 4 | Item `statics-materials-11:central-deflection` | error | A string method lower-cased the prompt, so the modulus read "e = 3000 mpa". Found when the stored prompts were read. | Prompt built with the correct symbol and unit |
| 5 | Item `statics-materials-13:time-to-2K` | error | The id contained a capital letter, which the schema rejects, so the whole course failed validation. | Renamed `time-to-2k` |
| 6 | Lesson 13 | inconsistency | The section on reading outcomes compared wet lives with a dry control that the test plan did not contain. | A dry control was added to the plan (45 to 50 specimens), with a test pin on the total |
| 7 | Lesson 10 | unclear | One sentence about the third principal stress in plane stress was garbled, and the worked example printed "+ −33.15²". | Rewritten with the three-dimensional maximum shear (46.21 MPa, above the in-plane 42.43 MPa) and the reason Tresca uses all three differences; parentheses added |
| 8 | Lessons 9, 11 and 12 | minor | The buckling worked example sits just below the transition slenderness (21 against 22.21) without saying that the real capacity is lower; the thicker strip in the beam example has a span-to-thickness ratio of 15.7, under the usual 16; "modulus" meant the Weibull modulus in some sentences and the elastic modulus in others. | Caveats added and the terms made explicit |
| 9 | Lesson 13 | cosmetic | Lives were printed to seven figures (for example 7,487,914 cycles). | Written in millions of cycles |
| 10 | Lab | cosmetic | The worked calculation printed 1.8e+07 (raw exponent notation) and hyphens before negative numbers; the stored upload check carried 15-digit floats. | Written as 18 million cycles, minus signs typeset, check values rounded to six decimals |
| 11 | Items | clarity | Twenty-two follow-up prompts referred to a previous item ("that state", "the same strip", "at that rate"), so they could not be read on their own. | Each prompt now restates the data it needs |

One mistake in the new test code itself (an expected string with a stray trailing zero) was also found and fixed; it
involved no key.

## Statements without a cited source

The package adds no references. These statements and values are at textbook level, and a reviewer should confirm
that each is acceptable as stated: the stress concentration factors of a circular and an elliptical hole and the
notch relation K_t ≈ 1 + 2√(a/ρ), the fatigue notch factor K_f = 1 + q(K_t − 1) and the trends of q (lesson 7);
Basquin's law, the Goodman line, Miner's rule, the statement that fatigue lives scatter by a factor of several to
ten or more, and that many polymers have no endurance limit (lesson 8); Euler's formula, the effective-length
factors 1, 0.5, about 0.7 and 2, the transition slenderness and the effect of imperfections (lesson 9); the
transformation equations, Mohr's circle, the Tresca and von Mises criteria, the statement that they differ by at
most about 15%, and that von Mises is usually closer in torsion (lesson 10); the standard deflection formulas,
the three-point flexural modulus, the span-to-thickness rule of thumb of 16 and the 10% limit for small
deflection (lesson 11); the Weibull distribution, the range of about 5 to 20 for many ceramics, the flaw-size
relation σ_f = K_Ic/(Y√(πa)), the ranked-probability estimate of the modulus and the statement that standards for
ceramics call for tens of specimens (lesson 12); and the hysteretic heating formula W = π σ_a ε_a sin δ with its
adiabatic bound (lesson 13). The strut amplification factor, the Basquin constants, the loss of strength and the
dissipation in lesson 13 are illustrative inputs, not properties of any real material.

## For a human reviewer

- Lesson 8 treats mean stress with the Goodman line only. A materials engineer should judge whether that is
  acceptable for a first treatment, and whether the sentence on run-outs and the lab's handling of them are
  right.
- Lesson 13 lists a test plan (specimen counts, controls, stopping criteria and the adiabatic heating check). A
  person who runs fatigue tests should judge whether the minimum set of controls is right and whether the
  statement that the estimate is an upper bound on the heating rate is stated clearly enough.
- The lab fits only the three levels without run-outs. Real data would be analyzed with a method that uses the
  run-outs directly (maximum likelihood with censoring), which the lab names and does not teach.
- Lesson 12 estimates the Weibull modulus from six specimens only to show how uncertain that is; check that the
  warning is clear.
- Prototype units 1 to 4 are still 67 to 82 words each. The earlier lessons 5 and 6 were not re-read in this
  pass.
