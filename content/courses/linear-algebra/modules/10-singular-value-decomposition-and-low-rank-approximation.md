# The singular value decomposition and low-rank approximation

Every matrix, square or not, symmetric or not, can be written as orthogonal changes of coordinates and a possibly rectangular stretch. This is the singular value decomposition (SVD), and it is a central tool in applied linear algebra: it gives the rank, the best approximation of the matrix by one of lower rank, the condition number and the principal axes of a data set. A large data matrix of samples by genes, or of pixels by frames, is often well described by a few singular values, but smaller components may contain important signals as well as noise. This lesson states the decomposition, computes it for a small example by hand, measures how much of a matrix a rank-one approximation captures and counts what storing the approximation saves. All values are synthetic.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute the singular values of a small matrix from the eigenvalues of AᵀA.
2. Compute the energy captured by a rank-k approximation and the error of the approximation.
3. Count the storage saved by a low-rank approximation and evaluate when it is useful.

## The decomposition

Any m × n matrix can be factored as

**A = U Σ Vᵀ,**

where U (m × m) and V (n × n) have orthonormal columns and Σ is an m × n rectangular diagonal matrix with nonnegative entries σ₁ ≥ σ₂ ≥ … ≥ 0, the **singular values**. The positive squared singular values are the nonzero eigenvalues shared by AᵀA and AAᵀ; their zero eigenvalue multiplicities can differ when m ≠ n. The columns of V are the eigenvectors of AᵀA, and the number of nonzero singular values is the rank. Equivalently, A is a sum of rank-one pieces,

**A = σ₁ u₁v₁ᵀ + σ₂ u₂v₂ᵀ + … ,**

in descending singular-value order. Orthogonal factors may include reflections. Singular values measure algebraic size, not biological importance.

**Synthetic data matrix** (three samples by two variables): A = [[3, 1], [2, 2], [1, 3]]. Then AᵀA = [[14, 10], [10, 14]], with trace 28 and determinant 14 × 14 − 10² = 96, so its eigenvalues are 14 ± 10 = 24 and 4. The singular values are **σ₁ = √24 = 4.8990** and **σ₂ = √4 = 2.0**. The eigenvectors of AᵀA are v₁ = (1, 1)/√2 and v₂ = (1, −1)/√2, and u₁ = Av₁/σ₁ = (1, 1, 1)/√3 and u₂ = Av₂/σ₂ = (1, 0, −1)/√2.

## Energy and the best low-rank approximation

The sum of squares of all entries of A, its squared Frobenius norm, equals the sum of the squared singular values: 28 = 24 + 4, so ‖A‖_F = √28 = **5.2915**. The **Eckart–Young theorem** says that the best rank-k approximation to A (the one with the smallest error in the Frobenius norm) keeps the first k terms of the sum, and that its error is the square root of the sum of the squares of the singular values that were dropped. Here the rank-one approximation is A₁ = σ₁u₁v₁ᵀ = [[2, 2], [2, 2], [2, 2]], each entry being the average of the matrix, and the error matrix A − A₁ = [[1, −1], [0, 0], [−1, 1]] has norm √4 = **2.0** = σ₂. The fraction of the energy captured by the first singular value is σ₁²/‖A‖²_F = 24/28 = **0.8571**, and the relative error is σ₂/‖A‖_F = 0.3780. The ratio σ₁/σ₂ = 2.4495 is the condition number of A.

## Why it saves storage

An m × n matrix has mn entries. A rank-k approximation can be stored as k columns of U, k rows of V and k singular values, which is k(m + n + 1) numbers. For a 1000 × 50 matrix (1000 samples, 50 variables) and k = 3, that is 3 × (1000 + 50 + 1) = **3,153** numbers instead of 50,000, a compression by a factor of **15.86**. Storage decreases only when k(m + n + 1) < mn, and the approximation is useful only when its error is acceptable for the task. Rapid spectral decay can help accuracy but alone does not guarantee fewer stored numbers. Noise need not have a rapidly decaying spectrum. For the 3 × 2 example above, rank-one storage is 1 × (3 + 2 + 1) = 6 numbers, equal to the six original entries, which is also a useful reminder that the idea pays for large matrices with a few dominant directions.

## Singular values as a diagnostic

A very small last singular value signals near rank deficiency: the matrix almost maps a whole direction to zero. For T = [[2, 2], [1, 1], [3, 3.1]] the singular values are 5.3487 and **0.0418**, a ratio of 128; the two columns are almost equal, and a fit that uses both has an unstable difference between its coefficients. The next lessons turn this ratio into error bounds.

## Common mistakes

- Taking the singular values to be the eigenvalues of A itself (they are the square roots of the eigenvalues of AᵀA).
- Forgetting the square root: σ = √λ.
- Reporting the error of the rank-k approximation without the square root of the sum of the dropped squared singular values.
- Calling a matrix low rank because a few singular values are large, when the others are small but not zero.
- Using a low-rank approximation of a matrix whose singular values decay slowly.
- Centering data before the SVD in one analysis and not in another, and then comparing the results.

## Worked example

**Problem.** For A = [[1, 1], [1, −1], [2, 0]] find the singular values, the fraction of energy in the first, and the error of the rank-one approximation.

**Step 1: AᵀA.** AᵀA = [[6, 0], [0, 2]], so the eigenvalues are 6 and 2 and the singular values are **√6 = 2.4495** and √2 = 1.4142.

**Step 2: energy.** ‖A‖²_F = 1 + 1 + 1 + 1 + 4 + 0 = 8, and the first singular value carries 6/8 = **0.75**.

**Step 3: error.** The rank-one approximation is [[1, 0], [1, 0], [2, 0]] and the error matrix is [[0, 1], [0, −1], [0, 0]], with norm √2 = **1.4142** = σ₂.

## Limits of this lesson

All numbers are synthetic. The lesson computes singular values through AᵀA for small matrices, which squares the condition number and is not how software does it; real data matrices are decomposed with stable algorithms, and the choice of rank needs a criterion beyond a threshold on the energy.
