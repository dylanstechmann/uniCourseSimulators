# Stiff equations and implicit methods: stability limits of explicit Euler and the Michaelis–Menten depletion time

Biological and chemical systems often combine processes that run at very different speeds: a binding equilibrium that settles in a fraction of a second, a metabolic drain that takes hours. An equation that contains both is called **stiff**. Solving it with the simple explicit Euler method forces a step size set by the fastest process, even long after that process has finished and when only the slow one matters, and a step that is too large does not just lose accuracy: it produces numbers that oscillate in sign or blow up, including negative concentrations. Implicit methods remove the stability limit. This lesson works out the limits for the test equation, shows how stiffness is measured from eigenvalues, and solves a Michaelis–Menten depletion exactly as a check. All values are synthetic.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute the stability and positivity limits of explicit Euler and the amplification factors of explicit and implicit Euler for a decay equation.
2. Measure the stiffness of a linear system from its eigenvalues and estimate the number of steps a stable explicit method needs.
3. Solve a Michaelis–Menten depletion for the time to reach a concentration, and use it to judge a numerical result.

## The test equation

The decay equation y′ = −λy (λ > 0) has the exact solution y(t) = y₀ e^(−λt). **Explicit Euler** advances it by y_(n+1) = y_n + h(−λ y_n) = (1 − λh) y_n. The numerical solution decays in magnitude only if |1 − λh| < 1, that is **h < 2/λ**, and it stays nonnegative and monotone only if 1 − λh ≥ 0, that is **h ≤ 1/λ**. At equality the first step reaches zero; strict positivity requires h < 1/λ. **Implicit Euler** evaluates the right side at the new point, y_(n+1) = y_n − h λ y_(n+1), so y_(n+1) = y_n/(1 + λh): the factor is between 0 and 1 for every positive h, so the solution is stable and positive at any step size for this decay equation, although it is accurate only to first order in h.

**Synthetic fast process:** λ = 50 h⁻¹. The explicit stability limit is h < 2/50 = **0.04 h** and the positivity limit is h ≤ **0.02 h**. With h = 0.05 h, the explicit factor is 1 − 50 × 0.05 = −1.50, with magnitude **1.5**, so the solution flips sign and grows: 1, −1.5, 2.25, −3.38. The implicit factor is 1/(1 + 2.5) = **0.2857**, giving 1.0000, 0.2857, 0.0816, 0.0233, a smooth decay (the exact factor per step is e^(−2.5) = 0.0821).

## Stiffness

For a linear system y′ = A y with real, negative eigenvalues, the stability of explicit Euler is governed by the most negative eigenvalue, and the time scale of interest by the least negative one. The ratio of their magnitudes is the **stiffness ratio**. For complex eigenvalues, check |1 + hλ| < 1 for every mode rather than using this real-eigenvalue rule. **Synthetic two-compartment model:** a drug exchanges between two compartments at rate k_f = 25 h⁻¹ each way and is eliminated from the first at k_e = 0.1 h⁻¹. The matrix has trace −(2k_f + k_e) = −50.1 and determinant k_f k_e = 2.5, so λ² + 50.1λ + 2.5 = 0 and the eigenvalues are **−0.04995** and −50.050 h⁻¹. The ratio is |−50.050/−0.04995| = **1002**. The fast mode has a time constant of 0.02 h and is gone after about 0.1 h, while the slow mode has a time constant of 20 h, but explicit Euler must keep h below 2/50.05 = 0.0400 h throughout: at least 251 equal steps to cover 10 h, against 20 steps for implicit Euler with h = 0.5 h. Rounding the bound to 0.04 h would give 250 steps but an amplification factor slightly below −1, so that choice is unstable. For one equation the cost is trivial, for hundreds of coupled reactions it is not.

## Michaelis–Menten depletion

A substrate S consumed by an enzyme follows dS/dt = −V_max S/(K_m + S). Separating variables gives the implicit solution **K_m ln(S₀/S) + (S₀ − S) = V_max t**, which gives the time to reach a concentration directly. **Synthetic values:** V_max = 2.0 mM/h, K_m = 0.5 mM and S₀ = 5 mM. The initial rate is V_max S₀/(K_m + S₀) = **1.818 mM/h**, close to V_max because the enzyme is nearly saturated. The time to fall to S = 0.5 mM is (0.5 ln(10) + 4.5) / 2.0 = **2.826 h**. This exact value is a check on any numerical solution of the same equation.

Explicit Euler can make this solution negative. Near S = 0 the rate is about (V_max/K_m) S, which is first-order with λ = V_max/K_m = 4 h⁻¹, so the positivity limit is **h ≤ K_m/V_max = 0.25 h**. A step of 3 h from S = 0.5 mM would give S = 0.5 − 3 × 2.0 × 0.5/(0.5 + 0.5) = −2.5 mM, a negative concentration. The quasi-steady-state treatment of the enzyme–substrate complex used to derive the rate law is itself valid only when the enzyme concentration is small compared with K_m + S₀: for 0.01 mM enzyme the ratio is 0.01/(0.5 + 5) = 0.0018.

## Common mistakes

- Choosing the step from the accuracy needed for the slow process and ignoring the fast one's stability limit.
- Treating a stable-looking explicit solution as accurate; a step between 1/λ and 2/λ is stable but oscillates in sign.
- Applying implicit Euler to a nonlinear equation without solving the implicit equation (it needs an iteration).
- Assuming that an implicit method is accurate for any step; it is stable, not accurate.
- Reading a negative concentration as a rounding error instead of a step-size or model failure.
- Using the Michaelis–Menten rate law outside the range where the enzyme is much less abundant than the substrate.

## Worked example

**Problem.** For y′ = −20y with h = 0.08 h, find the explicit stability and positivity limits, the explicit and implicit factors and the exact factor. Then find the time for a substrate with V_max = 1.5, K_m = 0.8 and S₀ = 4 to fall to 0.4.

**Step 1: limits.** 2/20 = **0.10 h** and 1/20 = 0.05 h.

**Step 2: factors.** Explicit: 1 − 1.6 = **−0.6** (stable, since |−0.6| < 1, but the sign flips because h exceeds 0.05); implicit: 1/(1 + 1.6) = **0.3846**; exact: e^(−1.6) = 0.2019.

**Step 3: depletion time.** (0.8 ln(10) + 3.6)/1.5 = **3.628 h**, and the positivity limit of explicit Euler is 0.8/1.5 = 0.53 h.

## Limits of this lesson

All numbers are synthetic. The lesson treats the linear test equation and one nonlinear rate law; real stiff systems need adaptive implicit solvers, and the stiffness ratio is only a guide. The step-size limits are for explicit Euler, not for higher-order methods, which have different limits.
