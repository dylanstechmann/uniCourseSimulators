# AI-assisted check: Signals, Systems & Feedback Control 0.4.0

**This is not a human review.** It was run on 2026-10-08 by an AI coding assistant (Claude Sonnet 5.5 in
Claude Code) on material that the same kind of system had just written, so it is not independent and may
share that material's blind spots. It changes no maturity or review label. The package remains `partial`,
unreviewed and formative-only.

- **Version checked:** the working tree that became 0.4.0.
- **Scope:** lessons 7 to 13 (poles, zeros and the final value; second-order systems and damping; Bode plots,
  decibels and delay; stability margins; PI control, tuning and integrator windup; sampling, aliasing and a
  discrete PI controller; a sensor filter that makes a fast loop oscillate), the step-test identification lab
  (reading, dataset and nine items), the schedule, the learner-facing limitations and the syllabus. It also
  covers the numerical keys of the earlier lessons 1, 2, 3, 5 and 6. All 71 new items were checked.
- **Not checked:** teaching depth and sequencing, Bloom labels, accessibility, the text of the earlier lessons 1
  to 6, and the textbook-level statements listed below, which cite no source.

## Method

1. Every numerical key in the package (all 73 numeric items, old and new, and the numeric field of the lab's
   data-interpretation item) was recomputed independently from the numbers in its prompt, with constants written
   out. The calculations are kept as tests in `tests/content/test_ai_assisted_checks.py`, which also asserts that
   every numeric item is covered. Where a lesson prints a closed form, the check used a different route: the step
   responses of the second-order systems were integrated numerically (fourth-order Runge–Kutta), the overshoot
   and peak time were read off the simulated peak, the crossover frequencies and margins were found by bisection on
   the complex frequency response, the aliased frequencies were found as the peak of a discrete Fourier transform
   of sampled cosines, and the discrete plant was stepped as a recursion.
2. A delay-differential simulation of the proportional incubator loop was added: it rings down at 90% of the
   ultimate gain computed from the gain margin, grows at 110%, and at the ultimate gain oscillates with the period
   2π/ω_pc that the lesson prints (3.85 min). This checks the gain margin, the phase crossover and the
   Ziegler–Nichols inputs together.
3. Numbers that the lessons quote but no item asks for were recomputed too, by writing the expected sentence
   fragments from independent formulas and requiring them in the rendered text: the partial-fraction
   coefficients and exact settling times, the poles and amplitude ratios of the pressure-line example, the Bode
   values of the cascade, the margin table for three gains, the table of tuning parameters, the Ziegler–Nichols
   settings and their (low) phase margin, the hold phase loss, the discrete update, the table of filter times and
   every worked example.
4. The lab keys were recomputed from the lab CSV with separate code: the settled rise, the gain, the delay, the
   interpolated 63.2% time, the time constant and the gain ratio. The CSV was also checked to follow the
   first-order-plus-delay response with gains 0.500, 0.485 and 0.460 °C/W (readings within 0.06 °C), to have two
   runs of 61 samples at each of three step sizes, and to carry the table in the lab text.
5. All 71 new items were graded with the real grader using a correct response: 71 of 71 earned full credit on
   the first run. Units that the grader does not support (rad/min, W/°C, °C/W, degrees, decibels) were avoided by
   asking for a number only.
6. Each lesson and the lab were read once as rendered, for accuracy, internal consistency and overclaiming.

## Results

No answer key in the package was wrong, including the 13 older numeric keys. Seven drafting problems were found and
fixed before the version was committed:

| # | Where | Severity | Finding | Status |
|---|---|---|---|---|
| 1 | Lab | error | The first dataset ran for 40 minutes, but with a 10-minute time constant the response is only 97.5% settled by then, so the "settled" rise was 2% low, the gains read 2 to 2.5% low and the 63.2% time came out at 10.6 min instead of 11. | The record runs for 60 minutes (more than 99% settled) |
| 2 | Lab, upload item | error | The row labels (`s10`, `s20`, `s30`) made the generated rubric criteria shorter than the schema allows, so the question bank failed validation. | Labels renamed `test_10w`, `test_20w`, `test_30w` |
| 3 | Lab, upload item | error | A count column of 122 values exceeded the schema's limit of 100 values per check. | Replaced by a count of samples per run (61) |
| 4 | Lesson 9, item `lag-phase` | error | The hint ("ωτ = 5.") was shorter than the schema's minimum, which failed validation. | Hint rewritten |
| 5 | Lesson 8, worked example and item solution | unit error | The peak time was printed as "π/57.59 = 54.55 ms", which is 0.0546 s; the seconds step was missing. | Printed as seconds, then milliseconds |
| 6 | Lesson 10 | overclaim | A gain of 18.0 W/°C instead of 20 W/°C was said to give "a much better-behaved loop"; it raises the phase margin by 6.3°, from 38.7° to 45°. | States the gain in margin |
| 7 | Lesson 7 | minor | The example of a plant that starts in the wrong direction ("a heater that first cools a probe") is not physically plausible. | Replaced by the boiler-drum level, the usual example |

One mistake in the new test code itself (minus signs typeset as U+2212 in the lessons but written with a hyphen in
three expected strings) was also found and fixed; it involved no key.

## Statements without a cited source

The package adds no references. These statements and values are at textbook level, and a reviewer should confirm
that each is acceptable as stated: the Laplace transform pairs, partial fractions and the final value theorem
(lesson 7); the second-order step-response measures, the settling-time rule 4/(ζω_n) and the statement that a
damping ratio near 0.64 to 0.7 gives the flattest amplitude response of a measuring line, together with the
description of a fluid-filled catheter and transducer as a second-order system (lesson 8); decibel conventions and
the first-order and delay frequency responses (lesson 9); the definitions of the gain and phase margins and of the
delay margin, the design targets of 45° and 2, and the rule ζ ≈ PM/100 (lesson 10); the cancellation (lambda or
internal-model) tuning of a PI controller for a lag-plus-delay plant, the Ziegler–Nichols closed-loop rules, the
mechanism of windup and its remedies and the statement that PI is enough for most thermal loops (lesson 11); the
sampling theorem, the alias formula, the half-period delay of a zero-order hold and the rule of ten samples per
closed-loop time constant (lesson 12); and the retuning sequence, including the relay test (lesson 13). The
quoted plant, filter and tuning values are illustrative inputs, not properties of any real incubator.

## For a human reviewer

- Lesson 10 uses the two-crossover reading of the Nyquist criterion for a stable plant with one crossover. A
  control engineer should judge whether the limits paragraph is clear enough about plants with several crossovers.
- Lesson 11 tunes by cancelling the plant lag and notes that the disturbance response stays slow for a
  lag-dominant plant. Check that the caution and the comparison with the Ziegler–Nichols settings (a phase margin
  of about 31°) are fair.
- Lesson 13 outlines a retuning sequence and an acceptance test of 45° and 2. A person who commissions control
  loops should judge whether the sequence is the right minimum and whether measuring margins with small
  sinusoids or a relay test is realistic for a slow thermal plant.
- The lab estimates the model from the mean of two runs by a two-point rule, which is crude; the lab says so and
  names fitting the whole record as the better method.
- Prototype units 1 to 4 are still 67 to 75 words each. The earlier lessons 5 and 6 were not re-read in this pass.
