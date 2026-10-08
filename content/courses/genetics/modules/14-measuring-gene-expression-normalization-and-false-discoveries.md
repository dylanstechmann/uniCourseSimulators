# Measuring gene expression: read counts, normalization, fold change and false discoveries

Asking how a perturbation, a disease or age changes gene activity usually means measuring messenger RNA, today mostly by sequencing. An RNA-sequencing experiment produces a count of reads for each of about 20,000 genes in each sample. Turning those counts into a trustworthy list of changed genes needs three things: normalization, so samples are comparable; replication, so biological variation can be estimated; and control of false discoveries, because thousands of genes are tested at once. This lesson works through each with synthetic numbers and ends with the design choices that decide whether a result means anything.

## Learning objectives

By the end of this lesson, you should be able to:

1. Normalize read counts for library size (counts per million) and compute a log₂ fold change.
2. Explain why testing many genes at once requires false-discovery control, and apply the Benjamini–Hochberg procedure to a short list of p-values.
3. Design an expression comparison with biological replicates, balanced batches and a pre-specified analysis, and evaluate what a fold change does not show.

## Normalizing for sequencing depth

Two samples are rarely sequenced to the same depth. **Synthetic data:** gene G has 300 reads in a control sample with 15,000,000 reads in total, and 450 reads in a treated sample with 25,000,000 in total. The raw counts suggest a 1.5-fold increase, but the treated library is larger.

**Counts per million** divide by library size: CPM = reads / total reads × 10⁶. Control: 300/15,000,000 × 10⁶ = 20. Treated: 450/25,000,000 × 10⁶ = 18. After normalization, G is slightly lower in the treated sample.

Expression changes are reported on a log₂ scale, where +1 means doubling and −1 halving: log₂(18/20) = -0.152. The log scale makes increases and decreases symmetric.

Total-count normalization assumes that most genes do not change. If a few very abundant transcripts rise sharply, they take up a larger share of reads, and every other gene appears to fall. Methods used in practice (for example, trimmed-mean or median-of-ratios normalization) are designed to resist this composition effect. Comparing different genes within one sample also needs a correction for transcript length, because longer transcripts yield more reads.

## Replicates and variation

A fold change from one sample per group says nothing about whether the difference exceeds normal variation. **Biological replicates** (independent cultures, animals or donors) estimate that variation; repeated sequencing of one RNA prep does not. Read counts vary more between biological replicates than a simple Poisson model predicts, so standard tools model counts with a negative binomial distribution and share information across genes to estimate the variance when replicates are few. Genes with few reads have very noisy fold changes, which is why many tools shrink extreme estimates for low-count genes toward zero.

## Thousands of tests

Testing 20,000 genes at p < 0.05 when **no** gene truly changes would still flag about 20,000 × 0.05 = 1,000 genes. Two common controls:

- **Bonferroni** keeps the chance of any false positive below α by testing each gene at α/m. It is strict and loses power when m is large.
- **Benjamini–Hochberg (BH)** controls the **false discovery rate**, the expected fraction of false positives among the genes called significant. Sort the m p-values from smallest to largest, find the largest rank k with p(k) ≤ (k/m) × q, and call the k smallest significant.

**Synthetic example** with m = 10 and q = 0.05:

| Rank k | p-value | (k/m) × q | p ≤ threshold? |
|---:|---:|---:|---|
| 1 | 0.001 | 0.005 | yes |
| 2 | 0.008 | 0.010 | yes |
| 3 | 0.02 | 0.015 | no |
| 4 | 0.021 | 0.020 | no |
| 5 | 0.024 | 0.025 | yes |
| 6 | 0.2 | 0.030 | no |
| 7 | 0.35 | 0.035 | no |
| 8 | 0.6 | 0.040 | no |
| 9 | 0.8 | 0.045 | no |
| 10 | 0.9 | 0.050 | no |

The largest rank that passes is k = 5, so BH calls the 5 smallest p-values significant. That includes ranks 3 and 4, which miss their own thresholds: BH is a step-up procedure, and one passing rank pulls in every smaller p-value. Bonferroni (p ≤ 0.005) calls 1. The statistics course covers both procedures in more depth.

## Design decides what the data can mean

- **Batches.** Library preparation day, sequencing lane and RNA extraction kit all leave signatures. If all controls are processed on one day and all treated samples on another, treatment and batch are confounded, and no analysis can separate them. Spread each group across batches and record the batch so it can be modelled.
- **Randomization and blinding** of sample processing order.
- **Pre-specified analysis:** the comparison, the normalization, the threshold (for example, BH q < 0.05) and any minimum fold change, stated before looking.
- **Cell composition.** In tissue, an apparent change in one gene can reflect a change in the proportions of cell types. This matters especially when comparing young and old tissue, where composition often shifts.
- **Validation** of key genes by an independent method or in new samples.

## Common mistakes

- Comparing raw counts between samples of different depth.
- Counting technical replicates as biological replicates.
- Calling every gene with p < 0.05 a discovery when thousands were tested.
- Stopping at the first rank that fails its threshold instead of taking the largest rank that passes.
- Confounding treatment with processing batch.
- Treating an mRNA fold change as a change in protein level or cell function.

## Worked example

**Problem.** A study compares skin fibroblasts from young and old synthetic donors: 3 donors per group, all young samples prepared in week 1 and all old samples in week 2, with 2 sequencing runs of each RNA prep. It reports 1,200 genes with p < 0.05 out of 20,000. Identify the problems and redesign it.

**Step 1: multiple testing.** About 1,000 genes would pass p < 0.05 by chance alone, so 1,200 unadjusted hits are mostly uninterpretable; apply BH.

**Step 2: confounding.** Age is completely confounded with preparation week. Redesign: prepare young and old samples together in each week, in random order.

**Step 3: replication.** The two runs of one prep are technical replicates; n is 3 donors per group, not 6. Use more donors if the expected differences are modest, and estimate the needed number from pilot variance.

**Step 4: interpretation.** Report changed genes as changes in fibroblast mRNA under culture conditions, check for shifts in cell-type composition, and validate key genes in new donors before drawing conclusions about aging.

## Limits of this lesson

All counts and p-values are synthetic. The lesson does not cover statistical models of count data in detail, single-cell methods, or alternative splicing.
