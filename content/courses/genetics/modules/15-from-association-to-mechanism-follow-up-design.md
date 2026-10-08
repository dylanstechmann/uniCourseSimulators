# From an association signal to a mechanism: designing the follow-up of a locus

A genome-wide association study ends with a list of regions, not a list of causes. Each region may hold dozens of correlated variants, sits in an unknown cell type and may act on a gene that is not the nearest one. This lesson walks through the follow-up that turns a region into a testable mechanism, using a synthetic locus associated with slower wound closure in a synthetic cohort. It computes the quantities that narrow the candidates, names what each kind of evidence can and cannot show, and ends with the design reasoning that the course case asks you to write. Nothing here is a finding about a real gene, a real cohort or any person.

## Learning objectives

By the end of this lesson, you should be able to:

1. Narrow an association signal to a credible set of candidate variants from approximate Bayes factors, assuming a single causal variant.
2. Quantify allele-specific expression in heterozygous samples and state what an imbalance does and does not show.
3. Design a staged follow-up, from cell type to variant-to-gene link to perturbation with rescue, naming the confounders and the claim each stage can support.

## Stage 1: from a region to candidate variants (fine-mapping)

Variants close together are inherited together (linkage disequilibrium), so the most significant variant in a region need not be causal. **Fine-mapping** asks how the evidence is spread over the variants. Under the simplifying assumption that the region contains exactly **one** causal variant, with equal prior probability for each variant, the posterior probability that variant i is the causal one is its **posterior inclusion probability**

**PIP(i) = BF(i) / Σ BF(j),**

where BF is the Bayes factor, a measure of how much better variant i explains the signal than no association. A **95% credible set** is the smallest group of variants, taken in descending PIP order, whose PIPs sum to at least 0.95.

**Synthetic region:** five variants have Bayes factors 600, 300, 60, 30, 10, summing to 1000.

| Variant | Bayes factor | PIP | Cumulative PIP |
|---|---:|---:|---:|
| V1 | 600 | 0.60 | 0.60 |
| V2 | 300 | 0.30 | 0.90 |
| V3 | 60 | 0.06 | 0.96 |
| V4 | 30 | 0.03 | 0.99 |
| V5 | 10 | 0.01 | 1.00 |

The top variant has a PIP of 0.60: it is the best single candidate, yet there is a probability of 0.40 that the causal variant is another one. The 95% credible set needs 3 variants (cumulative PIP 0.96). Where variants are in near-perfect linkage disequilibrium their Bayes factors are almost equal, and the credible set grows; statistics alone cannot separate them. The assumptions matter: if two variants are independently causal, or if the linkage reference panel is from a different ancestry than the study sample, PIPs can be badly miscalibrated.

## Stage 2: which cell type?

A variant that changes gene regulation must sit in a regulatory element that is active in the relevant cell. Overlaying credible-set variants on maps of open chromatin and histone marks from candidate cell types (for example fibroblasts, keratinocytes and immune cells for wound closure) prioritizes cell types. With only a handful of variants, the overlap is weak evidence: it generates a hypothesis to test, and a variant inside an active element in a given cell type does not show that it affects that element's activity.

## Stage 3: allele-specific expression

If a variant acts in cis, then in a person heterozygous for it (or for a transcribed variant on the same haplotype) the two copies of the gene should be expressed unequally, while the two copies share the same nucleus, the same transcription factors and the same environment. Counting RNA reads that carry each allele therefore tests a cis effect with internal controls.

**Synthetic data:** in a heterozygous cell sample, 140 of 200 reads carry the reference allele and 60 the alternative allele, a ratio of 2.33. If there were no cis effect the expected split is 50:50. A normal approximation for the count gives z = (observed − expected)/√(n p (1 − p)) = (140 − 100)/√(200 × 0.25) = 5.66, far beyond 1.96.

The caveats are as important as the number. Reads that match the reference genome map more easily than reads with mismatches, which pushes counts toward the reference allele even when expression is equal. Copy-number changes, imprinting and allele-specific DNA methylation also cause imbalance. Controls are sequencing the same cells' DNA (where heterozygotes should show about 50:50), aligning to a reference that includes both alleles, and testing several donors. Finally, an imbalance is a property of the haplotype: it shows that something on the haplotype acts in cis, not that the lead variant is the cause.

## Stage 4: testing the variant itself

To test a single variant, change only that base in an otherwise identical cell, ideally by editing each allele in isogenic cells and comparing, with independent clones or reagents, a non-targeting control delivered the same way, and a measured effect on the gene's expression (see the perturbation lesson). If the phenotype of interest can be modelled in vitro, such as the closure of a scratch in a cell layer, test whether it follows the edit and whether restoring the gene's activity reverses it. A positive result shows that the variant changes the gene's expression and that expression changes the phenotype **in that cell system**. It does not show the same in the tissue of a person.

## What each stage can claim

| Evidence | Supports the claim |
|---|---|
| Association | A region contains one or more variants correlated with the trait |
| Fine-mapping | A short list of candidate variants, each with a probability under stated assumptions |
| Chromatin overlap | A candidate cell type or regulatory element |
| Allele-specific expression | Something on the haplotype acts in cis on the gene |
| Variant editing | The variant changes expression in this cell system |
| Phenotype and rescue | The gene's activity affects the phenotype in this system |

Confounders to name in a design: ancestry and population structure (which can create associations and distort PIPs), differences in cell-type composition between samples, processing batch, and linkage disequilibrium between the candidate and its neighbours.

## Common mistakes

- Treating the top variant of a locus as the causal variant.
- Reading a PIP as certain when its assumptions (one causal variant, matched linkage reference) are not checked.
- Interpreting allele-specific expression without controlling for reference-allele mapping bias.
- Concluding that the lead variant is causal from an imbalance that shows only that the haplotype acts in cis.
- Skipping rescue and independent reagents when moving from expression to phenotype.
- Extending a result from one cell system to a person.

## Worked example

**Problem.** A second synthetic locus has Bayes factors 90, 60, 30, 15, 5, and in a heterozygous sample 62 of 100 reads carry the reference allele. What are the PIPs, how large is the 95% credible set, and what does the imbalance add?

**Step 1: PIPs.** The Bayes factors sum to 200, so the PIPs are 0.450, 0.300, 0.150, 0.075, 0.025 with cumulative values 0.450, 0.750, 0.900, 0.975, 1.000.

**Step 2: credible set.** The cumulative PIP first reaches 0.95 at 4 variants (0.975), so the 95% credible set has 4 variants and the top variant's PIP is only 0.45.

**Step 3: imbalance.** z = (62 − 50)/√(100 × 0.25) = 2.4, just beyond 1.96. With one sample, possible reference bias and no DNA control, this is a lead for replication in more donors, not a conclusion.

**Step 4: next stages.** Test the 4 credible variants in the relevant cell type by editing, with independent clones and rescue, before naming a causal variant.

## Limits of this lesson

All Bayes factors and read counts are synthetic. Single-causal-variant fine-mapping, a normal approximation for read counts and a one-sample imbalance are teaching simplifications; real analyses allow several causal variants, use beta-binomial models for read counts and combine many donors. The lesson summarizes the logic of follow-up studies without reproducing any specific one.
