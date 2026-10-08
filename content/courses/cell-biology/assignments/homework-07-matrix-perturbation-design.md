# Homework 7 practice: matrix stiffness, controls and perturbation design

**Status:** open formative practice; this packet and its answer specifications are public and are not suitable for a protected or summative exam. It does not contribute to a course grade.  
**Course package:** Foundations of Cell and Molecular Biology, version 0.19.0
**Suggested time:** 2–3 hours  
**Prerequisite lessons:** [Cytoskeletal systems, adhesion, and extracellular matrix](../modules/11a-cytoskeleton-adhesion-and-extracellular-matrix.md) and [Matrix mechanics and mechanotransduction](../modules/11b-matrix-mechanics-and-mechanotransduction.md).  
**Dataset:** [synthetic measurements](https://raw.githubusercontent.com/dylanstechmann/uniStemCourseSimulators/main/content/courses/cell-biology/assignments/homework-07-matrix-spreading.csv).

## Purpose

Cells spread more on stiffer gels in this constructed experiment. Stiffness is rarely the only thing that changes: ligand density, cell number, gel thickness and viability can differ too. This problem set asks which controls separate stiffness from those alternatives, what the spreading readout does and does not mean, and how to design the next perturbation.

The four rows per condition are independent coverslips from separate gel preparations. Many cells were measured on each coverslip; cells within a coverslip are not independent.

## Learning objectives

After working through the packet, learners should be able to:

1. Summarize coverslip-level data without treating cells as independent.
2. Compute and interpret a fold ratio.
3. Identify covariates that confound a stiffness comparison.
4. Choose controls that separate stiffness from ligand density, cell number and gel properties.
5. State what a spreading readout does not show about fate or force.

## Experimental scenario and data dictionary

Cells were plated on gels of three stiffnesses coated to the same nominal ligand density. After a fixed time, spread area per cell (mean of the cells on the coverslip), cell density and measured ligand density (relative to the soft gels) were recorded. All values are synthetic teaching data.

| Condition | Coverslip | Spread area (µm²) | Cell density (per mm²) | Ligand density (rel.) |
|---|---|---:|---:|---:|
| Soft (0.5 kPa) | S1 | 420 | 140 | 100 |
| Soft (0.5 kPa) | S2 | 450 | 150 | 98 |
| Soft (0.5 kPa) | S3 | 400 | 135 | 102 |
| Soft (0.5 kPa) | S4 | 430 | 145 | 100 |
| Medium (5 kPa) | M1 | 880 | 138 | 101 |
| Medium (5 kPa) | M2 | 900 | 142 | 99 |
| Medium (5 kPa) | M3 | 860 | 150 | 100 |
| Medium (5 kPa) | M4 | 920 | 146 | 100 |
| Stiff (50 kPa) | S1 | 1480 | 143 | 99 |
| Stiff (50 kPa) | S2 | 1500 | 139 | 101 |
| Stiff (50 kPa) | S3 | 1450 | 148 | 100 |
| Stiff (50 kPa) | S4 | 1530 | 150 | 100 |

## Work sequence

To use the software checks, open **Practice gradebook** and select **Homework 7: matrix stiffness, controls and perturbation design (open, ungraded practice)**. The interactive points are practice feedback only; they are not added to a course grade.

### Part A — Summarize the independent coverslips

Retain all four coverslip values. Calculate the mean spread area, mean cell density and mean relative ligand density and report a coverslip count of four. Upload one UTF-8 CSV with exactly this header and column order:

```csv
condition,batch_count,mean_spread_area_um2,mean_cell_density,mean_ligand_density
soft,4,425,142.5,100
medium,4,890,144,100
stiff,4,1490,145,100
```

The software scores the summary cells only.

### Part B — Plot spreading

Plot the mean spread area on the supplied axes (0 = soft, 1 = medium, 2 = stiff).

### Part C — Ratio and what it supports

Calculate the stiff-to-soft ratio of mean spread area and choose the best-supported conclusion.

### Part D — Design controls

Use the structured checks to choose controls that separate stiffness from ligand density, cell number and gel properties, and the multiple-select item to review mechanotransduction claims.

## Worked calculation

Worked calculation: Mean spread area is (420 + 450 + 400 + 430) / 4 = 425 µm² on soft, 890 µm² on medium and 1490 µm² on stiff gels. The stiff-to-soft ratio is 1490 / 425 = 3.51. Cell density (about 140 to 150 per mm²) and relative ligand density (about 100) are matched, so those two alternatives are reduced, but gel stiffness is a stand-in for several properties and the readout is one cell shape measure.

## Analytic instructor rubric

For instructor-led discussion, use 0–2 points for each criterion. Zero indicates absent or incompatible evidence; one indicates a partially correct response that omits a key assumption or control; two indicates the evidence described below. This guide is not connected to the software gradebook.

| Criterion | Evidence for full credit |
|---|---|
| Replication and summary | Retains four independent coverslips; cells within a coverslip are not independent. |
| Matched covariates | Uses ligand and cell density measurements to reduce those alternatives. |
| Design | Proposes ligand-density, thickness and cell-number controls and an independent stiffness measurement. |
| Scope | Does not claim stiffness alone determines fate; notes the single shape readout. |
| Follow-up | Proposes a perturbation of the force pathway with a readout beyond shape. |

The autograded public practice set covers a subset of these criteria with deterministic numeric, CSV, graph-coordinate, multiple-select and structured-choice rules. Its keys are open in this repository. Responses requiring a written explanation are not automatically scored.

## Limitations and provenance

Original paper exercise using constructed data. It is not a wet-lab protocol, an actual experimental result, or a clinical or therapeutic claim. The scenario follows the corresponding course lesson; no outside text, question, dataset or figure is reproduced or adapted. Original packet and synthetic dataset: CC BY 4.0. The public question specifications are for formative study and must not be treated as confidential exam materials.
