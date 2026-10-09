# Nonlinear systems and linearization: a two-gene toggle switch and bistability

Most of the systems this course models are nonlinear, and the linear tools of the previous lessons still apply to them in one way: near a steady state, a small disturbance obeys a linear equation, and the eigenvalues of that equation say whether it grows or decays. This lesson applies the idea to the simplest model of a binary cell-fate decision, two genes that repress each other. With weak repression the cell sits in one balanced state. With strong repression the balanced state becomes a saddle and two new stable states appear, one with gene X high and Y low and the other the reverse. The cell chooses one, and keeps it: a memory. All values are dimensionless and synthetic.

## Learning objectives

By the end of this lesson, you should be able to:

1. Find the steady states of a two-variable nonlinear system, including the symmetric one, and write the Jacobian there.
2. Compute the eigenvalues of the Jacobian and interpret a positive one as an instability and a negative one as a relaxation rate.
3. Explain bistability, and how a parameter crossing a threshold creates two stable states.

## The model

Let x and y be the levels of two proteins, each degraded at unit rate and each made at a rate that is repressed by the other:

**dx/dt = a/(1 + y²) − x,  dy/dt = a/(1 + x²) − y.**

Here a is the maximal synthesis rate in units of the repression threshold, and the exponent 2 means the repression is cooperative. Time is measured in units of the protein lifetime.

## Steady states

At a steady state, x = a/(1 + y²) and y = a/(1 + x²). One solution has x = y = s, so s(1 + s²) = a. For a = 3, s³ + s − 3 = 0 gives **s = 1.2134**. Other solutions have x ≠ y. For a = 3 they are x = (3 + √5)/2 = **2.6180** with y = (3 − √5)/2 = 0.3820 (and the mirror image), which can be checked: 3/(1 + 2.6180²) = 0.3820.

## Linearization

Near a steady state (x*, y*), write x = x* + u and y = y* + v. Then du/dt and dv/dt are linear in u and v, with the **Jacobian** matrix of partial derivatives. For this model

J = [[−1, −c_y], [−c_x, −1]],  with c_y = 2ay/(1 + y²)² and c_x = 2ax/(1 + x²)² (the minus signs are the derivatives of the repressed synthesis terms).

At the symmetric state, c_x = c_y = m = 2as/(1 + s²)² = 2 × 3 × 1.2134/(1 + 1.4724)² = **1.1911**. The eigenvalues of [[−1, −m], [−m, −1]] are −1 ± m: with eigenvector (1, 1) the eigenvalue is −1 − m = −2.1911, and with eigenvector (1, −1) it is **−1 + m = 0.1911**. The determinant is 1 − m² = −0.419 < 0, so by the classification of the previous lesson the symmetric state is a **saddle**: the symmetric combination decays, but a small difference between x and y grows at the rate 0.191.

At the asymmetric state (x, y) = (2.618, 0.382), c_y = 1.7454 and c_x = 0.2546, and the eigenvalues are −1 ± √(c_x c_y) = −1 ± 0.6667, that is **−0.3333** and −1.6667. Both are negative, so this state is stable, and a disturbance decays with the time constant 1/0.3333 = **3.0** protein lifetimes along the slow direction.

## Bistability and memory

The symmetric state is a saddle exactly when m > 1. For this model the threshold is a = 2: at a = 2, s = 1 and m = 2 × 2 × 1/(1 + 1)² = 1. Below the threshold, for example a = 1.5, m = 0.8517 < 1, the symmetric state is stable and is the only state, so the cell has no memory. Above the threshold, there are three steady states, the unstable symmetric one and two stable asymmetric ones, and the system is **bistable**. Integrating from a start with x slightly above y, (1.3, 1.1), the system settles at (2.618, 0.382); from (1.1, 1.3) it settles at the mirror image (0.382, 2.618). The tiny initial difference decides the outcome, and once there the system stays: a transient signal that tips the balance is remembered.

## Common mistakes

- Stopping at the symmetric steady state because it is the easiest to find.
- Linearizing and then using the linear solution far from the steady state.
- Forgetting the sign of the off-diagonal terms: repression gives negative entries in the Jacobian.
- Calling any system with a positive eigenvalue "unstable" without noting that the nearby stable states may still hold.
- Using the eigenvalue of the symmetric combination (−1 − m) to judge stability when the antisymmetric one is positive.
- Treating the threshold a = 2 as universal; it depends on the exponent and the form of the repression.

## Worked example

**Problem.** Take a = 4 in the same model. Find the symmetric steady state, the coupling m there, the unstable eigenvalue, and the stable asymmetric states.

**Step 1: symmetric state.** s³ + s − 4 = 0 gives **s = 1.3788**.

**Step 2: coupling.** m = 2 × 4 × 1.3788/(1 + 1.9011)² = **1.3106**, which exceeds 1, so the eigenvalue −1 + m = **0.3106** is positive: a saddle.

**Step 3: asymmetric states.** Solving x = 4/(1 + y²) and y = 4/(1 + x²) numerically gives x = 3.7321 and y = 0.2679, with Jacobian eigenvalues −1 ± √(c_x c_y) = −0.5000 and −1.5000, both negative.

## Limits of this lesson

All values are dimensionless and synthetic. The model is a textbook caricature: real cell-fate circuits have more genes, delays, noise and signaling inputs, and a stable state of a deterministic model is not a prediction about any real cell. The lesson treats only steady states and their local stability.
