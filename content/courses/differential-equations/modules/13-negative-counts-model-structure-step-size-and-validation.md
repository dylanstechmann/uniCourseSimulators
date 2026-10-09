# When a fitted population model predicts negative counts: model structure, extrapolation, step size and validation

This lesson works through the course case. A model has been fitted to the first 24 hours of a time course. It reproduces those hours well, and then, used to predict later times, it returns negative cell counts. A count cannot be negative, so something is wrong, and the useful question is not only what but how it could have been caught earlier, before anyone used the prediction. There are two quite different kinds of cause, one in the equation and one in the arithmetic of the numerical solution, and a small set of validation habits catches both. The course case has a three-criterion self-assessment checklist; try it first, then compare your answer with the analysis below. All values are synthetic.

## Learning objectives

By the end of this lesson, you should be able to:

1. Distinguish a model-structure error from a numerical error as the cause of an impossible prediction.
2. Compute where a straight-line model crosses zero, the step-size limits of explicit Euler for a decay, and the results of Euler steps of different sizes.
3. Design validation that reveals the failure early: hold-out prediction, step refinement, independent data and invariant checks.

## The synthetic data

Viable cells per well (in thousands) are counted at 0, 6, 12, 18 and 24 hours after the growth factor is removed: **100.0, 78.7, 61.9, 48.7, 38.3**. The counts fall, and the decline slows a little as the numbers get smaller, which is hard to see in five noisy-looking points.

## Cause 1: the wrong model, used outside the window

Suppose the decline is described by a constant loss, dN/dt = −b, so that N = a − b t. A least-squares line through the five points has slope **−2.5567** per hour and intercept 96.20. The largest residual is 3.8, under 4% of the starting value, so the line can look adequate when judged against the starting count. But it reaches zero at t = 96.20/2.5567 = **37.6 h**, and at 48 h it predicts **−26.5**: an impossible negative count. A death process in which each cell has the same chance of dying per hour has a loss proportional to N, dN/dt = −kN, so N = N₀e^(−kt). A straight line of ln N against t gives k = **0.0400 h⁻¹**, and the prediction at 48 h is 14.7, positive at every time. The two models already have different residual patterns inside the window; whether measurement error can distinguish them needs an error model. Their forecasts diverge further outside the window, and the hold-out check below exposes the line's failure.

## Cause 2: the numerical method

Now take the correct equation dN/dt = −kN and solve it with explicit Euler, N_(n+1) = (1 − kh) N_n. The solution stays nonnegative only if h ≤ 1/k = **25 h**, and decays in magnitude only if h < 2/k = 50 h. At h = 25 h the first step gives zero rather than a positive count. Starting from the observed 38.3 at 24 h and predicting 72 h, the exact answer is 5.62. A single Euler step of 48 h gives 38.3 × (1 − 1.92) = **−35.2**: negative, because h exceeds 1/k, although the equation is right. Smaller steps repair the sign but not at once: 12 h steps (four of them) give **2.80**, 3 h steps give 4.95 and 0.75 h steps give 5.45, approaching 5.62. Explicit Euler converges only as the step shrinks, and answers that change by tens of percent when the step is divided by four have not converged.

## Validation that would have caught it

- **Hold out later data.** Fit only the first 12 h and predict 24 h. The line through the first three points (100.0, 78.7, 61.9) predicts 23.05 at 24 h, against an observed 38.3: an error of 15.25, or 40% of the observed value. The exponential fitted to the same three points predicts the 24 h value within 0.1. The failure of the line appears well inside the data, before any extrapolation.
- **Refine the step.** Halve h (or divide it by four) until the result changes by less than a stated tolerance, and report the step used.
- **Use independent data.** Compare the prediction with a second experiment run to a later time than the first.
- **Check invariants.** A count must stay at or above zero, and the total of conserved quantities must balance; make the code flag any negative value rather than clipping it.
- **State the domain.** A fitted model is a statement about the time range and conditions of the data, and a forecast beyond them needs its own evidence.

## Common mistakes

- Judging a model by its fit within the window and extrapolating.
- Choosing a model form because it is the simplest curve through the points.
- Clipping negative counts to zero instead of finding why they arise.
- Taking a numerical solution as correct because it looks smooth, without refining the step.
- Using one Euler step for a long horizon.
- Validating on the same data used to fit.

## Worked example

**Problem.** A second synthetic time course (thousands of cells) is 80.0, 59.3, 43.9, 32.5, 24.1 at 0, 6, 12, 18 and 24 h, from N₀ = 80 and k = 0.05 h⁻¹. Find the line's slope and zero crossing, its prediction at 48 h, the Euler positivity limit and the result of a single 48 h Euler step from 24 h.

**Step 1: line.** The least-squares slope is −2.310 per hour with intercept 75.68, so the line reaches zero at **32.8 h**.

**Step 2: prediction.** At 48 h, 75.68 + (−2.310) × 48 = **−35.2**, impossible.

**Step 3: Euler.** The positivity limit is 1/0.05 = **20 h**. A single 48 h step from 24.1 gives 24.1 × (1 − 0.05 × 48) = **−33.7**, while the exact value is 2.19.

**Step 4: validation.** Fitting the line to the first three points and predicting 24 h gives 6.9 against an observed 24.1, so the structural error shows inside the data.

## Limits of this lesson

All numbers are synthetic. The lesson treats a single population with a loss term that is either constant or proportional, and uses explicit Euler as the simplest solver; real populations have births, subpopulations that behave differently and measurement error, and the validation list is a minimum, not a protocol for any real experiment.
