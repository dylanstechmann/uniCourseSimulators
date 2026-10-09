# Quadrature, step error and stability checks

**Status:** original formative instruction with substantial AI assistance. Functions, time steps and states are synthetic. This lesson extends the compact numerical-integration reading by separating approximation error from unstable dynamics and from error in the model itself.

## Learning objectives

1. Compute trapezoid and Simpson approximations with explicit grids and units.
2. Use refinement to estimate error only when a stated order model is plausible.
3. Distinguish stability, accuracy and physical constraints in an explicit time step.

## Integrating observations is a weighted sum

For samples (t_i,y_i), the trapezoid approximation sums (t_{i+1}−t_i)(y_i+y_{i+1})/2 over adjacent intervals. If t is in seconds and y in mg/s, the integral is in mg. An unweighted sum of y has different units and depends on the number of observations. Nonuniform time intervals require their own widths rather than a single average time step.

Sorting timestamps is not sufficient if duplicate times represent independent measurements rather than a trajectory. A pipeline must decide how replicates are aggregated, how missing intervals are treated and whether adjacent points belong to the same run. Joining the last point from one specimen to the first point from another creates an integral across an invented interval. Identity and units are part of the numerical problem.

For the smooth constructed function y(t)=t² on [0,1], the exact integral is 1/3. With spacing 0.5, the trapezoid sum is 0.375. With spacing 0.25 it is 0.34375. Simpson's rule on the three equally spaced points 0,0.5,1 gives (0.5/3)(0+4×0.25+1)=1/3. That exactness is a property of this polynomial, not a guarantee about noisy observations or arbitrary curves.

Simpson's composite rule in its usual equal-spacing form needs an even number of intervals. Applying its alternating weights to irregular timestamps without a different derivation changes the method. Higher formal order also does not remove measurement noise, missing peaks or the inability to observe variation between widely separated times.

## What refinement can and cannot show

Suppose a method's leading error is C hᵖ, so I_h=I+C hᵖ plus smaller terms. Then I_h−I_{h/2}≈C hᵖ(1−2⁻ᵖ). The estimated magnitude of the fine-grid error is |I_h−I_{h/2}|/(2ᵖ−1). For second-order trapezoids, the divisor is three. The fine approximation for t² has estimated error (0.375−0.34375)/3=0.0104167, exactly its difference from 1/3 here.

Richardson extrapolation combines I_{h/2}+(I_{h/2}−I_h)/(2ᵖ−1), canceling the assumed leading term. It gives 1/3 for this construction. The derivation requires refinement of the same mathematical problem and an appropriate asymptotic error regime. Adding independently noisy measurements is not equivalent to refining evaluations of a known function. Neither is shifting the endpoint or changing a discontinuity treatment between runs.

Three resolutions can help diagnose order. If errors shrink by a factor near four when h halves, second-order behavior is plausible. At very fine resolution, roundoff can dominate. At coarse resolution, leading-order behavior may not yet apply. An apparent convergence pattern does not establish that a fitted curve is physically correct; numerical accuracy is conditional on the curve being integrated.

## A stable step can still be inaccurate

For the synthetic differential equation y' = −λy with λ=2 per second, explicit Euler gives y_{n+1}=(1−2h)y_n. Stability of the decaying scalar mode requires |1−2h|<1, or 0<h<1 second. At h=0.75, the multiplier is −0.5. Its magnitude decays, but the sign alternates, which is inappropriate if y represents a nonnegative concentration. Stability and positivity are distinct requirements; positivity here needs h≤0.5.

At h=1.1, the multiplier is −1.2, so the numerical solution alternates with growing magnitude while the exact state decays. More iterations do not repair that instability. At h=0.25 over one second, four Euler steps give 0.5⁴=0.0625 from initial state one. The exact value is exp(−2)≈0.135335. The stable positive step is still substantially inaccurate. Refinement addresses this error when the model and interval are fixed.

Stiff systems have widely separated time scales. A step suitable for a slow component can violate an explicit solver's stability limit for a fast component. Selecting a solver solely because it has a higher formal order does not guarantee an adequate stability region. The general problem requires more analysis than this scalar example supplies.

## Worked example

Three nonuniform synthetic observations at times [0,1,3] seconds have rates [0,2,2] mg/s. The first area is one mg and the second is four mg, so total area is five mg. Replacing both interval widths by one second gives three mg and incorrectly shortens the experiment. Plotting the points and intervals makes the difference visible before choosing a method.

For Euler with λ=2 and h=0.1, ten steps yield 0.8¹⁰≈0.107374 after one second. Halving h gives 0.9²⁰≈0.121577, closer to exp(−2). The refinement difference is about 0.014202. A first-order estimate uses divisor one, but the exact fine-grid error is about 0.013759: the leading-order estimate is approximate at these finite steps. Report that distinction rather than calling the refinement difference a measured uncertainty interval.

## Common mistakes

Dropping interval widths, pooling different trajectories, applying equal-grid weights to irregular points, and confusing solver stability with accuracy all change the problem. Reporting more decimal places cannot recover an unobserved peak. A conservation check must match the model: a decaying state alone is not conserved unless its sink is also included in the ledger.

## Limits of this lesson

These deterministic examples cover simple quadrature and one linear differential mode. They do not validate experimental time sampling, adaptive solvers, stiff systems or numerical confidence intervals. Practice checks selected calculations and judgments without executing learner code. Existing numerical-methods curriculum links remain link-only scope comparators. Original instruction is CC BY 4.0; qualified review and measured workload remain outstanding.
