# Conditioning, error bounds and regularization

A full-rank measurement matrix can still determine its unknowns poorly. Rank asks whether an exact inverse exists; conditioning asks how much the answer moves when the data move. This distinction matters when two columns encode almost the same measurement. Elimination can return many decimal places while the last several digits contain little information about the underlying displacement. This lesson separates sensitivity of the mathematical problem from accuracy of a numerical algorithm, derives a perturbation bound and shows what ridge regularization changes. All matrices, displacements and errors below are synthetic teaching values.

## Learning objectives

1. Calculate a 2-norm condition number and apply a right-hand-side perturbation bound.
2. Distinguish numerical stability, measurement uncertainty and a small residual.
3. Calculate a ridge estimate and explain its bias and dependence on scaling.

## A direction the sensors barely see

Let A = [[1, 0.99], [0.99, 1]] and let x = (2, 3). Then b = Ax = (4.97, 4.98). The orthonormal directions q₊ = (1, 1)/√2 and q₋ = (1, −1)/√2 are eigenvectors with eigenvalues 1.99 and 0.01. Since A is symmetric positive definite, these are also its singular values. The common displacement is measured strongly, while the difference between the components is multiplied by only 0.01. The 2-norm condition number is κ₂(A) = σ_max/σ_min = 199. This number refers to the Euclidean norm and the stated coordinate scales. A different norm or different scaling can change it.

Perturb the signals by δb = (0.01, −0.01), a small change in opposite directions. It lies along q₋, so δx = A⁻¹δb = (1, −1). The reported solution becomes (3, 2), even though the data changed by only about two tenths of one percent. Its residual is exactly zero in exact arithmetic: A(3, 2) equals the perturbed b. A small residual measures agreement with the supplied data; it does not certify closeness to the unobserved truth. Here the model has as many independent equations as unknowns, so every signal pair is fitted exactly.

## Absolute and relative bounds

For fixed invertible A, δx = A⁻¹δb gives ‖δx‖₂ ≤ ‖A⁻¹‖₂ ‖δb‖₂. Here ‖A⁻¹‖₂ = 100, the signal perturbation norm is √2 × 0.01, and the bound on the displacement error is √2. Equality holds because this perturbation is in the least-sensitive direction. An equally large perturbation along q₊ would produce an error only 1/1.99 as large as its signal norm. A condition number bounds the worst direction, not the realized error for every direction.

Dividing by ‖x‖ and using ‖b‖ ≤ ‖A‖‖x‖ yields ‖δx‖/‖x‖ ≤ κ₂(A) ‖δb‖/‖b‖. For this example, ‖x‖ = √13 and ‖b‖ = √(4.97² + 4.98²). The actual relative displacement error is √(2/13) = 0.3922. If only an upper bound of 0.001 on relative signal error is known, the condition-number bound is 0.199. This last bound concerns a different hypothetical error budget; it is not the bound for the preceding δb. State which perturbation is being considered.

If A itself is uncertain, the fixed-matrix formula is insufficient. Calibration uncertainty changes both the inverse and the meaning of the data. For small δA, the equation to first order is A δx ≈ δb − δA x. A complete uncertainty analysis must include that term and the error correlations. Treating the matrix as exact when its entries came from noisy calibration understates uncertainty.

## Stable software cannot supply missing information

A backward-stable solve returns the exact answer to a nearby problem. On a well-conditioned problem this usually implies a close answer; on a poorly conditioned one the nearby problem may have a very different answer. QR and SVD can reduce numerical error, but neither creates information that the experiment failed to measure. For full column rank, κ₂(AᵀA) = κ₂(A)², here 39,601. Explicit normal equations can therefore worsen floating-point sensitivity compared with solving by QR or SVD. This statement concerns the Gram matrix used by the algorithm, not a claim that QR reduces the physical sensitivity of the original measurements.

## Ridge changes the question

Ridge chooses x_α to minimize ‖Ax − b‖² + α‖x‖² for α > 0, giving (AᵀA + αI)x_α = Aᵀb. In a singular direction it multiplies the unregularized coefficient by σ²/(σ² + α). With α = 0.01, the common-direction multiplier is 3.9601/3.9701 = 0.9975 and the difference multiplier is 0.0001/0.0101 = 0.009901. For noiseless b, the common component of x is 2.5 and the signed difference component is −0.5, so the estimate is approximately (2.4888, 2.4987). Ridge almost removes the difference, because a penalty on parameter size has supplied a preference that the sensors cannot supply reliably.

Regularization trades sensitivity for bias. Its estimate is not an additional measurement. The value of α has meaning only relative to the units and scales used in the objective; changing a displacement from micrometers to meters changes a naive penalty. If parameters have different physical scales, define a scaled penalty or a justified prior. Choose tuning on training data with validation or with an explicit noise model, and report the choice. Do not tune α on the final held-out observations and then call them an independent test.

## Worked example

Replace A with G = [[1, 0.2], [0.2, 1]]. Its singular values are 1.2 and 0.8, so κ₂(G) = 1.5. Apply the same δb = (0.01, −0.01). Since this is the difference direction, δx = δb/0.8 = (0.0125, −0.0125), with norm 0.01768. The geometry improves this directional sensitivity by a factor of 80 compared with A. The maximum absolute amplification is now 1/0.8 = 1.25. This improvement assumes the same calibrated signal units and the same error budget; changing both geometry and sensor noise would require recomputing the comparison.

## Common mistakes

- Confusing full rank with reliable parameter estimation.
- Treating the condition number as the actual error instead of a worst-case multiplier.
- Inferring accurate parameters from an exact fit to two signals.
- Calling a stable solver a cure for collinear measurement columns.
- Describing a ridge estimate as unbiased or independent of coordinate scales.

## Limits of this lesson

The bounds use fixed, exactly known matrices and Euclidean norms. They are deterministic error bounds, not confidence intervals. Real sensor calibration and noise covariance require independent evidence. The synthetic geometry comparison gives no specifications for a real tissue experiment or device.
