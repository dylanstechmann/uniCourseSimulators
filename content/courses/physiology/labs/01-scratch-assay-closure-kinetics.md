# Virtual lab 1: closure kinetics in a synthetic scratch assay

**Activity type:** synthetic-data analysis with public, ungraded formative checks
**Course package:** Human Physiology for Engineers. **Estimated learner time:** 2–3 hours
**Data status:** all measurements are constructed for instruction. They describe no real cells, compound or experiment, and nothing here is evidence about any treatment or about human healing.
**Dataset:** [synthetic closure measurements (CSV)](https://raw.githubusercontent.com/dylanstechmann/uniStemCourseSimulators/main/content/courses/physiology/labs/scratch-assay-closure.csv).

## Experimental question

A confluent layer of cultured cells is scraped to leave a straight cell-free gap about 400 μm wide. The gap is imaged at 0, 6, 12, 18 and 24 hours and its area is expressed as a percent of the starting area (100% at 0 h). Three conditions are compared in four independent experiments each (one well per condition per experiment, performed on separate days): untreated **control**, a **migration-inhibitor**, and **division-blocked**, in which cell division is prevented. The lab asks how fast the gap closes, whether the inhibitor slows it, how much of the closure depends on division, and what these results do and do not say about healing.

## Learning objectives

1. Summarize repeated closure measurements by condition and time, counting independent experiments and averaging open area.
2. Calculate a closure rate, a relative closure and an edge migration speed from mean open area.
3. Evaluate which conclusions a closure assay with a migration inhibitor and a division block supports about migration, division and healing.

## Data dictionary

| Column | Meaning |
|---|---|
| condition | control, migration-inhibitor or division-blocked |
| experiment | 1 to 4, an independent experiment (own plate, separate day) |
| time_h | hours after the scratch |
| open_area_pct | cell-free area as a percent of the area at 0 h |

## The synthetic data

Open area (% of starting area) for each experiment:

**Control**

| Experiment | 0 h | 6 h | 12 h | 18 h | 24 h |
|---|---:|---:|---:|---:|---:|
| 1 | 100 | 73 | 48 | 19 | 6 |
| 2 | 100 | 76 | 45 | 22 | 3 |
| 3 | 100 | 72 | 49 | 20 | 5 |
| 4 | 100 | 75 | 46 | 23 | 2 |

**Migration inhibitor**

| Experiment | 0 h | 6 h | 12 h | 18 h | 24 h |
|---|---:|---:|---:|---:|---:|
| 1 | 100 | 88 | 72 | 62 | 46 |
| 2 | 100 | 85 | 75 | 59 | 49 |
| 3 | 100 | 89 | 73 | 61 | 45 |
| 4 | 100 | 86 | 76 | 58 | 48 |

**Division blocked**

| Experiment | 0 h | 6 h | 12 h | 18 h | 24 h |
|---|---:|---:|---:|---:|---:|
| 1 | 100 | 74 | 52 | 24 | 8 |
| 2 | 100 | 77 | 49 | 27 | 5 |
| 3 | 100 | 75 | 51 | 23 | 9 |
| 4 | 100 | 78 | 48 | 26 | 6 |

## Work sequence

To use the software checks, open **Practice gradebook** and select **Virtual lab 1: closure kinetics in a scratch assay (ungraded practice)**. The points are practice feedback only.

1. **Summarize each condition.** Count the independent experiments at 12 h and average the open area at 12 h and 24 h. Upload a table with columns `condition`, `experiments`, `mean_open_12h` and `mean_open_24h`.
2. **Compute rates.** Convert open area to closure (100 minus open area). Compute the average control closure rate over 0 to 12 h, the inhibitor's closure as a fraction of control, and the speed of each advancing edge, assuming straight edges and a 400 μm gap.
3. **Separate migration from division.** Compare the division-blocked group with control at 24 h.
4. **Decide what is supported.** State what the experiment shows, what the replicates are, and what it leaves out.

## Worked calculation

At 12 h the control mean open area is 47%, so 53 percentage points have closed, an average of 4.42 points per hour over 0 to 12 h. The inhibitor group has closed 26 points, 0.49 of control closure. For a 400 μm gap, 0.53 of the width is 212 μm, so each edge moved 106 μm in 12 h, 8.83 μm/h.

At 24 h the division-blocked group has closed 93 points against 96 in control, 0.97 of control closure. In this synthetic assay, most closure over 24 h is therefore independent of division. The control curve is not a straight line: the group closes about 27 points between 6 and 12 h and about 17 between 18 and 24 h, because little gap is left near the end, so a rate computed from the first half is more representative than one computed from the whole period.

## Analytic rubric for discussion

| Criterion | Evidence for full credit |
|---|---|
| Summary table | Counts independent experiments, averages the open area by condition and time |
| Rates | Converts to closure, divides by time, and takes the gap speed to be two edge speeds |
| Migration versus division | Uses the division-blocked group to estimate the share of closure that depends on division |
| Replication | Treats separate experiments, not fields or images, as the replicates |
| Scope | Limits conclusions to this culture system and notes what a flat layer leaves out |

## Limits and provenance

This is an original exercise with constructed data and round numbers. Real scratch assays are noisier, measure gap area by image segmentation with stated rules, and vary in scratch width, cell density and serum conditions. Original lab text and dataset: CC BY 4.0.
