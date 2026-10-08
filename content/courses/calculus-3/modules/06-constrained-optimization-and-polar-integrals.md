# Optimizing with and without constraints, and integrating over a disk in polar coordinates

Two multivariable skills recur in engineering biology. Optimization picks the best design when several variables interact, often under a constraint such as a fixed volume or budget. Multiple integrals add up a quantity spread over an area or volume, and choosing coordinates that match the geometry turns a hard integral into an easy one. This lesson finds and classifies an unconstrained critical point, uses Lagrange multipliers to design a culture vessel, and integrates a radially symmetric surface density over a disk in polar coordinates.

## Learning objectives

By the end of this lesson, you should be able to:

1. Find critical points of a two-variable function and classify them with the second-derivative (Hessian) test.
2. Solve a constrained optimization with a Lagrange multiplier and interpret the optimal design.
3. Set up and evaluate a double integral in polar coordinates, including the Jacobian factor r, for a radially symmetric quantity.

## Unconstrained critical points

For f(x, y) = x² + xy + y² − 3x, set both partial derivatives to zero:

f_x = 2x + y − 3 = 0, f_y = x + 2y = 0 ⇒ (x, y) = (2, -1), f = -3.

The second-derivative test uses D = f_xx f_yy − (f_xy)² = 2 × 2 − 1² = 3. Since D > 0 and f_xx > 0, the point is a local minimum (here also the global one, since f is a convex quadratic). If D < 0 the point would be a saddle; if D = 0 the test is inconclusive.

## Constrained optimization: a vessel with the least wall

A closed cylindrical vessel must hold V = 100 cm³. Its wall area (sides plus two ends) is A(r, h) = 2πr² + 2πrh, to be minimized subject to g(r, h) = πr²h − V = 0. At a constrained optimum the gradients are parallel: **∇A = λ ∇g**.

- ∂A/∂r = 4πr + 2πh = λ · 2πrh
- ∂A/∂h = 2πr = λ · πr²

The second equation gives λ = 2/r. Substituting into the first: 4πr + 2πh = 4πh, so **h = 2r**: the best cylinder is as tall as it is wide. With the volume constraint, πr²(2r) = V, so r = (V/2π)^(1/3) = 2.515 cm, h = 5.031 cm, and A = 6πr² = 119.3 cm².

The multiplier has a meaning: λ = dA/dV at the optimum, the extra wall area per extra unit of volume, here 2/r = 0.795 cm⁻¹. Real vessels depart from h = 2r for good reasons (headspace, mixing, handling, the cost of ends versus sides), and those reasons can be added as further terms or constraints.

## Integrating over a disk in polar coordinates

A signaling molecule bound to a surface has a synthetic density σ(r) = 100 exp(−r²/5000) molecules/μm², depending only on distance r from a source. How many molecules lie within R = 50 μm?

In Cartesian coordinates the integral ∬ σ dx dy over a disk has awkward limits. In polar coordinates the disk is simply 0 ≤ r ≤ R, 0 ≤ θ ≤ 2π, and the area element is **dA = r dr dθ** (the factor r is the Jacobian of the transformation: a ring at larger radius has more area). Then

N = ∫₀^(2π) ∫₀^R 100 e^(−r²/5000) r dr dθ = 2π × 100 × (5000/2) × (1 − e^(−R²/5000)).

With R = 50 μm, 1 − e^(−0.5) = 0.3935, so N = 618,060 molecules. Over the whole plane (R → ∞) the total is 1,570,796, so the disk holds 39.3% of it. The substitution u = r²/5000 works only because of the r from the Jacobian; forgetting it gives an integral with no elementary antiderivative and a wrong answer.

## Common mistakes

- Omitting the Jacobian r in polar integrals.
- Concluding a minimum from f_xx > 0 alone without checking D.
- Solving Lagrange equations but forgetting to apply the constraint to fix the scale.
- Treating λ as meaningless; it is the sensitivity of the optimum to the constraint.

## Worked example

**Problem.** An open-topped cylindrical dish (bottom but no lid) must hold 100 cm³. What shape minimizes the material?

**Step 1.** A = πr² + 2πrh with πr²h = V. Lagrange: 2πr + 2πh = λ 2πrh and 2πr = λπr², so λ = 2/r and 2πr + 2πh = 4πh, giving h = r.

**Step 2.** πr³ = V gives r = (V/π)^(1/3) = 3.169 cm = h.

**Step 3.** A = 3πr² = 94.7 cm². Removing the lid makes the optimum squatter (h = r instead of 2r), because the top no longer costs material.

## Limits of this lesson

All values are synthetic. The density field is a fixed illustration and the vessel model ignores wall thickness, manufacturing and use constraints.
