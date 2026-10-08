# Many tests at once: family-wise error, Bonferroni and the false discovery rate

Modern biology rarely tests one hypothesis. An expression study compares thousands of genes, a screen tests hundreds of compounds, and an aging study may examine dozens of biomarkers. At a 5% significance level, each true null hypothesis has a 5% chance of a false positive, so across many tests some false positives are nearly certain. This lesson quantifies that problem, applies the Bonferroni correction, and walks through the Benjamini–Hochberg procedure for controlling the false discovery rate, using a synthetic set of ten p-values.

## Learning objectives

By the end of this lesson, you should be able to:

1. Calculate the family-wise error rate and the expected number of false positives across many independent tests.
2. Apply the Bonferroni correction and the Benjamini–Hochberg procedure to a list of p-values and count the rejections each allows.
3. Choose between family-wise and false-discovery control for a study goal, and interpret an adjusted result correctly.

## How false positives accumulate

If m independent tests are each run at level α and all null hypotheses are true, the probability of at least one false positive, the **family-wise error rate (FWER)**, is 1 − (1 − α)ᵐ. For 20 tests at 0.05, FWER = 1 − 0.95²⁰ = 0.642: more likely than not. In a screen of 1,000 genes with no real differences, about α × m = 50 would pass p < 0.05 by chance. A list of "significant" hits from such a screen, reported without correction, is likely to contain many false positives.

## Bonferroni: control the chance of any false positive

The Bonferroni correction tests each hypothesis at α/m. That guarantees FWER ≤ α whatever the dependence between tests. **Synthetic p-values from ten tests:** 0.001, 0.004, 0.012, 0.02, 0.031, 0.04, 0.18, 0.33, 0.52, 0.81. With α = 0.05 and m = 10, the threshold is 0.005, and 2 tests pass. Bonferroni is simple and strict; with many tests it sacrifices a lot of power, because the threshold becomes tiny.

## Benjamini–Hochberg: control the false discovery rate

Often the goal is not to avoid every false positive but to keep the **false discovery rate (FDR)**, the expected fraction of rejected hypotheses that are false, below a level q. The Benjamini–Hochberg (BH) procedure:

1. Sort the p-values from smallest to largest: p₍₁₎ ≤ … ≤ p₍ₘ₎.
2. For each rank i, compute the threshold (i/m) q.
3. Find the largest i with p₍ᵢ₎ ≤ (i/m) q.
4. Reject the hypotheses with ranks 1 to i.

With q = 0.05 the thresholds for ranks 1 to 6 are 0.005, 0.010, 0.015, 0.020, 0.025, 0.030. The sorted p-values 0.001, 0.004, 0.012, 0.02, 0.031, 0.04 meet their thresholds up to rank 4 (0.020 ≤ 0.020) and fail at ranks 5 and 6 (0.031 > 0.025, 0.040 > 0.030). So BH rejects **4** hypotheses, twice as many as Bonferroni. Note that the step-up rule looks for the largest qualifying rank; an earlier failure does not stop the search.

**Adjusted p-values** (often called q-values in this context) summarize the same result per test: the BH-adjusted value for rank i is the minimum over j ≥ i of p₍ⱼ₎ m/j. For rank 4 the raw ratio is 0.020 × 10/4 = 0.050. A test is rejected at FDR q when its adjusted value is ≤ q.

## Choosing and interpreting

- Use **FWER control** (Bonferroni or less conservative variants such as Holm) when any false positive is costly, for instance when a small number of confirmatory endpoints will drive a decision.
- Use **FDR control** for discovery: screens and omics studies whose hits go on to validation. An FDR of 5% means that, on average, about 5% of the reported hits are expected to be false; it says nothing about which ones.
- BH assumes independence or certain kinds of positive dependence among tests; other procedures exist for arbitrary dependence.
- Correction must cover every test performed, including ones not reported. Testing many outcomes and reporting the best ones without correction is a common way that aging-biomarker and intervention studies overstate findings.

## Common mistakes

- Correcting only the tests that look interesting.
- Treating an FDR-controlled list as if each item had a 5% chance of being false.
- Stopping the BH procedure at the first failure instead of finding the largest qualifying rank.
- Forgetting that pre-registered primary endpoints reduce the multiplicity problem by design.

## Worked example

**Problem.** A synthetic study measures 12 blood markers before and after an intervention and reports the one with p = 0.03 as the main finding. How should that result be read?

**Step 1.** If none of the markers truly changed, the chance that at least one of 12 would reach p < 0.05 is 1 − 0.95¹² = 0.46.

**Step 2.** The Bonferroni threshold is 0.05/12 = 0.0042; 0.03 does not pass. With BH, a single p = 0.03 at rank 1 would need p ≤ 0.05/12 as well, so it also fails if the others are larger.

**Step 3.** The result is a hypothesis for a new study with that marker named in advance as the primary endpoint, not evidence that the intervention changed it.

## Limits of this lesson

All p-values are synthetic. The lesson covers the basic procedures; permutation-based corrections, hierarchical testing and estimating the proportion of true nulls are not covered.
