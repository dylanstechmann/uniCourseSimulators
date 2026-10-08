# Virtual lab 1: pseudoreplication and nested designs

**Activity type:** synthetic-data analysis with public, ungraded formative checks
**Course package:** Probability, Biostatistics & Experimental Design. **Estimated learner time:** 2–3 hours
**Data status:** all measurements are constructed for instruction. They describe no real animals, assay or treatment, and nothing here is evidence about any compound or any organism.
**Dataset:** [synthetic nested readings (CSV)](https://raw.githubusercontent.com/dylanstechmann/uniStemCourseSimulators/main/content/courses/statistics/labs/nested-biomarker-readings.csv).

## Experimental question

A biomarker is measured in arbitrary units (au) in samples from 4 animals in a **control** group and 4 animals in a **treated** group. Each animal's sample is read 3 times, so the table has 24 readings from 8 animals. The question is whether the groups differ, and the lab compares the analysis that counts every reading with the analysis that counts every animal.

## Learning objectives

1. Summarize nested readings to one value per animal and identify the number of independent units in each group.
2. Estimate the technical variance, the between-animal variance and the intraclass correlation from nested readings.
3. Compare an analysis that treats readings as independent with an animal-level analysis, and state what the design supports.

## Data dictionary

| Column | Meaning |
|---|---|
| group | control or treated |
| animal_id | c1 to c4 (control) and t1 to t4 (treated), one per animal |
| reading | 1 to 3, a repeated reading of the same animal's sample |
| value_au | biomarker value in arbitrary units |

## The synthetic data

**Control**

| Animal | Reading 1 | Reading 2 | Reading 3 | Mean |
|---|---:|---:|---:|---:|
| c1 | 52.4 | 48.8 | 48.8 | 50.0 |
| c2 | 56.2 | 58.6 | 59.2 | 58.0 |
| c3 | 44.9 | 45.5 | 41.6 | 44.0 |
| c4 | 51.4 | 50.2 | 54.4 | 52.0 |

**Treated**

| Animal | Reading 1 | Reading 2 | Reading 3 | Mean |
|---|---:|---:|---:|---:|
| t1 | 58.5 | 56.1 | 56.4 | 57.0 |
| t2 | 63.9 | 67.2 | 66.9 | 66.0 |
| t3 | 52.3 | 53.8 | 49.9 | 52.0 |
| t4 | 59.5 | 61.3 | 62.2 | 61.0 |

## Work sequence

To use the software checks, open **Practice gradebook** and select **Virtual lab 1: pseudoreplication and nested designs (ungraded practice)**. The points are practice feedback only.

1. **Summarize.** Count the readings and average them for each animal. Upload a table with columns `animal_id`, `readings` and `mean_value`.
2. **Estimate the technical variation.** For each animal compute the sum of squared deviations of its three readings from their own mean; pool them over the eight animals.
3. **Run the reading-level test.** Treat the 12 readings per group as independent and compute the pooled-variance t statistic.
4. **Run the animal-level test.** Compute the same statistic from the four animal means in each group.
5. **Estimate the intraclass correlation** and the design effect, and explain why the two tests disagree.
6. **State what the design supports.** Decide what can be concluded from four animals per group, and what a better design would change.

## Worked calculation

The group means are 51.0 and 59.0, a difference of 8.0 au. At the reading level the pooled SD is 5.52, so SE = 5.52 × √(2/12) = 2.26, t = 3.55 on 22 degrees of freedom and p = 0.0018. At the animal level the pooled SD of the animal means is 5.86, so SE = 5.86 × √(2/4) = 4.14, t = 1.93 on 6 degrees of freedom, p = 0.102, and the 95% interval for the difference is −2.1 to 18.1 au. The animal-level standard error is 1.84 times the reading-level one. The within-animal sum of squares is 53.46 on 16 degrees of freedom, a technical variance of 3.341 (SD 1.83); MS(animals) = 3 × 34.33 = 103.0, σ_b² = (103.0 − 3.341)/3 = 33.22, and the intraclass correlation is 0.909. The design effect is 1 + 2 × 0.909 = 2.82, so 12 readings per group carry about the information of 4.3, close to the 4 animals. For this balanced design the F test for groups in a nested analysis of variance (group mean square over the animals-within-group mean square, 384/103 = 3.73) equals the square of the animal-level t statistic (1.93² = 3.73). The honest summary is a difference of 8.0 au with a wide interval that includes zero, from too few animals.

## Analytic rubric for discussion

| Criterion | Evidence for full credit |
|---|---|
| Summary table | Reports the number of readings and the mean for each animal |
| Variance components | Estimates the technical SD and the intraclass correlation from the nested data |
| Two analyses | Computes the reading-level and animal-level t statistics and explains why they differ |
| Conclusion | States that four animals per group cannot settle the question and reports an interval |
| Design | Recommends more animals, with a primary outcome and analysis fixed in advance, over more readings |

## Limits and provenance

This is an original exercise with constructed numbers, equal group sizes and a balanced layout. Real experiments have unequal numbers, batch effects and missing readings, for which mixed models are the usual tool. Original lab text and dataset: CC BY 4.0.
