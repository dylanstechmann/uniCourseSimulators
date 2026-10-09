# AI-assisted check: Differential Equations for Living & Engineered Systems 0.3.0

**This is not a human review.** It was run on 2026-10-08 by an AI coding assistant (Claude Sonnet 5.5 in
Claude Code) on material that the same kind of system had just written, so it is not independent and may
share that material's blind spots. It changes no maturity or review label. The package remains `partial`,
unreviewed and formative-only.

- **Version checked:** the working tree that became 0.3.0.
- **Scope:** lessons 7 to 13 (forced first-order systems in a perfused chamber; resonance and damping of a
  spring–mass–damper; phase portraits of linear systems; the exact solution, fitting and extrapolation of logistic
  growth; linearization and bistability in a toggle switch; stiff equations and implicit methods; a fitted model that
  predicts negative counts), the decay-fitting lab (reading, dataset and eight items), the schedule, the
  learner-facing limitations and the syllabus. It also covers the numerical keys of the earlier lessons 1, 2, 4, 5
  and 6. All 71 new items were checked.
- **Not checked:** teaching depth and sequencing, Bloom labels, accessibility, the text of the earlier lessons 1
  to 6, and the textbook-level statements listed below, which cite no source.

## Method

1. Every numerical key in the package (all 74 numeric items, old and new, and the numeric field of the lab's
   data-interpretation item) was recomputed independently from the numbers in its prompt, with constants written
   out. The calculations are kept as tests in `tests/content/test_ai_assisted_checks.py`, which also asserts that
   every numeric item is covered. Where a lesson prints a closed form, the check used a different route: the
   perfused chamber, the spring–mass–damper (free decay and driven steady state), the linear flows, the logistic
   equation, the toggle switch and the Michaelis–Menten depletion were integrated numerically (fourth-order
   Runge–Kutta); the response to a pulse was integrated in two stages, switching the input at its edge; the
   steady-state amplitude and lag of the sinusoidal response were found by projecting the last period on a sine
   and a cosine; the Jacobians of the toggle switch were taken by finite differences; the explicit Euler limits
   were found by bisection on the sign and size of the amplification factor; and the thresholds and crossing times
   were found by bisection or interpolation of the simulated flow.
2. Numbers that the lessons quote but no item asks for were recomputed too, by writing the expected sentence
   fragments from independent formulas and requiring them in the rendered text: the attenuation and lag of a
   10 min feed cycle, the resonance peak position, the log decrement after ten cycles, the asymmetric states of the
   switch and their eigenvalues, the stiffness ratio and the number of explicit steps, the Euler results for four
   step sizes and the hold-out prediction, together with every worked example. The half-power width of the exact
   amplitude curve was also computed and agrees with the lesson's approximation 2ζωn to within 3% (6.15 against 6.0).
3. The lab keys were recomputed from the lab CSV with separate code: the means by time, the early-window decay
   rate, the straight line and its zero crossing, the two predictions at 48 h and the ratio of the observed to the
   predicted mean. The CSV was also checked to follow the model it was built from (means within 0.1 thousand cells,
   three wells at each of seven times).
4. All 71 new items were graded with the real grader using a correct response: 71 of 71 earned full credit on
   the first run. Units that the grader does not support (rad/s, h⁻¹, per-hour rates, mM/h) were avoided by asking
   for a number only where needed.
5. Each lesson and the lab were read once as rendered, for accuracy, internal consistency and overclaiming.

## Results

No answer key in the package was wrong, including the 14 older numeric keys. Seven drafting problems were found and
fixed before the version was committed:

| # | Where | Severity | Finding | Status |
|---|---|---|---|---|
| 1 | Lesson 10 | error | It said that the exponential forecast at 72 h exceeds the carrying capacity of the culture. The forecast is 7.32 million cells, which is below the capacity of 8 million. | The comparison now uses 96 h (24.3 million, three times the capacity) |
| 2 | Lesson 10, half-capacity line | unclear | The sentence read "the exponential term equals 1/39... precisely when", which is not a sentence and not correct as written. | Rewritten: the denominator equals 2, so ((K − N₀)/N₀)e^(−rt) = 1 |
| 3 | Lesson 10, common mistakes | unclear | One bullet about the half-capacity time was garbled ("not symmetric in time about that point only in the sense of the logit"). | Replaced by a numerical comparison: the 90% time is 1.6 times the half-capacity time |
| 4 | Lesson 11 | unclear | The definition of the Jacobian entries was garbled ("∂/∂y of … in magnitude"). | Rewritten with explicit c_y and c_x |
| 5 | Lesson 12 | minor | It said that the slow mode "needs about 40 h" although its time constant is 20 h. | States both time constants (0.02 h and 20 h) |
| 6 | Lesson 7 | unclear | "Two hours after the switch it is still within 5% of the change" could be read as the opposite of what is meant. | Now reads "has covered only 95% of the change" |
| 7 | Lesson 9, item `determinant` | error | The hint ("ad − bc.") was shorter than the schema's minimum, which failed validation of the whole course. | Hint rewritten |

