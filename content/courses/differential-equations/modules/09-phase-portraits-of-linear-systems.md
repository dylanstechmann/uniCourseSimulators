# Phase portraits of linear systems: eigenvalues, eigenvectors and the shape of the flow

Two coupled state variables (two compartments, two cell types, a concentration and its rate of change) are described by x′ = A x with a 2 × 2 matrix A. Plotting y against x for many starting points, the **phase portrait**, shows where the system goes: straight into the equilibrium, around it in a spiral, away from it or past it. The shape is fixed by two numbers computed from A, its trace and determinant, and the details by its eigenvalues and eigenvectors. This lesson reads those numbers, classifies the equilibrium and computes the solution from a given start. All values are synthetic.

## Learning objectives

By the end of this lesson, you should be able to:

1. Classify the equilibrium of x′ = A x from the trace and determinant of A.
2. Compute eigenvalues, eigenvectors and the constants of the solution for a given initial condition.
3. Interpret the behavior of a node, a spiral and a saddle, including the period and decay of a spiral.

## Eigenvalues, eigenvectors and the solution

If A v = λ v with v ≠ 0, then x(t) = v e^(λt) is a solution: the state stays on the line through v and scales exponentially. For two distinct real eigenvalues, the general solution is

**x(t) = c₁ v₁ e^(λ₁t) + c₂ v₂ e^(λ₂t),**

and the constants follow from x(0) = c₁ v₁ + c₂ v₂. The eigenvalues are the roots of λ² − T λ + D = 0, where T is the trace (the sum of the diagonal entries) and D the determinant, and T = λ₁ + λ₂ and D = λ₁ λ₂. For complex eigenvalues λ = α ± jβ, the solution is an oscillation of angular frequency β under the envelope e^(αt).

## Classification by trace and determinant

- **D < 0:** the eigenvalues are real with opposite signs: a **saddle**, always unstable.
- **D > 0 and T² − 4D > 0:** distinct real eigenvalues of the same sign, a **node**; stable if T < 0, unstable if T > 0. Equality gives a repeated eigenvalue and requires a separate check of the eigenvectors.
- **D > 0 and T² − 4D < 0:** complex eigenvalues, a **spiral**; stable if T < 0, unstable if T > 0, and a closed orbit (a **center**) if T = 0.
- **D = 0:** at least one zero eigenvalue. Equilibria are the null space of A: a line if A has rank one, or the whole plane if A is the zero matrix. This boundary case is outside the distinct-eigenvalue classification above.

## A stable node

**Synthetic example:** A = [[−2, 1], [1, −2]] has trace −4 and determinant **3**; T² − 4D = 4 > 0, so the eigenvalues are real and negative: λ₁ = **−1** and λ₂ = −3, with eigenvectors (1, 1) and (1, −1). From x(0) = (3, 1), writing (3, 1) = c₁(1, 1) + c₂(1, −1) gives c₁ = **2** and c₂ = 1, so

x(t) = 2(1, 1) e^(−t) + 1(1, −1) e^(−3t).

At t = 1, x = (2e^(−1) + e^(−3), 2e^(−1) − e^(−3)) = (**0.7855**, 0.6860). The e^(−3t) term dies quickly, so the trajectory bends onto the slow direction (1, 1) and then approaches the origin along it.

## A stable spiral

**Synthetic example:** A = [[−0.5, 2], [−2, −0.5]] has trace −1 and determinant 4.25, and T² − 4D < 0. The eigenvalues are −0.5 ± 2j: an oscillation with angular frequency 2 rad per unit time, a period of 2π/2 = **3.1416**, under an envelope e^(−0.5t). Each full turn shrinks the distance from the origin by the factor e^(−0.5 × 3.1416) = **0.2079**, so the system spirals inward and is close to the equilibrium after two or three turns.

## A saddle

**Synthetic example:** A = [[1, 2], [2, 1]] has determinant −3 < 0. The eigenvalues are **3** and −1, with eigenvectors (1, 1) and (1, −1). Starting exactly on the line of (1, −1), x(t) = (1, −1)e^(−t) decays to the origin; this line is the **stable direction**. Any start with a component along (1, 1) is eventually thrown out along that unstable direction. For x(0) = (1.1, −1) = 0.05(1, 1) + 1.05(1, −1), the unstable component is small at first, but at t = 2 the state is (20.3, 20.0), very far from the origin. A saddle is therefore highly sensitive: a small error in the starting point or in a model parameter decides whether the system returns or departs.

## Common mistakes

- Judging stability from the trace alone; the determinant must also be positive in two dimensions.
- Normalizing eigenvectors differently in the vector and in the constants, so that c₁ and c₂ no longer match.
- Using the eigenvalues of A for a system written as x′ = A x + b without first shifting to the equilibrium.
- Reading the period of a spiral from the real part of the eigenvalue instead of the imaginary part.
- Treating the shape of the portrait as unchanged when the units of one variable are rescaled; the straight-line directions change although the eigenvalues do not.
- Expecting a trajectory to approach the origin along the fast direction; it approaches along the slow one.

## Worked example

**Problem.** A = [[−3, 2], [1, −2]] and x(0) = (1, 2). Classify the equilibrium and find x(0.5).

**Step 1: trace and determinant.** T = −5 and D = **4**, so λ² + 5λ + 4 = 0 and the eigenvalues are −1 and −4: a stable node.

**Step 2: eigenvectors.** For λ = −1, (A + I)v = 0 gives v = (1, 1); for λ = −4, (A + 4I)v = 0 gives v = (2, −1).

**Step 3: constants.** (1, 2) = c₁(1, 1) + c₂(2, −1) gives c₁ = 5/3 and c₂ = −1/3.

**Step 4: the state.** x(t) = (5/3)(1, 1)e^(−t) − (1/3)(2, −1)e^(−4t), so x(0.5) = (**0.9207**, 1.0560).

## Limits of this lesson

All numbers are synthetic. The lesson treats two-variable linear systems with constant coefficients and distinct eigenvalues; repeated eigenvalues, three or more variables and nonlinear terms need further tools, and a linear portrait describes a nonlinear system only near an equilibrium.
