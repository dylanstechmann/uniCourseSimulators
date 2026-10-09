# Local approximations, Newton steps and sensitivity

A derivative describes local behavior. It can turn a nonlinear function into a useful nearby line, convert a small input error into an approximate output error or generate an iterative root-finding step. Each use needs a point, a scale and a statement about how far the local approximation is being extended. This lesson derives linearization and a curvature bound, works through Newton iteration and compares absolute with relative sensitivity. All numerical models are synthetic. A local calculation is not a global guarantee or evidence about a real sensor's calibration.

## Learning objectives

1. Construct a local linear approximation and bound its error using curvature.
2. Calculate Newton steps and identify conditions that can make iteration fail.
3. Interpret dimensionless relative sensitivity and distinguish approximation from certainty.

## A tangent line with a stated center

Near x = a, the first-order approximation is f(a+h) ≈ f(a) + f′(a)h. The increment h is measured from the stated center, not from zero unless a = 0. For f(x) = √x about a = 9, f(a) = 3 and f′(a) = 1/6. At x = 9.3, h = 0.3 and the estimate is 3 + 0.3/6 = 3.05. The exact value is approximately 3.049590, so the estimate is high by about 0.000410. Since the square root is concave down, its tangent lies above the curve on its positive domain.

For f(x) = ln x about 1, the tangent approximation is ln(1+h) ≈ h. At h = 0.1 it gives 0.1, compared with ln 1.1 = 0.095310. The sign and size of the error depend on curvature and distance from the center. Saying "use the derivative" without specifying a point or an increment does not define an approximation.

## Curvature gives an error bound

If the second derivative is bounded by M in absolute value throughout the interval joining a and a+h, the first-order remainder satisfies |f(a+h) − f(a) − f′(a)h| ≤ Mh²/2. One way to see this is to integrate the change of derivative over the interval: |f′(a+s) − f′(a)| ≤ M|s|, and integrating that bound yields Mh²/2. The bound concerns the entire connecting interval, not only the value of f″ at the center.

For ln x on [1, 1.1], |f″(x)| = 1/x² ≤ 1, so the error bound is 0.1²/2 = 0.005. The actual error 0.004690 lies below it. For √x on [9, 9.3], |f″| ≤ 1/(4×9^(3/2)) = 1/108. The bound is 0.3²/216 = 0.000417, consistent with the observed 0.000410. These bounds apply because the functions have the required derivatives throughout the intervals.

Crossing a domain boundary invalidates this argument. The tangent to ln x at 1 can be evaluated algebraically at x = −1, but ln(−1) has no real value. A locally constructed line is defined at more points than the original real function and must not be confused with that function.

## Newton iteration comes from a tangent

To solve f(x) = 0, approximate the function near an iterate x_n by f(x_n) + f′(x_n)(x−x_n). Setting that line to zero gives x_(n+1) = x_n − f(x_n)/f′(x_n), when the denominator is nonzero. For f(x) = x² − 2 and x₀ = 1.5, the first step is 1.5 − 0.25/3 = 17/12 = 1.416667. The next is 577/408 = 1.414216. The true positive root is √2 = 1.414214, so the second step is already close.

Near a simple root, with suitable smoothness and a sufficiently close starting point, Newton's method can converge quadratically. This local statement does not ensure convergence from every initial value. A zero derivative makes the displayed step undefined; a small derivative can produce a large jump; an iteration can leave the function's domain or cycle. A residual |f(x_n)| and a step size |x_(n+1)−x_n| test different things, and neither alone provides a universal root error bound.

For this square-root example, choosing x₀ = 0 fails because f′(0) = 0. A bracketed method can provide a more conservative fallback for a continuous function with opposite signs at known endpoints. The method choice should follow the available domain and accuracy evidence, not an expectation that every Newton step improves every starting guess.

## Absolute versus relative sensitivity

For R(c) = 100c/(2+c), the absolute slope is R′ = 200/(2+c)². It has signal units per concentration unit. For positive c and R, the dimensionless elasticity is E = (c/R)R′ = 2/(2+c). At c = 2, E = 0.5. A small relative input change δc/c therefore produces approximate relative output change δR/R ≈ E δc/c. A 2% input increase predicts about a 1% signal increase locally.

Calculate the exact finite change to test the approximation: c rises from 2 to 2.04, R rises from 50 to 100×2.04/4.04 = 50.495050, so the relative increase is 0.009901. This differs from the linear prediction 0.01. The approximation becomes more accurate for smaller increments under the same smoothness assumptions. Relative sensitivity also becomes undefined if its reference output is zero; use a suitable absolute scale there rather than dividing by zero.

## Worked example

Take f(x) = x² near a = 3. Linearization gives f(3+h) ≈ 9 + 6h, while exact expansion gives 9 + 6h + h². Thus the remainder is exactly h². The curvature bound uses f″ = 2 and gives Mh²/2 = h², equal to the actual error. At h = −0.2, the approximation is 7.8 and the exact value is 7.84. The tangent underestimates on both sides because the function is convex.

## Common mistakes

- Using an increment measured from the wrong center.
- Bounding curvature only at the center instead of over the interval.
- Extending an approximation outside the original function's domain.
- Treating Newton's local convergence rate as a global guarantee.
- Confusing a dimensionless relative sensitivity with a slope carrying units.

## Limits of this lesson

These calculations use exact differentiable functions and specified intervals. They do not include uncertain parameters or omitted dependencies. A sensitivity estimate is local, and a numerical root needs a justified stopping criterion and domain checks. None of these examples supplies a real device specification or experimental recommendation.
