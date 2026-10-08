# Mendelian randomization: using genetic variants to test whether an exposure causes an outcome

Observational studies find that many measurable traits, such as blood lipids, inflammatory markers and body weight, are associated with disease and survival. Whether they cause those outcomes is harder to establish, because people with different levels also differ in many other ways. Mendelian randomization (MR) uses genetic variants as natural experiments: alleles are assigned at conception, largely independently of later lifestyle and environment, so a variant that shifts an exposure can act like a randomized treatment assignment. This lesson computes a simple MR estimate with synthetic numbers and lays out the assumptions that decide whether it can be trusted.

## Learning objectives

By the end of this lesson, you should be able to:

1. State the three core instrumental-variable assumptions and explain why genetic variants can satisfy them.
2. Compute a Wald-ratio causal estimate with its approximate standard error and convert a log-odds estimate to an odds ratio.
3. Evaluate an MR result for weak instruments and pleiotropy, and distinguish it from an observational association.

## The logic

An instrument Z (a genetic variant) is used to estimate the effect of an exposure X (for example, a circulating protein level) on an outcome Y (a disease). Three assumptions are needed:

1. **Relevance:** Z is associated with X.
2. **Independence:** Z is not associated with confounders of X and Y. Random assortment of alleles at meiosis supports this, within a population.
3. **Exclusion restriction:** Z affects Y only through X, not by another pathway (no horizontal pleiotropy).

If all three hold, any association between Z and Y must run through X, and its size reveals X's effect.

## The Wald ratio

With summary statistics for one variant, the causal estimate is the ratio of the variant's effect on the outcome to its effect on the exposure:

**β_XY = β_ZY / β_ZX.**

**Synthetic data:** each copy of the effect allele raises the exposure by 0.1 units (SE 0.01) and raises the log-odds of disease by 0.05 (SE 0.01). Then β_XY = 0.05/0.1 = 0.50 log-odds per unit of exposure, an odds ratio of e^0.50 = 1.65 per unit. A first-order standard error is SE(β_ZY)/|β_ZX| = 0.01/0.1 = 0.10, giving a 95% interval for the log-odds of (0.30, 0.70), or odds ratios 1.36 to 2.01. This approximation ignores uncertainty in β_ZX, which is reasonable only when the instrument is strong.

In practice, many independent variants are combined (for example, by inverse-variance weighting), and their individual ratios are compared: if they disagree more than chance allows, some variants likely violate the assumptions.

## Instrument strength

A weak instrument explains little of the exposure. The F-statistic for one variant is roughly (β_ZX/SE)². Here F = (0.1/0.01)² = 100. A common rule of thumb treats F below about 10 as weak, because weak instruments bias estimates (toward the observational association in one-sample designs, toward the null in two-sample designs) and make intervals unreliable. A variant with β_ZX = 0.02 and SE 0.01 has F = 4, weak by that rule.

## Pleiotropy and other threats

- **Horizontal pleiotropy:** the variant affects the outcome through a different trait. Sensitivity analyses (MR-Egger, weighted median, mode-based estimators) estimate the effect under weaker assumptions; agreement across methods adds confidence.
- **Population structure:** if allele frequencies and outcome rates both differ between ancestral groups, independence fails; analyses adjust for ancestry or use within-family designs.
- **Linkage disequilibrium:** the variant may be correlated with a nearby variant affecting another gene.
- **Lifelong exposure:** MR estimates the effect of a lifelong genetic shift in exposure, which can differ from the effect of changing the exposure later in life by a drug or behavior.

MR has been applied widely in aging research, for example to ask whether circulating factors or metabolic traits causally influence age-related disease or lifespan. Its results are strongest when they agree with other kinds of evidence, such as experiments and trials, and when sensitivity analyses do not undermine them.

## Common mistakes

- Treating an MR estimate as free of assumptions because genes are "randomized".
- Ignoring weak-instrument bias.
- Reading a lifelong genetic effect as the effect of a short-term intervention.
- Using variants whose effect on the exposure is uncertain or tissue-specific without checking.

## Worked example

**Problem.** A second synthetic variant raises the exposure by 0.08 units per allele and the log-odds of disease by 0.12. Is it consistent with the first variant's estimate?

**Step 1.** Its Wald ratio is 0.12/0.08 = 1.50 log-odds per unit, three times the first variant's 0.50.

**Step 2.** If both variants act only through the exposure, their ratios should agree within sampling error. A threefold difference with small standard errors suggests that at least one variant affects the outcome by another route.

**Step 3.** The next steps are to examine the second variant's other associations (a pleiotropy check) and to apply estimators that are robust to some invalid instruments before drawing a causal conclusion.

## Limits of this lesson

All effect sizes are synthetic. The lesson covers the core idea with one or two variants; multi-variant methods, colocalization and two-sample design details are beyond its scope.
