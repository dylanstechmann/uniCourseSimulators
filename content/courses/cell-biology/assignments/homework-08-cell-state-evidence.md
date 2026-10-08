# Homework 8 practice: quiescence, senescence and cell-state markers

**Status:** open formative practice; this packet and its answer specifications are public and are not suitable for a protected or summative exam. It does not contribute to a course grade.  
**Course package:** Foundations of Cell and Molecular Biology, version 0.19.0
**Suggested time:** 2–3 hours  
**Prerequisite lessons:** [Cell-cycle control, checkpoints, and mitosis](../modules/12a-cell-cycle-checkpoints-and-mitosis.md) and [Quiescence, senescence, apoptosis, and cell-fate evidence](../modules/12b-senescence-apoptosis-and-cell-fate.md).  
**Dataset:** [synthetic measurements](https://raw.githubusercontent.com/dylanstechmann/uniStemCourseSimulators/main/content/courses/cell-biology/assignments/homework-08-cell-state.csv).

## Purpose

Arrested cells can be quiescent, senescent or temporarily slowed. This problem set shows why one marker cannot assign a state, and what a reversibility test adds. A marker pattern is evidence about a cell state in a culture system; it is not a statement about function, potency or any therapy.

The four rows per condition are independent cultures; several fields were scored per culture.

## Learning objectives

After working through the packet, learners should be able to:

1. Summarize culture-level cell-state data without treating fields as independent cultures.
2. Explain why a single marker does not assign quiescence or senescence.
3. Use a reversibility test and state its limits.
4. Compute a signed percentage-point contrast.
5. Keep a marker pattern separate from claims about function or potency.

## Experimental scenario and data dictionary

Three kinds of cultures were prepared: proliferating cells, cells arrested by serum withdrawal, and cells arrested after a defined DNA-damage exposure. Each culture was scored for a DNA-synthesis label, a senescence-associated enzyme marker, and, after returning serum, a second DNA-synthesis label to test re-entry into the cell cycle. All values are synthetic teaching data.

| Condition | Culture | DNA-synthesis label (%) | Senescence-associated enzyme marker (%) | DNA-synthesis label after stimulation (%) |
|---|---|---:|---:|---:|
| Proliferating | P1 | 38 | 4 | 41 |
| Proliferating | P2 | 40 | 5 | 39 |
| Proliferating | P3 | 42 | 6 | 42 |
| Proliferating | P4 | 40 | 5 | 40 |
| Serum-withdrawn (quiescent) | Q1 | 4 | 8 | 33 |
| Serum-withdrawn (quiescent) | Q2 | 5 | 9 | 35 |
| Serum-withdrawn (quiescent) | Q3 | 6 | 10 | 34 |
| Serum-withdrawn (quiescent) | Q4 | 5 | 9 | 34 |
| Damage-induced arrest | D1 | 3 | 62 | 6 |
| Damage-induced arrest | D2 | 4 | 65 | 7 |
| Damage-induced arrest | D3 | 5 | 68 | 5 |
| Damage-induced arrest | D4 | 4 | 65 | 6 |

## Work sequence

To use the software checks, open **Practice gradebook** and select **Homework 8: quiescence, senescence and cell-state markers (open, ungraded practice)**. The interactive points are practice feedback only; they are not added to a course grade.

### Part A — Summarize the independent cultures

Retain all four culture values. Calculate the mean for the DNA-synthesis label, the enzyme marker and the after-stimulation label and report a culture count of four. Upload one UTF-8 CSV with exactly this header and column order:

```csv
condition,batch_count,mean_edu_pct,mean_sabgal_pct,mean_reentry_edu_pct
proliferating,4,40,5,40.5
quiescent,4,5,9,34
damage_induced,4,4,65,6
```

The software scores the summary cells only.

### Part B — Plot re-entry

Plot the mean after-stimulation DNA-synthesis label on the supplied axes (0 = proliferating, 1 = quiescent, 2 = damage-induced).

### Part C — Contrast and interpretation

Calculate the descriptive difference in re-entry, quiescent minus damage-induced, in percentage points, and choose the best-supported statement about what the markers together support.

### Part D — Evidence logic

Use the structured checks to decide what each marker and the reversibility test do and do not show.

## Worked calculation

Worked calculation: Both arrested states have a low DNA-synthesis label (5% and 4% against 40% in proliferating cells), so that marker alone does not separate them. The stress-associated enzyme marker is 9% in the serum-withdrawn cultures and 65% in the damage-induced cultures. After stimulation, re-entry averages 34% for the quiescent cultures and 6% for the damage-induced cultures, a 28 percentage-point difference.

## Analytic instructor rubric

For instructor-led discussion, use 0–2 points for each criterion. Zero indicates absent or incompatible evidence; one indicates a partially correct response that omits a key assumption or control; two indicates the evidence described below. This guide is not connected to the software gradebook.

| Criterion | Evidence for full credit |
|---|---|
| Replication and summary | Retains four independent cultures. |
| Multiple markers | Explains why no single marker assigns a state and uses the combination. |
| Reversibility | Uses re-entry after stimulation as a functional distinction and notes its limits (incomplete, time-dependent). |
| Scope | Does not equate a marker pattern with function, potency or a clinical outcome. |
| Follow-up | Proposes additional senescence markers and a longer re-entry time course. |

The autograded public practice set covers a subset of these criteria with deterministic numeric, CSV, graph-coordinate, multiple-select and structured-choice rules. Its keys are open in this repository. Responses requiring a written explanation are not automatically scored.

## Limitations and provenance

Original paper exercise using constructed data. It is not a wet-lab protocol, an actual experimental result, or a clinical or therapeutic claim. The scenario follows the corresponding course lesson; no outside text, question, dataset or figure is reproduced or adapted. Original packet and synthetic dataset: CC BY 4.0. The public question specifications are for formative study and must not be treated as confidential exam materials.
