# Designing a controlled gene-perturbation experiment: tools, controls, quantification and replication

The question "what does this gene do?" is usually answered by changing the gene and measuring what follows. That simple idea is easy to get wrong: the perturbation may hit other genes, the measurement may be normalized badly, and replicates may not be independent. This lesson takes a synthetic knockdown experiment from tool choice to sample size, so that the design can support a causal statement about the gene rather than about the procedure.

## Learning objectives

By the end of this lesson, you should be able to:

1. Choose a perturbation tool and the controls needed to attribute an effect to the targeted gene.
2. Quantify knockdown by the ΔΔCt method and state its assumptions.
3. Plan biological replication and sample size, and distinguish independent replicates from repeated measurements.

## Choosing a perturbation

- **CRISPR knockout** disrupts the gene's coding sequence, often by small insertions or deletions that shift the reading frame. Loss is permanent in the edited cells, but editing is a population of outcomes, and in-frame edits can leave partial function.
- **CRISPR interference (CRISPRi)** uses a catalytically inactive Cas9 fused to a repressor to block transcription without cutting DNA. It is reversible and avoids DNA-damage responses to cutting, which matter in some cell types.
- **RNA interference (siRNA, shRNA)** degrades the transcript. It is fast and transient, and partial knockdown is common.
- **Overexpression and rescue** add back the gene, often in a form the perturbation cannot hit.

Each tool can affect genes other than the target: guides and siRNAs can bind similar sequences elsewhere, and the delivery method itself (transfection, viral transduction, selection drugs) can change cell behavior.

## Controls that make the conclusion about the gene

1. **A non-targeting control** delivered the same way, so the comparison isolates the targeting sequence rather than the procedure.
2. **At least two independent reagents** (different guides or siRNAs) against the same gene. Off-target effects differ between sequences; a phenotype seen with both is less likely to be off-target.
3. **Rescue**: restoring the gene, in a form resistant to the reagent, should reverse the phenotype. This is the strongest single control for specificity.
4. **A measured perturbation**: confirm the target's RNA or protein actually fell, by how much, and at the time the phenotype was measured.
5. **Pre-specified readout**: name the primary phenotype and analysis before seeing the data, so that many possible readouts do not become a search for a significant one.

## Quantifying knockdown by ΔΔCt

Quantitative PCR reports a cycle threshold (Ct): the cycle at which product crosses a detection level. More starting template means a lower Ct. For a target gene normalized to a reference gene:

- ΔCt = Ct(target) − Ct(reference) within each sample
- ΔΔCt = ΔCt(perturbed) − ΔCt(control)
- relative expression = 2^(−ΔΔCt)

**Synthetic Ct values:** control target 24.0, reference 18.0; knockdown target 26.5, reference 18.2. Then ΔCt(control) = 6.0, ΔCt(knockdown) = 8.3, ΔΔCt = 2.3, and relative expression = 2^(−2.3) = 0.203, an 80% knockdown.

The method assumes both amplicons double each cycle (efficiency near 100%) and that the reference gene is unaffected by the perturbation. If efficiency is lower, 2 should be replaced by the measured amplification factor; if the reference changes, the normalization is biased. Validating these assumptions is part of the experiment, not an extra.

## Replication and sample size

The **unit of replication** is the thing that could vary independently: separate cultures, separately transfected or derived, ideally on different days. Three wells pipetted from one transfection are technical replicates of one biological replicate; treating them as independent inflates confidence. This error is called pseudoreplication.

For comparing two group means with a normal approximation, the number per group for a two-sided test at α = 0.05 with 80% power is about

**n ≈ 2 (z₁₋α/₂ + z₁₋β)² σ² / δ²,**

where σ is the standard deviation between biological replicates and δ the smallest difference worth detecting. For a log₂ expression readout with σ = 0.5 and δ = 1.0, n ≈ 2 × (1.96 + 0.8416)² × 0.5² / 1.0² = 3.92, so 4 per group. This normal approximation is optimistic at small n: an exact t-test calculation shows that 4 per group gives only about 66% power, and 6 per group are needed for 80%. If replicate variability were σ = 0.8, the same formula gives 10.05, so 11 per group (12 by the exact t-test calculation). The variance estimate usually comes from pilot data or prior experiments in the same system and should be stated.

## Randomization and blinding

Plate position, passage number and processing order can all create effects. Assign conditions to positions and processing order at random, and where the readout involves judgement (for example, scoring images) keep the scorer unaware of condition until analysis is finished.

## Worked example

**Problem.** A team reports that knocking down gene G slows proliferation, using one siRNA, three wells from a single transfection and a non-targeting control. Which additions would let the conclusion be about G?

**Step 1: specificity.** Add a second siRNA with a different sequence and a rescue construct resistant to the siRNA. Agreement across reagents and reversal by rescue address off-target effects.

**Step 2: replication.** Repeat the transfection independently at least 6 times per condition (the exact t-test figure above, if variability is similar), treating each transfection as one replicate and averaging its wells.

**Step 3: measurement.** Confirm knockdown by ΔΔCt (and ideally protein) in each replicate at the time proliferation is measured, with a validated reference gene.

**Step 4: analysis.** Pre-specify proliferation at one time point as the primary readout and the test to be used.

## Limits of this lesson

All Ct values and variances are synthetic. The sample-size formula is a normal approximation for two independent groups; paired designs, multiple comparisons and non-normal readouts need other methods.
