# Virtual lab 1: a lifespan cohort with censoring and a survivor-only healthspan test

**Activity type:** synthetic-data analysis with public, ungraded formative checks
**Course package:** Geroscience & Regenerative Biology. **Estimated learner time:** 2–3 hours
**Data status:** all observations are constructed for instruction. They describe no real animals, intervention or study, and nothing here is evidence about any compound or about human aging.
**Dataset:** [synthetic cohort (CSV)](https://raw.githubusercontent.com/dylanstechmann/uniStemCourseSimulators/main/content/courses/geroscience/labs/lifespan-cohort.csv).

## Experimental question

Two groups of 12 laboratory animals of one sex and strain are followed from young adulthood: a control group and a group given an intervention. The study records the last day each animal was observed and whether it had died, and on day 730 measures grip strength in the animals still alive as a healthspan measure. The study ends at day 1000. Two analysis errors are common in exactly this design: treating animals still alive at the end as if they had died, and comparing a late healthspan measure across groups without noticing that it was measured only in survivors. This lab works through both.

## Learning objectives

1. Summarize a lifespan cohort correctly when some animals are still alive at the end of the study, using counts and Kaplan–Meier medians rather than naive means.
2. Identify survivorship bias in a healthspan measure taken only in animals alive at a late time point.
3. Evaluate which conclusions a single synthetic cohort supports about an intervention's effect on lifespan and healthspan.

## Data dictionary

| Column | Meaning |
|---|---|
| group | control or intervention |
| animal | identifier |
| last_day_observed | day of death, or day 1000 for animals alive at study end |
| died | 1 if the animal died on that day, 0 if it was alive at study end (censored) |
| grip_strength_g_day730 | grip strength in grams at day 730, blank if the animal had died before then |

## The synthetic data

**Control**

| Animal | Last day | Died | Grip at 730 (g) |
|---|---:|---:|---:|
| C01 | 612 | 1 | — |
| C02 | 655 | 1 | — |
| C03 | 690 | 1 | — |
| C04 | 718 | 1 | — |
| C05 | 742 | 1 | 92 |
| C06 | 760 | 1 | 88 |
| C07 | 781 | 1 | 95 |
| C08 | 803 | 1 | 90 |
| C09 | 826 | 1 | 86 |
| C10 | 850 | 1 | 93 |
| C11 | 879 | 1 | 89 |
| C12 | 915 | 1 | 91 |

**Intervention**

| Animal | Last day | Died | Grip at 730 (g) |
|---|---:|---:|---:|
| I01 | 640 | 1 | — |
| I02 | 701 | 1 | — |
| I03 | 745 | 1 | 94 |
| I04 | 772 | 1 | 90 |
| I05 | 798 | 1 | 97 |
| I06 | 821 | 1 | 92 |
| I07 | 846 | 1 | 88 |
| I08 | 870 | 1 | 95 |
| I09 | 905 | 1 | 91 |
| I10 | 940 | 1 | 93 |
| I11 | 1000 | 0 | 89 |
| I12 | 1000 | 0 | 96 |

## Work sequence

To use the software checks, open **Practice gradebook** and select **Virtual lab 1: lifespan cohort (ungraded practice)**. The points are practice feedback only.

1. **Summarize the groups.** Count animals and grip measurements per group and average the grip values that exist. A blank is a missing measurement, not a zero. Upload the summary table.
2. **Estimate survival.** Build the Kaplan–Meier estimate for each group (see the lesson on survival curves and healthspan endpoints, and the statistics lesson on time-to-event data). With no censoring before the end, each death at a time with n animals at risk multiplies survival by (1 − 1/n). Find the first day survival falls to 0.5 or below.
3. **See why a naive mean misleads.** Average the recorded days for the intervention group as if the two survivors died at day 1000, and explain why that is a lower bound.
4. **Reason about the grip test.** Decide what the survivor-only measurement allows you to say.
5. **Decide what the cohort supports.** Separate the conclusions this design can carry from those it cannot.

## Worked calculation

Control: all 12 animals died. After the sixth death (day 760), survival is 6/12 = 0.5, so the Kaplan–Meier median is day 760. Intervention: 10 deaths and 2 censored at day 1000. Because censoring happens only at the end, survival after the k-th death is (12 − k)/12, which first reaches 0.5 at the sixth death, day 821. The difference in medians is 61 days. A mean of the intervention group's recorded days, treating survivors as deaths, is 836.5 days; the true mean is unknown but larger.

Grip strength was measured in 8 control and 10 intervention animals, means 90.5 g and 92.5 g. The intervention group retained more animals to day 730; if weaker animals tend to die earlier, the control survivors are a more selected (possibly stronger) subset, or vice versa. The difference cannot be attributed to the intervention without methods that account for survival, such as analyzing grip in all animals at an earlier time point when all were alive, or joint models of survival and function.

## Analytic rubric for discussion

| Criterion | Evidence for full credit |
|---|---|
| Summary table | Counts all animals, counts measured animals separately, averages only existing values |
| Censoring | Treats survivors as censored and uses a Kaplan–Meier median, not a naive mean |
| Survivor bias | States that the grip comparison involves survivor subsets of different size and composition |
| Scope | Limits conclusions to this synthetic cohort and names replication across sex, strain and site |

## Limits and provenance

This is an original exercise with constructed data. Real lifespan studies use larger cohorts, formal survival tests, pre-specified analysis plans and several sites; none of that is simulated here. Original lab text and dataset: CC BY 4.0.
