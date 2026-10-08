# Least squares as linear algebra: fitting a calibration line, normal equations and reading residuals

Almost every quantitative assay depends on a calibration curve: known standards are measured, a line is fitted, and unknown samples are read off it. The fit is a least-squares problem, and least squares is linear algebra: an overdetermined system Ax ≈ b with more equations than unknowns. This lesson sets up a calibration fit as a matrix problem, solves the normal equations by hand, interprets the residuals geometrically, and uses the fitted line to read an unknown, with the cautions that apply.

## Learning objectives

By the end of this lesson, you should be able to:

1. Write a straight-line fit as an overdetermined system Ax ≈ b and form and solve the normal equations AᵀAx = Aᵀb.
2. Compute residuals and R², and explain why the residual vector is orthogonal to the columns of A.
3. Use a fitted calibration to estimate an unknown and evaluate when the fit or its use is unreliable.

## The overdetermined system

**Synthetic calibration data:** standards at concentrations x = [0.0, 1.0, 2.0, 3.0, 4.0] (μM) give signals y = [0.1, 2.1, 3.9, 6.2, 7.9] (arbitrary units). We want y ≈ β₀ + β₁x. Each standard gives one equation, so

A = [[1, x₁], [1, x₂], …, [1, x₅]], x = [β₀, β₁]ᵀ, b = [y₁, …, y₅]ᵀ.

Five equations, two unknowns: no exact solution exists when the points are not perfectly collinear. Least squares chooses x to minimize ‖b − Ax‖², the sum of squared residuals.

## The normal equations

The minimizer satisfies **AᵀA x = Aᵀb**. For a straight line,

AᵀA = [[n, Σx], [Σx, Σx²]] = [[5, 10], [10, 30]], Aᵀb = [Σy, Σxy] = [20.2, 60.1].

The determinant of AᵀA is n Σx² − (Σx)² = 50. Solving the 2×2 system by Cramer's rule:

β₁ = (n Σxy − Σx Σy) / det = (5 × 60.1 − 10 × 20.2) / 50 = 1.970,

β₀ = (Σy Σx² − Σx Σxy) / det = (20.2 × 30 − 10 × 60.1) / 50 = 0.100.

The fitted line is y = 0.100 + 1.970x. AᵀA is invertible exactly when the columns of A are independent, which for a line means the standards are not all at the same x. A design with standards bunched together makes AᵀA nearly singular and the slope poorly determined.

## Residuals and their geometry

The residuals r = b − Ax̂ are 0.000, 0.030, -0.140, 0.190, -0.080. Two properties follow from the normal equations. Rearranged, they say **Aᵀr = 0**: the residual vector is orthogonal to every column of A. With a column of ones, that means the residuals sum to zero; with the x column, it means they are uncorrelated with x. Geometrically, Ax̂ is the orthogonal projection of b onto the column space of A, and r is the part of b that the model cannot represent.

The sum of squared residuals is 0.0630. Relative to the total variation about the mean, Σ(y − ȳ)² = 38.872, this gives **R² = 1 − SSR/SST = 0.9984**. A high R² does not show the model is right: a curve sampled over a short range can give a high R² with a straight line, while the residuals show a systematic pattern (positive at the ends and negative in the middle, say). Plotting residuals against x is the check; random scatter around zero supports the model, and structure suggests curvature, saturation or an outlier.

## Using the calibration

An unknown sample gives signal 5.0. Inverting the line, x = (y − β₀)/β₁ = (5.0 − 0.100) / 1.970 = 2.487 μM. This is reliable only inside the range of the standards; outside it, the line is an extrapolation, and assays often saturate at high concentration. The uncertainty in the read-back value grows with distance from the mean of the standards and is larger than the residual scatter suggests, because β₀ and β₁ are themselves uncertain.

## Common mistakes

- Forcing the line through the origin without checking whether the blank gives zero signal.
- Reading unknowns outside the calibrated range.
- Judging fit quality by R² alone without looking at residuals.
- Fitting a polynomial with as many coefficients as there are points: it passes through every standard, has zero residual and predicts nothing between them reliably.
- Placing all standards close together, which leaves the slope poorly determined.

## Worked example

**Problem.** Suppose the top standard had read 6.5 instead of 7.9 (signal saturating). Without refitting, what would its residual be against the original line, and what should be done?

**Step 1.** Predicted value at x = 4: 0.100 + 1.970 × 4 = 7.980.

**Step 2.** Residual = 6.5 − 7.980 = -1.480, far larger than the others.

**Step 3.** A single large, negative residual at the top of the range is the signature of saturation. The remedy is to restrict the calibration to the linear range or use a nonlinear model, and to report the range used, not to delete the point silently.

## Limits of this lesson

All data are synthetic. Ordinary least squares assumes errors only in y with constant variance; weighted least squares and errors-in-variables methods address other cases.
