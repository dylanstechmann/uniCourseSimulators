# Orthogonality, projections and QR: the geometry behind least squares

Least squares has a geometric meaning that makes it easy to understand, to check and to compute stably. The fitted values are the closest point to the data in the space that the model can reach, the residual is perpendicular to that space, and an orthogonal basis for the space turns the whole problem into reading off components. This lesson defines orthogonal projection onto a vector, builds an orthonormal basis by Gram–Schmidt, writes the result as the QR factorization and uses it to solve a small line-fitting problem without forming the normal equations. All values are synthetic.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute the orthogonal projection of a vector onto another and verify that the residual is orthogonal to it.
2. Build an orthonormal basis for two vectors by Gram–Schmidt and write the QR factorization.
3. Solve a least-squares problem by back-substitution with R and compute the residual norm.

## Projection onto a vector

The orthogonal projection of b onto the line through a is

**p = (a·b / a·a) a,**

the closest point to b on that line, and the **residual** r = b − p is perpendicular to a. **Synthetic vectors:** a = (1, 2, 2) and b = (4, 1, 2). Then a·b = 4 + 2 + 4 = 10, a·a = 1 + 4 + 4 = 9, the coefficient is 10/9 = **1.1111**, and p = (1.1111, 2.2222, 2.2222). The residual is r = (2.8889, −1.2222, −0.2222) with length **3.1447**, and a·r = 0.0: perpendicular, as it must be. By Pythagoras, ‖b‖² = ‖p‖² + ‖r‖².

## Orthonormal bases and Gram–Schmidt

Vectors q₁, q₂, … are **orthonormal** if each has length 1 and any two are perpendicular. With such a basis, the component of b along q_i is simply q_i·b, with no linear system to solve. Gram–Schmidt turns independent vectors a₁, a₂ into an orthonormal pair: q₁ = a₁/‖a₁‖; subtract from a₂ its component along q₁, v₂ = a₂ − (q₁·a₂) q₁; and q₂ = v₂/‖v₂‖.

**Synthetic line-fitting problem:** fit y = β₀ + β₁x to the points (1, 1), (2, 2), (3, 2). Then A has columns a₁ = (1, 1, 1) and a₂ = (1, 2, 3), and b = (1, 2, 2). Here ‖a₁‖ = √3 = 1.7321, so q₁ = (1, 1, 1)/√3. The component of a₂ along q₁ is q₁·a₂ = 6/√3 = 3.4641, and v₂ = a₂ − 3.4641 q₁ = (1, 2, 3) − 2(1, 1, 1) = (−1, 0, 1), with ‖v₂‖ = √2 = 1.4142, so q₂ = (−1, 0, 1)/√2.

## The QR factorization

Collecting the lengths and components into an upper-triangular matrix gives A = Q R with orthonormal columns in Q:

R = [[‖a₁‖, q₁·a₂], [0, ‖v₂‖]] = [[1.7321, 3.4641], [0, 1.4142]].

The least-squares problem min ‖b − Ax‖ becomes R x = Qᵀ b, because Qᵀ(b − Ax) has the components of the residual in the model space and nothing else. Here Qᵀb = (q₁·b, q₂·b) = (5/√3, 1/√2) = (2.8868, 0.7071). Back-substitution gives β₁ = 0.7071/1.4142 = **0.5000** and β₀ = (2.8868 − 3.4641 × 0.5000)/1.7321 = **0.6667**, the line y = 0.6667 + 0.5x. The residual norm follows from Pythagoras: ‖r‖² = ‖b‖² − ‖Qᵀb‖² = 9 − (8.3333 + 0.5000) = 0.1667, so **‖r‖ = 0.4082**.

## Why use QR

For full column rank, forming the Gram matrix AᵀA squares its 2-norm condition number compared with A (a later lesson), so a fit that is only mildly delicate can become unreliable in finite precision. Solving Rx = Qᵀb avoids forming AᵀA and is the standard way to solve least-squares problems in software. Projection by Qᵀ does not amplify the Euclidean norm. R retains the conditioning of A, so QR avoids added numerical sensitivity from forming AᵀA while leaving measurement sensitivity unchanged.

## Common mistakes

- Dividing by a·b instead of a·a in the projection coefficient.
- Normalizing q₂ before subtracting the q₁ component, or forgetting to normalize it afterwards.
- Treating a basis as orthonormal when its vectors are orthogonal but not unit length.
- Applying Gram–Schmidt to dependent vectors: v₂ = 0 signals the dependence.
- Reading the residual norm from the coefficients instead of from ‖b‖² − ‖Qᵀb‖².
- Forgetting that R is upper triangular and solving from the top instead of the bottom.

## Worked example

**Problem.** Project b = (1, 4, 1) onto a = (2, 1, 2), and then solve Rx = Qᵀb for the 2 × 2 problem A = [[3, 1], [0, 2]], b = (6, 4).

**Step 1: projection.** a·b = 8, a·a = 9, so the coefficient is **0.8889**, p = (1.7778, 0.8889, 1.7778), r = (−0.7778, 3.1111, −0.7778) with length 3.2998.

**Step 2: QR.** a₁ = (3, 0) has length 3, so q₁ = (1, 0); q₁·a₂ = 1, v₂ = (1, 2) − (1, 0) = (0, 2), and q₂ = (0, 1). So R = [[3, 1], [0, 2]] and Qᵀb = (6, 4).

**Step 3: back-substitution.** x₂ = 4/2 = 2, x₁ = (6 − 1 × 2)/3 = **1.3333**.

## Limits of this lesson

All numbers are synthetic. The lesson treats real vectors and small examples in exact arithmetic; classical Gram–Schmidt loses orthogonality in finite precision for nearly dependent columns, so software uses Householder reflections to compute Q and R.
