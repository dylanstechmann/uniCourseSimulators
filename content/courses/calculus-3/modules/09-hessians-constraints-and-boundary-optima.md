# Hessians, constraints and boundary optima

## Learning objectives

1. Solve stationary equations and classify a smooth two-variable point using its Hessian.
2. Apply regular equality-constraint conditions and interpret a multiplier's convention.
3. Compare feasible interior and boundary candidates instead of assuming every stationary point is optimal.

## Stationary equations together

For a differentiable function on an open region, an interior local extremum requires ∇f=0. Solve all component equations together. A zero derivative in one coordinate leaves possible change in another. The synthetic objective f(x,y)=x²+2xy+3y²−4x−8y has equations 2x+2y−4=0 and 2x+6y−8=0. Subtracting them gives y=1, then x=1. At that point the objective is −6.

Its Hessian is H=[[2,2],[2,6]]. The determinant is 8, and the first diagonal entry is positive, so H is positive definite. The point is a strict local minimum. Because this quadratic has the same positive-definite Hessian everywhere, the point is also its unique global minimum on the whole plane. That global conclusion uses the additional convex structure, not just a local test at one point.

In two dimensions, determinant D=f_xx f_yy−f_xy² gives a useful classification at a stationary point: D>0 and f_xx>0 indicates a local minimum; D>0 and f_xx<0 indicates a local maximum; D<0 indicates a saddle; D=0 is inconclusive. An inconclusive test means higher-order terms or another argument are needed, not that the point is absent or flat in every direction.

## A degenerate Hessian can hide different shapes

At the origin, both x⁴+y⁴ and x⁴−y⁴ have zero Hessian. The first has a strict minimum because it is positive away from zero. The second has both positive values along the x axis and negative values along the y axis, so it is a saddle. These examples share the same second derivatives at the point yet have different local geometry. A determinant of zero cannot decide between them.

The Hessian also depends on what variables are being optimized. A physical cost may combine quantities with different dimensions; derivatives and multipliers then carry corresponding units. Rescaling coordinates changes matrix entries but should preserve the underlying feasible design question when the objective and constraints are transformed consistently.

## Equality constraints

For a smooth equality g(x,y)=b with nonzero gradient on the constraint near a local constrained extremum, a necessary condition is ∇f=λ∇g. The regularity condition matters. At a point with ∇g=0, the standard Lagrange condition need not identify all extrema. The equations produce candidates; feasibility and comparison are still needed.

For f=xy subject to x²+y²=1, the equations are y=2λx and x=2λy. Multiplying or solving shows y=x at maximum candidates and y=−x at minimum candidates. The maximum value is 1/2, occurring at both (1/√2,1/√2) and (−1/√2,−1/√2). The minimum is −1/2 at the other diagonal pair. Reporting a single positive-coordinate maximizer would miss another valid point unless the feasible region explicitly restricted both coordinates to be positive.

With the convention ∇f=λ∇g and g=x²+y²=b, the optimal maximum is b/2 for b>0, so λ=1/2 is its sensitivity to b. Rewriting the same geometric constraint as 2g=2b changes the numerical multiplier to 1/4. Thus a multiplier's number must be interpreted with the exact constraint scaling and sign convention. It is not an invariant physical property independent of the written constraint.

## Boundaries change the candidates

Now restrict the earlier quadratic objective to the rectangle 0≤x≤0.5, 0≤y≤2. Its unconstrained minimum (1,1) is infeasible. On each edge, substitute the fixed coordinate and optimize the remaining one-variable function, checking its endpoints too. The right edge x=0.5 has derivative 1+6y−8, giving y=7/6. This point is feasible and has value −35/6, approximately −5.833333.

The left edge x=0 has its minimum at y=4/3 with value −16/3. On the bottom edge y=0 the objective decreases through the allowed x range and its minimum is −1.75 at x=0.5. On the top edge y=2, the objective is x²−4, minimized at x=0 with value −4. Comparing all edge minima, with corners included in those checks, selects (0.5,7/6). The correct feasible optimum has a nonzero unconstrained gradient; it sits on a boundary.

## Worked example

First solve the unconstrained quadratic equations to get (1,1), classify it using D=8 and record value −6. Then impose the rectangle. Discard the infeasible stationary point, solve all four edge problems, and compare −35/6, −16/3, −1.75 and −4. The smallest is −35/6 at (0.5,7/6). The constrained minimum is higher than the unconstrained one, as expected when a feasible set is made smaller. This scale check catches an alleged constrained value below −6 for this particular objective.

## Common mistakes and checks

Do not treat Lagrange conditions as a sufficient global guarantee. Do not ignore corners or infeasible candidates. Check the constraint gradient and any positivity assumptions. A constrained optimum need not satisfy the unconstrained stationary equations. State whether a multiplier measures change in a resource, its scaled version or a differently signed constraint residual.

## Limits of this lesson

Objectives, designs and resource constraints are synthetic mathematical constructions. This is not a complete inequality-optimization or numerical optimization course, and it establishes no real manufacturing optimum. Practice checks selected candidates and classifications rather than full proof or solver reliability. Original instruction was developed with substantial AI assistance. The package remains partial, unreviewed and formative-only.