Two mistakes in the new test code itself (a spiral crossing tested in the wrong direction, and a pulse integrated
across its edge so that the fourth decimal of the simulation disagreed with the exact value) were also found and
fixed; neither involved a key.

## Continuation check by Codex (2026-10-08)

Codex recovered Claude's completed verification log and reread lessons 7 to 13 and the lab before finishing
this staged pass. This is another AI-assisted check, not qualified human review. It found five additional
issues and corrected them without changing any numerical answer key or tolerance:

1. Lesson 12 rounded a strict Euler stability bound to 250 equal steps over 10 h. The fast eigenvalue requires
   at least 251; 250 gives a growing amplification factor. The recalculation test now uses the smallest integer
   strictly above the bound and explicitly checks amplification on both sides.
2. Lessons 12 and 13 and a retrieval card called the Euler boundary strictly positive. At equality it reaches
   zero. They now distinguish nonnegativity from positivity, and decay in magnitude from monotone decay.
3. Lesson 9's classification included repeated eigenvalues despite its stated distinct-eigenvalue scope, and
   called every singular matrix's equilibrium set a line. It now separates the repeated-root boundary and
   includes the zero matrix's whole plane of equilibria.
4. Lesson 13 called the two fits indistinguishable, although its own hold-out calculation exposes a difference.
   It now describes the different residuals and the missing measurement-error model.
5. Lesson 8 omitted the damping condition for a nonzero-frequency amplitude peak, conflated that peak with the
   natural frequency's 90-degree phase crossing, and used the direct-force response to explain base excitation.
   It now states the damping condition and distinguishes the forcing mechanisms.

Fresh verification and exact results are recorded in `docs/VALIDATION_REPORT.md` and the workspace's
`PROGRESS.md`. The original drafting checks above remain attributed to Claude.

## Statements without a cited source

The package adds no references. These statements and values are at textbook level, and a reviewer should confirm
that each is acceptable as stated: the integrating-factor solution and the step, ramp, sinusoidal and decaying
responses of a first-order system (lesson 7); the free and forced solutions of the damped oscillator, the
logarithmic decrement, the quality factor, the half-power width ≈ 2ζω_n and the remark on vibration isolation
(lesson 8); the trace and determinant classification of planar linear systems (lesson 9); the exact solution of the
logistic equation, the doubling time, the maximum growth rate rK/4 and the logit linearization, and the statement
that a straight-line fit to the early window gives a slightly low rate (lesson 10); the two-gene toggle switch with
cooperativity 2 as a minimal model of a binary fate decision, with its threshold a = 2 (lesson 11); the stability
and positivity limits of explicit Euler, the stiffness ratio, the implicit solution of the Michaelis–Menten
depletion and the condition for the quasi-steady-state treatment (lesson 12); and the validation list of the
capstone (lesson 13). The rate constants, damping ratios and masses are illustrative inputs, not properties of any
real system.

## For a human reviewer

- Lesson 9 classifies the equilibria of planar linear systems with distinct eigenvalues and says that repeated
  eigenvalues need further tools; a mathematician should judge whether that is acceptable for a first treatment.
- Lesson 11 uses a symmetric, dimensionless toggle switch and speaks of memory and a binary fate. A cell biologist
  should judge the wording, since a stable state of a deterministic model is not a statement about any real cell.
- Lesson 12 covers explicit and implicit Euler only. A numerical analyst should judge whether the statement that
  higher-order and adaptive methods have different limits is enough.
- Lesson 13 and the lab contrast a constant-loss line with a first-order decay and attribute the slow late decline
  in the lab data to part of the population decaying more slowly. That is one explanation among several, and the lab
  says so.
- Prototype units 1 to 4 are still 67 to 72 words each. The earlier lessons 5 and 6 were not re-read in this pass.
