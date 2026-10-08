# Integrals as accumulation: total consumption from rate data, numerical rules with error bounds and improper integrals

Experiments often measure rates: how fast cells consume glucose, how fast a gel releases a protein, how fast oxygen is taken up. The total over a period is the integral of the rate. This lesson computes totals both exactly, when a model is available, and numerically from sampled data, quantifies the numerical error, and uses an improper integral to find the total ever released by a decaying source.

## Learning objectives

By the end of this lesson, you should be able to:

1. Set up and evaluate the definite integral of a rate model to obtain a total accumulated amount.
2. Apply the trapezoidal and Simpson's rules to sampled rate data and bound the trapezoidal error using the second derivative.
3. Evaluate an improper integral of a decaying rate, test its convergence and interpret the finite total.

## Accumulation is an integral

If q(t) is a rate (amount per time), the amount accumulated between t = a and t = b is

**Q = ∫ₐᵇ q(t) dt.**

Units check: (amount/time) × time = amount. Suppose a growing culture consumes glucose at a synthetic rate q(t) = 0.5 e^(0.03t) mmol/h, rising as the cells multiply. Over 0 to 48 h the exact total is

∫₀^48 0.5 e^(0.03t) dt = (0.5/0.03)(e^(1.44) − 1) = 53.68 mmol.

## When only samples exist

In an experiment you might measure the rate every 12 hours:

| t (h) | q (mmol/h) |
|---|---|
| 0 | 0.5 |
| 12 | 0.7167 |
| 24 | 1.0272 |
| 36 | 1.4723 |
| 48 | 2.1103 |

The **trapezoidal rule** joins the samples with straight lines:

T = h [q₀/2 + q₁ + q₂ + q₃ + q₄/2] = 12 × [0.5/2 + 0.7167 + 1.0272 + 1.4723 + 2.1103/2] = 54.26 mmol.

**Simpson's rule** fits parabolas through pairs of intervals (it needs an even number of intervals):

S = (h/3)[q₀ + 4q₁ + 2q₂ + 4q₃ + q₄] = 53.68 mmol.

Compared with the exact 53.68, the trapezoidal estimate is off by 0.58 mmol and Simpson's by 0.005.

## Bounding the error

For the trapezoidal rule with step h over [a, b],

**|E_T| ≤ (b − a) h² / 12 × max|q″(t)|.**

Here q″(t) = 0.5 × 0.03² e^(0.03t), largest at t = 48: 0.00190. The bound is 48 × 12² / 12 × 0.00190 = 1.09 mmol, and the actual error (0.58) is within it. Because q is convex (q″ > 0), straight chords lie above the curve and the trapezoidal rule overestimates. Halving h would cut the bound by four. With real data the true q″ is unknown, but this analysis still says which way and roughly how much sampling interval matters, and that measurement noise in q may dominate once h is small.

## Improper integrals: the total from a source that never quite stops

A gel releases a factor at a rate that decays as the supply depletes: synthetic r(t) = 2.0 e^(−0.1t) μg/h. The total ever released is an improper integral:

∫₀^∞ 2.0 e^(−0.1t) dt = lim_(T→∞) (2.0/0.1)(1 − e^(−0.1T)) = 20 μg.

The integral converges because the integrand decays exponentially. Half of that total is released by t = ln 2 / 0.1 = 6.9 h. Not every decaying rate gives a finite total: a rate falling like 1/t does not converge on [1, ∞), because ∫ dt/t = ln t grows without bound, while 1/t² does converge. Comparing a rate with these reference functions is how convergence is tested.

## Common mistakes

- Mixing units: integrating a rate in mmol per hour over a time axis in minutes gives an answer sixty times too small.
- Using Simpson's rule with an odd number of intervals, which the formula does not allow.
- Assuming a numerical answer is accurate because many decimals are printed; the error bound and the measurement noise set the useful precision.
- Concluding that an improper integral converges because the integrand tends to zero.
- Forgetting that the trapezoidal rule's sign of error depends on curvature: it overestimates convex rates and underestimates concave ones.

## Worked example

**Problem.** If the culture's rate data were sampled every 24 h instead of 12 h (points at 0, 24 and 48 h only), what would the trapezoidal estimate and its error bound be?

**Step 1: estimate.** T = 24 × [0.5/2 + 1.0272 + 2.1103/2] = 55.98 mmol.

**Step 2: error.** Actual error = 2.30 mmol; the bound becomes 48 × 24² / 12 × 0.00190 = 4.38 mmol, four times the 12 h bound.

**Step 3: decision.** Sampling interval choice is part of experimental design: if the total must be known to within 1 mmol, sampling every 24 h is not enough for a rate that grows this fast.

## Limits of this lesson

Rates are synthetic and noise-free. Real rate measurements carry noise and bias that numerical integration does not remove.
