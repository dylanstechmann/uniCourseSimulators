# Homework 3 practice: replication, repair and lesion-removal evidence

**Status:** open formative practice; this packet and its answer specifications are public and are not suitable for a protected or summative exam. It does not contribute to a course grade.  
**Course package:** Foundations of Cell and Molecular Biology, version 0.19.0
**Suggested time:** 2–3 hours  
**Prerequisite lessons:** [DNA structure, genome organization, and semiconservative replication](../modules/06a-dna-structure-and-replication.md) and [DNA damage, repair pathways, and evidence of lesion removal](../modules/06b-dna-damage-and-repair-evidence.md).  
**Dataset:** [synthetic measurements](https://raw.githubusercontent.com/dylanstechmann/uniStemCourseSimulators/main/content/courses/cell-biology/assignments/homework-03-lesion-removal.csv).

## Purpose

Cells with a defective repair factor retain more of a lesion-specific signal after damage. This problem set asks whether that retention reflects slower lesion removal or something else: lesion signal can fall because DNA replication dilutes it per genome, because cells die, or because the assay recovers material unequally. A large mean difference is one part of the evidence; it does not by itself identify a repair pathway or a mutation rate.

The four rows per condition are independent cultures. Several microscopy fields were scored from each culture. The replicate unit is the culture.

## Learning objectives

After working through the packet, learners should be able to:

1. Summarize replicate-level lesion-removal data without treating microscopy fields as independent cultures.
2. Compute a signed percentage-point contrast and avoid calling it a relative change.
3. Use replication, viability and complementation controls to evaluate alternative explanations for retained lesion signal.
4. State why lesion removal, DNA synthesis, cell survival and mutation frequency are different outcomes.
5. Apply semiconservative replication and strand polarity to a simple density-labeling prediction.

## Experimental scenario and data dictionary

Three isogenic lines are compared: wild type, a line lacking one repair factor, and the same line with the factor restored (complemented). A synthetic lesion-specific signal was measured immediately after a brief damage exposure (0 h) and again 4 h later, and is reported as the percentage of the 0 h signal that remains. The fraction of cells in S phase (an independent DNA-synthesis label) and viability were measured in the same cultures. All values are synthetic teaching data and have no biological or clinical source.

| Condition | Culture | Lesion signal remaining at 4 h (% of 0 h) | S-phase cells (%) | Viability (%) |
|---|---|---:|---:|---:|
| Wild type | W1 | 38 | 31 | 95 |
| Wild type | W2 | 42 | 29 | 94 |
| Wild type | W3 | 40 | 30 | 96 |
| Wild type | W4 | 40 | 30 | 95 |
| Repair-deficient | R1 | 83 | 30 | 93 |
| Repair-deficient | R2 | 86 | 32 | 94 |
| Repair-deficient | R3 | 84 | 29 | 92 |
| Repair-deficient | R4 | 87 | 31 | 94 |
| Complemented | C1 | 45 | 30 | 95 |
| Complemented | C2 | 48 | 31 | 96 |
| Complemented | C3 | 46 | 29 | 94 |
| Complemented | C4 | 47 | 30 | 95 |

## Work sequence

To use the software checks, open **Practice gradebook** and select **Homework 3: replication, repair and lesion-removal evidence (open, ungraded practice)**. The interactive points are practice feedback only; they are not added to a course grade.

### Part A — Route and mechanism

Review the lesson on lesion classes and repair routes. In the multiple-select item choose the statements that correctly describe semiconservative replication and strand polarity; the item is about the replication model, not about repair.

### Part B — Summarize the independent cultures

Retain all four culture-level values per condition. Calculate the mean percentage of lesion signal remaining at 4 h and the mean S-phase percentage; report a culture count of four. Upload one UTF-8 CSV with exactly this header and column order:

```csv
condition,batch_count,mean_lesion_remaining_pct,mean_s_phase_pct
wt,4,40,30
repair_deficient,4,85,30.5
complemented,4,46.5,30
```

The displayed rows show the format only; calculate your own values from the linked file. The software scores the summary cells only.

### Part C — Quantify and bound the contrast

Calculate the descriptive difference `repair-deficient − wild type` in percentage points for lesion signal remaining. Use a signed value. Do not call it a relative change, a p-value, or proof of a specific repair pathway. Then use the structured checks to decide which control addresses each alternative explanation.

## Worked calculation

Worked calculation: The wild-type lesion signal remaining at 4 h averages (38 + 42 + 40 + 40) / 4 = 40%, and the repair-deficient line averages 85%. The difference is 45 percentage points. S-phase fractions are about 30% in all three lines, so unequal replication-dilution of the signal is a less likely explanation.

## Analytic instructor rubric

For instructor-led discussion, use 0–2 points for each criterion. Zero indicates absent or incompatible evidence; one indicates a partially correct response that omits a key assumption or control; two indicates the evidence described below. This guide is not connected to the software gradebook.

| Criterion | Evidence for full credit |
|---|---|
| Replication and summary | Retains four independent cultures and does not treat fields as extra replicates. |
| Alternative explanations | Uses S-phase fraction, viability and the complemented line to reduce replication dilution, cell death and line-specific artifacts, with their limits. |
| Outcome definitions | Keeps lesion removal, DNA synthesis, survival and mutation frequency as different outcomes. |
| Replication model | States strand polarity and semiconservative inheritance correctly. |
| Scope | Limits the conclusion to this constructed comparison and names a follow-up that measures lesion removal directly across a time course. |

The autograded public practice set covers a subset of these criteria with deterministic numeric, CSV, graph-coordinate, multiple-select and structured-choice rules. Its keys are open in this repository. Responses requiring a written explanation are not automatically scored.

## Limitations and provenance

Original paper exercise using constructed data. It is not a wet-lab protocol, an actual experimental result, or a clinical or therapeutic claim. The scenario follows the corresponding course lesson; no outside text, question, dataset or figure is reproduced or adapted. Original packet and synthetic dataset: CC BY 4.0. The public question specifications are for formative study and must not be treated as confidential exam materials.
