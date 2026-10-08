# Effect sizes, confidence intervals and regression to the mean: reading a result for what it can support

A p-value answers a narrow question: how surprising would data like these be if there were no effect? It does not say how large the effect is, how precisely it is estimated, or whether an apparent change after an intervention is real. This lesson builds the tools that answer those questions with synthetic data: the difference in means with its confidence interval, a standardized effect size, the dependence of precision on sample size, and regression to the mean, the statistical artifact that makes extreme measurements look like they improved.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute a difference in means, its standard error and a 95% confidence interval, and interpret the interval.
2. Calculate a standardized effect size and explain how sample size changes precision but not the effect.
3. Predict the expected remeasurement of an extreme value under regression to the mean and evaluate study designs that guard against it.

## Difference in means and its confidence interval

**Synthetic two-group study:** treated mean 12.0, control mean 10.5, standard deviation 3.0 in each group, n = 20 per group. The difference is 1.5. Its standard error, for equal SDs and sizes, is SE = s √(2/n) = 3.0 × √(2/20) = 0.949. With the t critical value for 38 degrees of freedom (about 2.024), the 95% confidence interval is

1.5 ± 2.024 × 0.949 = (-0.42, 3.42).

The interval includes zero, so a two-sided test at 0.05 would not reject "no difference". But the interval also includes differences as large as 3.4. The data are compatible both with no effect and with a substantial one: the honest summary is "imprecise", not "no effect". A confidence interval describes the range of effect sizes reasonably compatible with the data under the model; a 95% interval procedure captures the true value in 95% of repeated studies, which is a statement about the procedure, not a probability for this one interval.

## Standardized effect size

Cohen's d expresses the difference in standard-deviation units: d = 1.5/3.0 = 0.50. Standardized effects help compare outcomes measured on different scales, but they depend on the variability of the sample: the same raw difference looks larger in a homogeneous group. Report the raw difference with its units alongside d.

## Sample size changes precision, not the effect

With four times as many per group (80), SE = 3.0 × √(2/80) = 0.474, half as large. If the observed difference stayed 1.5, the interval would be roughly 1.5 ± 0.95, excluding zero. The effect did not change; only the precision did. Conversely, a very large study can make a trivially small effect "statistically significant". Effect size and interval together tell whether a result matters; the p-value alone cannot.

## Regression to the mean

When a quantity is measured with error, or fluctuates, individuals selected for an extreme first measurement will on average be less extreme when remeasured, even with no intervention. If a population has mean μ and the test–retest correlation is r, the expected second value for someone whose first value was x is

**E[x₂ | x₁] = μ + r (x₁ − μ).**

With μ = 100, r = 0.7, and a first reading of 130, the expected second reading is 100 + 0.7 × 30 = 121. A study that enrolls people because a marker is high, treats them and remeasures will see an average "improvement" of about 9 units from regression alone. This affects studies of blood pressure, inflammatory markers, biological-age scores and any noisy biomarker.

**Defenses:** a randomized control group selected the same way (it regresses equally, so the difference between groups isolates the effect), multiple baseline measurements averaged before selection, and selecting on one measurement while analyzing a separate one.

## Common mistakes

- Reading "p > 0.05" as "no effect" when the interval is wide.
- Reporting only d, which hides the units and the clinical or biological scale.
- Attributing within-group change after selection on an extreme value to the intervention.
- Interpreting a 95% interval as a 95% probability that the true value is inside this particular interval.

## Worked example

**Problem.** People whose synthetic biological-age score was at least 10 years above their chronological age are given a supplement and retested; the average excess falls from 12 to 8 years. The test–retest correlation of the score is 0.6 and the population mean excess is 0. What change is expected without any effect?

**Step 1.** Expected retest = 0 + 0.6 × 12 = 7.2 years.

**Step 2.** The observed 8 years is close to 7.2, so the apparent improvement of 4 years is roughly what regression to the mean predicts.

**Step 3.** Only a randomized comparison group selected the same way could show whether the supplement did anything; the uncontrolled before–after change cannot.

## Limits of this lesson

All data are synthetic. The formulas assume roughly normal data and, for regression to the mean, a stable population mean and a linear relationship between measurements.
