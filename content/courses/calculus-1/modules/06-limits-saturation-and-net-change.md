# Limits of saturating responses and the fundamental theorem as net change

Two ideas from the first calculus course do steady work in biology. Limits describe what a model does at its extremes: what a saturating response approaches at high input and how it behaves near zero, which is where linear approximations come from. The fundamental theorem of calculus says that integrating a rate gives net change, which is how a measured flow rate becomes a volume, or a measured growth rate becomes a population change. This lesson applies both to synthetic models and pays attention to what a limit claim needs in order to be justified.

## Learning objectives

By the end of this lesson, you should be able to:

1. Evaluate limits of a saturating function at large and small input, and justify continuity and limit claims algebraically.
2. Use the limit of a difference quotient to find the initial slope of a response and judge the accuracy of the linear approximation near zero.
3. Interpret a definite integral of a rate as net change, distinguish net change from total change, and evaluate both from a rate function.

## Limits at infinity: saturation

The Michaelis–Menten form v(S) = V_max S / (K_m + S) describes many saturating responses: enzyme rates, receptor occupancy, transporter flux. To find its behavior at large S, divide numerator and denominator by S:

v(S) = V_max / (K_m/S + 1) → V_max / (0 + 1) = V_max as S → ∞.

The limit is V_max, but the function never reaches it for finite S. With synthetic V_max = 100 and K_m = 5, at S = 1000 the rate is 99.50, still below 100. A claim like "the response has saturated" therefore needs a tolerance: within 1% of V_max requires S ≥ 99 K_m.

## Limits at zero and the initial slope

At S = 0, v = 0, and the function is continuous there because both numerator and denominator are continuous and the denominator K_m + S is not zero. The initial slope is the limit of the difference quotient:

v′(0) = lim_(h→0) [v(h) − v(0)]/h = lim_(h→0) V_max/(K_m + h) = V_max/K_m = 20.

So for small S, v ≈ (V_max/K_m) S: the response is approximately linear. How small is small? At S = 0.5 (one tenth of K_m), the linear approximation gives 10.0 while the true value is 9.09, an overestimate of 10%. The relative error of the linear approximation equals S/K_m exactly for this function, which gives a rule: stay below a few percent of K_m for a few-percent error.

## Continuity claims need checking

A function can fail to have a limit, or have one that differs from its value. A rate defined as "0 below a threshold, k above it" jumps at the threshold, so it is not continuous there; numerical methods that assume smoothness can behave badly near such points. Saying a model is continuous is a mathematical claim that can be checked: are all pieces continuous, and do the one-sided limits agree at each junction?

## The fundamental theorem as net change

If F is an antiderivative of a rate r(t), then **∫ₐᵇ r(t) dt = F(b) − F(a)**: the net change in the quantity whose rate is r. Consider a synthetic net flow into a reservoir, r(t) = 6 − 2t mL/min for 0 ≤ t ≤ 5 min (positive means filling). An antiderivative is F(t) = 6t − t², so

net change = F(5) − F(0) = 30 − 25 = 5 mL.

But the rate changes sign at t = 3 min: the reservoir fills for 3 minutes (F(3) − F(0) = 9 mL) and then drains (F(5) − F(3) = 5 − 9 = −4 mL). The **net change** is 9 − 4 = 5 mL; the **total volume moved** is 9 + 4 = 13 mL, which is ∫|r(t)| dt. The two answer different questions: how much is in the reservoir now, versus how much medium passed through the pump.

## Common mistakes

- Claiming a saturating function "reaches" its limit at a finite input.
- Using the linear approximation far from the point where the slope was taken.
- Integrating a rate that changes sign and reporting the result as the total amount moved.
- Asserting continuity of a piecewise model without checking one-sided limits.

## Worked example

**Problem.** A receptor occupancy model is f(L) = L/(K_d + L). What ligand concentration gives 90% occupancy, and what is the initial slope?

**Step 1: 90%.** L/(K_d + L) = 0.9 gives L = 9 K_d. Occupancy rises slowly near saturation: from 50% at K_d to 90% at 9 K_d, a ninefold increase.

**Step 2: initial slope.** f′(0) = lim_(h→0) 1/(K_d + h) = 1/K_d.

**Step 3: interpretation.** Below about 0.05 K_d occupancy is within 5% of L/K_d, so a dose-response measured only at low concentrations looks linear and cannot reveal the saturation that a limit analysis predicts.

## Limits of this lesson

All parameters are synthetic. The models are smooth idealizations; measured responses carry noise and may not follow a single hyperbola.
