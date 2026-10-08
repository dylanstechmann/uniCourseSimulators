# From p-values to evidence: base rates, positive predictive value and replication

A p-value answers the question "if there were no effect, how often would data like these arise?" Readers usually want the reverse: "given these data, how likely is it that the effect is real?" The two questions have different answers, and the gap between them is set by something the data cannot reveal, namely how plausible the hypothesis was before the experiment. The same arithmetic governs diagnostic tests, where a positive result from an accurate test can still mean that the person is probably well, and screening of many biological hypotheses, where a large fraction of "significant" findings can be false even when every analysis was done correctly. This lesson uses Bayes' rule in its simplest form, with natural frequencies, to compute how likely a positive finding is to be true, and what that implies for replication.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute the positive predictive value of a diagnostic test from prevalence, sensitivity and specificity, and express the update with a likelihood ratio.
2. Compute the probability that a statistically significant finding is true from the prior probability of a real effect, the power and the significance level.
3. Evaluate what a significant result, a replication and a screening pipeline can support.

## Natural frequencies for a test

**Synthetic screening test:** prevalence 2%, sensitivity 90% (probability of a positive test if the condition is present) and specificity 95% (probability of a negative test if absent). Think of 10,000 people.

- 200 have the condition; the test is positive in 90% of them, so **180 true positives** and 20 false negatives.
- 9800 do not; the test is falsely positive in 5%, so **490 false positives**.

Of the 670 positive tests, 180 are true, so the **positive predictive value** is 180/670 = **0.269**. A positive result from a test with 90% sensitivity and 95% specificity is more likely a false alarm than not, because the condition is rare. The negative predictive value is 0.998, because a negative test mostly reflects the many unaffected people.

The same update can be written with odds. The **likelihood ratio** of a positive test is LR⁺ = sensitivity/(1 − specificity) = 0.9/0.05 = 18. Prior odds 0.02/0.98 = 0.0204 times 18 give posterior odds of 0.367, a probability of 0.269, the same answer. A strong test multiplies the odds by a large factor, but it starts from small odds.

## The same arithmetic for significant findings

Replace "has the condition" with "the hypothesis is true", prevalence with the **prior probability** π that a hypothesis tested by a lab is true, sensitivity with the **power** of the study, and the false-positive rate with the significance level α. Then

**PPV = power × π / (power × π + α (1 − π)).**

With π = 0.10 (one hypothesis in ten is true), α = 0.05 and power 0.5, PPV = 0.5 × 0.1 / (0.5 × 0.1 + 0.05 × 0.90) = **0.526**: about half of the significant results are true, and the chance that the null hypothesis is actually true for a significant result is 0.47, far from the 0.05 that the threshold might suggest. Raising power to 0.8 gives PPV = 0.64. If the hypotheses tested are riskier, with π = 0.01, even a power of 0.8 gives only 0.14.

Three levers follow:

- **Higher power** (larger samples, less noise) increases the fraction of significant results that are true.
- **A higher prior**, from a strong rationale or earlier independent evidence, increases it more.
- **A stricter threshold or multiplicity control** reduces false positives, as in the lesson on testing many hypotheses at once.

Selective reporting, flexible analysis and testing many outcomes act as a higher effective α and a lower effective π, which is why they reduce the share of true findings.

## What it means for replication

If a significant result is replicated with a new experiment of the same power, the chance that the replication is significant is PPV × power + (1 − PPV) × α. With PPV = 0.53 and power 0.5, this is 0.526 × 0.5 + 0.474 × 0.05 = **0.29**. A failed replication of a single underpowered result is therefore expected much of the time and does not show that the first result was fraudulent or that the second was flawed. Replication is most informative when it is adequately powered, pre-specified and independent. A single result, however small its p-value, is a hypothesis to be confirmed.

## Common mistakes

- Reading "p = 0.04" as "a 4% chance the finding is false".
- Treating a positive result from a good test as near-certain regardless of prevalence.
- Ignoring the base rate when interpreting a screen of many candidates.
- Using the power of an observed effect after the fact to argue for the truth of the finding.
- Expecting a significant result to replicate with probability 95%.
- Treating the prior as something the data supply, when it comes from earlier evidence and judgment.

## Worked example

**Problem.** A second synthetic test has prevalence 10%, sensitivity 80% and specificity 90%. Find the positive predictive value and the likelihood ratio.

**Step 1: 1,000 people.** 100 have the condition: 80 test positive. 900 do not: 90 test positive.

**Step 2: PPV.** 80/(80 + 90) = 0.471.

**Step 3: likelihood ratio.** LR⁺ = 0.8/0.1 = 8.

**Step 4: odds check.** Prior odds 0.111 × 8 = 0.889, which is a probability of 0.471, the same as the PPV.

## Limits of this lesson

All values are synthetic. The prior probability of a hypothesis is rarely known and varies between fields and labs; the formula for significant findings treats each test as a clean yes-or-no event and ignores effect-size distributions, bias and reporting. The aim is to show how the pieces combine, not to estimate a field's false-discovery rate. The same Bayes' rule appears in the genetics lesson on carrier risk.
