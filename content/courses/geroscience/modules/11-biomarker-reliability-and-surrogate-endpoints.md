# Biomarkers of aging under scrutiny: reliability, the smallest detectable change and surrogate endpoints

Aging research increasingly relies on biomarkers: epigenetic clocks, blood-based scores, frailty indices and functional tests. They promise to show whether an intervention is working years before outcomes such as disease or death could be counted. Two questions decide whether that promise holds for a given marker: is the measurement reliable enough that a change in one person can be distinguished from noise, and does changing the marker actually change the outcome it predicts? This lesson works through the first quantitatively with synthetic numbers and the second conceptually.

## Learning objectives

By the end of this lesson, you should be able to:

1. Calculate the intraclass correlation coefficient from between-person and within-person variance and interpret it as test–retest reliability.
2. Compute the smallest detectable change for an individual and show how averaging repeated measurements improves it.
3. Evaluate whether a biomarker can serve as a surrogate endpoint for an intervention, distinguishing prediction from causal mediation.

## Reliability: how much of the variation is real

Suppose a synthetic biological-age score varies between people with a standard deviation of 5 years, and repeated measurements of the same person on the same day (different samples, batches or runs) vary with a within-person standard deviation of 3 years. The **intraclass correlation coefficient** is the share of total variance due to real differences between people:

**ICC = σ²_between / (σ²_between + σ²_within)** = 5² / (5² + 3²) = 0.735.

An ICC of 0.74 means about 26% of the variation in a single reading is measurement noise. That can be acceptable for comparing groups, where noise averages out over many people, while still being too noisy for judging one person.

## The smallest detectable change

For one person measured twice, the difference between readings has a standard deviation of √2 × σ_within. A change is distinguishable from measurement noise at about 95% confidence only if it exceeds

**SDC = 1.96 × √2 × σ_within** = 1.96 × 1.414 × 3 = 8.3 years.

So an individual whose score drops by 4 years between two tests has not shown a change the measurement can detect. Claims such as "my biological age fell by four years" based on two readings of a marker with these properties are within noise.

**Averaging helps.** If each time point uses the mean of 3 independent measurements, the within-person SD falls to 3/√3 = 1.73, the SDC to 4.8 years, and the ICC of the averaged score rises to 0.893. Technical replicates reduce only the technical component of noise; day-to-day biological fluctuation needs measurements on different days.

## From predictor to surrogate endpoint

A marker that predicts outcomes across people is a **predictor**. To serve as a **surrogate endpoint** for an intervention, more is needed: the intervention's effect on the outcome must run through the marker, so that changing the marker by a given amount reliably changes the outcome by a predictable amount. Several things can break this:

- **Confounding of the prediction:** the marker may track something else that causes the outcome (overall health, smoking, socioeconomic factors).
- **Off-pathway effects:** an intervention can move the marker without touching the processes that cause disease, or change the outcome by a route the marker does not capture.
- **Measurement artifacts:** some interventions can change the composition of the sampled tissue (for example, the proportions of blood cell types), shifting a blood-based score without changing aging in other tissues.

Medicine has examples where drugs improved a well-established predictor without improving, or while worsening, the outcomes that mattered. That history is why regulators accept surrogates only after validation in trials that measured both the marker and the hard outcome. For aging biomarkers that validation is still largely ahead; an intervention that lowers a clock score has shown that it lowers the score.

## Common mistakes

- Treating a high correlation with chronological age as evidence that a score measures aging rates.
- Reading an individual's change from two measurements without comparing it with the SDC.
- Using the same sample to build a marker and to test it.
- Equating "predicts mortality across people" with "changing it changes mortality".

## Worked example

**Problem.** A synthetic study plans to show that an intervention lowers the score by 2 years in a group. Is the marker reliable enough at the group level?

**Step 1.** With n people per group, the within-person noise contributes σ_within/√n to the group-mean change; for n = 100, 3/10 = 0.3 years.

**Step 2.** Between-person variation in true change also contributes, and a randomized control group is needed to remove regression to the mean and drift (see the statistics lessons).

**Step 3.** A 2-year group difference is detectable with enough people even though it is far below the individual SDC of 8.3 years. Whether that difference matters for health is a separate, surrogate-validation question that this design does not answer.

## Limits of this lesson

All variances are synthetic and describe no specific biomarker. The lesson does not assess any commercial test, and it makes no claim that any intervention changes human aging.
