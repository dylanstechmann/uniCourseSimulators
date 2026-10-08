# Homework 4 practice: ChIP-qPCR percent input and matched reporters

**Status:** open formative practice; this packet and its answer specifications are public and are not suitable for a protected or summative exam. It does not contribute to a course grade.  
**Course package:** Foundations of Cell and Molecular Biology, version 0.19.0
**Suggested time:** 2–3 hours  
**Prerequisite lessons:** [Chromatin accessibility and regulatory DNA](../modules/07a-chromatin-accessibility-and-regulatory-dna.md) and [Transcription-factor occupancy and reporter evidence](../modules/07b-transcription-occupancy-and-reporter-evidence.md).  
**Dataset:** [synthetic measurements](https://raw.githubusercontent.com/dylanstechmann/uniStemCourseSimulators/main/content/courses/cell-biology/assignments/homework-04-chip-reporter.csv).

## Purpose

A transcription factor is reduced by knockdown, and the question is whether the regulatory element it is thought to occupy responds. This problem set separates three kinds of evidence: ChIP-qPCR enrichment, a matched reporter with and without the motif, and the controls that make each interpretable. Occupancy at a region and reporter activity are both consistent with, but do not prove, direct control of the endogenous gene.

The four rows per condition are independent cultures. Several qPCR wells were run for each culture; wells are technical replicates, not additional cultures.

## Learning objectives

After working through the packet, learners should be able to:

1. Summarize culture-level ChIP-qPCR and reporter data without treating qPCR wells as independent cultures.
2. Compute fold enrichment over IgG and distinguish it from percent input.
3. Assign each control its distinct role.
4. Interpret a matched motif-mutant reporter and state what it does not show.
5. State the limits of occupancy and reporter evidence for endogenous regulation.

## Experimental scenario and data dictionary

Control and factor-knockdown cultures were crosslinked and processed for chromatin immunoprecipitation with an antibody to the factor and a matched IgG. Enrichment at one candidate regulatory region is reported as simplified percent input. In parallel, independent transfections measured a wild-type reporter and a motif-mutant reporter as firefly/renilla ratios normalized to the promoter-only mean. All values are synthetic teaching data.

| Condition | Culture | Specific antibody (% input) | Matched IgG (% input) | Wild-type reporter (rel.) | Motif-mutant reporter (rel.) |
|---|---|---:|---:|---:|---:|
| Control | C1 | 6.0 | 0.4 | 3.1 | 1.2 |
| Control | C2 | 6.4 | 0.5 | 3.3 | 1.1 |
| Control | C3 | 5.8 | 0.4 | 2.9 | 1.3 |
| Control | C4 | 6.2 | 0.5 | 3.1 | 1.2 |
| Factor knockdown | K1 | 2.1 | 0.4 | 1.4 | 1.1 |
| Factor knockdown | K2 | 2.4 | 0.5 | 1.6 | 1.2 |
| Factor knockdown | K3 | 2.0 | 0.5 | 1.5 | 1.2 |
| Factor knockdown | K4 | 2.3 | 0.4 | 1.5 | 1.1 |

## Work sequence

To use the software checks, open **Practice gradebook** and select **Homework 4: ChIP-qPCR percent input and matched reporters (open, ungraded practice)**. The interactive points are practice feedback only; they are not added to a course grade.

### Part A — Summarize the independent cultures

Retain all four culture-level values. Calculate, for each condition, the mean specific-antibody percent input, mean IgG percent input, mean wild-type reporter and mean motif-mutant reporter, and report a culture count of four. Upload one UTF-8 CSV with exactly this header and column order:

```csv
condition,batch_count,mean_specific_pct_input,mean_igg_pct_input,mean_reporter_wt,mean_reporter_mut
control,4,6.1,0.45,3.1,1.2
knockdown,4,2.2,0.45,1.5,1.15
```

The software scores the summary cells only.

### Part B — Plot the specific-antibody mean

Plot the mean specific-antibody percent input on the supplied axes (0 = control, 1 = knockdown).

### Part C — Enrichment over IgG and what it means

Calculate fold enrichment over matched IgG in the control cultures (mean specific divided by mean IgG). Then choose the strongest supported conclusion. Percent input and fold over IgG answer different questions and must name their denominators.

### Part D — Controls

Use the structured checks to decide the role of input, IgG, a positive locus, a negative locus, the motif-mutant reporter and a no-template qPCR well.

## Worked calculation

Worked calculation: The control specific-antibody mean is (6.0 + 6.4 + 5.8 + 6.2) / 4 = 6.1% input and the matched IgG mean is 0.45% input, so enrichment over IgG is 6.1 / 0.45 = 13.56-fold. The knockdown mean falls to 2.2% input. The wild-type reporter falls from 3.1 to 1.5 after knockdown while the motif-mutant reporter stays near 1.2 and 1.15.

## Analytic instructor rubric

For instructor-led discussion, use 0–2 points for each criterion. Zero indicates absent or incompatible evidence; one indicates a partially correct response that omits a key assumption or control; two indicates the evidence described below. This guide is not connected to the software gradebook.

| Criterion | Evidence for full credit |
|---|---|
| Replication and summary | Retains four independent cultures; qPCR wells are not extra replicates. |
| Denominators | Names the denominator for percent input and for fold over IgG. |
| Controls | Assigns input, IgG, positive and negative loci, mutant reporter and no-template controls their distinct roles. |
| Causal scope | States that occupancy and a reporter response do not prove direct control of the endogenous gene. |
| Follow-up | Proposes an endogenous-locus perturbation and orthogonal evidence. |

The autograded public practice set covers a subset of these criteria with deterministic numeric, CSV, graph-coordinate, multiple-select and structured-choice rules. Its keys are open in this repository. Responses requiring a written explanation are not automatically scored.

## Limitations and provenance

Original paper exercise using constructed data. It is not a wet-lab protocol, an actual experimental result, or a clinical or therapeutic claim. The scenario follows the corresponding course lesson; no outside text, question, dataset or figure is reproduced or adapted. Original packet and synthetic dataset: CC BY 4.0. The public question specifications are for formative study and must not be treated as confidential exam materials.
