# Homework 1 practice: trafficking, localization, and fractionation evidence

**Status:** open formative practice; this packet and its answer specifications are public and are not suitable for a protected or summative exam. It does not contribute to a course grade.  
**Course package:** Foundations of Cell and Molecular Biology, version 0.19.0
**Suggested time:** 2–3 hours  
**Prerequisite lessons:** [Organelle compartments and protein targeting](../modules/03a-organelle-compartments-and-protein-targeting.md) and [Protein sorting and vesicle traffic](../modules/03b-protein-sorting-and-vesicle-traffic.md).  
**Dataset:** [synthetic M6P-receptor sorting results](https://raw.githubusercontent.com/dylanstechmann/uniStemCourseSimulators/main/content/courses/cell-biology/assignments/homework-01-m6p-sorting.csv).

## Purpose

This problem set asks whether a change in a receptor's cytosolic tail is consistent with altered post-binding cargo sorting. It combines trafficking topology, quantitative summaries, an accessible fixed-axis plot, assay controls, biological replication, and limits on causal interpretation. A correct mean is one part of the evidence; it does not by itself identify a molecular mechanism.

The four rows per condition are independent culture preparations. Several measurements were made from each preparation. The replicate unit is the culture preparation, not each measurement column, fraction, or detector reading.

## Learning objectives

After working through the packet, learners should be able to:

1. Trace a soluble M6P-bearing hydrolase and its receptor through the trans-Golgi network and endosome while keeping cargo and receptor destinations distinct.
2. Summarize replicate-level cargo-distribution measurements without treating fractions or technical measurements as independent experiments.
3. Use ligand binding, receptor abundance, lysosome-marker recovery, and viability measurements to evaluate alternative explanations for a sorting pattern.
4. State what a repaired clone adds to the evidence and what it does not establish about direct adaptor binding, universal trafficking, or lysosomal function.
5. Propose a follow-up measurement that separates delivery, secretion, degradation, and fraction recovery.

## Experimental scenario and data dictionary

Three isogenic cell lines are compared: a wild-type M6P receptor, a substitution in a cytosolic-tail sorting motif, and a scarlessly repaired clone in which that motif is restored. Each line was independently propagated in four culture preparations. Cells received a short pulse label of newly synthesized cathepsin D, followed by a 90-minute chase. The table records the percentage of the initial labeled cargo recovered in the lysosome-enriched fraction and in conditioned medium. The two percentages are separate measured destinations; they are not expected to sum to 100 because other cell-associated material, degradation, and incomplete recovery are not displayed.

M6P ligand binding was measured in a matched assay and normalized to the wild-type mean. Receptor abundance was measured in whole-cell input relative to a total-protein stain. Lysosome-marker recovery reports recovery of a reference lysosomal marker through fractionation; it is a process control, not proof that the fraction is pure. Viability is reported for the corresponding culture preparation. All measurements are synthetic teaching data and have no biological or clinical source.

| Condition | Culture preparation | M6P binding index | Receptor abundance index | Labeled cargo in lysosome fraction (% of pulse) | Labeled cargo in medium (% of pulse) | Lysosome-marker recovery (%) | Viability (%) |
|---|---|---:|---:|---:|---:|---:|---:|
| Wild type | W1 | 100 | 98 | 66 | 20 | 90 | 95 |
| Wild type | W2 | 98 | 102 | 70 | 22 | 92 | 95 |
| Wild type | W3 | 102 | 100 | 68 | 21 | 89 | 94 |
| Wild type | W4 | 101 | 101 | 67 | 20 | 91 | 96 |
| Tail mutant | M1 | 98 | 100 | 40 | 45 | 89 | 94 |
| Tail mutant | M2 | 101 | 97 | 44 | 48 | 91 | 93 |
| Tail mutant | M3 | 99 | 101 | 42 | 46 | 90 | 95 |
| Tail mutant | M4 | 100 | 100 | 43 | 44 | 88 | 94 |
| Motif repaired | R1 | 100 | 101 | 60 | 27 | 91 | 94 |
| Motif repaired | R2 | 99 | 102 | 64 | 25 | 92 | 95 |
| Motif repaired | R3 | 103 | 99 | 63 | 26 | 90 | 96 |
| Motif repaired | R4 | 101 | 100 | 63 | 27 | 91 | 94 |

The numbers are purposefully constructed to create a sizeable descriptive change while keeping the measured binding, receptor-abundance, fraction-recovery, and viability indices in similar ranges. This pattern is a teaching example, not an estimate of a real effect size.

## Work sequence

To use the software checks, open **Practice gradebook** and select **Homework 1: trafficking and localization evidence (open, ungraded practice)**. The interactive points are practice feedback only; they are not added to a course grade.

### Part A — Route and topology

Review the M6P and receptor-recycling account in the protein-sorting lesson. In the interactive set, select the statements that correctly connect cargo recognition, cytosolic-tail sorting, endosomal release, and the different later destinations of receptor and hydrolase. Keep lumenal cargo inside the vesicle lumen: vesicle transport between endomembrane compartments does not require soluble cargo to cross a lipid bilayer.

### Part B — Summarize the independent preparations

For each condition, retain all four culture-level values. Calculate the arithmetic mean lysosomal-delivery percentage and the mean conditioned-medium percentage; also report a preparation count of four. Upload one UTF-8 CSV with exactly this header and column order:

```csv
condition,batch_count,mean_lysosomal_delivery_pct,mean_conditioned_medium_pct
wt,4,67.75,20.75
tail_mutant,4,42.25,45.75
motif_repaired,4,62.5,26.25
```

The displayed rows show the required format and rounding; make your own calculations from the linked data file before submitting. The software scores these summary cells only. It does not assess the analysis code or infer whether a learner understood the experiment.

### Part C — Plot a measured outcome

Plot the mean lysosomal-delivery percentage using the supplied axes. The x-axis codes are fixed: 0 = wild type, 1 = tail mutant, and 2 = motif repaired. Plot the four-preparation mean for each group. The underlying replicate values remain available in the prompt and CSV; the three plotted means do not show variability or uncertainty.

### Part D — Quantify and bound the contrast

Calculate the descriptive difference `tail mutant − wild type` in percentage points for lysosomal delivery. Use a signed value so the direction is explicit. Do not call this a relative percent decrease, a p-value, a population estimate, or proof of a specific molecular step. Then use the structured checks to evaluate what the binding, abundance, recovery, viability, and repaired-clone observations do and do not help rule out.

### Part E — Design the next discriminating experiment

Before writing a conclusion, consider at least two alternatives: a changed endpoint can reflect altered biosynthesis, receptor abundance, cargo degradation, or fraction recovery as well as transport. A stronger study could collect a time course of pulse-labeled cargo in cell-associated, lysosome-enriched, and medium fractions; quantify total labeled cargo and receptor abundance at each time; verify fraction identity and recovery with multiple compartment markers; and preserve independent cultures as the biological unit. A second localization method can support a compartment claim, but colocalization alone does not prove direct binding or function.

The interactive control-design item evaluates selected evidence criteria. It does not grade an open-ended experimental plan or claim to assess the learner's prose.

## Worked calculation

The wild-type lysosome-enriched values average to `(66 + 70 + 68 + 67) / 4 = 67.75%`. The mutant-minus-wild-type descriptive contrast is `42.25% − 67.75% = −25.50 percentage points`. This is an absolute difference between displayed percentages. The relative percent change would use the wild-type mean as a denominator and answers a different question. Neither calculation estimates uncertainty.

## Analytic instructor rubric

For instructor-led discussion, use 0–2 points for each criterion. Zero indicates absent or incompatible evidence; one indicates a partially correct response that omits a key assumption or control; two indicates the evidence described below. This guide is not connected to the software gradebook.

| Criterion | Evidence for full credit |
|---|---|
| Replication and summary | Retains four independent culture preparations and reports all three group means without treating the assay columns as extra replicates. |
| Route and topology | Separates M6P cargo recognition from the receptor-tail sorting role and keeps lumenal cargo distinct from the cytosolic receptor tail. |
| Alternative explanations | Uses the matched binding, receptor-abundance, lysosome-recovery, and viability measures while recognizing their limits. |
| Rescue and causal scope | Notes that the repaired clone moves toward the wild-type pattern, while limiting the conclusion to this constructed comparison and not a direct adaptor mechanism. |
| Follow-up design | Proposes time-resolved cargo accounting, fraction identity/recovery checks, and an independent replicate unit. |

The autograded public practice set covers a subset of these criteria with deterministic numeric, CSV, graph-coordinate, multiple-select, and structured-choice rules. Its keys are open in this repository. Responses requiring a written explanation are not automatically scored.

## Limitations and provenance

This is an original paper exercise using constructed data. It is not a wet-lab protocol, actual experimental result, or clinical/therapeutic claim. The scenario is informed at the topic level by the cell-trafficking section of [MIT OCW 7.016 Lecture 19](https://ocw.mit.edu/courses/7-016-introductory-biology-fall-2018/resources/lecture-19-cell-trafficking-and-protein-localization/) and linked primary work by [Johnson and Kornfeld (1992)](https://pubmed.ncbi.nlm.nih.gov/1324923/); those sources are curriculum and scientific references only. No text, question, dataset, or figure from them is reproduced or adapted, and no MIT endorsement or course equivalency is implied. Original packet and synthetic dataset: CC BY 4.0. The public question specifications are for formative study and must not be treated as confidential exam materials.
