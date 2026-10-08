# Homework 2 practice: initial rates and reversible inhibition

**Status:** open formative practice; this packet and its answer specifications are public and are not suitable for a protected or summative exam. It does not contribute to a course grade.
**Course package:** Foundations of Cell and Molecular Biology, version 0.19.0
**Suggested time:** 2–3 hours
**Prerequisite lessons:** [Enzyme catalysis, reaction mechanisms, and free energy](../modules/04a-enzyme-catalysis-and-free-energy.md) and [Initial-rate evidence and reversible enzyme inhibition](../modules/04b-initial-rates-and-enzyme-inhibition.md).
**Dataset:** [synthetic initial-rate measurements](https://raw.githubusercontent.com/dylanstechmann/uniStemCourseSimulators/main/content/courses/cell-biology/assignments/homework-02-inhibition-rates.csv).

## Purpose

Two compounds lower the rate of the same enzyme reaction. This problem set asks what a single substrate concentration can and cannot tell you, how the apparent Michaelis constant changes in a simple competitive model, and which controls separate a real change in catalytic rate from a readout artifact. A correct mean is one part of the evidence; it does not by itself identify an inhibition mechanism or a binding site.

The four rows per condition are independent assay days, each with its own enzyme dilution. Several time points were collected on each day to estimate the initial rate. The replicate unit is the assay day, not each time point.

## Learning objectives

After working through the packet, learners should be able to:

1. Calculate an initial rate from the single-substrate model and an apparent Michaelis constant under a stated simple inhibition model, with units.
2. Summarize replicate-level initial rates without treating time points as independent experiments.
3. Explain why equal rates at one substrate concentration do not distinguish inhibition patterns, and design the substrate range that would.
4. Choose controls that address substrate depletion, detector interference, solvent effects and enzyme instability.
5. State what a competitive-looking pattern supports and what requires independent evidence about binding.

## Experimental scenario and data dictionary

A purified enzyme converts one substrate to a fluorescent product. For each condition, the substrate concentration `[S]` was varied while enzyme concentration, buffer, pH, temperature and solvent were held fixed. Initial rates were estimated from the early linear part of product accumulation. The vehicle curve is generated from `Vmax = 120 nM·s⁻¹` and `Km = 20 µM`. Inhibitor A was constructed as a competitive pattern with `α = 3` (apparent `Km` 60 µM, same `Vmax`). Inhibitor B was constructed as an uncompetitive pattern with `α′ = 2` (apparent `Vmax` 60 nM·s⁻¹, apparent `Km` 10 µM). Both compounds were tested at one fixed concentration. All values are synthetic teaching data and have no biological or clinical source.

Curve values (model-generated, rounded to two decimals):

| [S] (µM) | Vehicle (nM·s⁻¹) | Inhibitor A (nM·s⁻¹) | Inhibitor B (nM·s⁻¹) |
|---:|---:|---:|---:|
| 5 | 24.00 | 9.23 | 20.00 |
| 10 | 40.00 | 17.14 | 30.00 |
| 20 | 60.00 | 30.00 | 40.00 |
| 40 | 80.00 | 48.00 | 48.00 |
| 80 | 96.00 | 68.57 | 53.33 |
| 160 | 106.67 | 87.27 | 56.47 |

At `[S] = 40 µM` the constructed curves for A and B cross. The four independent assay days at that substrate concentration are:

| Condition | Assay day | Initial rate at 40 µM (nM·s⁻¹) |
|---|---|---:|
| Vehicle | D1 | 79 |
| Vehicle | D2 | 81 |
| Vehicle | D3 | 80 |
| Vehicle | D4 | 80 |
| Inhibitor A | D1 | 47 |
| Inhibitor A | D2 | 49 |
| Inhibitor A | D3 | 48 |
| Inhibitor A | D4 | 48 |
| Inhibitor B | D1 | 47 |
| Inhibitor B | D2 | 48 |
| Inhibitor B | D3 | 49 |
| Inhibitor B | D4 | 48 |

The vehicle curve is additionally measured on four assay days at `[S] = 10 µM` (39, 41, 40, 40 nM·s⁻¹) and at `[S] = 160 µM` (107, 107, 106, 107 nM·s⁻¹); these appear in the dataset file with the 40 µM rows.

## Work sequence

To use the software checks, open **Practice gradebook** and select **Homework 2: initial rates and reversible inhibition (open, ungraded practice)**. The interactive points are practice feedback only; they are not added to a course grade.

### Part A — Summarize the independent assay days

For each condition retain all four assay-day values at `[S] = 40 µM`. Calculate the arithmetic mean initial rate and report a day count of four. Upload one UTF-8 CSV with exactly this header and column order:

```csv
condition,batch_count,mean_rate_nm_per_s
vehicle,4,80
inhibitor_a,4,48
inhibitor_b,4,48
```

The displayed rows show the required format only; make your own calculations from the linked data file before submitting. The software scores these summary cells only.

### Part B — Plot the vehicle curve

Plot the mean vehicle initial rate at `[S] = 10`, `40` and `160 µM` on the supplied axes. Three points do not define a curve; the plot shows a rising, flattening trend and nothing more.

### Part C — Apparent constant and what one concentration shows

Under the simple competitive model, `α = 1 + [I]/Ki`, and the apparent `Km` is `α·Km`. For `[I] = 40 µM` and `Ki = 20 µM`, calculate the apparent `Km` of inhibitor A in µM. Then decide what the equal 48 nM·s⁻¹ means for A and B at 40 µM. Do not conclude that the two compounds act the same way.

### Part D — Controls and mechanism limits

Use the structured checks to decide which control addresses each alternative explanation, and use the multiple-select item to review how kinetic patterns are and are not interpreted.

## Worked calculation

The inhibitor A mean at 40 µM is `(47 + 49 + 48 + 48) / 4 = 48 nM·s⁻¹`. In the competitive model with `α = 3`, `v = 120 × 40 / (60 + 40) = 48 nM·s⁻¹`. In the uncompetitive model with `α′ = 2`, `v = (120/2) × 40 / (20/2 + 40) = 48 nM·s⁻¹`. The same rate arises from two different parameter changes, so a single substrate concentration cannot classify the pattern. At `[S] = 5 µM` A gives 9.23 and B gives 20.00 nM·s⁻¹; at `[S] = 160 µM` A gives 87.27 and B gives 56.47 nM·s⁻¹. The shapes diverge across the range.

## Analytic instructor rubric

For instructor-led discussion, use 0–2 points for each criterion. Zero indicates absent or incompatible evidence; one indicates a partially correct response that omits a key assumption or control; two indicates the evidence described below. This guide is not connected to the software gradebook.

| Criterion | Evidence for full credit |
|---|---|
| Replication and summary | Retains four independent assay days and does not treat time points as extra replicates. |
| Model calculation | Computes the apparent constant with units and states the model assumption behind `α`. |
| Single-concentration limit | Explains that equal rates at 40 µM can arise from different parameter changes and proposes a wider substrate series. |
| Controls | Matches vehicle, no-enzyme, inhibitor-plus-product and calibration controls to the alternatives they address. |
| Mechanism scope | Limits the conclusion to a pattern in a simple model and does not claim a binding site. |

The autograded public practice set covers a subset of these criteria with deterministic numeric, CSV, graph-coordinate, multiple-select and structured-choice rules. Its keys are open in this repository. Responses requiring a written explanation are not automatically scored.

## Limitations and provenance

Original paper exercise using constructed data. It is not a wet-lab protocol, an actual experimental result, or a clinical or therapeutic claim. The scenario follows the course lesson on initial-rate evidence; no outside text, question, dataset or figure is reproduced or adapted. Original packet and synthetic dataset: CC BY 4.0. The public question specifications are for formative study and must not be treated as confidential exam materials.
