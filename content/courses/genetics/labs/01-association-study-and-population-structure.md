# Virtual lab 1: a case–control association study with population structure

**Activity type:** synthetic-data analysis with public, ungraded formative checks
**Course package:** Genetics & Genomics. **Estimated learner time:** 2–3 hours
**Data status:** all genotypes are constructed for instruction. They describe no real people, variants, trait or study, and nothing here is evidence about any gene or about human health.
**Dataset:** [synthetic genotypes (CSV)](https://raw.githubusercontent.com/dylanstechmann/uniStemCourseSimulators/main/content/courses/genetics/labs/case-control-genotypes.csv).

## Experimental question

A synthetic study compares 50 people with a trait (cases) and 50 without (controls). Each person comes from one of two populations, A or B, and is genotyped at three variants, SYN1, SYN2 and SYN3, recorded as the number of copies of the effect allele (0, 1 or 2). Population A is over-represented among cases (40 of 50), and population B among controls (40 of 50). The variants differ in what drives their association signal, and the lab asks which signals deserve follow-up and why a very small p-value is not enough.

## Learning objectives

1. Summarize genotype data by ancestry and case status with counts and mean allele dosage, and convert dosage to allele frequency.
2. Compute an allelic odds ratio and chi-square statistic from allele counts and compare the result with a multiple-testing threshold.
3. Evaluate confounding by ancestry with a stratified analysis, and decide which association signals warrant follow-up.

## Data dictionary

| Column | Meaning |
|---|---|
| id | person identifier |
| ancestry | A or B, the person's population in this synthetic study |
| status | case or control |
| syn1, syn2, syn3 | copies of the effect allele at each variant (0, 1 or 2) |

## The synthetic data

The CSV lists all 100 people in mixed order. The table below gives the same genotype counts by stratum, where the label gives ancestry first and status second, in lowercase (a-case, a-control, b-case, b-control).

| Stratum | People | SYN1 (dosage 0 / 1 / 2) | SYN2 (dosage 0 / 1 / 2) | SYN3 (dosage 0 / 1 / 2) |
|---|---:|---:|---:|---:|
| a-case | 40 | 6 / 20 / 14 | 10 / 20 / 10 | 22 / 14 / 4 |
| a-control | 10 | 2 / 4 / 4 | 5 / 4 / 1 | 6 / 4 / 0 |
| b-case | 10 | 7 / 2 / 1 | 3 / 4 / 3 | 6 / 3 / 1 |
| b-control | 40 | 26 / 12 / 2 | 20 / 16 / 4 | 23 / 14 / 3 |

## Work sequence

To use the software checks, open **Practice gradebook** and select **Virtual lab 1: association study with population structure (ungraded practice)**. The points are practice feedback only.

1. **Summarize each stratum.** Count the people and average the dosage of SYN1 and SYN2 within each of the four strata. Upload a table with columns `stratum`, `individuals`, `mean_dosage_syn1` and `mean_dosage_syn2`. Divide a mean dosage by 2 to get an allele frequency.
2. **Pool and test.** Add the allele counts of the two populations to get one 2×2 table of effect and other alleles for cases and controls. Compute the allelic odds ratio and the chi-square statistic with 1 degree of freedom, and compare with the Bonferroni threshold for three tests.
3. **Stratify.** Compute the odds ratio within population A and within population B, then the Mantel–Haenszel combined odds ratio. Compare them with the pooled value.
4. **Decide.** Separate the signal that is explained by ancestry from the signal that survives, and say what each result does and does not support.

The allelic test treats the two alleles of a person as independent. That is reasonable here because genotype frequencies within each stratum are close to Hardy–Weinberg proportions, but a genotype-based test is preferred in practice.

## Worked calculation

For SYN1, the pooled counts are 52 effect and 48 other alleles in cases and 28 and 72 in controls, an odds ratio of (52/48) / (28/72) = 2.79. Expected effect alleles in each group are 40, and χ² = 3.6 + 2.4 + 3.6 + 2.4 = 12.0, p about 0.0005, below the Bonferroni threshold of 0.0167. Inside population A, the effect-allele frequency is 0.60 in both cases and controls; inside population B it is 0.20 in both. The within-population odds ratios are 1.00, and so is the Mantel–Haenszel odds ratio. The pooled signal exists only because population A, with the higher frequency, supplies most of the cases.

For SYN2 the pooled counts are 50 and 50 in cases and 30 and 70 in controls: odds ratio 2.33, χ² = 8.33, p about 0.004. Both populations show the same odds ratio (2.33 and 2.33), so ancestry does not explain it, and it passes the corrected threshold. It remains a candidate: one small sample, one design, no mechanism. SYN3 shows odds ratio 1.17 and χ² = 0.24, which is no evidence of association.

## Analytic rubric for discussion

| Criterion | Evidence for full credit |
|---|---|
| Summary table | Counts and averages computed within the four ancestry-by-status strata, not pooled |
| Test statistics | Allelic odds ratio and chi-square computed from allele counts with the right degrees of freedom |
| Multiple testing | Uses α/3 and notes that a threshold controls chance findings, not confounding |
| Stratified analysis | Compares pooled with within-population and Mantel–Haenszel odds ratios and identifies SYN1 as confounded |
| Scope | Treats SYN2 as a candidate needing replication and fine-mapping, not as a cause |

## Limits and provenance

This is an original exercise with constructed data and round numbers. Real association studies use thousands of people and millions of variants, model ancestry continuously, handle relatedness and genotyping quality, and use much stricter thresholds. Original lab text and dataset: CC BY 4.0.
