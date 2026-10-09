# Logistic growth: the exact solution, fitting from data and the risk of extrapolating

Cells in a culture dish multiply almost exponentially at first and then slow as they run out of space or medium. The logistic equation is the simplest model with that shape, and unlike most nonlinear equations it can be solved exactly. The solution gives the time to reach any fraction of capacity, shows where growth is fastest and, most usefully, exposes why a rate fitted to the early exponential phase can mislead badly when it is used to predict later counts. This lesson solves the equation, derives the quantities that matter and compares the logistic with a naive exponential forecast. All values are synthetic.

## Learning objectives

By the end of this lesson, you should be able to:

1. Solve the logistic equation by separation of variables and evaluate the solution at a given time.
2. Compute the half-capacity time, the fraction of capacity reached, the early doubling time and the maximum growth rate.
3. Fit the growth rate from two counts by a logit transformation and quantify the error of an exponential extrapolation.

## The equation and its solution

The logistic equation is dN/dt = r N (1 − N/K), with growth rate r and carrying capacity K. Separating variables, ∫ dN/(N(1 − N/K)) = ∫ r dt, and the partial fractions 1/(N(1 − N/K)) = 1/N + (1/K)/(1 − N/K) give ln(N/(K − N)) = r t + constant. Solving for N,

**N(t) = K / (1 + ((K − N₀)/N₀) e^(−rt)).**

Rewriting the intermediate result gives a useful straight line: **ln(N/(K − N)) = ln(N₀/(K − N₀)) + r t**, so the logit of the fraction of capacity grows linearly with slope r if K is known.

**Synthetic culture:** K = 8 million cells, N₀ = 0.2 million and r = 0.05 h⁻¹, so (K − N₀)/N₀ = **39**. Then N(24 h) = 8/(1 + 39e^(−1.2)) = **0.6276 million**, and N(48 h) is **0.2204** of capacity (1.763 million).

## Times and rates that matter

- **Half-capacity.** N = K/2 when the denominator equals 2, that is when ((K − N₀)/N₀) e^(−rt) = 1, so t = ln((K − N₀)/N₀)/r = ln(39)/0.05 = **73.3 h**.
- **Ninety percent of capacity.** Setting the denominator to 1/0.9 gives t = ln(9 (K − N₀)/N₀)/r = ln(351)/0.05 = 117.2 h.
- **Early doubling time.** While N is much smaller than K the growth is nearly exponential with doubling time ln 2/r = **13.86 h**.
- **Fastest growth.** The growth rate r N (1 − N/K) is largest at N = K/2, where it equals rK/4 = **0.10 million cells per hour**.

The curve is S-shaped, with the inflection (the steepest part) at K/2, which is reached at 73.3 h here, long after the early phase that most experiments sample.

## Fitting the rate

From two counts with K known, the logit gives r directly. For N₀ = 0.2 million at t = 0 and N = 0.628 million at t = 24 h, logit(N₀) = ln(0.2/7.8) = −3.664 and logit(N) = −2.464, so the slope is **0.0500 h⁻¹**, recovering r. In practice the counts are noisy and K is not known, and fitting r from the early points by a straight line of ln N against t gives a slightly low value, because the growth has already begun to saturate in the window.

## The risk of extrapolating

Suppose the early phase is fitted perfectly by N = 0.2 e^(0.05t) and used for prediction. At 24 h it overestimates the logistic value by 5.8% (0.664 against 0.628 million), which looks harmless. At 72 h the exponential gives 7.32 million cells, and the logistic gives 3.873 million: the exponential forecast is too high by **3.45 million cells**, about 89% of the correct value, and it keeps growing: by 96 h it gives 24.3 million cells, 3.0 times the capacity of 8 million that the culture cannot exceed. A fit that matches the data over the window it was fitted on says nothing about the window beyond.

## Common mistakes

- Using the early doubling time to predict counts after the culture has begun to saturate.
- Forgetting that the logistic solution has the ratio (K − N₀)/N₀, not K/N₀.
- Treating the time to half capacity as half the time to reach capacity; the logistic approaches K only asymptotically, so even the time to 90% (117 h) is 1.6 times the time to half capacity.
- Applying the logit transformation with a wrong value of K.
- Treating the growth rate r as the observed relative growth rate (it is the rate at N ≪ K).
- Judging a model only by how well it fits the data it was fitted to.

## Worked example

**Problem.** A synthetic culture has K = 5 million, N₀ = 0.1 million and r = 0.08 h⁻¹. Find the half-capacity time, N at 36 h, the early doubling time and the maximum growth rate, and compare the exponential and logistic forecasts at 72 h.

**Step 1: ratio.** (K − N₀)/N₀ = 49, so t₁/₂ = ln(49)/0.08 = **48.6 h**.

**Step 2: N at 36 h.** N = 5/(1 + 49e^(−2.88)) = **1.333 million**.

**Step 3: rates.** Doubling time ln 2/0.08 = 8.66 h and maximum growth rate rK/4 = 0.10 million per hour.

**Step 4: forecasts at 72 h.** The exponential gives 0.1 e^(5.76) = 31.7 million, the logistic gives 4.33 million, which is at most the capacity of 5.

## Limits of this lesson

All numbers are synthetic. The logistic equation is a minimal model: it assumes that the growth rate falls linearly with N and that the culture is homogeneous. Real cultures can have a lag phase, a death phase and nutrient depletion that is not logistic, and the counts carry error that the formulas ignore.
