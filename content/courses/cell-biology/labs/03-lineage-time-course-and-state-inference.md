# Virtual lab 3: lineage-marker time course and state inference

**Activity type:** synthetic-data analysis with public, ungraded formative checks  
**Course package:** Foundations of Cell and Molecular Biology, version 0.19.0. **Estimated learner time:** 2–3 hours  
**Data status:** all 160 observations are constructed for instruction; no laboratory measurements or biological samples are represented.

## Experimental question

A population of undifferentiated cells is cultured with or without a differentiation-inducing factor. Over eight days the fraction of cells positive for a lineage marker rises and a pluripotency-associated marker falls. What can these marker fractions show, and what do they leave open? The activity separates three questions that are often collapsed: how the marker fractions changed over time, whether a fraction change reflects conversion of cells or a change in which cells survive and divide, and whether a marker pattern says anything about defined function or potency.

## Learning objectives

By completing the activity, learners should be able to:

1. Calculate culture-level summaries at a named day and graph the time-ordered mean without treating fields or time points as independent cultures.
2. Compare a fraction with an absolute count by combining marker fraction and cell number.
3. Distinguish conversion from selective survival or growth as explanations for a changed fraction, and name the data that would separate them.
4. State why lineage and pluripotency-associated marker patterns are not demonstrations of potency or function.

These objectives map to the week-14 developmental-potency objectives and the course outcomes on information flow and experimental reasoning. The interactive set returns deterministic practice feedback on fixed numeric, table, graph and structured-choice rules; it does not score written explanations.

## Design and replicate structure

The linked [synthetic CSV](lineage-timecourse.csv) has two conditions (control medium and factor), five days (0, 2, 4, 6, 8) and four independent cultures (P01–P04) per condition and day, each a separate well started from a separate vial. Each row is one culture's marker percentages, cell number per well and viability. A destructive readout means different cultures are collected at different days; the P-labels distinguish independent cultures within a day, not the same culture followed over time.

The day-8 rows are shown below.

| Condition (day 8) | Culture | Lineage marker (%) | Pluripotency-associated marker (%) | Cells per well (thousands) | Viability (%) |
|---|---|---:|---:|---:|---:|
| Control | P01 | 7 | 64 | 450 | 94 |
| Control | P02 | 8 | 66 | 458 | 95 |
| Control | P03 | 7 | 63 | 444 | 95 |
| Control | P04 | 8 | 65 | 452 | 94 |
| Factor | P01 | 58 | 18 | 240 | 89 |
| Factor | P02 | 60 | 20 | 246 | 90 |
| Factor | P03 | 57 | 17 | 236 | 88 |
| Factor | P04 | 59 | 19 | 242 | 89 |

## Work sequence

To use the software checks, open **Practice gradebook** and select **Virtual lab 3: lineage-marker time course and state inference (ungraded practice)**. The points are practice feedback only and are not added to a course grade.

### Part A — Summarize day 8

For each condition, use the four day-8 cultures. Calculate the mean lineage-marker percentage, the mean pluripotency-associated marker percentage and the mean cells per well (thousands), and report a culture count of four. Upload one UTF-8 CSV with exactly this header and column order:

```csv
condition,batch_count,mean_lineage_pct,mean_pluripotency_pct,mean_cells_thousands
control,4,7.5,64.5,451
factor,4,58.5,18.5,241
```

The software scores the summary cells only.

### Part B — Plot the lineage-marker trajectory

Plot the mean lineage-marker percentage for the factor condition at days 0, 4 and 8 on the supplied axes. Use the four culture values per day from the linked file.

### Part C — Contrast and counts

Calculate factor minus control in lineage-marker percentage points at day 8. Then decide what that fraction does and does not show given that cell number per well differs.

### Part D — Interpretation

Use the structured checks to decide which data or controls separate conversion from selective survival, and what a marker pattern leaves unestablished about function.

## Worked calculation

At day 8 the factor condition averages (58 + 60 + 57 + 59) / 4 = 58.5% lineage-marker-positive cells against 7.5% in control, a 51 percentage-point difference. Cells per well average 241 thousand with the factor and 451 thousand in control, so the factor condition has fewer cells: a rise in the marker fraction can reflect conversion of cells, selective loss or slower growth of marker-negative cells, or a mix. The marker-positive cells per well are about 141 thousand (0.585 × 241) with the factor against about 34 thousand (0.075 × 451) in control, so the marker-positive count also rises, which a fraction alone cannot show.

## Limitations and provenance

Original paper exercise using constructed data. It is not a wet-lab protocol, an actual experimental result, or a clinical or therapeutic claim. The scenario follows the course lessons on developmental potency and integrative study design; no outside text, question, dataset or figure is reproduced or adapted. The marker names are intentionally generic. Original packet and synthetic dataset: CC BY 4.0. The public question specifications are for formative study and must not be treated as confidential exam materials.
