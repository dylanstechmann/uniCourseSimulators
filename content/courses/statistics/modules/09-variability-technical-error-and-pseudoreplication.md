# Sources of variability: biological variation, technical error and the standard error

Two experiments can both produce twelve numbers and yet contain very different amounts of information. If twelve numbers come from twelve independent animals, they say a lot about animals in general. If they are three readings from each of four animals, they say much less, because readings from the same animal share that animal's biology. Statistical inference works only when its unit of analysis matches the unit that could vary independently. This lesson separates the two main sources of variation in a measurement, shows how each enters the standard error of a mean, quantifies how badly a naive analysis can overstate precision when nested readings are treated as independent, and answers the practical question of where to spend replication effort. All values are in arbitrary units.

## Learning objectives

By the end of this lesson, you should be able to:

1. Distinguish biological variation from technical (measurement) error and estimate the technical error from replicate measurements.
2. Compute the standard error of a mean for nested data, the intraclass correlation and the effective sample size.
3. Evaluate how replication should be allocated between independent biological units and repeated measurements, and what a naive analysis overstates.

## Two kinds of variation

A measurement on a sample varies for two different reasons.

- **Biological (between-unit) variation** is real difference among the units being studied: animals, donors, cultures prepared on different days. It is what a conclusion about a population must account for.
- **Technical (measurement) error** is the scatter you get when the same unit is measured again: pipetting, instrument noise, plate position. It carries no information about other units.

A simple model writes a reading as y = μ + b + e, where b is the unit's deviation from the population mean (with standard deviation σ_b) and e is the measurement error (σ_t). Readings from one unit share b and differ only through e; readings from different units differ through both.

**Estimating technical error.** Measure each of several samples twice. The difference between the two readings of a sample removes b and leaves only the difference of two errors, whose standard deviation is √2 × σ_t. If the differences have a standard deviation of 7.07, then σ_t = 7.07/√2 = 5.0.

## The standard error with nested readings

Suppose n units are each measured k times and the unit means are averaged. Averaging k readings reduces only the technical part:

**Var(grand mean) = σ_b²/n + σ_t²/(n k),** and the standard error is its square root.

**Synthetic values:** σ_b = 10 and σ_t = 5.

| Design | Animals n | Readings per animal k | Standard error |
|---|---:|---:|---:|
| Baseline | 4 | 1 | 5.59 |
| More readings | 4 | 3 | 5.20 |
| More animals | 12 | 1 | 3.23 |

Tripling the readings per animal lowers the standard error by 7%, because it can shrink only the σ_t² term and the large σ_b² term is untouched. Tripling the number of animals lowers it by 42%. Beyond a small number of replicates per unit, further technical replication adds almost nothing, while each additional independent unit helps.

## What a naive analysis overstates

Suppose the four animals × three readings are analyzed as 12 independent numbers. The total standard deviation of one reading is √(σ_b² + σ_t²) = 11.18, and the naive standard error is 11.18/√12 = 3.23. The correct standard error is 5.20, which is 1.61 times larger. The naive analysis reports a precision that belongs to twelve independent animals, not four. Confidence intervals would be too narrow and p-values too small. This error is called **pseudoreplication**.

Two summaries quantify the clustering.

- The **intraclass correlation**, ICC = σ_b²/(σ_b² + σ_t²) = 100/125 = 0.80, is the share of variance that is between units. It is also the **reliability** of a single reading: 80% of its variance is real between-unit signal. The mean of three readings has a reliability of 92%.
- The **design effect** for k readings per unit is DEFF = 1 + (k − 1) ICC = 1 + 2 × 0.80 = 2.6, so the 12 readings are worth only 12/2.6 = **4.6 independent observations**, close to the 4 animals.

## Allocating replication

The question to ask is which variance term dominates. When σ_b is large relative to σ_t, as here, spend on more units. When measurement error is large and units are scarce or expensive, replicates per unit are valuable, up to the point where σ_t²/k is small relative to σ_b². With k = 3, the standard error reaches 3.0 only with n = (100 + 25/3)/9 = 12 animals. The calculation uses the unit that could vary independently: for a mouse experiment, the mouse; for cell culture, the independent culture or day; for a person, the person.

## Where this matters

- A pilot with three technical replicates per sample has the biological sample size of the number of samples, not three times that number.
- Wells in one plate, images from one well and sections from one animal are nested; analyzing them as independent inflates confidence.
- The right analysis averages within units first (or uses a model that includes the unit as a random effect) and carries the number of units into the inference.

## Common mistakes

- Counting technical replicates as biological replicates.
- Reducing the standard error by adding readings per unit when σ_b dominates.
- Computing a standard error from all readings pooled, as if independent.
- Estimating technical error from different units rather than repeated measurements of the same unit.
- Forgetting the factor √2 when converting the standard deviation of paired differences to a measurement error.
- Treating the ICC as a property of the instrument, when it depends on the population being measured.

## Worked example

**Problem.** Five synthetic animals are each measured twice, with σ_b = 6 and σ_t = 6. Compare the correct and naive standard errors of the grand mean, and find the effective sample size.

**Step 1: correct standard error.** √(6²/5 + 6²/(5 × 2)) = √(7.2 + 3.6) = 3.29.

**Step 2: naive standard error.** The total standard deviation is √(6² + 6²) = 8.49, so the naive standard error is 8.49/√10 = 2.68, which is 1.22 times too small.

**Step 3: clustering.** ICC = 36/72 = 0.50, DEFF = 1 + (2 − 1) × 0.50 = 1.50, and n_eff = 10/1.50 = 6.7.

**Step 4: reading the result.** Ten readings are worth 6.7 independent observations; the experiment has five animals, and its inference should reflect that.

## Limits of this lesson

All values are synthetic and in arbitrary units. The two-level model assumes equal variances and balanced data; real designs can have more levels (cells within wells within animals within litters), unequal replication and variances that change with the mean. The lesson explains the logic and does not replace fitting a mixed model.
