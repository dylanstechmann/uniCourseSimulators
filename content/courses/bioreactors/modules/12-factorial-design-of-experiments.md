# Design of experiments: factorial designs, effects, interactions and replication

Process development changes many things at once: temperature, pH, dissolved-oxygen setpoint, feed. The obvious way to learn what matters, to change one factor at a time and keep the others fixed, is also the least efficient, and it cannot see interactions, where the effect of one factor depends on the level of another. A factorial design varies all the factors together in a planned pattern, so every run contributes to every estimate and the interactions can be computed from the same runs. This lesson works through a synthetic two-level design with three factors, computes the main effects and an interaction, uses replicates at the center to estimate noise and curvature, and says what half of a design costs in aliasing. All values are synthetic.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute main effects and interactions from a two-level factorial design.
2. Estimate the standard error of an effect and the curvature from center-point replicates.
3. Evaluate a design for aliasing, randomization and the unit of replication.

## The 2³ design

**Synthetic experiment:** three factors, each at a low and a high level, in all 8 combinations (2³): A = temperature (36.0 °C and 37.0 °C), B = pH setpoint (6.9 and 7.2) and C = dissolved-oxygen setpoint (30% and 60% of air saturation). The response is the peak viable cell density. Each run is an independent culture.

| Run | A temperature | B pH setpoint | C DO setpoint | Peak VCD (10⁶ cells/mL) |
|---|---|---|---|---:|
| (1) | 36.0 °C | 6.9 | 30% | 3.1 |
| a | 37.0 °C | 6.9 | 30% | 3.9 |
| b | 36.0 °C | 7.2 | 30% | 3.3 |
| ab | 37.0 °C | 7.2 | 30% | 4.1 |
| c | 36.0 °C | 6.9 | 60% | 3.4 |
| ac | 37.0 °C | 6.9 | 60% | 4.6 |
| bc | 36.0 °C | 7.2 | 60% | 3.5 |
| abc | 37.0 °C | 7.2 | 60% | 5.0 |

## Main effects

The effect of a factor is the mean response at its high level minus the mean at its low level, averaged over the other factors. For temperature, the four runs at 37.0 °C average 4.400 and the four at 36.0 °C average 3.325, so **A = 1.075** × 10⁶ cells/mL. In the same way B = 0.225 and **C = 0.525**. Every run contributes to every effect, so each effect is a difference of two means of four runs, with standard error σ√(1/4 + 1/4) = 0.707σ. A one-factor-at-a-time study with the same eight runs (a baseline and each factor changed, each in duplicate) would give each effect only two runs per level, a standard error of σ, which is 1.414 times larger, and it would estimate no interactions.

## Interactions

An interaction asks whether the effect of one factor depends on another. Temperature raises the density by 1.35 when the oxygen setpoint is high (the mean of 4.6 − 3.4 and 5.0 − 3.5) and by 0.80 when it is low (the mean of 3.9 − 3.1 and 4.1 − 3.3). The interaction **AC** is half the difference: (1.35 − 0.80)/2 = **0.275**. The warmer culture benefits more from the higher oxygen setpoint, which a one-factor-at-a-time study could not have revealed. The other two-factor interactions are AB = 0.075 and BC = 0.025.

## Noise and curvature: center points

Three additional runs at the center of the region (36.5 °C, pH 7.05, 45% DO) give 4.2, 4.0 and 4.1, with mean 4.10 and standard deviation s = **0.10** on 2 degrees of freedom. The standard error of an effect from a design of N runs is 2s/√N = 2 × 0.10/√8 = **0.0707**. With a two-sided t critical value of 4.303 for 2 degrees of freedom, an effect must exceed about 0.30 to be called different from zero: A (1.075) and C (0.525) do, B (0.225) and AC (0.275) do not, though with only two degrees of freedom the test has little power and AC cannot be dismissed. The center runs also reveal curvature: the center mean (4.10) minus the mean of the factorial runs (3.8625) is **0.2375**, with standard error s√(1/8 + 1/3) = 0.0677, about 3.5 standard errors. A two-level design is blind to curvature, so a bent response means that the best setting may lie inside the region and that a design with more levels is needed next.

## Fractions, aliasing, randomization and blocks

A full two-level design needs 2^k runs: 16 for four factors and 32 for five. A **half fraction** (2^(k−1)) halves the runs by aliasing effects: with the defining relation I = ABCD, each main effect is confounded with a three-factor interaction (A with BCD) and two-factor interactions are confounded in pairs (AB with CD), which is acceptable only if three-factor interactions are negligible. Run order should be **randomized** to protect against drift in medium lots, seed trains and instruments, and runs that cannot be made at the same time should be **blocked** (by day, operator or seed batch) so that block differences do not masquerade as effects. The unit of replication is the independent culture, so repeated samples of one vessel are not replicates, and the noise estimate must come from independent runs.

## Common mistakes

- Changing one factor at a time and concluding that the factors do not interact.
- Estimating noise from repeated samples of the same culture.
- Calling an effect real without comparing it with an estimate of noise.
- Running the experiments in standard order instead of a random order.
- Taking a half fraction without writing down what is aliased.
- Fitting a straight line through points that show curvature.

## Worked example

**Problem.** A synthetic 2² design for a titer (g/L) with A = feed rate and B = seed density gives (1) = 2.0, a = 3.0, b = 2.6 and ab = 4.2. Find the effects and the interaction, and the number of runs for a five-factor full design and its half fraction.

**Step 1: effect of A.** ½[(a − (1)) + (ab − b)] = ½[1.0 + 1.6] = 1.30 g/L.

**Step 2: effect of B.** ½[(b − (1)) + (ab − a)] = ½[0.6 + 1.2] = 0.90 g/L.

**Step 3: interaction.** ½[(ab − b) − (a − (1))] = ½[1.6 − 1.0] = 0.30 g/L.

**Step 4: runs.** 2⁵ = 32 for the full design and 2⁴ = 16 for the half fraction.

## Limits of this lesson

All numbers are synthetic. A two-level design assumes that the response is roughly linear across each range; estimating noise from three center runs is crude; and real process development uses more factors, constraints, several responses and a sequence of designs. The lesson is not a recipe for any process.
