# Symmetric matrices, the spectral theorem and quadratic forms

Covariance matrices, stiffness matrices, the matrices AᵀA of least squares and the Hessians of optimization problems are all symmetric, and symmetric matrices have a particularly clean eigenstructure: their eigenvalues are real, and their eigenvectors can be chosen perpendicular. That fact, the spectral theorem, makes a symmetric matrix a set of independent stretches along perpendicular axes, and it is the algebra behind principal component analysis. This lesson states the theorem, computes it for a 2 × 2 example, connects it to the quadratic form xᵀAx and applies it to the variance of data along a direction. All values are synthetic.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute the eigenvalues and orthonormal eigenvectors of a 2 × 2 symmetric matrix and check the trace and determinant.
2. Evaluate a quadratic form and determine from the eigenvalues whether a symmetric matrix is positive definite.
3. Interpret the largest eigenvalue and its eigenvector as the direction of greatest variance of a covariance matrix.

## The spectral theorem

A real symmetric matrix A has real eigenvalues, and there is an orthonormal basis of eigenvectors q₁, q₂, …. Writing Q for the matrix with these as columns and Λ for the diagonal matrix of eigenvalues,

**A = Q Λ Qᵀ,**

with Q⁻¹ = Qᵀ. In the basis of the eigenvectors the matrix is diagonal: A just stretches by λ_i along each axis. The trace of A is the sum of the eigenvalues and the determinant is their product.

**Synthetic matrix:** A = [[4, 1], [1, 3]]. The trace is 7 and the determinant is 4 × 3 − 1² = **11**. The eigenvalues satisfy λ² − 7λ + 11 = 0, so λ = (7 ± √(5))/2, that is **λ₁ = 4.6180** and **λ₂ = 2.3820**; they add up to 7 and multiply to 11. The eigenvector of λ₁ makes an angle θ with the first axis, where θ = ½ atan2(2a₁₂, a₁₁ − a₂₂) = ½ atan2(2, 1), so **θ = 31.72°**, q₁ = (0.8507, 0.5257), and q₂ = (−0.5257, 0.8507) is perpendicular to it (their dot product is 0).

Using only tan 2θ loses quadrant information and can select the smaller eigenvalue. For [[1, 0], [0, 3]], the dominant axis is the second axis, at 90°. When a = d and b = 0, the eigenvalues repeat and any orthonormal axes work. An eigenvector and its negative describe the same axis.

## Quadratic forms and definiteness

The **quadratic form** of A is xᵀAx = a₁₁x₁² + 2a₁₂x₁x₂ + a₂₂x₂². For the matrix above, xᵀAx = 4x₁² + 2x₁x₂ + 3x₂². Along the unit vector w = (1, 1)/√2 it equals (4 + 2 + 3)/2 = **4.5**, which lies between the eigenvalues, and along q₁ it equals λ₁. In general, for unit vectors, xᵀAx ranges over the interval from λ_min to λ_max, and the extremes are reached along the eigenvectors (the **Rayleigh quotient**). A symmetric matrix is **positive definite** if xᵀAx > 0 for every nonzero x, which holds exactly when all eigenvalues are positive. For B = [[1, 2], [2, 1]], the eigenvalues are 3 and **−1**, so B is not positive definite: along x = (1, −1) the form equals 1 − 4 + 1 = **−2**, negative.

## Variance along a direction

If C is the covariance matrix of two measured variables, then the variance of the projection of the data onto a unit direction w is wᵀCw. Take C = A: the variance along the first axis is 4, along the second 3, and along the diagonal direction (1, 1)/√2 it is 4.5. The largest variance over all directions is λ₁ = 4.618, along q₁, at 31.7° from the first axis, and the smallest is λ₂ = 2.382, along q₂. The total variance is the trace, 7 = λ₁ + λ₂, whichever axes are used, and the fraction along the best direction is λ₁/(λ₁ + λ₂) = 0.660. The directions q₁ and q₂ are the principal axes, and finding them is principal component analysis.

## Common mistakes

- Using eigenvectors that are not orthogonal for a symmetric matrix; for distinct eigenvalues they are orthogonal automatically, and within a repeated eigenvalue they must be chosen so.
- Forgetting to normalize the eigenvectors, so that Q is not orthogonal.
- Treating a matrix with a zero or negative eigenvalue as positive definite because its diagonal entries are positive.
- Computing xᵀAx with a non-unit x and comparing it with the eigenvalues.
- Forgetting to halve the angle 2θ obtained from tan 2θ.
- Applying the theorem to a non-symmetric matrix, whose eigenvalues may be complex.

## Worked example

**Problem.** For C = [[5, 2], [2, 2]], find the eigenvalues, the angle of the dominant eigenvector, the variance along the second axis and the fraction of the total variance along the dominant direction.

**Step 1: eigenvalues.** Trace 7, determinant 6: λ = (7 ± √25)/2, so **6.0000** and 1.0000.

**Step 2: angle.** θ = ½ atan2(2 × 2, 5 − 2), so θ = **26.57°**.

**Step 3: variance and fraction.** Along the second axis the variance is c₂₂ = 2. The dominant direction carries 6.0000/7 = **0.857** of the total variance.

## Limits of this lesson

All numbers are synthetic. The lesson treats 2 × 2 real symmetric matrices in exact arithmetic; larger matrices are decomposed by software, and repeated eigenvalues leave the eigenvectors undetermined within a subspace.
