# A well-mixed perfused chamber: first-order linear ODEs, steady state, time constants and a numerical check

Perfusion bioreactors, organ-on-chip devices and even the blood in an organ can be idealized as a well-mixed volume with flow in and out and a reaction inside. The resulting differential equation is first-order and linear, and it is one of the most useful in engineering biology. This lesson solves it, extracts the steady state and the time constant, and then solves it numerically with Euler's method to show how a step size can produce nonsense and how to check for it.

## Learning objectives

By the end of this lesson, you should be able to:

1. Derive a first-order linear ODE for a well-mixed chamber from a mass balance and classify it.
2. Compute the steady state, the time constant and the time to reach 90% of steady state.
3. Apply Euler's method, compare a step with the exact solution, and use the stability limit to check a numerical result against physical constraints.

## The mass balance

A chamber of volume V is perfused at flow Q with medium at inlet concentration C_in. The chamber is well mixed, so the outlet concentration equals the chamber concentration C. Cells consume the solute at a rate proportional to C, with rate constant k. Then

**V dC/dt = Q C_in − Q C − k V C,** or **dC/dt = D (C_in − C) − kC,**

with dilution rate D = Q/V. Rearranged, dC/dt + (D + k) C = D C_in: a first-order, linear, constant-coefficient ODE. It can be solved by separation of variables or with an integrating factor.

**Synthetic parameters:** V = 10 mL, Q = 0.5 mL/min (so D = 0.05 min⁻¹), C_in = 10 mM, k = 0.02 min⁻¹, and C(0) = 0.

## Solution, steady state and time constant

Let λ = D + k = 0.07 min⁻¹. The solution starting from zero is

**C(t) = C_ss (1 − e^(−λt)),** with **C_ss = D C_in / (D + k).**

Here C_ss = 0.05 × 10 / 0.07 = 7.14 mM, lower than the inlet because cells consume part of the supply. The **time constant** is τ = 1/λ = 14.3 min: after one τ the chamber has covered 63% of the way to steady state, and after t = τ ln 10 = 32.9 min it reaches 90%. Note that the time constant depends on both flow and consumption, not on the flow alone.

The steady state is stable: if C is above C_ss, dC/dt is negative, and vice versa. Any disturbance decays with the same time constant τ.

## Euler's method and its failure

Euler's method steps forward with the slope at the start of each step: C_{n+1} = C_n + h f(C_n), with f(C) = D C_in − λC. With h = 10 min from C = 0, the first step gives C₁ = 0 + 10 × (0.05 × 10) = 5.00 mM, while the exact value at 10 min is 3.60 mM. Euler overshoots because it uses the initial (steepest) slope for the whole step.

For this linear equation each Euler step multiplies the deviation from steady state by (1 − λh). If |1 − λh| > 1, deviations grow and the numerical solution oscillates with increasing amplitude, though the true solution is smooth. The stability limit is therefore **h < 2/λ** = 28.6 min. Between 1/λ and 2/λ, the solution oscillates but still converges. A numerical result that oscillates, goes negative or exceeds the inlet concentration violates physical constraints of this system, and that is a reason to distrust the step size before the model.

## Checks to make on any numerical solution

- **Bounds:** concentrations stay between 0 and the largest source concentration when there is no production.
- **Steady state:** the numerical solution should settle at the analytically computed C_ss.
- **Convergence:** halving h should change the answer by a predictable amount (about half for Euler, which is first-order accurate).
- **Conservation:** inflow minus outflow minus consumption over a period should equal the change in amount in the chamber.

## Common mistakes

- Taking the time constant from the flow alone, when τ = 1/(D + k) includes consumption.
- Reporting the inlet concentration as the steady state and ignoring consumption.
- Using an Euler step larger than 2/λ and trusting results that oscillate or go negative.
- Reading stable as accurate: a step inside the stability limit can still overshoot badly.
- Skipping the checks on bounds, steady state, convergence and conservation because the output looks smooth.

## Worked example

**Problem.** The team doubles the flow to Q = 1.0 mL/min with everything else unchanged. What are the new steady state and time to 90%?

**Step 1.** D = 0.1 min⁻¹ and λ = 0.12 min⁻¹.

**Step 2.** C_ss = 0.1 × 10 / 0.12 = 8.33 mM, closer to the inlet, because consumption removes a smaller share of a faster supply.

**Step 3.** t₉₀ = ln 10 / 0.12 = 19.2 min, faster. The Euler stability limit falls to 2/0.12 = 16.7 min, so a step size that was stable before may not be now.

## Limits of this lesson

Parameters are synthetic. Real chambers are not perfectly mixed, consumption often saturates (Michaelis–Menten rather than first order) and cells grow, which makes k change with time.
