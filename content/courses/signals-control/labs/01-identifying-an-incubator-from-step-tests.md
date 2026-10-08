# Virtual lab 1: identifying an incubator from step tests and checking a PI design

**Activity type:** synthetic-data analysis with public, ungraded formative checks
**Course package:** Signals, Systems & Feedback Control. **Estimated learner time:** 2–3 hours
**Data status:** all measurements are constructed for instruction. They describe no real incubator, heater or sensor, and nothing here is evidence about any device.
**Dataset:** [synthetic step tests (CSV)](https://raw.githubusercontent.com/dylanstechmann/uniStemCourseSimulators/main/content/courses/signals-control/labs/incubator-step-tests.csv).

## Experimental question

An incubator-like chamber is at rest at room temperature. A step in heater power of 10, 20 or 30 W is applied at time 0, and the temperature rise above ambient is recorded every minute for 60 minutes, twice for each step size (366 rows). The lab asks for the gain, the delay and the time constant of a first-order-plus-delay model, a first PI tuning from those numbers, and what the three step sizes say about how far the model can be trusted.

## Learning objectives

1. Summarize step-test data by step size, counting runs and samples and averaging the settled response.
2. Estimate the gain, delay and time constant of a first-order-plus-delay model from step-response data and use them to tune a PI controller.
3. Evaluate what step tests of different sizes say about linearity and how that limits a tuning.

## Data dictionary

| Column | Meaning |
|---|---|
| test | test code: test_10w, test_20w, test_30w |
| power_w | step in heater power, W |
| run | 1 or 2, a repeat of the test |
| time_min | minutes after the step |
| rise_c | temperature rise above ambient, °C |

## The synthetic data (mean of the two runs)

| Time (min) | 10 W | 20 W | 30 W |
|---:|---:|---:|---:|
| 0 | 0.00 | 0.00 | 0.00 |
| 1 | 0.01 | 0.01 | 0.01 |
| 2 | 0.43 | 0.88 | 1.27 |
| 5 | 1.60 | 3.16 | 4.50 |
| 10 | 3.01 | 5.80 | 8.23 |
| 15 | 3.74 | 7.28 | 10.37 |
| 20 | 4.29 | 8.29 | 11.77 |
| 30 | 4.74 | 9.19 | 13.06 |
| 40 | 4.92 | 9.52 | 13.54 |
| 60 | 5.03 | 9.71 | 13.80 |

## Work sequence

To use the software checks, open **Practice gradebook** and select **Virtual lab 1: identifying an incubator from step tests and checking a PI design (ungraded practice)**. The points are practice feedback only.

1. **Summarize.** For each step size, count the runs and the sampled minutes in each run and average the rise over minutes 56 to 60 of both runs. Upload a table with columns `test`, `runs`, `samples` and `mean_final_rise`.
2. **Gain.** Divide the settled rise of the 20 W step by 20 W.
3. **Delay and time constant.** Average the two 20 W runs at each minute. The delay is the last minute at which the average is within 2% of the settled value. The 63.2% time is found by linear interpolation, and the time constant is the 63.2% time minus the delay.
4. **Tune.** Use the cancellation rule with λ = 2 min to get a proportional gain, and keep T_i equal to the time constant.
5. **Check linearity.** Compare the gains from the three step sizes and decide what they imply for the tuning and for the margins at high power.

## Worked calculation

The settled rises are 4.99, 9.67, 13.76 °C for 10, 20 and 30 W, so the gains are 0.499, 0.484, 0.459 °C/W. For the 20 W step the average is within 2% of the settled value (0.19 °C) up to minute 1, and reaches 63.2% of 9.67 °C, which is 6.11 °C, at 11.00 min by linear interpolation. The time constant is 11.00 − 1 = 10.00 min. With K = 0.49 °C/W, τ = 10 min, θ = 1 min and λ = 2 min, the proportional gain is 10/(0.49 × 3) = 6.803 W/°C. The gain at 30 W is 0.919 times the gain at 10 W: the plant is only approximately linear, and the loop gain varies by about 8% across the range. Open-loop tests do not show how the closed loop behaves with saturation, disturbances or a sensor filter.

## Analytic rubric for discussion

| Criterion | Evidence for full credit |
|---|---|
| Summary table | Counts runs and samples separately and averages the settled response over both runs |
| Model | Estimates the gain, delay and time constant from the averaged response with a stated rule |
| Tuning | Computes a proportional gain from the model and keeps the integral time equal to the time constant |
| Linearity | Compares the gains at the three step sizes and states the consequence for the loop gain and margins |
| Limits | States that open-loop steps do not establish closed-loop stability, saturation behavior or robustness to a filter |

## Limits and provenance

This is an original exercise with constructed data. Real step tests are disturbed by drafts, sensor drift and heater dynamics, and identification from a single step is crude; better methods fit a model to the whole record. Original lab text and dataset: CC BY 4.0.
