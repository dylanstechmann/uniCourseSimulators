# Homework 5 practice: mRNA, protein synthesis and turnover

**Status:** open formative practice; this packet and its answer specifications are public and are not suitable for a protected or summative exam. It does not contribute to a course grade.  
**Course package:** Foundations of Cell and Molecular Biology, version 0.19.0
**Suggested time:** 2–3 hours  
**Prerequisite lessons:** [RNA processing and isoform evidence](../modules/08a-rna-processing-and-isoform-evidence.md) and [Translation and protein turnover](../modules/08b-translation-and-protein-turnover.md).  
**Dataset:** [synthetic measurements](https://raw.githubusercontent.com/dylanstechmann/uniStemCourseSimulators/main/content/courses/cell-biology/assignments/homework-05-rna-protein.csv).

## Purpose

A sequence variant lowers the steady-state level of a protein while the mRNA level looks unchanged. This problem set asks which layer of gene expression the data point to: transcript abundance, synthesis rate, or turnover. Steady-state protein is the product of synthesis and degradation, so a protein level alone cannot say which changed.

The four rows per condition are independent cultures; several assay replicates were run for each.

## Learning objectives

After working through the packet, learners should be able to:

1. Summarize culture-level expression data across layers without treating assay replicates as independent cultures.
2. Compute a first-order half-life with units.
3. Distinguish mRNA abundance, synthesis rate and turnover.
4. Interpret matched measurements and state what remains undetermined.
5. Design a follow-up that separates candidate mechanisms.

## Experimental scenario and data dictionary

A wild-type line and a line carrying a variant in the transcript's untranslated region are compared. mRNA and protein are reported relative to the wild-type mean. Nascent-protein labeling is a short-pulse incorporation signal for the protein of interest (relative to wild type). Protein remaining 4 h after a translation block is the percentage of the starting protein that persists. All values are synthetic teaching data.

| Condition | Culture | mRNA (rel.) | Protein (rel.) | Nascent-protein labeling (rel.) | Protein remaining 4 h after synthesis block (%) |
|---|---|---:|---:|---:|---:|
| Wild type | W1 | 100 | 100 | 100 | 50 |
| Wild type | W2 | 98 | 101 | 97 | 52 |
| Wild type | W3 | 103 | 99 | 103 | 49 |
| Wild type | W4 | 99 | 100 | 100 | 49 |
| Variant | V1 | 99 | 52 | 51 | 49 |
| Variant | V2 | 102 | 48 | 49 | 51 |
| Variant | V3 | 98 | 50 | 50 | 50 |
| Variant | V4 | 101 | 50 | 50 | 50 |

## Work sequence

To use the software checks, open **Practice gradebook** and select **Homework 5: mRNA, protein synthesis and turnover (open, ungraded practice)**. The interactive points are practice feedback only; they are not added to a course grade.

### Part A — Summarize the independent cultures

Retain all four culture values. Calculate the mean for mRNA, protein, nascent labeling and protein remaining at 4 h, and report a culture count of four. Upload one UTF-8 CSV with exactly this header and column order:

```csv
condition,batch_count,mean_mrna,mean_protein,mean_labeling,mean_remaining_4h
wt,4,100,100,100,50
variant,4,100,50,50,50
```

The software scores the summary cells only.

### Part B — Plot protein

Plot the mean relative protein level on the supplied axes (0 = wild type, 1 = variant).

### Part C — Half-life and interpretation

Assuming first-order decay after the synthesis block, calculate the protein half-life in hours from the wild-type fraction remaining at 4 h (use the wild-type mean). Then choose the interpretation best supported by the mRNA, labeling and decay measurements together.

### Part D — Layer logic

Use the structured checks to decide which measurement addresses which layer, and the multiple-select item to review what each layer's measurement does not show.

## Worked calculation

Worked calculation: Both lines have a mean mRNA level of 100. The variant protein level averages (52 + 48 + 50 + 50) / 4 = 50 against 100, and its nascent-protein labeling averages 50 against 100. The fraction remaining after a 4 h synthesis block is 50% in both lines, so with first-order decay the half-life is 4 h in both; the lower protein is more consistent with reduced synthesis than with faster turnover.

## Analytic instructor rubric

For instructor-led discussion, use 0–2 points for each criterion. Zero indicates absent or incompatible evidence; one indicates a partially correct response that omits a key assumption or control; two indicates the evidence described below. This guide is not connected to the software gradebook.

| Criterion | Evidence for full credit |
|---|---|
| Replication and summary | Retains four independent cultures. |
| Layer separation | Separates mRNA abundance, synthesis and turnover and does not infer one from another. |
| Quantification | Computes the half-life with units from first-order decay and states the assumption. |
| Interpretation | Concludes the data favor reduced synthesis over faster degradation in this constructed example, with limits. |
| Follow-up | Proposes an experiment that separates initiation, elongation and localization effects. |

The autograded public practice set covers a subset of these criteria with deterministic numeric, CSV, graph-coordinate, multiple-select and structured-choice rules. Its keys are open in this repository. Responses requiring a written explanation are not automatically scored.

## Limitations and provenance

Original paper exercise using constructed data. It is not a wet-lab protocol, an actual experimental result, or a clinical or therapeutic claim. The scenario follows the corresponding course lesson; no outside text, question, dataset or figure is reproduced or adapted. Original packet and synthetic dataset: CC BY 4.0. The public question specifications are for formative study and must not be treated as confidential exam materials.
