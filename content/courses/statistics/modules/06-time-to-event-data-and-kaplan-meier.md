# Time-to-event data: censoring, Kaplan–Meier estimates and hazard ratios

Many outcomes in biology and medicine are times until something happens: death, disease onset, relapse, a cell line's senescence. Two things make them different from ordinary measurements. The time is always positive and often skewed, and, more importantly, some subjects have not yet had the event when observation ends. This lesson shows how to handle those subjects without discarding information, how the Kaplan–Meier estimate is built by hand, and how to compare groups with a rate ratio, which approximates a hazard ratio under stated assumptions.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute a Kaplan–Meier survival estimate at a stated time from event and censoring times.
2. Explain why censored observations must not be dropped or treated as events.
3. Compare two groups with an event rate per person-time and interpret a rate ratio and its limits as an estimate of a hazard ratio.

## Censoring

An observation is **censored** when the event has not been seen by the end of follow-up, or the subject leaves the study before the event. A censored subject still carries information: they were event-free for the time they were observed. Dropping them throws away that information and biases the result toward shorter times. Treating the censoring time as an event time makes survival look worse than it is. The standard analysis keeps each subject in the **risk set**, the set still under observation and event-free, up to their censoring time and then removes them without counting an event.

Censoring methods assume the reason for censoring is unrelated to the outcome (**non-informative censoring**). If animals are removed because they look unwell, or participants drop out because they feel worse, censoring is informative and the estimate is biased. Reporting why subjects were censored is part of the analysis.

## The Kaplan–Meier estimator

The Kaplan–Meier estimate of the survival function S(t), the probability of remaining event-free beyond time t, multiplies conditional survival at each event time:

**S(t) = ∏ over event times t_i ≤ t of (1 − d_i / n_i)**

where d_i is the number of events at t_i and n_i is the number at risk just before t_i. Censoring changes n_i for later times but is not itself a step in the curve. The estimate drops only at event times, so the curve is a staircase with small tick marks at censoring times. The **median survival** is the first time S(t) falls to 0.5 or below, and is undefined if the curve never reaches 0.5.

A figure with a Kaplan–Meier curve should show the number at risk below the time axis, because the curve at late times rests on few subjects and becomes unreliable there.

## Comparing groups: rates and hazards

The **hazard** is the instantaneous event rate among those still at risk. If it is roughly constant in each group, the event **rate** per unit of person-time, events divided by total time at risk, estimates it, and the **rate ratio** estimates the **hazard ratio** (HR). A hazard ratio of 0.5 means that at any time, those in the treated group who are still at risk have half the instantaneous event rate of controls. Hazard ratios from proportional-hazards models rest on the assumption that the ratio is constant over time. If curves cross, or the benefit fades, a single HR misleads, and the median or restricted-mean survival time may be easier to interpret. An HR is not a statement that people live "twice as long", and it says nothing about absolute risk without the baseline.

## Synthetic data: ten subjects

The values are **synthetic teaching data**: follow-up time in months and whether the event was observed.

| Subject | Time (months) | Status |
|---:|---:|---|
| 1 | 2 | event |
| 2 | 3 | event |
| 3 | 4 | censored |
| 4 | 5 | event |
| 5 | 6 | censored |
| 6 | 8 | event |
| 7 | 9 | censored |
| 8 | 10 | event |
| 9 | 12 | censored |
| 10 | 12 | censored |

## Common mistakes

- Dropping censored subjects, or treating a censoring time as an event time.
- Forgetting that a censored subject stays in the risk set until the censoring time.
- Drawing a step down in the curve at a censoring time.
- Assuming that censoring is unrelated to the outcome when subjects left because they felt worse.
- Reading a hazard ratio of 0.5 as halving the chance of surviving, or using one hazard ratio when the curves cross.
- Reading the late part of a curve without the number at risk.

## Worked example: the Kaplan–Meier table

| Time | At risk n | Events d | Censored | S(t) |
|---:|---:|---:|---:|---:|
| 2 | 10 | 1 | 0 | 0.9000 |
| 3 | 9 | 1 | 0 | 0.8000 |
| 4 | 8 | 0 | 1 | 0.8000 |
| 5 | 7 | 1 | 0 | 0.6857 |
| 6 | 6 | 0 | 1 | 0.6857 |
| 8 | 5 | 1 | 0 | 0.5486 |
| 9 | 4 | 0 | 1 | 0.5486 |
| 10 | 3 | 1 | 0 | 0.3657 |
| 12 | 2 | 0 | 2 | 0.3657 |

At month 2, 1 of 10 has the event: S = 1 − 1/10 = 0.9. At month 3, 1 of 9: S = 0.9 × 8/9 = 0.8. The subject censored at month 4 leaves the risk set without a step. At month 5 there are 7 at risk, so S = 0.8 × 6/7 = 0.6857. The estimate first falls below 0.5 at month 10 (0.3657), so the median survival is 10 months; at month 8 it is still 0.5486.

For group comparison, suppose treated participants had 12 events over 480 person-months (0.025 per month) and controls 20 events over 400 person-months (0.050 per month). The rate ratio is 0.025 / 0.050 = 0.50, an estimate of the hazard ratio if each group's hazard is about constant.

## Limits of this lesson

The data are synthetic and ten subjects are far too few for inference. The lesson shows how the arithmetic works. It does not cover confidence intervals for the curve, the log-rank test, or models with covariates, and it gives no clinical advice.
