# Heritability, polygenic scores and the limits of genetic prediction

Many traits that matter for health, including height, blood lipids and the age at which chronic diseases appear, are influenced by thousands of variants of small effect together with environment. Two ideas organize the evidence about such traits: heritability, which partitions variation in a population, and polygenic scores, which sum many small effects into a prediction for an individual. Both are frequently misread. This lesson computes each from synthetic numbers and then spells out what they do and do not mean.

## Learning objectives

By the end of this lesson, you should be able to:

1. Estimate additive genetic, shared-environment and unique-environment variance components from twin correlations under stated assumptions.
2. Compute a polygenic score from effect sizes and allele dosages and convert variance explained into a correlation.
3. Evaluate claims about heritability and polygenic prediction, including portability across populations and the difference between population variance and individual destiny.

## Heritability as a ratio of variances

For a trait measured in a population, total variance can be modeled as V_P = V_A + V_C + V_E: additive genetic variance, variance from environment shared by relatives raised together, and everything else (unshared environment plus measurement error). **Narrow-sense heritability** is h² = V_A / V_P. It is a property of a population in an environment, not of a trait in general and not of a person.

## Estimating components from twins

Monozygotic (MZ) twins share essentially all their genome; dizygotic (DZ) twins share on average half of the segregating variants. If both kinds of twin pair share their environment to the same degree, the classical (Falconer) estimates are

- h² = 2 (r_MZ − r_DZ)
- c² = 2 r_DZ − r_MZ
- e² = 1 − r_MZ

where r is the within-pair correlation for the trait.

**Synthetic teaching data:** r_MZ = 0.5, r_DZ = 0.3. Then h² = 2 × (0.5 − 0.3) = 0.40, c² = 2 × 0.3 − 0.5 = 0.10 and e² = 1 − 0.5 = 0.50.

The equal-environments assumption is the weak point: if MZ pairs are treated more alike than DZ pairs, h² is overestimated. Non-additive genetic effects (dominance, interactions) and assortative mating also bias the simple formulas. Modern designs estimate heritability from measured genotypes in unrelated people as well, and these estimates are usually lower than twin estimates for the same trait, a gap often called "missing heritability".

## Polygenic scores

A polygenic score adds up, across many variants, the number of effect alleles a person carries times each variant's estimated effect from a genome-wide association study:

**PGS = Σ β_i × g_i,** with g_i ∈ {0, 1, 2}.

**Synthetic four-variant example:** effects β = [0.1, -0.05, 0.2, 0.04] (trait units per allele) and dosages g = [2, 1, 0, 2] give PGS = (0.1)(2) + (-0.05)(1) + (0.2)(0) + (0.04)(2) = 0.23. Real scores use thousands to millions of variants, and the scale of a raw score only has meaning relative to a reference distribution.

How well a score predicts is summarized by the variance it explains in an independent test sample. If a score explains R² = 0.08 of trait variance, its correlation with the trait is √0.08 = 0.28. At that correlation, people with the same score still differ widely; the score shifts the average of a group more than it fixes any individual's value.

## What these numbers do not mean

- **High heritability does not mean unchangeable.** Heritability describes variation under current environments. A change in environment that affects everyone can shift the mean without changing h².
- **Heritability is not the fraction of one person's trait caused by genes.** It is a ratio of population variances.
- **Scores travel poorly.** Effect estimates come from the populations studied; differences in allele frequencies and linkage patterns mean that a score trained in one ancestry group usually predicts less well in others.
- **A predictive variant is not necessarily causal.** Association studies identify variants correlated with the trait; the causal variant may be nearby, and the association may partly reflect population structure or indirect effects through relatives' environments.
- **Prediction of a group average is not a diagnosis.** A small shift in risk at the population level can be real and useful for research while saying little about one person.

## Why this matters for aging research

Lifespan and age-related traits are studied with these same tools. The same cautions apply: a heritability estimate for longevity in one cohort describes that cohort, a polygenic score for an age-related trait is a statistical summary with limited individual accuracy, and neither identifies an intervention. Moving from association to mechanism requires the causal designs discussed in the gene-regulation lesson.

## Worked example

**Problem.** For a second synthetic trait, r_MZ = 0.7 and r_DZ = 0.45. Estimate the three components, then ask how much a polygenic score with R² = 0.08 narrows the spread of the trait among people who share the same score.

**Step 1: components.** h² = 2 × (0.7 − 0.45) = 0.50; c² = 2 × 0.45 − 0.7 = 0.20; e² = 1 − 0.7 = 0.30. The three sum to one, as they must under the model.

**Step 2: check the assumption.** If MZ pairs share more environment than DZ pairs, part of the 0.50 attributed to genes is environmental, and h² is an upper estimate.

**Step 3: prediction spread.** Among people with the same score, the residual standard deviation is √(1 − R²) = √0.92 = 0.959 of the population standard deviation. Conditioning on the score narrows the spread by only 4%. A score can shift group averages measurably while leaving individual outcomes highly uncertain.

## Limits of this lesson

All correlations, effects and dosages are synthetic. The Falconer formulas are a first approximation; the lesson does not cover structural-equation twin models, genomic relatedness methods or score construction and validation in detail.
