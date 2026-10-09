# Root brackets, residuals and conditioning

**Status:** original formative instruction with substantial AI assistance. All functions and thresholds below are synthetic. Root finding asks which input makes a declared model equal a target. It does not identify a real biological parameter unless the model and measurements support that interpretation.

## Learning objectives

1. Trace bisection updates and derive an interval-based error bound.
2. Diagnose a false bracket, an invalid Newton step or an ambiguous stopping condition.
3. Distinguish a small residual from a small parameter error using local sensitivity.

## Start with an equation and a domain

Write a target problem as f(x)=0. The variable has a meaning and permitted domain; f has a scale and perhaps units. A synthetic saturation law y(c)=c/(2+c) is defined for c≥0. To find the concentration at half response, solve f(c)=c/(2+c)−0.5. A bracket from zero to six has f(0)=−0.5 and f(6)=0.25. The model is continuous there and therefore crosses the target somewhere inside. In fact the solution is c=2.

Opposite signs alone do not prove a root without continuity. The function 1/(x−1) has opposite signs at zero and two but is undefined at one and never equals zero. Applying a sign-based solver across that discontinuity can return a misleading location or encounter division by zero. Domain inspection is a mathematical prerequisite, not a cosmetic programming check.

An even-multiplicity root can also lack a sign change: (x−2)² equals zero at two while remaining nonnegative on both sides. A bracketed sign method may reject an interval containing that root. This does not show that roots are absent; it shows that this particular method's assumptions are absent. Monotonicity gives additional information when uniqueness matters.

## Bisection preserves a justified interval

For a continuous function with an opposite-sign bracket [a,b], evaluate its midpoint m. If f(m)=0, the exact computed midpoint is a root under the model. Otherwise keep the half whose endpoints still have opposite signs. Each update halves the interval width. After k interval halvings, width is (b−a)/2ᵏ. Reporting the midpoint of the final interval bounds its distance to any root in that interval by half that width.

That last distinction matters when counting iterations. In this lesson, k counts completed interval halvings, and the reported estimate is the midpoint of the retained final interval. It is not necessarily the midpoint evaluated during the last update. State the convention before attaching a factor of two to an error bound.

An implementation also needs finite endpoint values, an iteration limit and a policy for stalled midpoints at floating-point resolution. Multiplying huge function values to compare signs can overflow; comparing signs directly avoids that particular failure. A routine should report nonconvergence explicitly. A numerical answer without its convergence status hides whether the stated tolerance was reached.

## Newton uses a different kind of information

Newton's update is x_new=x−f(x)/f'(x). It uses a tangent approximation rather than retaining a sign bracket. For f(x)=x²−2 and x=1, the first update is 1.5. The second is approximately 1.416667. Close to a simple root, the method can converge rapidly, but a zero derivative makes the step undefined. A nonzero derivative can still produce a step outside a physical domain.

For the saturation model, starting at c=10 gives f=1/3 and derivative 2/(12²)=1/72. Its Newton step is 10−24=−14, outside c≥0. A negative concentration is not justified by the fact that the update formula was executed correctly. A safeguarded method can retain a valid bracket and use Newton only when the proposed step respects its requirements. The stopping and rejection rules must be explicit.

## Residual scale and parameter scale

The residual is f(x_est), while parameter error is x_est−x_root. Near a simple root, f(x_est)≈f'(x_root)(x_est−x_root). Therefore a small residual may imply a large parameter error if the derivative is small. Rescaling the equation changes residual size without changing its root. A universal residual threshold such as “below one thousandth” has no meaning without a declared function scale.

Consider f(x)=0.001(x−2). At x=3, the residual is 0.001 but parameter error is one. Multiplying the function by 1000 makes residual one at the same estimate. Both equations have the same root. A bracket-width stopping condition addresses location directly; a residual condition addresses the equation value. Using both can be useful, but neither repairs an invalid model or discontinuity.

## Worked example

Use f(x)=x²−2 on [1,2]. The first midpoint 1.5 has positive residual, so retain [1,1.5]. The next midpoint 1.25 has negative residual, so retain [1.25,1.5]. After two halvings the width is 0.25 and the final midpoint is 1.375, with a location bound 0.125. Its actual error from √2 is about 0.039214, smaller than the bound.

Starting instead with [0,4], eight halvings give width 4/256=0.015625 and final-midpoint error bound 0.0078125. To guarantee a bound no greater than 0.001, solve 4/2^(k+1)≤0.001. The minimum integer k is eleven. These bounds require the valid root-containing interval to be preserved at every update. They are deterministic algorithmic guarantees, not confidence intervals for an estimated physical parameter.

## Common mistakes

Ignoring continuity, using a derivative at a pole, confusing the last evaluated midpoint with the final interval midpoint, and accepting a step outside the domain all break the argument. A tiny residual can also be caused by scaling. An unchanged printed value can hide ongoing changes beneath display precision; convergence checks use internal values and stated scales.

## Limits of this lesson

This lesson covers scalar deterministic models, not multidimensional roots or uncertainty propagation through fitted models. Choices assess solver decisions and numbers assess traces; no learner solver runs on the server. The official [SciPy bisection documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.bisect.html) is a link-only reference for continuity, bracket and convergence conventions. Original examples are CC BY 4.0 and unreviewed; no source code or documentation example was copied.
