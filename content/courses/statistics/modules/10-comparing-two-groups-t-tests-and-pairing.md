# Comparing two groups: the t statistic, Welch's test, paired designs and confidence intervals for a difference

Most experiments in biology and engineering end in a comparison of two conditions, and the most common analysis is a t-test. The test is simple enough to do by hand, and doing it by hand makes its logic and its limits visible: what the standard error is made of, what the degrees of freedom do, why a p-value just above 0.05 and an interval that just includes zero are the same statement, and how pairing measurements on the same unit removes a source of noise. This lesson works through one synthetic experiment in an independent-groups analysis and a paired analysis. It assumes that the units are independent, which the previous lesson on variability showed is a matter of design and not of arithmetic.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute the standard error, t statistic and Welch degrees of freedom for a difference between two independent group means.
2. Construct and interpret a confidence interval for the difference and a standardized effect size.
3. Choose between independent-groups and paired analyses, and compute a paired t statistic.

## The setup

**Synthetic experiment:** 6 independent cultures per group. Control: mean 10.2, standard deviation 2.0. Treated: mean 13.0, standard deviation 2.4 (arbitrary units). The estimand is the difference in means, treated minus control, here **2.8**. Because the sample means are uncertain, the difference is too, and the t statistic measures it in units of its standard error.

## The Welch statistic

The standard error of the difference between two independent means is

**SE = √(s₁²/n₁ + s₂²/n₂) = √(2.0²/6 + 2.4²/6) = 1.275,**

and the test statistic is **t = difference / SE = 2.8/1.275 = 2.195.**

Welch's version does not assume equal variances and approximates the degrees of freedom by

**df = (s₁²/n₁ + s₂²/n₂)² / [ (s₁²/n₁)²/(n₁ − 1) + (s₂²/n₂)²/(n₂ − 1) ] = 9.69,**

slightly below the 2n − 2 = 10 of the pooled test; with equal sample sizes and similar variances the two tests nearly coincide. The two-sided p-value for t = 2.195 with 9.7 degrees of freedom is about 0.054, and the 95% critical value is 2.238. Because 2.195 < 2.238, the difference is not significant at the 5% level, though only just.

## The confidence interval says more than the verdict

A 95% interval for the difference is difference ± t_crit × SE = 2.8 ± 2.238 × 1.275, which is **(−0.05, 5.65)**. The interval and the test agree: it barely includes zero, as the p-value barely exceeds 0.05. But the interval also shows the range of differences compatible with the data, from essentially none to more than five units. This is an inconclusive result, not evidence of no effect, and not evidence of a large one. The standardized effect size, Cohen's d = difference divided by the pooled standard deviation = 2.8/2.21 = **1.27**, is large by conventional benchmarks, which again shows that an estimate can be big and still uncertain when n is small.

## When pairing helps

Suppose the same 6 cultures had been measured before and after treatment, and the 6 within-culture differences had mean 2.8 and standard deviation 1.5. The paired analysis works on the differences:

**SE = s_d/√n = 1.5/√6 = 0.612,** **t = 2.8/0.612 = 4.57** with n − 1 = 5 degrees of freedom (critical value 2.571), p ≈ 0.006.

The same mean difference, but the standard error is half as large, because each culture serves as its own control and the variation between cultures drops out. How much pairing helps depends on the correlation ρ between the paired measurements: the variance of a difference is s₁² + s₂² − 2ρ s₁ s₂. Here a standard deviation of 1.5 for the differences implies ρ = (2.0² + 2.4² − 1.5²)/(2 × 2.0 × 2.4) = 0.78. If ρ were near zero, pairing would help little and would cost degrees of freedom. Pairing is a feature of the design, so the decision to pair must be made when the experiment is planned and not after seeing which analysis is significant.

## Assumptions

- **Independence of the units.** Technical replicates or repeated readings of one culture are not independent units.
- **Approximately normal sampling distribution of the means.** The central limit theorem makes this reasonable for moderate n, but for very small n and skewed data a transformation (for example, logarithms) or a resampling method is safer.
- **Outliers** can dominate a mean; check them before the test and report what you did.
- **The choice of analysis** is part of the design. Trying several tests and reporting the one with the smallest p-value inflates false positives.

## Common mistakes

- Reading p = 0.054 as evidence that there is no effect.
- Using the standard deviation instead of the standard error of the difference.
- Using the pooled test when variances differ and sample sizes are unequal.
- Treating before-and-after measurements on the same units as independent groups.
- Choosing paired or unpaired analysis after seeing the data.
- Reporting a p-value without the estimated difference and its interval.

## Worked example

**Problem.** In a second synthetic experiment, 8 independent animals per group give means 50 and 56 with standard deviations 5 and 7. Compute the Welch t statistic and the 95% interval.

**Step 1: standard error.** √(5²/8 + 7²/8) = √(3.125 + 6.125) = 3.041.

**Step 2: t.** (56 − 50)/3.041 = 1.973.

**Step 3: degrees of freedom and p.** Welch df = 12.67, p ≈ 0.071.

**Step 4: interval.** 6 ± 2.166 × 3.041 = (−0.59, 12.59).

**Step 5: reading the result.** The difference is not significant at 5%, and the interval ranges from a small negative to a large positive difference: more data are needed before concluding anything.

## Limits of this lesson

All values are synthetic and in arbitrary units. The p-values and critical values come from the t distribution, which assumes normally distributed data or large enough samples; a different analysis may be needed for counts, proportions or heavy-tailed data. The lesson explains how the test works and does not replace choosing an analysis in advance.
