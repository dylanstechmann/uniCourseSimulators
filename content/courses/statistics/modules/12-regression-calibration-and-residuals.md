# Regression and calibration: least squares, residuals, R² and prediction

Fitting a line is the most common modelling step in a laboratory. A calibration curve turns an instrument signal into a concentration, a dose–response line summarizes how an outcome changes with an exposure, and a trend over time summarizes drift. The arithmetic of a least-squares line is simple, and doing it by hand shows what each reported number measures: the slope and its uncertainty, the scatter around the line, the share of variation explained, and the extra uncertainty that appears when the line is run backwards to estimate an unknown. It also shows the three ways in which a fit can look excellent and still be wrong. This lesson works through one synthetic calibration, one example in which a high R² hides the wrong model, and the limits of extrapolation and of reading a regression causally.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute the least-squares slope, intercept, residual standard deviation, R² and standard error of the slope from data.
2. Use a calibration line to estimate an unknown and describe how its uncertainty depends on the data.
3. Evaluate a fit using residuals, and state when R², extrapolation or causal readings of a slope are unjustified.

## Least squares

For data (x_i, y_i) with n points, the least-squares line y = a + b x minimizes the sum of squared residuals. With x̄ and ȳ the means, S_xx = Σ(x_i − x̄)² and S_xy = Σ(x_i − x̄)(y_i − ȳ),

**b = S_xy / S_xx,** **a = ȳ − b x̄.**

**Synthetic calibration:** concentrations x = 0, 2, 4, 6, 8, 10 μM and signals y = 6.0, 24.0, 47.5, 62.0, 88.5, 101.0 (arbitrary units). Then x̄ = 5, ȳ = 54.83, S_xx = 70, S_xy = 683, so the slope is b = 683/70 = **9.757** signal units per μM and the intercept is a = 54.83 − 9.757 × 5 = **6.048**.

| x (μM) | y | fitted | residual |
|---:|---:|---:|---:|
| 0 | 6.0 | 6.05 | −0.05 |
| 2 | 24.0 | 25.56 | −1.56 |
| 4 | 47.5 | 45.08 | +2.42 |
| 6 | 62.0 | 64.59 | −2.59 |
| 8 | 88.5 | 84.10 | +4.40 |
| 10 | 101.0 | 103.62 | −2.62 |

## Scatter, R² and the uncertainty of the slope

The **residual standard deviation** is s = √(SSE/(n − 2)), where SSE is the sum of squared residuals; with n − 2 = 4 degrees of freedom it is s = √(41.20/4) = 3.210. The **coefficient of determination** is R² = 1 − SSE/SST, where SST = Σ(y − ȳ)² = 6705.3, so R² = 1 − 41.20/6705.3 = **0.9939**. The standard error of the slope is

**SE(b) = s / √S_xx = 3.210/√70 = 0.384,**

and a 95% confidence interval is b ± t × SE(b) with t = 2.776 for 4 degrees of freedom: (8.69, 10.82). The interval is wide in relative terms only if the scatter is large compared with the spread of the x values. More measurements and a wider range of x both reduce it.

## Running the line backwards

An unknown sample gives a signal of 55. Solving the fitted line for x gives the estimate x̂ = (y − a)/b = (55 − 6.048)/9.757 = **5.017 μM**. Its uncertainty is larger than the uncertainty of the slope alone, because it includes the scatter of the new reading and the uncertainty of the line. An approximate standard error is (s/|b|) √(1 + 1/n + (x̂ − x̄)²/S_xx) = 0.355, giving a 95% interval of about ±0.99 μM. The uncertainty is smallest near x̄ and grows toward and beyond the ends of the calibrated range, which is why unknowns should fall inside the standards.

## When a good fit is a wrong fit

- **A high R² does not show the model is right.** A second synthetic data set with signals 0, 18, 33, 44, 52, 57 (a response that saturates) has R² = 0.956 for a straight line, but its residuals (−5.6, +1.1, +4.7, +4.3, +0.9, −5.4) are negative, then positive, then negative: a curve. A line through curved data gives biased predictions near the ends and in the middle even though R² looks high. Always plot the residuals against x or the fitted values; they should show no pattern and no funnel.
- **Extrapolation is not supported.** The line was fitted for 0 to 10 μM. Predicting the signal at 20 μM gives 201, but nothing in the data shows that the response stays linear there, and detectors saturate.
- **A few points can dominate.** A point far from the others in x has high leverage and can pull the line. Check influence by refitting without it.
- **A slope is an association unless the design supports a causal reading.** A line through observational data does not show that changing x would change y; confounders can create or hide a slope.
- **Variance often changes with the signal.** If residuals grow with the fitted value, weighted fitting or a transformation is appropriate.

## Common mistakes

- Reporting R² without looking at the residuals.
- Extrapolating beyond the calibrated range.
- Treating the uncertainty of an inverse prediction as that of the slope alone.
- Using n instead of n − 2 degrees of freedom for the residual standard deviation.
- Fitting a line through repeated readings of the same sample as if they were independent points.
- Reading a regression slope from observational data as an effect of intervening on x.

## Worked example

**Problem.** A second synthetic calibration has x = 1, 2, 3, 4, 5 and y = 3.1, 4.9, 7.2, 8.8, 11.1. Find the line, R² and SE(b).

**Step 1: sums.** x̄ = 3, ȳ = 7.02, S_xx = 10, S_xy = 19.9.

**Step 2: line.** b = 19.9/10 = 1.99; a = 7.02 − 1.99 × 3 = 1.05.

**Step 3: scatter.** SSE = 0.107; s = √(0.107/3) = 0.189; R² = 1 − 0.107/39.708 = 0.9973.

**Step 4: slope uncertainty.** SE(b) = 0.189/√10 = 0.060.

**Step 5: reading the result.** The fit is excellent for these five points, but with only three residual degrees of freedom the interval for the slope is still sensitive to each point, and residuals should be plotted before relying on the line.

## Limits of this lesson

All values are synthetic. The standard errors assume independent errors with constant variance and a correctly specified straight line. Real calibrations are often weighted, nonlinear or fitted with several replicates per standard, and the inverse-prediction standard error is an approximation.
