# Virtual lab 1: stiffness, ligand density and the unit of analysis

**Activity type:** synthetic-data analysis with public, ungraded formative checks
**Course package:** Cellular Biomechanics & Mechanobiology. **Estimated learner time:** 2–3 hours
**Data status:** all measurements are constructed for instruction. They describe no real gel, cell or marker, and nothing here is evidence about any cell type or material.
**Dataset:** [synthetic marker expression (CSV)](https://raw.githubusercontent.com/dylanstechmann/uniStemCourseSimulators/main/content/courses/cellular-biomechanics/labs/stiffness-ligand-marker-expression.csv).

## Experimental question

Hydrogels of three stiffnesses (1, 10 and 100 kPa) are each made with a low and a high density of an adhesive ligand, so that stiffness and ligand density are varied independently. Three gels are made for each of the six conditions, and 10 cells are imaged on each gel, giving 180 cell-level values of a differentiation marker (arbitrary units). The lab asks for the main effects of stiffness and ligand density, whether they interact, how uncertain the estimates are when the gel is taken as the unit, and what the design cannot show.

## Learning objectives

1. Summarize cell-level values to gel means for each condition of a crossed design.
2. Estimate the main effects and the interaction of stiffness and ligand density from the condition means.
3. Compare gel-level and cell-level standard errors and state what the design supports.

## Data dictionary

| Column | Meaning |
|---|---|
| condition | stiffness and ligand level: s1_low, s1_high, s10_low, s10_high, s100_low, s100_high |
| gel | 1 to 3, an independently made gel within the condition |
| cell | 1 to 10, a cell imaged on that gel |
| marker_au | marker intensity of the cell, arbitrary units |

## The synthetic data (gel means)

The mean of the 10 cells on each gel, computed from the CSV, is:

| Condition | Gel 1 | Gel 2 | Gel 3 | Mean of gels |
|---|---:|---:|---:|---:|
| 1 kPa, low ligand | 16.0 | 22.0 | 28.0 | 22.0 |
| 1 kPa, high ligand | 28.0 | 34.0 | 22.0 | 28.0 |
| 10 kPa, low ligand | 42.0 | 30.0 | 36.0 | 36.0 |
| 10 kPa, high ligand | 44.0 | 50.0 | 56.0 | 50.0 |
| 100 kPa, low ligand | 42.0 | 48.0 | 36.0 | 42.0 |
| 100 kPa, high ligand | 74.0 | 62.0 | 68.0 | 68.0 |

## Work sequence

To use the software checks, open **Practice gradebook** and select **Virtual lab 1: stiffness, ligand density and the unit of analysis (ungraded practice)**. The points are practice feedback only.

1. **Summarize.** Average the cells within each gel, then the three gel means within each condition. Upload a table with columns `condition`, `gels`, `cells` and `mean_of_gels`.
2. **Main effect of stiffness.** Average the low- and high-ligand means at each stiffness and subtract the 1 kPa value from the 100 kPa value.
3. **Ligand effect and interaction.** Compute the ligand effect at 1 and at 100 kPa and half their difference.
4. **Uncertainty.** Compute the standard error of the ligand effect at 100 kPa from the gel means, then the (wrong) standard error from the 30 cells per arm, and compare them.
5. **Interpret.** State what the interaction means, what the design supports and which properties of the gels were not controlled or measured here.

## Worked calculation

The condition means are 22, 28, 36, 50, 42, 68 (in the order of the table). The main effect of stiffness is (42 + 68)/2 − (22 + 28)/2 = 30. The ligand effect is 26 at 100 kPa and 6 at 1 kPa, so the interaction is (26 − 6)/2 = 10: stiffness matters more when the ligand density is high. At 100 kPa the pooled SD of the gel means is 6.0, so the standard error of the ligand effect is 6.0 × √(2/3) = 4.90 and t = 5.3 on 4 degrees of freedom. Treating the 30 cells per arm as independent, with a pooled cell-level SD of 9.0, would give 2.32, about 2.1 times smaller. The design separates stiffness from ligand density, but it says nothing about the viscoelasticity or ligand mobility of the gels, and three gels per condition leave wide uncertainty.

## Analytic rubric for discussion

| Criterion | Evidence for full credit |
|---|---|
| Summary table | Averages cells within gels first and reports the number of gels and cells for each condition |
| Effects | Computes the main effect of stiffness, the ligand effect and the interaction correctly |
| Uncertainty | Computes the gel-level standard error and explains why cells are not independent |
| Interpretation | Reads the interaction as non-additive and avoids attributing the response to stiffness alone |
| Limits | States that viscoelasticity, ligand mobility and the viability of the assay were not controlled here |

## Limits and provenance

This is an original exercise with constructed data and round numbers. Real marker data are noisier, are often skewed, and need a model that includes the gel as a random effect. Original lab text and dataset: CC BY 4.0.
