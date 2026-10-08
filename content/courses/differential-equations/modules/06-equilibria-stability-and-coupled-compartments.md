# Equilibria and stability: harvesting a logistic population and two coupled compartments

Many questions about living systems are questions about equilibria: will a population settle, at what level, and does it recover after a disturbance? A culture that is continuously harvested, a tissue whose cells are replaced, and a molecule exchanging between blood and tissue can all be analyzed by finding equilibria and linearizing around them. This lesson does that for a harvested logistic population (one variable) and for two coupled compartments (a linear system with eigenvalues).

## Learning objectives

By the end of this lesson, you should be able to:

1. Find the equilibria of a one-variable nonlinear ODE and classify their stability from the sign of the derivative.
2. Interpret the linearized slope at a stable equilibrium as a recovery time constant and find the harvest rate that maximizes sustained yield.
3. Write two coupled compartments as a matrix system and use its eigenvalues to determine stability and the slow and fast time scales.

## A harvested population

A culture grows logistically and a constant fraction h of cells is removed per unit time, for example by continuous withdrawal:

**dN/dt = f(N) = rN(1 − N/K) − hN.**

**Equilibria** are where f(N) = 0: N = 0 and **N\* = K(1 − h/r)**, which is positive only if h < r. With synthetic values r = 0.03 h⁻¹, K = 10⁶ cells and h = 0.01 h⁻¹, N\* = 6.667×10⁵ cells, and the harvest yield is hN\* = 6667 cells/h.

## Stability by linearization

Near an equilibrium N_e, write N = N_e + x with x small. Then dx/dt ≈ f′(N_e) x: the deviation grows if f′(N_e) > 0 and decays if f′(N_e) < 0. Here f′(N) = r − 2rN/K − h, so

- f′(0) = r − h = 0.019999999999999997 h⁻¹ > 0: the empty state is unstable, as any few cells grow;
- f′(N\*) = −(r − h) = -0.019999999999999997 h⁻¹ < 0: the harvested population is stable, and a disturbance decays with time constant 1/(r − h) = 50 h.

If harvesting exceeds the growth rate (h > r), N\* disappears and the only equilibrium, N = 0, becomes stable: the population is washed out. Recovery also slows as h approaches r, which is a warning sign that a system is close to collapse.

**Maximum sustained yield.** The yield at equilibrium is Y(h) = hK(1 − h/r). Setting dY/dh = K(1 − 2h/r) = 0 gives h = r/2 = 0.015 h⁻¹ and Y = rK/4 = 7500 cells/h, achieved with the population held at K/2, the point of fastest logistic growth.

## Two coupled compartments

A tracer exchanges between a blood compartment (amount x) and a tissue compartment (amount y) and is eliminated from blood:

dx/dt = −(k₁₂ + k₁₀) x + k₂₁ y
dy/dt = k₁₂ x − k₂₁ y

In matrix form, **d/dt [x, y]ᵀ = A [x, y]ᵀ** with

A = [[−(k₁₂ + k₁₀), k₂₁], [k₁₂, −k₂₁]].

**Synthetic rate constants:** k₁₂ = 0.3, k₂₁ = 0.1, k₁₀ = 0.2 h⁻¹. Then A = [[-0.5, 0.1], [0.3, -0.1]], with trace -0.6 and determinant 0.02. The eigenvalues solve λ² − (trace)λ + det = 0:

λ = [-0.6 ± √(0.36 − 0.08)]/2, giving λ₁ = -0.0354 h⁻¹ and λ₂ = -0.5646 h⁻¹.

Both are negative, so the only equilibrium (zero tracer) is stable. The solution is a sum of two exponentials: a **fast** phase with time constant 1/|λ₂| = 1.77 h, dominated by distribution into tissue, and a **slow** phase with time constant 1/|λ₁| = 28.2 h, dominated by return from tissue and elimination. A semi-log plot of blood amount shows two straight segments, and the late slope estimates the slow eigenvalue. For a 2×2 system, trace < 0 and det > 0 together guarantee that both eigenvalues have negative real parts.

## Common mistakes

- Classifying an equilibrium as stable because the population is there now; stability is about whether small deviations shrink.
- Using a negative trace alone as proof of stability in two dimensions; the determinant must also be positive.
- Forgetting that linearization is local: a population far from N* can follow a different path.
- Reading the yield-maximizing harvest as the safest one; near h = r, recovery is slow and noise can push the population to washout.

## Worked example

**Problem.** In the harvested culture, the operator raises h from 0.01 to 0.025 h⁻¹. What are the new equilibrium, yield and recovery time constant?

**Step 1.** N\* = 10⁶ × (1 − 0.025/0.03) = 1.667×10⁵ cells.

**Step 2.** Yield = 0.025 × 1.667×10⁵ = 4167 cells/h, lower than at h = 0.01, because h is past r/2.

**Step 3.** Recovery time constant = 1/(0.03 − 0.025) = 200 h, ten times slower. Harvesting harder past the optimum gives less yield and a more fragile population.

## Limits of this lesson

Parameters are synthetic. Linearization describes behavior only near an equilibrium; large disturbances, delays and noise can produce behavior that it misses.
