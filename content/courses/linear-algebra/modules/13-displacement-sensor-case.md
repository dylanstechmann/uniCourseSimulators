# Two displacement sensors: a small residual and an unreliable answer

The course case asks why nearly collinear sensor columns can yield a tiny residual and unreliable displacement estimates. This capstone turns that question into a reproducible analysis. It combines exact solutions, singular directions, statistical uncertainty and experimental redesign. The goal is to report what the data support, what is supplied by assumptions and what an additional measurement should distinguish. All displacements, signal units, calibrations and repeated observations here are synthetic. They describe a mathematical exercise, not a validated tissue measurement system.

## Learning objectives

1. Diagnose a sensor model using singular directions, perturbations and residuals.
2. Propagate a stated noise covariance and distinguish random error from calibration bias.
3. Compare a redesigned geometry and regularization, then specify independent validation.

## State the measurement model

Let x = (x₁, x₂) be two displacement components in a common arbitrary teaching unit and let the two signals obey b = Ax + ε. The poor geometry is A = [[1, 0.99], [0.99, 1]]. Both columns are almost parallel. A reference displacement x = (2, 3) produces ideal signals (4.97, 4.98). Although det A = 0.0199 is nonzero, the condition number is 199. The determinant has no universal threshold for reliability because its scale changes with units; singular values and a stated noise model make a more interpretable diagnostic.

The common direction q₊ = (1, 1)/√2 has gain 1.99, while q₋ = (1, −1)/√2 has gain 0.01. Separate what can be measured well: the sum of the components is relatively robust, but their difference is fragile. A single numerical condition number summarizes the worst direction; the singular vectors identify which reported combination carries that vulnerability.

## An exact fit can be wrong

For measured b = (4.98, 4.97), solve using x₁ + 0.99x₂ = 4.98 and 0.99x₁ + x₂ = 4.97. Subtracting the equations gives 0.01(x₁ − x₂) = 0.01, hence x₁ − x₂ = 1. Adding gives 1.99(x₁ + x₂) = 9.95, hence x₁ + x₂ = 5. The solution is (3, 2), with residual norm zero. Compared with the reference (2, 3), its error norm is √2 = 1.4142. A signal error (0.01, −0.01) has reversed the sign of the component difference. A residual plot alone cannot expose this error because two independent equations exactly fit two unknowns.

More observations can help if they provide independent information about the weak direction. Repeating the same two sensors reduces random error under an independence assumption but does not change the geometry. Adding a sensor with a different sensitivity can increase the weak singular value. Adding a duplicate sensor with perfectly correlated noise supplies much less information than an independent sensor; the full error covariance matters.

## From noise to parameter uncertainty

Assume ε has zero mean and covariance s²I with s = 0.01 signal units. This is a stated model, not an inference from the five demonstration repeats in the lab. The unregularized estimator has covariance s² A⁻¹A⁻ᵀ. In singular coordinates the variance is s²/σ_i²: the common-direction standard deviation is 0.01/1.99 = 0.005025 and the difference-direction standard deviation is 0.01/0.01 = 1. Each coordinate mixes those directions equally, so Var(x₁) = Var(x₂) = (s²/2)(1/1.99² + 1/0.01²) = 0.500013. Each coordinate standard deviation is approximately 0.707116. Their covariance is negative, because a perturbation that raises one displacement tends to lower the other while preserving their sum.

If 25 independent signal pairs measure the same fixed displacement and their average is inverted, the covariance divides by 25 and the weak-direction standard deviation falls to 0.2. This reduction assumes independent errors, unchanged calibration and a constant displacement. Shared drift or a fixed offset does not average away. Twenty-five repeated readouts from one drifting calibration are not equivalent to 25 independent calibrations. A standard deviation is also not automatically a confidence interval; interval coverage needs distributional assumptions or an appropriate resampling design.

## Calibration bias is a different problem

Suppose the second sensor has a fixed positive offset of 0.01 while the first has none. Averaging any number of repeats retains this offset. Solve A δx = (0, 0.01): δx₁ = −0.99 × 0.01/0.0199 = −0.497487 and δx₂ = 0.01/0.0199 = 0.502513. The estimate is biased even though its repeat-to-repeat spread can become tiny. Include zero controls, known displacements that exercise both directions and independent calibration checks. A small repeat spread establishes precision under that repeat design, not accuracy relative to a reference.

## Redesign versus a penalty

For a better synthetic geometry G = [[1, 0.2], [0.2, 1]], singular gains are 1.2 and 0.8 and κ₂ = 1.5. With the same s = 0.01 and independent errors, each coordinate variance is (s²/2)(1/1.2² + 1/0.8²) = 1.12847 × 10⁻⁴, giving standard deviation 0.010623. The weak-direction standard deviation is 0.0125, an 80-fold improvement over A. These comparisons require comparable calibrated signals and noise; a geometry that improves gains while greatly worsening noise may not improve uncertainty.

Ridge is an alternative estimator when redesign is unavailable, but it does not provide a new observation. With α = 0.01 it nearly removes the weak difference direction. That can reduce variance while biasing estimates toward equal components. Report the penalty, its units and the validation used to choose it. If the scientifically important signal is precisely the displacement difference, suppressing that direction can conceal the quantity of interest. A favorable condition number after regularization does not prove the experiment identified it.

## Worked example

Plan validation with reference displacements (2, 3) and (3, 2). They have the same sum and opposite differences. Poor geometry produces signals (4.97, 4.98) and (4.98, 4.97), whose Euclidean separation is 0.014142. Better geometry gives (2.6, 3.4) and (3.4, 2.6), separated by 1.131371. Test both directions with new measurements after fixing the calibration and estimator. Reserve these reference observations for evaluation rather than tuning α on them. Report directional bias and repeat variability, not only the average residual across signals.

## Common mistakes

- Claiming zero residual establishes accurate displacement.
- Reporting repeat precision as accuracy despite shared calibration bias.
- Counting correlated repeats as independent observations.
- Using ridge without disclosing the preference it adds.
- Evaluating only a common-mode displacement when the weak direction is the difference.

## Limits of this lesson

All uncertainty numbers assume linear response, exactly known matrices and the specified independent equal-variance noise. No real sensor, tissue model, protocol or calibration accuracy is established. The case checklist remains self-assessment; no written project is graded and no instructor review is claimed.
