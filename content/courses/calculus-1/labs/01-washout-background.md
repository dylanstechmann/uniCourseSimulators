# Virtual lab 1: washout signals, background and semilog estimates

**Status:** open formative practice, with public answers and unlimited retries. Points are learning feedback, not a course grade. The exercise uses 21 constructed observations, not measured clearance data. Prerequisites are the lessons on logarithmic growth and numerical calculus; the background model is introduced below. The washout capstone follows in week 14.

## Learning objectives

1. Summarize observations and calculate raw and corrected endpoint decay rates.
2. Compare half-life and a reserved late prediction under different measurement assumptions.
3. Explain which uncertainty and model-identification claims the data do and do not support.

## Scenario and data dictionary

The underlying teaching concentration is C(t)=20e^(−0.1t), with time t in hours. The sensor reports Y(t)=C(t)+2 in a common arbitrary signal scale. The constant blank 2 is independently supplied and exact in this construction. At seven times, the mean signal is rounded to three decimal places and three readings are placed at mean minus 0.1, mean, and mean plus 0.1. Their offsets deliberately balance. Reusing replicate numbers does not establish independence across times, and no confidence interval or real sensor-noise distribution is inferred.

[Download the synthetic CSV](https://raw.githubusercontent.com/dylanstechmann/uniStemCourseSimulators/main/content/courses/calculus-1/labs/washout-signals.csv). The `time` column is the stable row group code; `hours` is elapsed time; `replicate` is a constructed reading identifier from 1 to 3; `signal` is the reported value including background; and `blank` is the known background. Signals and blank share the same scale. Every corrected mean is positive in this exercise. The row values, rather than the unrounded generating function, define the numeric answers below.

## Summary of the supplied observations

| Time code | Hours | Readings | Mean signal | Mean minus blank |
|---|---:|---:|---:|---:|
| t00 | 0 | 3 | 22.000 | 20.000 |
| t05 | 5 | 3 | 14.131 | 12.131 |
| t10 | 10 | 3 | 9.358 | 7.358 |
| t15 | 15 | 3 | 6.463 | 4.463 |
| t20 | 20 | 3 | 4.707 | 2.707 |
| t30 | 30 | 3 | 2.996 | 0.996 |
| t40 | 40 | 3 | 2.366 | 0.366 |

The table is a reference for checking your grouping. It is not an extra independent dataset. Read the full CSV to confirm that averaging the three values yields each mean and that every group has three readings.

## Work sequence

Open Practice gradebook and select **Virtual lab 1: washout signals, background and semilog estimates (ungraded practice)**. First group the observations by time. Upload a summary with exact columns `time,replicates,mean_signal`, seven row codes t00 through t40 as displayed above, counts and arithmetic means. The upload checks seven counts and seven means; the mean tolerance is 0.005 signal units. It does not grade a written uncertainty explanation.

Second, use only the means at 0 and 20 h for the two endpoint estimates. Compute k_raw=ln(Y₀/Y₂₀)/20. Then subtract the blank and compute k_corrected=ln((Y₀−2)/(Y₂₀−2))/20. Retain intermediate precision. Both quantities have inverse-hour units, but they answer different model questions: the raw estimate assumes zero background, while the corrected estimate uses the independently supplied offset. The difference is not a change in logarithm base or in time units.

Third, calculate the corrected half-life as ln 2/k_corrected. Fourth, use the raw endpoint model Y_pred(t)=Y₀e^(−k_raw t) to predict 40 h and compare it with the mean at 40 h. The 40 h value is reserved from this fitting calculation. A model chosen using all late observations would need further data for an independent prediction test. Finally, explain what changes if the blank is estimated with uncertainty instead of supplied exactly.

## Worked calculation

The endpoint means are 22.000 and 4.707. Without correction, k_raw=0.077100 h⁻¹. Subtracting 2 gives 20.000 and 2.707, hence k_corrected=0.099995 h⁻¹. The tiny difference from the exact generating rate 0.1 comes from rounding the supplied observations. The half-life is 6.931849 h. The raw zero-background prediction at 40 h is 1.007084, while the reserved mean is 2.366. Their ratio is 2.3494, showing substantial underprediction.

An exact background-corrected generating model would give a straight natural-log ratio and the rate 0.1. The raw sensor signal instead approaches the constant blank, so its semilog curve flattens. This conclusion is known from the construction. In a real dataset, curvature alone would not distinguish a background from mixed decay rates, time-varying behavior or sensor dynamics. A better fit with extra parameters is not by itself evidence for a unique mechanism.

## Discussion criteria

| Criterion | Evidence to discuss |
|---|---|
| Summary | Correct time grouping, counts and mean signal values |
| Calculation | Positive corrected ratios, natural logarithms, interval width and rate units |
| Prediction | A 40 h prediction made from the specified earlier endpoints only |
| Uncertainty | Shared effects of an estimated blank and limits of small balanced synthetic groups |
| Interpretation | Multiple explanations for real semilog curvature and an independent way to distinguish them |

These criteria guide discussion, not an automatically graded written report or instructor review. Structured choices check selected distinctions only. Negative or zero corrected observations would require a justified analysis change, not an arbitrary logarithm or silent removal. An estimated blank can correlate errors across all corrected times; averaging repeats does not remove a fixed calibration offset.

## Limits and provenance

The mean curve and offsets are constructed and unusually orderly. They establish no real decay parameter, noise distribution, compartment mechanism or therapeutic conclusion. The example gives no experimental protocol or device setting. Original lab and CSV: CC BY 4.0, developed with substantial AI assistance. Existing calculus references provide scope; no third-party dataset or teaching text was reproduced.
