# Resampling and rank-based methods: permutation tests, the bootstrap and the Mann–Whitney test

The usual t-test and confidence interval rest on a mathematical model of how an estimate varies: a normal distribution, or a large enough sample for averages to behave as if it were. When samples are small, data are skewed or the statistic is unusual, that model may be a poor description. Resampling methods replace the formula with a computation. A **permutation test** asks how often a difference as large as the observed one arises when group labels are shuffled; the **bootstrap** asks how much an estimate varies when the sample is resampled. Rank-based tests, such as the Mann–Whitney test, use the order of values rather than the values themselves. These methods require fewer assumptions about the distribution but not about the design: independence and randomization still matter. This lesson works through each by hand with a very small synthetic experiment, so that every step can be counted.

## Learning objectives

By the end of this lesson, you should be able to:

1. Carry out an exact permutation test for a difference in means and compute its p-value by counting arrangements.
2. Explain the logic of the bootstrap and compute simple properties of bootstrap resamples.
3. Compute rank sums and a Mann–Whitney statistic, and choose among t-test, permutation and rank-based analyses for a given design.

## An exact permutation test

**Synthetic experiment:** four independent animals per group. Control: 12, 15, 14, 16. Treated: 18, 20, 17, 21. The observed difference in means is 19.00 − 14.25 = **4.75**.

If the treatment had no effect, each of the eight values was equally likely to have landed in either group, and the assignment of four to each group was one of C(8, 4) = **70** equally likely arrangements. For each arrangement the difference in means can be computed. The p-value is the fraction of arrangements giving a difference at least as large in size as the observed one. Here the observed arrangement places the four smallest values in the control group, which is the most extreme possible split in one direction; the mirror image is the most extreme in the other. Only 2 of 70 arrangements are this extreme, so the two-sided p-value is 2/70 = **0.0286**. The result depends only on the assignment mechanism, so it is valid for any distribution of the data provided the groups were formed by random assignment. The smallest p-value attainable with four per group is 2/70 = 0.029, which shows why very small experiments cannot reach very small p-values.

For larger samples the number of arrangements is enormous, so the test uses a random sample of arrangements (for example 10,000), and the p-value is a proportion with its own small sampling error.

## The bootstrap

To see how much a statistic would vary from sample to sample, a bootstrap treats the sample as a stand-in for the population and draws many resamples of the same size *with replacement* from it. Computing the statistic on each resample gives a distribution that approximates its sampling variability, whose spread is an estimated standard error and whose percentiles give an interval.

Some properties can be counted. A resample of size n has n^n equally likely ordered outcomes: for n = 4 there are 256. A given observation is missed by one draw with probability 1 − 1/n, so it appears in a resample of size n with probability 1 − (1 − 1/n)ⁿ: 0.684 for n = 4, 0.651 for n = 10, approaching 1 − e⁻¹ = 0.632 for large n. About a third of the sample is therefore absent from any one resample.

The bootstrap needs the sample to represent the population, which fails for very small n, for statistics that depend on extremes (such as a maximum), and for dependent data, where resampling single values breaks the structure. As with every other method, the units that are resampled must be the independent units.

## Rank-based tests

The Mann–Whitney (Wilcoxon rank-sum) test replaces values by their ranks in the combined sample. The eight values are ranked 1 to 8: the control group has ranks 1 to 4, a rank sum of 10, and the treated group ranks 5 to 8, a rank sum of 26. The U statistic counts pairs in which a control value exceeds a treated value: U = 0 here, the smallest possible. Its exact p-value is again 2/70 = 0.0286, because with no ties the rank test is a permutation test on the ranks. Ranks make the test insensitive to outliers and to the scale of the data, at the cost of ignoring the size of the difference; the estimated effect should still be reported (for example, the difference in medians with a bootstrap interval).

## Choosing a method

- **Roughly symmetric data with moderate n:** a t-test or a t-interval is adequate.
- **Small n, skewed data or heavy tails:** a permutation or rank test is safer for testing; a bootstrap or a transformation (such as logarithms) can help for intervals.
- **Complicated statistics** (a ratio, a median, a maximum difference): the bootstrap is often the only practical way to get a standard error.
- **Dependent or nested data:** none of these methods works until the unit of resampling or permutation matches the independent unit.

## Common mistakes

- Permuting readings instead of the independent units, which destroys the clustering.
- Reading an exact p-value as free of assumptions, when it still assumes random assignment or exchangeability.
- Believing that a rank test cannot be affected by small sample size.
- Resampling without replacement and calling it a bootstrap.
- Expecting a bootstrap interval to fix a biased or non-representative sample.
- Reporting only a p-value from a rank test, without an effect estimate.

## Worked example

**Problem.** A second synthetic experiment has control 11, 14, 13, 18 and treated 15, 17, 16, 19, four independent animals each. Find the observed difference, the exact permutation p-value and the rank sum of the treated group.

**Step 1: difference.** 16.75 − 14.00 = 2.75.

**Step 2: permutations.** There are 70 arrangements; 14 give a difference of at least 2.75 in size in either direction, so p = 14/70 = 0.20.

**Step 3: ranks.** The ranks of the treated values are 4, 5, 6, 8, a rank sum of 23 (the control rank sum is 13).

**Step 4: reading the result.** The difference is not unusual under random assignment (p = 0.20); with four per group, only a very clean separation could have given a small p-value.

## Limits of this lesson

All values are synthetic and the samples are deliberately tiny so that every arrangement can be counted. Exact counting is feasible only for small samples; real analyses sample random permutations or use software. Permutation and rank tests answer questions about differences in distribution, not necessarily about means, and the bootstrap has several variants with different properties.
