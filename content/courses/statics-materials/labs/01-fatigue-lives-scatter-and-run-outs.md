# Virtual lab 1: fatigue lives, scatter and run-outs

**Activity type:** synthetic-data analysis with public, ungraded formative checks
**Course package:** Statics & Mechanics of Materials. **Estimated learner time:** 2–3 hours
**Data status:** all measurements are constructed for instruction. They describe no real material, specimen or test machine, and nothing here is evidence about any device.
**Dataset:** [synthetic fatigue lives (CSV)](https://raw.githubusercontent.com/dylanstechmann/uniStemCourseSimulators/main/content/courses/statics-materials/labs/fatigue-lives-by-stress-amplitude.csv).

## Experimental question

Twenty nominally identical synthetic specimens are cycled at four stress amplitudes (300, 260, 230 and 200 MPa), five at each level, and the number of cycles to failure is recorded. Testing stops at 2,000,000 cycles, and a specimen that has not failed by then is recorded as a run-out. The lab asks how to summarize lives that scatter by a large factor, how to fit a Basquin line, how to treat the run-outs, and how far the fitted line can be trusted.

## Learning objectives

1. Summarize fatigue lives by stress amplitude, counting failures and run-outs and averaging the logarithm of the life.
2. Fit a Basquin line to the level means and read the exponent and a predicted life from it.
3. Evaluate how scatter, censoring and extrapolation limit what fatigue data support.

## Data dictionary

| Column | Meaning |
|---|---|
| level | stress level code: s300, s260, s230, s200 |
| amplitude_mpa | stress amplitude in MPa (fully reversed loading) |
| specimen | 1 to 5, a specimen at that level |
| cycles | cycles at failure, or the cutoff of 2,000,000 for a run-out |
| status | failed or runout |

## The synthetic data

Cycles to failure by specimen (run-outs marked):

| Level (MPa) | Specimen 1 | Specimen 2 | Specimen 3 | Specimen 4 | Specimen 5 | Failures |
|---:|---:|---:|---:|---:|---:|---:|
| 300 | 18,200 | 24,600 | 30,900 | 38,000 | 51,300 | 5 |
| 260 | 155,000 | 205,000 | 66,300 | 110,000 | 132,000 | 5 |
| 230 | 461,000 | 568,000 | 821,000 | 272,000 | 334,000 | 5 |
| 200 | 853,000 | 1,290,000 | 1,910,000 | 2,000,000 (run-out) | 2,000,000 (run-out) | 3 |

## Work sequence

To use the software checks, open **Practice gradebook** and select **Virtual lab 1: fatigue lives, scatter and run-outs (ungraded practice)**. The points are practice feedback only.

1. **Summarize.** For each level, count the specimens and the failures and average log10 of the cycles to failure of the failures. Upload a table with columns `level`, `specimens`, `failures` and `mean_log10_failed`.
2. **Scatter.** Compute the standard deviation of log10(cycles) at 260 MPa and the ratio of the longest to the shortest life at that level.
3. **Fit.** Regress the mean log10 life on log10 of the stress amplitude for the three levels with no run-outs, and invert the slope to get the Basquin exponent b.
4. **Run-outs.** Compare the mean log10 life at 200 MPa of the failures only with the mean when the run-outs are counted at the cutoff.
5. **Extrapolate and interpret.** Predict the median log10 life at 160 MPa from the fitted line and decide what the data support.

## Worked calculation

The level means of log10 life (failures only) are 4.486, 5.097, 5.658, 6.108, in the order of the table. The standard deviation of log10(cycles) at 260 MPa is 0.183, a factor of 1.53 in cycles, and the longest life is 3.1 times the shortest. A line through the first three level means has slope −10.15, so b = 1/−10.15 = −0.099. At 200 MPa, 2 specimens did not fail: the mean log10 life of the three failures is 6.108 and the mean with the run-outs counted at the cutoff is 6.185; both are low because the run-outs lasted at least as long as the cutoff. At 160 MPa the line predicts a median log10 life of 7.25, about 18 million cycles, but this is below the lowest tested level of 200 MPa, rests on three level means, and is a median, not a design life.

## Analytic rubric for discussion

| Criterion | Evidence for full credit |
|---|---|
| Summary table | Counts specimens and failures separately, averages logarithms of failure lives and keeps run-outs out of the mean of failures |
| Scatter | Computes the spread of log life and expresses it as a factor in cycles |
| Fit | Fits log life against log stress and converts the slope to the Basquin exponent |
| Run-outs | Explains that run-outs are censored and that both simple treatments bias the life low |
| Limits | States that the extrapolation lies beyond the data and that a median life is not a design life |

## Limits and provenance

This is an original exercise with constructed data. Real fatigue data have specimen-to-specimen scatter that depends on the surface, the environment and the frequency, and are analyzed with methods that use run-outs directly (for example, maximum likelihood with censoring). Original lab text and dataset: CC BY 4.0.
