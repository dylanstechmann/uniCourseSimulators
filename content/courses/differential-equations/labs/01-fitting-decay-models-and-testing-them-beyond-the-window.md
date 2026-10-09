# Virtual lab 1: fitting decay models to a time course and testing them beyond the window

**Activity type:** synthetic-data analysis with public, ungraded formative checks
**Course package:** Differential Equations for Living & Engineered Systems. **Estimated learner time:** 2–3 hours
**Data status:** all measurements are constructed for instruction. They describe no real cells, medium or growth factor, and nothing here is evidence about any culture.
**Dataset:** [synthetic cell counts (CSV)](https://raw.githubusercontent.com/dylanstechmann/uniStemCourseSimulators/main/content/courses/differential-equations/labs/cell-counts-after-growth-factor-removal.csv).

## Experimental question

Viable cells are counted in three wells at 0, 6, 12, 18, 24, 36 and 48 hours after a growth factor is removed (21 counts, in thousands of cells per well). The first five time points (0 to 24 h) are used to fit two models, a straight line N = a − bt and a first-order decay dN/dt = −kN, and the later points (36 and 48 h) are held back to test them. The lab asks what each model predicts, which one fails and how, and what a validation done on the early window alone would have missed.

## Learning objectives

1. Summarize replicate counts by time and fit a straight line and a first-order decay to the early window.
2. Use each fitted model to predict later times and compare the predictions with the observed means.
3. Evaluate what the later observations say about the structure of each model and what validation would have shown it.

## Data dictionary

| Column | Meaning |
|---|---|
| time | time code: t00h, t06h, t12h, t18h, t24h, t36h, t48h |
| hours | hours after the growth factor is removed |
| well | 1 to 3, a replicate well at that time |
| count_k | viable cells in the well, thousands |

## The synthetic data (mean of the three wells)

| Time (h) | Mean count (thousands per well) |
|---:|---:|
| 0 | 100.0 |
| 6 | 64.2 |
| 12 | 42.0 |
| 18 | 28.3 |
| 24 | 19.8 |
| 36 | 11.3 |
| 48 | 8.0 |

## Work sequence

To use the software checks, open **Practice gradebook** and select **Virtual lab 1: fitting decay models to a time course and testing them beyond the window (ungraded practice)**. The points are practice feedback only.

1. **Summarize.** Count the wells and average the counts at each time. Upload a table with columns `time`, `wells` and `mean_count`.
2. **First-order fit.** Fit a straight line to the natural logarithm of the mean count against time over 0 to 24 h; the decay rate k is the negative of the slope and N₀ is the exponential of the intercept.
3. **Linear fit.** Fit a straight line to the mean count against time over 0 to 24 h. Find where it reaches zero and what it predicts at 48 h.
4. **Predict and compare.** Use the first-order model to predict the 48 h mean, and compare it with the observed mean.
5. **Interpret.** State which model fails by giving an impossible value, which fails by under-predicting, and what validation would have shown it.

## Worked calculation

The means are 100.0, 64.2, 42.0, 28.3, 19.8, 11.3, 8.0. Over 0 to 24 h, the line of ln N against t has slope −0.0676, so k = 0.0676 h⁻¹, and N₀ = 97.3. The straight line is 90.11 + (−3.272)t, which reaches zero at 27.5 h and predicts −66.9 at 48 h. The first-order prediction at 48 h is 97.3 × e^(−0.0676 × 48) = 3.79, while the observed mean is 8.0, a ratio of 2.11: the first-order model never goes negative, but it under-predicts the late counts; one explanation is that part of the population decays more slowly than the early rate suggests. A better model needs later data and an independent test.

## Analytic rubric for discussion

| Criterion | Evidence for full credit |
|---|---|
| Summary table | Counts the replicate wells at each time and averages their counts |
| Fits | Fits the line and the first-order decay to the early window with correct formulas |
| Predictions | Evaluates both models at later times, including the zero crossing of the line |
| Comparison | Compares the predictions with the observed means and identifies which model fails in sign and which in size |
| Validation | Explains how hold-out data, later independent data and invariant checks would have shown the failure |

## Limits and provenance

This is an original exercise with constructed data. Real cell-loss data are noisier, the wells may differ in more than counting error, and a decay with a slowly dying subpopulation is only one of several explanations for a slowing decline. Original lab text and dataset: CC BY 4.0.
