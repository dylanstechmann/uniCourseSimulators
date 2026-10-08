# Homework 6 practice: penetrance and isogenic evidence

**Status:** open formative practice; this packet and its answer specifications are public and are not suitable for a protected or summative exam. It does not contribute to a course grade.  
**Course package:** Foundations of Cell and Molecular Biology, version 0.19.0
**Suggested time:** 2–3 hours  
**Prerequisite lessons:** [Inheritance, penetrance, and pedigree evidence](../modules/09a-inheritance-penetrance-and-pedigree-evidence.md) and [Variant mechanism and isogenic evidence](../modules/09b-variant-mechanism-and-isogenic-evidence.md).  
**Dataset:** [synthetic measurements](https://raw.githubusercontent.com/dylanstechmann/uniStemCourseSimulators/main/content/courses/cell-biology/assignments/homework-06-isogenic-clones.csv).

## Purpose

Two kinds of evidence are often confused: how often a genotype is followed by a trait in families, and whether changing the variant in an otherwise identical cell line changes a cellular readout. This problem set computes penetrance, then uses isogenic clones to ask what a correction and a re-introduction add. Neither a family table nor a clonal comparison, alone, identifies the molecular mechanism or shows what will happen to any individual.

## Learning objectives

After working through the packet, learners should be able to:

1. Calculate penetrance and state what it does and does not mean.
2. Summarize clone-level data without treating assay replicates as independent clones.
3. Interpret a correction and re-introduction in isogenic lines with stated limits.
4. Separate association in families from mechanism in cells.
5. State what is not shown about prediction for individuals.

## Experimental scenario and data dictionary

**Pedigree summary (synthetic).** Across several constructed families, carriers and non-carriers of a variant were counted and the number with a defined trait was recorded.

| Group | People | Affected |
|---|---:|---:|
| Variant carriers | 30 | 18 |
| Non-carriers | 70 | 7 |

**Isogenic cell lines (synthetic).** A parental line carrying the variant, three independently derived clones in which the variant was corrected, and a line in which the variant was re-introduced into a corrected clone were each scored with one quantitative cellular assay (higher is closer to the reference state). Four independent clones or derivations per condition; assay replicates were collapsed within each clone. All values are synthetic teaching data.

| Condition | Independent clone | Assay score |
|---|---|---:|
| Parental variant line | P1 | 41 |
| Parental variant line | P2 | 44 |
| Parental variant line | P3 | 39 |
| Parental variant line | P4 | 40 |
| Corrected clones | C1 | 78 |
| Corrected clones | C2 | 80 |
| Corrected clones | C3 | 77 |
| Corrected clones | C4 | 79 |
| Variant re-introduced | R1 | 43 |
| Variant re-introduced | R2 | 40 |
| Variant re-introduced | R3 | 42 |
| Variant re-introduced | R4 | 43 |

## Work sequence

To use the software checks, open **Practice gradebook** and select **Homework 6: penetrance and isogenic evidence (open, ungraded practice)**. The interactive points are practice feedback only; they are not added to a course grade.

### Part A — Penetrance

Calculate the penetrance among carriers (affected carriers divided by carriers, as a percentage) and choose the best-supported statement about what penetrance does and does not show.

### Part B — Summarize the independent clones

Retain all four clone-level values per condition. Calculate the mean assay score and report a clone count of four. Upload one UTF-8 CSV with exactly this header and column order:

```csv
condition,batch_count,mean_assay_score
parental_variant,4,41
corrected,4,78.5
reintroduced,4,42
```

The software scores the summary cells only.

### Part C — Plot the isogenic means

Plot the mean assay score on the supplied axes (0 = parental variant, 1 = corrected, 2 = variant re-introduced).

### Part D — Evidence logic

Use the structured checks to decide what the family table, the correction and the re-introduction each add, and the multiple-select item to review common errors.

## Worked calculation

Worked calculation: Penetrance among carriers is 18 / 30 = 60%, against 7 / 70 = 10% among non-carriers, so affected status is six times as frequent in carriers in this constructed table; it is an association in one dataset. In the isogenic comparison the variant line averages (41 + 44 + 39 + 40) / 4 = 41, the corrected clones 78.5 and the re-introduced variant 42.

## Analytic instructor rubric

For instructor-led discussion, use 0–2 points for each criterion. Zero indicates absent or incompatible evidence; one indicates a partially correct response that omits a key assumption or control; two indicates the evidence described below. This guide is not connected to the software gradebook.

| Criterion | Evidence for full credit |
|---|---|
| Penetrance | Computes affected carriers over carriers and distinguishes it from transmission and from the effect of the variant on a given person. |
| Replication and summary | Retains four independent clones and does not treat assay replicates as extra clones. |
| Correction and re-introduction | States that a correction that moves the readout toward reference and a re-introduction that moves it back together support a role for the variant in this cell system. |
| Limits | Notes off-target effects, clonal variation and the single readout, and does not claim pathogenicity or prediction for individuals. |
| Follow-up | Proposes additional clones, independent readouts and a different cell background. |

The autograded public practice set covers a subset of these criteria with deterministic numeric, CSV, graph-coordinate, multiple-select and structured-choice rules. Its keys are open in this repository. Responses requiring a written explanation are not automatically scored.

## Limitations and provenance

Original paper exercise using constructed data. It is not a wet-lab protocol, an actual experimental result, or a clinical or therapeutic claim. The scenario follows the corresponding course lesson; no outside text, question, dataset or figure is reproduced or adapted. Original packet and synthetic dataset: CC BY 4.0. The public question specifications are for formative study and must not be treated as confidential exam materials.
