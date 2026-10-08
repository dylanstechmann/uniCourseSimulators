# Power and sample size: what an experiment can detect, and what a non-significant result means

A statistical test answers a narrow question, "are these data unlikely under no effect?", and whether it can answer "yes" when there really is an effect depends on how much information the experiment holds. That property is the power of the test: the probability of a significant result when a particular true effect exists. Power is chosen at the design stage by choosing the sample size, and it is the reason that small experiments produce results that are both frequently inconclusive and, when they are significant, frequently exaggerated. This lesson computes power and sample size for a two-group comparison, shows how they depend on the effect and on the noise, and draws out the two consequences that matter for reading the literature: a non-significant result from a small study means little, and a significant one from a small study overstates the effect.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute the signal-to-noise ratio, the approximate power and the sample size per group for a two-group comparison.
2. Show how the required sample size scales with the effect size and the variability.
3. Evaluate a small study's results, including the smallest significant difference and the exaggeration of significant estimates, and state what a non-significant result does and does not show.

## Power and the noise in the estimate

For two groups of size n with common standard deviation σ, the standard error of the difference is SE = σ√(2/n). If the true difference is δ, the test statistic is centered near δ/SE (the **signal-to-noise ratio**), and the test succeeds when this value plus chance fluctuation exceeds the critical value.

**Synthetic planning values:** σ = 2.2, δ = 2.8, n = 6 per group. Then SE = 2.2 × √(2/6) = 1.270 and δ/SE = **2.204**. In a normal approximation with a two-sided 5% test (critical value 1.96), power = Φ(δ/SE − 1.96) = Φ(0.244) = 0.60. The exact calculation, using the noncentral t distribution with 10 degrees of freedom (critical value 2.228), gives 0.51, a little lower: the normal approximation is optimistic for small n. With power near one half, such an experiment would miss a real difference of this size about half the time.

## Sample size

Solving for n at a target power gives the normal-approximation formula already used in earlier lessons:

**n per group = 2 (z₁₋α/₂ + z₁₋β)² σ² / δ²,**

with z₁₋α/₂ = 1.96 and z₁₋β = 0.8416 for 80% power. Here n = 2 × (1.96 + 0.8416)² × 2.2² / 2.8² = 9.69, so 10 per group by this formula, and the exact t calculation asks for 11. Two scaling rules follow directly: **n grows with the square of σ/δ**. Halving the effect to δ = 1.4 quadruples the requirement to 38.8 per group (about 39 or more with the exact test), and doubling the standard deviation does the same. The smallest effect worth detecting, not the effect hoped for, should drive the calculation, and σ should come from similar data, not from optimism.

Conversely, with n = 6 per group the effect detectable with 80% power is (z₁₋α/₂ + z₁₋β) × SE = 3.56, or 1.6 standard deviations: only a large effect would be reliably found.

## Two consequences of low power

**A non-significant result is inconclusive.** With power 0.51 for the planning effect, and much less for smaller effects (0.17 for a true δ of 1.4), a non-significant result is uninformative about whether an effect exists. The confidence interval, not the verdict, shows what is compatible with the data.

**A significant result from a small study overstates the effect.** With n = 6 per group, an observed difference must exceed t_crit × SE = 2.228 × 1.270 = **2.83** to be significant. If the true difference is 1.4, then every significant result is at least 2.83/1.4 = **2.0 times** the truth. Selecting significant results from underpowered studies therefore inflates published effects (the "winner's curse"), and replications, which are not selected, find smaller effects.

## Power is not only about n

- **Reduce σ** by better measurement, matched or paired designs, or adjusting for known covariates.
- **Increase the effect** the experiment can detect, for example with a more sensitive readout.
- **Use the right n.** The relevant n is the number of independent units, as in the lesson on variability.
- **Pre-specify** the primary comparison, because testing many outcomes with the same n lowers the power for each after multiplicity is accounted for.
- **Do not compute "observed power"** from the study's own p-value; it carries no information beyond the p-value.

## Common mistakes

- Computing sample size from the effect that was observed in a pilot, which is itself noisy and often inflated.
- Treating "not significant" as "no effect".
- Using technical replicates as the n in a power calculation.
- Forgetting that halving the target effect quadruples n.
- Treating the normal-approximation sample size as exact for small samples.
- Reporting power after the fact from the observed effect.

## Worked example

**Problem.** An experiment will compare two groups with σ = 3 and a smallest effect of interest δ = 2. How many animals per group are needed for 80% power? What power would 6 per group have, and what effect would 6 per group reliably detect?

**Step 1: sample size.** n = 2 × (1.96 + 0.8416)² × 3² / 2² = 35.3, so at least 36 per group.

**Step 2: power at 6 per group.** SE = 3 × √(2/6) = 1.73; δ/SE = 1.15; power ≈ Φ(−0.81) = 0.21.

**Step 3: detectable effect.** With 6 per group, 80% power needs δ ≈ (1.96 + 0.8416) × 1.73 = 4.85, more than twice the effect of interest.

**Step 4: decision.** Either use 36 per group, reduce σ, or accept that the experiment can answer only a question about a much larger effect.

## Limits of this lesson

All values are synthetic. The normal approximation assumes known σ and symmetric tests; exact power for t-tests, and power for other designs and analyses, requires the appropriate distributions or simulation. The effect size for planning is a judgment about what matters scientifically, which no calculation supplies.
