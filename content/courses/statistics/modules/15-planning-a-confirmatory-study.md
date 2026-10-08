# Planning a confirmatory study: what a pilot with one p = 0.04 can and cannot support

Small pilot experiments measure many things, and a pilot that finds one promising result among many is a normal event, not a discovery. What a pilot is good for is deciding whether a confirmatory study is worth running and how to design it. This lesson works through a synthetic version of a situation that comes up often: a pilot reports p = 0.04 for one of 18 measured biomarkers, with no outcome chosen in advance and several technical readings from each animal. It uses the earlier lessons together: multiplicity, the unit of analysis, power, the exaggeration of selected effects and the base rate of true hypotheses. The course case on this topic has a three-criterion self-assessment checklist; try it first and then compare your answer with the analysis below.

## Learning objectives

By the end of this lesson, you should be able to:

1. Re-analyze a pilot result with the independent unit and a correction for the number of outcomes examined.
2. Plan the sample size of a confirmatory study from the smallest effect of interest and the variance components, including the number of technical readings.
3. Specify the elements of a pre-specified confirmatory plan and state what the pilot supports and does not support.

## The synthetic pilot

**Design:** 6 animals per group, two groups, 3 technical readings of each sample for each of 18 biomarkers; no primary outcome was named beforehand. **Observation:** for one biomarker the group means differ by **7.0** arbitrary units, and a t-test on all 36 readings gave p = 0.04. **Variance components estimated from the pilot:** between-animal SD 8.5, technical SD 5.0 (so an animal's mean of 3 readings has SD √(8.5² + 5.0²/3) = 8.98, and a single reading has SD √(8.5² + 5.0²) = 9.86).

## Step 1: how surprising is one p < 0.05 among 18?

If none of the 18 markers truly differed, the probability that at least one reaches p < 0.05 is 1 − 0.95^18 = **0.603**, and the expected number of false positives is 18 × 0.05 = 0.9. A single "hit" is therefore the usual outcome, not unusual. Controlling the family-wise error rate at 0.05 with the Bonferroni rule gives a per-test threshold of 0.05/18 = **0.0028**, and the adjusted p-value is min(1, 18 × 0.04) = **0.72**. Nothing in the pilot approaches either bar.

## Step 2: what is the unit of analysis?

The reported test treated the 36 readings as independent observations, with standard error 9.86 × √(2/18) = 3.287, t = 7.0/3.287 = 2.129 on 34 degrees of freedom, p = 0.041. The independent units are the 12 animals. With animals as units, the standard error is 8.98 × √(2/6) = 5.183, so t = 7.0/5.183 = **1.351** on 10 degrees of freedom, and p = **0.21**. Technical readings measure each animal more precisely; they do not add animals, and the earlier lesson on variability showed how much precision a naive analysis invents.

## Step 3: why the pilot's effect is not the planning effect

A marker is highlighted because it was the most extreme of 18, which biases its estimate upward. With animals as the units, a result in this design can be called significant only if the difference between group means exceeds t × SE = 2.228 × 5.183 = **11.5** units, more than twice the 5.0 units that the plan below treats as the smallest difference worth detecting, so a significant pilot necessarily reports a large effect. The exact power of the pilot at a true difference of 5.0 would have been only 0.14. A pilot's best use is its variance components, which are themselves uncertain with only 6 animals per group.

## Step 4: planning the confirmatory sample size

Choose the **smallest effect of interest** from the biology or engineering question, not from the pilot's p-value: here 5.0 units, with power 0.80 and a two-sided α of 0.05 for one pre-specified primary outcome. The unit of analysis is the animal, so the variance of one animal's mean of m readings is σ_b² + σ_t²/m, and the normal approximation gives

**n per group = 2 (1.96 + 0.8416)² (σ_b² + σ_t²/m) / δ².**

| Readings per animal (m) | Variance of an animal's mean | Animals per group |
|---|---|---|
| 1 | 97.25 | 62 |
| 3 | 80.58 | 51 |
| 6 | 76.42 | 48 |

Going from one to three readings saves 11 animals per group; going from three to six saves only 3 more. The exact t-based calculation needs 52 animals per group for m = 3. If an animal costs 20 times as much as a reading, the cost-minimizing number of readings per animal is m = √(σ_t² c_animal / (σ_b² c_reading)) = √(25 × 20 / (72.25 × 1)) = **2.63**, so three readings is near the best use of resources. If the true SD of animal means were 25% larger than the pilot estimate, n would grow by 1.25² to about 80 animals per group, which is why a plan shows how n changes with the assumed variance. Naming all 18 markers as confirmatory outcomes with Bonferroni (z = 2.99 for α = 0.05/18) would need 95 animals per group; naming one primary outcome and reporting the others as exploratory costs 51.

## Step 5: what to write down before the data exist

- The primary outcome, the contrast, the unit (animal) and the test, with α and the direction of the alternative.
- The sample size from Step 4, with the assumptions and a sensitivity range.
- Random assignment of animals to groups, randomized order of sample processing and an operator blind to group.
- How technical readings enter the analysis (averaged within animal, or a nested model) and rules for excluding data, decided before unblinding.
- Which other outcomes are exploratory, or how the family-wise error rate or false discovery rate is controlled across them.
- That all measured outcomes will be reported, with intervals.

## Step 6: reading the result honestly

Even a successful confirmation of one marker with a low prior is one study. The base-rate lesson showed that with a low prior and moderate power a large fraction of significant findings are false, so independent replication carries much of the weight. A confirmatory study that finds a difference near the planning effect with an interval that excludes zero is evidence for the hypothesis; one that finds an interval spanning zero and the planning effect is inconclusive.

## Common mistakes

- Treating one p < 0.05 among many tests as a finding.
- Counting technical replicates as independent observations.
- Planning a sample size from the pilot's observed effect, which was selected for being large.
- Choosing the primary outcome after seeing which marker has the smallest p-value.
- Adding more technical readings to compensate for too few animals.
- Treating variance estimates from six animals per group as exact.

## Worked example

**Problem.** A synthetic pilot measured 12 outcomes in 5 animals per group with 4 readings each, and the best outcome had p = 0.03. Find the chance of at least one p < 0.05 among 12 null outcomes, the Bonferroni threshold and adjusted p-value, and the degrees of freedom with and without pseudoreplication.

**Step 1: chance of a hit.** 1 − 0.95^12 = 0.460.

**Step 2: Bonferroni.** Threshold 0.05/12 = 0.0042; adjusted p = min(1, 12 × 0.03) = 0.36.

**Step 3: units.** Reading-level degrees of freedom would be 40 − 2 = 38; animal-level degrees of freedom are 10 − 2 = 8.

**Step 4: conclusion.** The best p-value of 0.03 among 12 outcomes is compatible with chance, and the test counted 20 readings per group when the design has 5 animals.

## Limits of this lesson

All numbers are synthetic. The normal approximation, the equal variances and the independence of animals are simplifications, and real plans also consider attrition, batch effects, multiple time points and the sampling variability of the variance estimates. This is a planning exercise for analysis, not guidance for any real study or for any person or animal. The lesson draws on the earlier lessons of this package and cites no outside source.
