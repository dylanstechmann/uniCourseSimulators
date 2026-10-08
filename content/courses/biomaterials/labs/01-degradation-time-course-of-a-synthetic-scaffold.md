# Virtual lab 1: degradation time course of a synthetic scaffold

**Activity type:** synthetic-data analysis with public, ungraded formative checks
**Course package:** Biomaterials & Tissue Engineering. **Estimated learner time:** 2–3 hours
**Data status:** all measurements are constructed for instruction. They describe no real polymer, scaffold or experiment, and nothing here is evidence about any material or implant.
**Dataset:** [synthetic time course (CSV)](https://raw.githubusercontent.com/dylanstechmann/uniStemCourseSimulators/main/content/courses/biomaterials/labs/scaffold-degradation-time-course.csv).

## Experimental question

A synthetic polyester scaffold (repeat unit 72 g/mol) is incubated in buffer at 37 °C. At 7 time points from day 0 to day 84, three specimens are removed and three things are measured on each: the number-average molar mass (in kDa), the mass remaining (percent of the initial mass) and the compressive modulus (MPa). The lab asks how fast bonds are cleaved, in what order the three measurements change, and how long the scaffold keeps a modulus of at least 0.8 MPa.

## Learning objectives

1. Summarize replicate specimens by time point for molar mass, mass and modulus.
2. Estimate the fraction of bonds cleaved, the scission rate constant and the exponential rate of modulus loss from time-course means.
3. Compare the time courses of molar mass, mass and modulus and state which measurement predicts the period of mechanical support.

## Data dictionary

| Column | Meaning |
|---|---|
| day | time in buffer, days |
| specimen | 1 to 3, an independent specimen removed at that time |
| mn_kda | number-average molar mass, kDa |
| mass_pct | mass remaining, percent of the initial mass |
| modulus_mpa | compressive modulus, MPa |

## The synthetic data

**Number-average molar mass (kDa)**

| Day | Specimen 1 | Specimen 2 | Specimen 3 | Mean |
|---:|---:|---:|---:|---:|
| 0 | 103.0 | 99.0 | 98.0 | 100.00 |
| 14 | 20.07 | 21.09 | 20.27 | 20.48 |
| 28 | 11.53 | 11.08 | 11.65 | 11.42 |
| 42 | 7.69 | 8.0 | 8.08 | 7.92 |
| 56 | 6.19 | 6.13 | 5.89 | 6.07 |
| 70 | 4.87 | 4.83 | 5.07 | 4.92 |
| 84 | 4.23 | 4.06 | 4.14 | 4.14 |

**Mass remaining (percent of the initial mass; values slightly above 100 reflect weighing variability)**

| Day | Specimen 1 | Specimen 2 | Specimen 3 | Mean |
|---:|---:|---:|---:|---:|
| 0 | 99.0 | 100.3 | 100.7 | 100.0 |
| 14 | 100.7 | 100.3 | 99.0 | 100.0 |
| 28 | 99.7 | 99.3 | 101.0 | 100.0 |
| 42 | 100.7 | 99.3 | 100.0 | 100.0 |
| 56 | 101.0 | 99.7 | 99.3 | 100.0 |
| 70 | 97.1 | 98.7 | 97.4 | 97.7 |
| 84 | 74.1 | 73.2 | 74.4 | 73.9 |

**Modulus (MPa)**

| Day | Specimen 1 | Specimen 2 | Specimen 3 | Mean |
|---:|---:|---:|---:|---:|
| 0 | 1.98 | 1.96 | 2.06 | 2.000 |
| 14 | 1.542 | 1.481 | 1.512 | 1.512 |
| 28 | 1.177 | 1.131 | 1.12 | 1.143 |
| 42 | 0.846 | 0.889 | 0.855 | 0.863 |
| 56 | 0.659 | 0.633 | 0.666 | 0.653 |
| 70 | 0.478 | 0.498 | 0.503 | 0.493 |
| 84 | 0.38 | 0.376 | 0.362 | 0.373 |

## Work sequence

To use the software checks, open **Practice gradebook** and select **Virtual lab 1: degradation time course of a synthetic scaffold (ungraded practice)**. The points are practice feedback only.

1. **Summarize.** Count the specimens and average each measurement at each time point. Upload a table with columns `time_point`, `replicates`, `mn_kda`, `mass_pct` and `modulus_mpa` for d0, d14, d28, d56 and d84.
2. **Bonds cleaved.** From the day-0 and day-28 mean molar masses, compute the fraction of bonds cleaved with p = M_u (1/Mn − 1/Mn0), then the rate constant k = −ln(1 − p)/t.
3. **Modulus.** Fit an exponential decay through the day-0 and day-56 means, and compute the half-time and the day on which the modulus reaches 0.8 MPa.
4. **Mass.** Find the first sampled day on which the mean mass is below 95% of its starting value.
5. **Compare.** Put the three time courses side by side, and say which measurement predicts the period of mechanical support and what the experiment does not show.

## Worked calculation

The mean molar mass falls from 100.00 kDa at day 0 to 11.42 kDa at day 28, so p = 72 × (1/11420 − 1/100000) = 0.00558 (0.56% of bonds) and k = −ln(1 − 0.00558)/28 = 0.00020 per day. The mean modulus falls from 2.000 to 0.653 MPa, so k_E = ln(2.000/0.653)/56 = 0.0200 per day, the half-time is 34.7 days and the modulus reaches 0.8 MPa at 45.8 days. The mean mass is still 100.0% at day 56 and 97.7% at day 70, and first falls below 95% of its starting value at day 84 (73.9%). Chain length and modulus therefore change long before any mass is lost, and a period of support judged from the mass would be much too long. The data come from buffer; rates in tissue can differ.

## Analytic rubric for discussion

| Criterion | Evidence for full credit |
|---|---|
| Summary table | Reports the number of specimens and the mean of each measurement at each time point |
| Bonds cleaved | Converts molar masses correctly and obtains p and k |
| Modulus | Obtains the exponential rate, the half-time and the time to the threshold |
| Order of events | States that molar mass and modulus change before mass and why |
| Scope | Treats the result as a property of this synthetic scaffold in buffer, not of an implant or a tissue |

## Limits and provenance

This is an original exercise with constructed data and round parameters. Real degradation data are noisier, usually need more specimens per time point, and are affected by crystallinity, sample geometry, enzymes and flow. Original lab text and dataset: CC BY 4.0.
