# Gene interaction: epistasis, complementation and modified dihybrid ratios

Mendel's dihybrid crosses gave 9:3:3:1 because each of two genes controlled its own visible trait. Many traits are built by several genes acting in one pathway, and then the familiar ratio changes shape: two genes can produce 9:7, 9:3:4 or 15:1. Those altered ratios are not failures of Mendel's laws; they are evidence about how gene products work together. This lesson shows how to predict them, how to test which one a cross fits, and how geneticists use gene interactions to order genes in a pathway, including a classic case from the genetics of lifespan.

## Learning objectives

By the end of this lesson, you should be able to:

1. Predict phenotype ratios for two independently assorting genes, including the modified ratios produced by epistasis (9:3:4, 9:7, 12:3:1 and 15:1).
2. Test an observed ratio against competing genetic hypotheses with a chi-square goodness-of-fit test.
3. Use complementation tests and epistasis analysis to decide whether mutations affect the same gene and to order genes in a pathway.

## From 9:3:3:1 to modified ratios

In a cross between two double heterozygotes (AaBb × AaBb) with independent assortment, the 16 equally likely gamete combinations give genotype classes in the proportions 9 A_B_ : 3 A_bb : 3 aaB_ : 1 aabb. When each gene controls a separate trait, these are also the phenotype classes. When the genes act in the same pathway, some classes look alike and merge:

| Interaction | Example logic | Ratio |
|---|---|---|
| Complementary genes | Both enzymes of a two-step pigment pathway are needed; losing either gives white | 9 : 7 |
| Recessive epistasis | Gene B sets pigment type, but the recessive genotype ee at gene E prevents any pigment from being deposited | 9 : 3 : 4 |
| Dominant epistasis | A dominant allele of one gene blocks the colour set by the other | 12 : 3 : 1 |
| Duplicate genes | Either gene alone is enough for the trait | 15 : 1 |

A gene whose genotype masks the effect of another is **epistatic** to it; the masked gene is **hypostatic**. In genetics this word describes a pattern of phenotypes in crosses. It is related to, but not the same as, "epistasis" in statistical genetics, where it means a departure from additive effects in a model.

## Testing which ratio fits

**Synthetic data:** two true-breeding white-flowered lines are crossed, the F1 is purple, and the F1 is self-fertilized. The F2 has 160 plants: 96 purple and 64 white.

A one-gene hypothesis predicts 3:1, so 120 purple and 40 white. χ² = Σ (O − E)²/E = (96 − 120)²/120 + (64 − 40)²/40 = 19.2, with one degree of freedom (two classes, no parameter estimated from the data). The 5% critical value is 3.84, so 3:1 is rejected.

The complementary-gene hypothesis predicts 9:7, so 90 purple and 70 white. χ² = 0.914, well below 3.84: the data fit two genes acting in one pathway. Fitting a hypothesis is not proof of it; it means this hypothesis is not contradicted, while the one-gene model is.

Chi-square tests must use **counts**, not percentages, because the statistic depends on sample size. With three phenotype classes there are two degrees of freedom and the 5% critical value is 5.99.

## Complementation: same gene or different genes?

When two independently isolated recessive mutants share a phenotype, a **complementation test** asks whether they carry mutations in the same gene. Cross them. If the F1 is wild type, each parent supplied a working copy of the gene the other lacked: the mutations **complement**, so they are in different genes. If the F1 is mutant, neither parent supplied a working copy of the shared gene: the mutations fail to complement and are alleles of one gene. The white-flowered lines above complemented (their F1 was purple), which is what the 9:7 result also implies.

## Ordering genes: epistasis analysis

If two mutations with opposite phenotypes affect one switch-like pathway, the double mutant usually resembles the mutant of the gene acting later (downstream), because the downstream step determines the output. Genetic analysis of lifespan in the nematode worm used exactly this logic. Mutations in the gene *daf-2* let adult worms live more than twice as long as wild type, and that extension required the activity of a second gene, *daf-16* (Kenyon and colleagues, 1993). Because the longevity needed *daf-16*, *daf-16* is epistatic to *daf-2* for this trait, which is consistent with *daf-16* acting downstream in the same pathway. Later biochemical work, not part of the cited paper, showed that *daf-2* encodes a receptor in an insulin/IGF-1-like signalling pathway. The genetic result is from one species and says nothing directly about people, and epistasis alone does not show how the gene products interact.

## Common mistakes

- Running a chi-square test on percentages instead of counts.
- Using the wrong degrees of freedom: classes minus one, minus any parameters estimated from the data.
- Reading "fits 9:7" as proof of a mechanism rather than as a hypothesis that survived a test.
- Concluding that two mutations are in the same gene when their F1 is wild type; that is complementation, the opposite conclusion.
- Assuming epistasis analysis reveals direct physical contact between proteins; it orders genetic steps only.

## Worked example

**Problem.** In a synthetic cross of black mice heterozygous at two pigment genes, 192 F2 pups are 105 black, 39 brown and 48 white. Test the recessive-epistasis hypothesis (9:3:4).

**Step 1: expected counts.** With gene E (deposition) and gene B (pigment type), the expected shares 9/16 black, 3/16 brown and 4/16 white of 192 are 108, 36 and 48.

**Step 2: statistic.** χ² = (105 − 108)²/108 + (39 − 36)²/36 + (48 − 48)²/48 = 0.333.

**Step 3: decide.** With two degrees of freedom the 5% critical value is 5.99, so the data are consistent with 9:3:4. The white class (4/16) combines the 3/16 of pups that are homozygous recessive at the deposition gene but carry a dominant pigment-type allele with the 1/16 that are homozygous recessive at both genes: without deposition, the pigment type cannot show.

## Limits of this lesson

All counts are synthetic. The lesson assumes independent assortment, full penetrance and equal viability of all genotype classes; linkage, lethal classes or incomplete penetrance distort the ratios. The worm example is summarized from a link-only reference that was checked for its record and abstract, not reproduced.
