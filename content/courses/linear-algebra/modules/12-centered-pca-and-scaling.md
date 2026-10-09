# Centered PCA, scaling and interpretation

Principal component analysis describes directions of variation in a data matrix. Its algebra comes from symmetric covariance matrices and the SVD, but its meaning depends on what was centered, what units were used and which samples were included. A beautifully separated scatterplot can reveal a batch difference as readily as a biological mechanism. This lesson computes a complete two-variable PCA, connects covariance eigenvalues to singular values and shows why standardization changes the question. All observations are synthetic. No component is evidence about a real population.

## Learning objectives

1. Center observations, form a sample covariance matrix and compute principal axes.
2. Calculate scores, explained variance and a rank-one reconstruction error.
3. Evaluate scaling, confounding and leakage in a PCA workflow.

## Center before interpreting variation

Rows are samples and columns are variables. Consider four observations (8, 19), (12, 21), (10, 19), (10, 21). The column means are (10, 20). Subtract those means to obtain Z = [[−2, −1], [2, 1], [0, −1], [0, 1]]. Each centered column sums to zero. With n = 4 observations, the sample covariance is C = ZᵀZ/(n − 1), giving [[8/3, 4/3], [4/3, 4/3]]. We use n − 1 here because these four rows are treated as a sample; a population covariance convention would use n and produce smaller eigenvalues but the same axes and explained-variance fractions.

An SVD of the original uncentered matrix answers a different question. It minimizes error relative to the origin, and the large mean vector contributes strongly to its leading direction. PCA of centered observations describes variation around the mean. An uncentered decomposition is legitimate for some applications, but it must be named and interpreted accordingly. Centering is a modeling choice, not an optional formatting operation.

## Covariance axes and scores

The trace of C is 4 and its determinant is 16/9. The characteristic equation is λ² − 4λ + 16/9 = 0, so the eigenvalues are λ₁ = 3.490712 and λ₂ = 0.509288. They are nonnegative, as a covariance matrix must be. Using θ = ½ atan2(2c₁₂, c₁₁ − c₂₂) gives θ = 31.7175°. Choose q₁ = (cos θ, sin θ) and q₂ = (−sin θ, cos θ). The choice of sign is arbitrary; changing q₁ to −q₁ changes all its scores' signs while preserving distances and reconstructions.

A centered row z has score t₁ = z·q₁. For the second observation, z = (2, 1), so t₁ = 2.227033. Its rank-one centered reconstruction is t₁q₁, approximately (1.8944, 1.1708). Add (10, 20) to return to the original coordinate system. Omitting that last step would reconstruct a deviation, not an observation. The residual is perpendicular to q₁ and lies along the discarded axis q₂.

The first component explains λ₁/(λ₁ + λ₂) = 0.872678 of the sample variance. This is a fraction of variance in these variables and scales, not a fraction of causal explanation or predictive accuracy. Let Z = UΣVᵀ. Its right singular vectors are the PCA axes and σ_i² = (n − 1)λ_i, so σ₁ = 3.236068. Keeping one component gives total squared reconstruction error (n − 1)λ₂ = 1.527864; the Frobenius error is 1.236068. These are sums across all four observations. Dividing the squared error by n would give a mean squared Euclidean error per observation, a different quantity.

## Scaling changes the geometry

The sample standard deviations are √(8/3) and √(4/3). Divide each centered column by its own standard deviation to obtain standardized data. Their covariance is the correlation matrix [[1, 1/√2], [1/√2, 1]], with eigenvalues 1 + 1/√2 and 1 − 1/√2. The leading standardized axis is (1, 1)/√2, at 45°, and its explained fraction is (1 + 1/√2)/2 = 0.853553. This differs from the unstandardized result because the two variables now have equal variance by construction.

Changing only the second variable's unit by multiplying it by 100 would inflate its variance by 10,000 and its covariance with the first variable by 100. An unstandardized PCA could then point almost along that variable. Standardization removes the unit conversion when the sample standard deviations scale with it. However, standardization also gives a low-variance variable equal standing, even if most of its variation is measurement noise. The appropriate choice depends on the scientific question and measurement reliability. Neither centered covariance PCA nor correlation PCA is universally correct.

## Confounding and independent evaluation

Suppose all samples processed in one batch have an additive offset in both variables, and all samples from one treatment were processed in that batch. PCA may separate treatments because it detects the batch offset. It cannot distinguish the two explanations from that design. Annotate scores with batches, acquisition times, groups and relevant covariates, then design balanced or independent measurements. Removing a component because it correlates with batch can also remove true signal when batch and treatment are confounded. Algebra cannot identify information the design did not separate.

For predictive work, split data before estimating means, scales or PCA axes. Fit all those quantities on training samples only, and transform validation or test samples with the fitted quantities. Recomputing the axes using held-out samples lets information from evaluation data affect the representation. Choosing the component count on the test set similarly compromises the test. Variance preservation is not a substitute for evaluating prediction on independent samples.

## Worked example

Use two centered columns with covariance [[9, 0], [0, 1]]. Unstandardized PCA selects the first coordinate and explains 9/10 = 0.9 of variance. Standardization produces the identity matrix: both eigenvalues are 1, each explains 0.5, and there is no unique leading axis. Any orthonormal pair is valid. Reporting a stable 45° biological axis in this repeated-eigenvalue case would overinterpret an arbitrary software choice. When eigenvalues are close but unequal, the leading direction can also move substantially under small sample changes; examine stability rather than trusting one loading vector.

## Common mistakes

- Using uncentered singular vectors while describing covariance variation around a mean.
- Mixing n and n − 1 between the covariance and singular-value calculation.
- Comparing loadings from different units without stating scaling.
- Treating variance explained as mechanism explained.
- Fitting preprocessing on held-out data or interpreting confounded groups causally.

## Limits of this lesson

PCA describes linear variation and uses squared Euclidean distances. Outliers, missing values, nonlinear structure, sample dependence and uncertain measurements require further decisions. The four synthetic rows do not establish population axes or robust uncertainty intervals. The lesson gives no real biomarker, treatment or mechanism claim.
