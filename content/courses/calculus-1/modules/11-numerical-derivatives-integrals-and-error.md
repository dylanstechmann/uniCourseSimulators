# Numerical derivatives, quadrature and error budgets

Measurements provide values at selected times, while derivatives and integrals describe a continuous function. Numerical calculus connects them through an approximation and an error budget. A smaller time step can reduce smooth-function truncation error while making a noisy derivative worse. An integration formula can be accurate for a stated smooth curve yet unjustified for irregular samples or an unresolved jump. This lesson compares finite differences, trapezoids and Simpson's rule using a synthetic decay function, then separates mathematical approximation error from measurement error.

## Learning objectives

1. Compare finite-difference derivatives and explain the tradeoff between truncation and noise.
2. Calculate composite trapezoidal and Simpson approximations from sampled values.
3. Apply smooth-function error bounds and state the assumptions they require.

## A reference curve for checking the methods

Use C(t) = 20e^(−0.1t), with t expressed in hours and C in a chosen concentration unit. Its exact derivative is C′(t) = −2e^(−0.1t); at t = 10 it is −2/e = −0.735759 concentration units per hour. Its exact accumulation over [0, 20] is 200(1 − e^(−2)) = 172.932943 concentration-unit hours. These exact values provide a teaching reference; real observations generally do not come with an exact curve against which to check them.

The forward difference [C(t+h) − C(t)]/h uses the interval after t. For h = 5 at t = 10 it is −0.578997. It is less negative than the derivative because the decay slope flattens over that interval. For a sufficiently smooth function, its leading local truncation error is proportional to h. This is a statement about the exact function samples, before adding measurement or rounding errors.

## Centering cancels a leading error

The central difference [C(t+h) − C(t−h)]/(2h) averages information from both sides of t. Expanding each side about t cancels the even powers in the numerator, leaving C′(t) plus a leading error proportional to h². For h = 5 at t = 10 the estimate is −0.766801. For h = 1 it is −0.736986, much closer to −0.735759. Its bias remains nonzero; the values do not become exact simply because the formula is symmetric.

The usual second-order central formula assumes equally spaced observations around the target. With unequal time intervals, the displayed formula estimates a different interval-centered quantity unless one derives the appropriate nonuniform weights. Near a measurement-window endpoint, a central estimate may require an unavailable outside observation. Use a justified one-sided formula or restrict the target; do not fabricate the missing sample.

## Noise can reverse the benefit of smaller steps

Suppose each of the two sampled concentrations has an unknown error bounded in absolute value by ε. The central-difference error contributed by those two errors is bounded by (ε+ε)/(2h) = ε/h. For ε = 0.02 and h = 0.1, this bound is 0.2 concentration units per hour. Halving h doubles the noise bound while reducing smooth truncation error roughly fourfold. The sum of those competing contributions need not decrease.

This bound is deterministic and permits errors of opposite signs. If the errors instead have a known variance and correlation, a statistical uncertainty calculation uses that covariance, and need not equal the worst-case bound. Smoothing or fitting a model can reduce noise amplification but introduces additional assumptions and possible bias. Choose the window using an explicit accuracy question and validation, rather than selecting the smallest available sampling interval automatically.

## Composite trapezoids

For equally spaced values C₀ through C_n at spacing h, the composite trapezoidal approximation is T = h[C₀/2 + C₁ + … + C_(n−1) + C_n/2]. It integrates straight-line segments between adjacent samples. At times 0, 5, 10, 15 and 20, using the exact model values, T = 176.520790. This exceeds the exact accumulation by 3.587847 because this decay curve is convex: straight chords lie above it.

If |C″| ≤ M₂ over an interval of length L, the composite trapezoid error is bounded by LM₂h²/12. Here C″ = 0.2e^(−0.1t), so M₂ = 0.2 on [0, 20]. With L = 20 and h = 5, the bound is 8.333333. The actual error is smaller than this bound, as required. A worst-case bound is not a prediction that the error equals its upper limit.

## Simpson's rule and its conditions

For an even number of equal-width panels, composite Simpson's rule uses weights 1, 4, 2, 4, …, 2, 4, 1 and multiplies their weighted sum by h/3. With four panels here, S = (5/3)[C₀ + 4C₁ + 2C₂ + 4C₃ + C₄] = 172.991248, whose error is 0.058305. For functions with a bounded fourth derivative, the error bound is LM₄h⁴/180. Here M₄ = 0.002, giving 0.138889. Both the fourth derivative and the evenly spaced, even-panel setup matter.

A fourth-order formula is not a universal guarantee for noisy samples. Its alternating interior weights give measurement errors different influence from trapezoids. Nor should one apply these weights unchanged to nonuniform time coordinates. For unequal intervals, trapezoids can be computed interval by interval using each actual width. Resolve a known discontinuity by splitting the interval rather than invoking a smooth-function bound across it.

## Worked example

Integrate f(t) = t² from 0 to 2 using two panels of width 1. Samples are 0, 1 and 4. Trapezoids give (0/2 + 1 + 4/2) = 3, whereas the exact integral is 8/3. Simpson gives (1/3)(0 + 4×1 + 4) = 8/3 exactly. The fourth derivative of this quadratic is zero, so the Simpson error bound is zero. This exactness for a quadratic does not make Simpson exact for every smooth function.

## Common mistakes

- Confusing a forward interval slope with the instantaneous derivative at its left endpoint.
- Assuming smaller h always helps a noisy derivative.
- Applying equal-spacing formulas to irregular observations.
- Treating a worst-case bound as an estimated standard deviation.
- Using Simpson weights with an odd number of panels or without checking smoothness.

## Limits of this lesson

The reference calculations use exact constructed functions. Real data require uncertainty, correlation, interpolation and sampling decisions. Error bounds concern the approximation of the stated smooth curve; they do not include omitted model behavior or certify a measured physical quantity.
