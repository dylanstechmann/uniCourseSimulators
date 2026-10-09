# Virtual lab 1: sensor geometry, noise and displacement estimates

**Status:** open, ungraded formative practice. Public keys and unlimited retries are for learning, not a protected exam. This virtual lab uses ten constructed signal pairs, not measurements from a real device. Prerequisites are the lessons on conditioning and the SVD; the displacement case follows in week 14.

## Learning objectives

1. Solve repeated signal pairs and calculate mean estimates and parameter RMSE.
2. Compare geometry sensitivity while keeping the noise assumptions explicit.
3. Explain why small residuals and balanced means do not establish real accuracy.

## Model and dataset

The reference displacement is x = (2, 3), in common arbitrary displacement units. Each signal pair follows b = Ax + ε. Poor geometry uses A = [[1, 0.99], [0.99, 1]]; improved geometry uses G = [[1, 0.2], [0.2, 1]]. Their weak-direction gains are 0.01 and 0.8. Both matrices are full rank. Signals use the same arbitrary calibrated scale for the comparison.

[Download the synthetic CSV](https://raw.githubusercontent.com/dylanstechmann/uniStemCourseSimulators/main/content/courses/linear-algebra/labs/sensor-pairs.csv). The complete data also appear below. Columns a11 through a22 give each row's matrix entries; b1 and b2 are its supplied signals; reference_x1 and reference_x2 are the known teaching reference. Replicate identifies a constructed pair, not an independent experimental replicate. The deliberate error sequence is d = −0.02, −0.01, 0, 0.01, 0.02 with ε = (d, −d). These perfectly opposed errors target the vulnerable difference direction. They are not independent equal-variance sensor errors.

| Geometry | Replicate | b1 | b2 |
|---|---:|---:|---:|
| poor | 1 | 4.95 | 5.0 |
| poor | 2 | 4.96 | 4.99 |
| poor | 3 | 4.97 | 4.98 |
| poor | 4 | 4.98 | 4.97 |
| poor | 5 | 4.99 | 4.96 |
| improved | 1 | 2.58 | 3.42 |
| improved | 2 | 2.59 | 3.41 |
| improved | 3 | 2.6 | 3.4 |
| improved | 4 | 2.61 | 3.39 |
| improved | 5 | 2.62 | 3.38 |

## Work sequence

Open Practice gradebook and select **Virtual lab 1: sensor geometry, noise and displacement estimates (ungraded practice)**. Points are feedback, not a course grade. First solve each row separately. For [[1, c], [c, 1]], the solution is x̂₁ = (b₁ − cb₂)/(1 − c²), x̂₂ = (b₂ − cb₁)/(1 − c²). Avoid rounding intermediate values; round the final summary to four decimal places. Check that substituting your estimate reproduces each signal pair.

Second, average the five estimated x₁ values and the five estimated x₂ values for each geometry. Upload a CSV with header `geometry,mean_x1,mean_x2` and two rows identified as `poor` and `improved`. The automatic check compares four mean cells with tolerance 0.005. It checks numeric summaries only; your discussion of uncertainty is a separate learning activity.

Third, compute the parameter RMSE for each geometry: √[Σ((x̂₁ − 2)² + (x̂₂ − 3)²)/5]. This is an error against a supplied known reference, not a signal residual and not the standard deviation of one coordinate. Compare the ratio of the two RMSE values. Explain why averaging signed errors before taking a magnitude would miss the spread.

Fourth, consider a separate noise model with covariance 0.01²I for one signal pair. Predict the weak-direction standard deviation as 0.01/σ_min. Do not estimate this independent-noise quantity from the opposed errors in the CSV. Finally, explain which aspects of the example would have to be established independently in a real calibration: linearity, matrix entries, displacement units, noise covariance, fixed offsets and stability across repeated measurements.

## Worked calculation

For poor geometry and d = 0.01, b = (4.98, 4.97). Subtracting signals gives 0.01(x̂₁ − x̂₂) = 0.01; adding gives 1.99(x̂₁ + x̂₂) = 9.95. Therefore x̂ = (3, 2). Its parameter error is (1, −1), with squared norm 2, while its signal residual is zero. Across the five poor-geometry rows, errors are (−2, 2), (−1, 1), (0, 0), (1, −1), (2, −2); squared norms 8, 2, 0, 2, 8 average to 4. The parameter RMSE is 2.

The same errors applied to improved geometry divide by 0.8 instead of 0.01. Parameter errors shrink by a factor of 80, giving RMSE 0.025. Both mean estimates equal (2, 3) because the imposed d values sum to zero. The equal means conceal the difference in uncertainty. Under the separate independent-noise model, the weak-direction SD is 1 for poor geometry and 0.0125 for improved geometry. The CSV RMSE and this model SD are different quantities from different error assumptions.

## Discussion rubric

| Criterion | Evidence to discuss |
|---|---|
| Solves | Reconstructs each signal pair and summarizes estimates by geometry |
| Error | Distinguishes signal residual, mean signed error and parameter RMSE |
| Noise | Names the paired-error construction and the separate independent-noise assumption |
| Bias | Explains why fixed calibration offsets do not average away |
| Validation | Proposes new reference displacements that exercise opposite differences |

These criteria guide written discussion; they are not an automatically scored written report or an instructor-reviewed project. Structured-choice checks cover only selected conclusions. A final validation design should reserve new measurements for evaluation, after selecting the estimator and tuning any penalty.

## Limits and provenance

The rows are exactly constructed around fixed matrices and a known reference. Their imposed balance and noise direction simplify the exercise and cannot establish a real uncertainty distribution. Real geometry changes can also change signal noise. No tissue experiment, device specification or experimental protocol is provided. Original lab and synthetic CSV: CC BY 4.0, developed with substantial AI assistance. Existing linear-algebra references provide scope only; no source text or dataset was copied.
