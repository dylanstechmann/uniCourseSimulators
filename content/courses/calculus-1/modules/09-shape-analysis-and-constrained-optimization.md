# Curve shape, critical points and constrained optimization

A derivative tells us where a quantity is increasing, but locating its largest value requires more than setting the derivative to zero. Feasible boundaries, points where a derivative fails and the shape between candidates all matter. This lesson uses sign analysis to connect first and second derivatives to graph shape, then minimizes a geometric cost after eliminating a constraint. The functions, dimensions and objectives are synthetic. A mathematically optimal design within a stated model is not evidence that a real design is safe, feasible or optimal under omitted constraints.

## Learning objectives

1. Use derivative signs to identify increasing intervals, local extrema and concavity.
2. Compare interior candidates and feasible endpoints for an absolute optimum.
3. Eliminate a geometric constraint before optimizing and interpret model-dependent conclusions.

## First derivative: intervals before labels

Let f(x) = x³ − 6x² + 9x + 1 on the closed interval [0, 3]. Its derivative is f′(x) = 3x² − 12x + 9 = 3(x − 1)(x − 3). It is positive for 0 < x < 1 and negative for 1 < x < 3. The function therefore increases up to x = 1 and decreases afterward. At x = 1 the sign changes from positive to negative, so this point is a local maximum. At x = 3, the derivative is zero but the point is also the boundary of the stated feasible interval.

The derivative vanishing is only a candidate test. For g(x) = x³, g′(0) = 0, but the function increases through 0 and has no local maximum or minimum there. Conversely, |x| has a minimum at 0 where its derivative does not exist. A complete search includes feasible interior points with zero derivative or an undefined derivative, together with endpoints.

## Absolute extrema on a closed interval

A continuous function on a closed bounded interval attains a maximum and a minimum. For the cubic above, evaluate the candidates: f(0) = 1, f(1) = 5 and f(3) = 1. The absolute maximum is 5 at x = 1. The minimum value 1 occurs at both endpoints. Reporting only one minimizer would omit another equally good feasible answer. The existence theorem does not guarantee uniqueness, and it does not identify the candidates for us.

The domain is part of the problem. On the open interval (0, 1), the function x has neither an attained maximum nor an attained minimum, even though its values have an upper and lower bound. A supremum can be approached without being reached. Likewise, if a physical parameter must be strictly positive, an optimum at zero may be an unattainable limiting design. State whether a boundary is included before comparing values.

## Second derivative and inflection

The second derivative of the cubic is f″(x) = 6x − 12. It is negative below 2 and positive above 2, so the graph changes from concave down to concave up at x = 2, where f(2) = 3. This is an inflection point because concavity changes. A zero of f″ alone is insufficient: x⁴ has f″(0) = 0 but is concave up on both sides and has no inflection there.

At an interior stationary point, a positive second derivative confirms a strict local minimum and a negative one a strict local maximum. A zero second derivative leaves the test inconclusive; use the first-derivative sign or another argument. Concavity concerns how the slope changes. A function can decrease while being concave up, as the cubic does between 2 and 3. Do not equate concave up with increasing.

## Feasible boundaries can decide the answer

Consider C(p) = 4p² − 12p + 15 for 0 ≤ p ≤ 1. The stationary point p = 1.5 lies outside the feasible domain. On [0, 1], C′(p) = 8p − 12 is negative, so C decreases throughout the interval. The minimum is at p = 1, where C = 7; the unconstrained stationary value is irrelevant to this feasible problem. This is the mathematical pattern behind the compact course case about a constrained design, but the cost coefficients here are constructed rather than measured.

## Eliminate a geometric constraint

A closed cylinder has volume V = πr²h and surface area S = 2πr² + 2πrh. Fix V = 16π cm³, with positive r and h. Then h = 16/r² and S(r) = 2πr² + 32π/r for r > 0. Differentiating gives S′ = 4πr − 32π/r². Setting this to zero yields r³ = 8, so r = 2 cm and h = 4 cm. The second derivative S″ = 4π + 64π/r³ is positive for every positive r. Also S diverges as r approaches zero or infinity, so the stationary point is the unique global minimum. The minimum area is 24π = 75.398224 cm².

The conclusion h = 2r depends on counting both ends and using uniform area cost. An open-top vessel, unequal material costs or a maximum allowable height produces a different objective or feasible set. Optimization cannot compensate for an incorrectly stated design problem. Write the objective, the units and every constraint before differentiating.

## Worked example

Suppose the same cylinder must also satisfy h ≤ 1 cm. Since h = 16/r², feasible radii satisfy r ≥ 4 cm. The unconstrained optimum r = 2 is excluded. For r ≥ 4, S′ is positive, so area is minimized at the boundary r = 4, h = 1. Its area is 2π(16) + 2π(4)(1) = 40π cm². The new feasible optimum is larger in area than 24π, because adding a constraint cannot improve the minimum of the same objective over a smaller feasible set.

## Common mistakes

- Treating every zero derivative as an extremum.
- Omitting endpoints or nondifferentiable feasible points.
- Identifying an inflection from f″ = 0 without checking a sign change.
- Keeping an infeasible stationary point.
- Optimizing before writing the constraint or silently changing the objective.

## Limits of this lesson

The examples use exact one-variable functions and ideal geometry. Real design criteria may include uncertain parameters, discontinuities, multiple competing objectives and constraints absent here. These are calculus exercises, not engineering specifications or validated experimental choices.
