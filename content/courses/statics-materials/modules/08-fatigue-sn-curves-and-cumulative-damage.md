# Fatigue under cyclic loading: S–N curves, Basquin's law, mean stress and cumulative damage

A part can survive a load once and fail after the same load has been applied a million times. A scaffold that is perfused with a pulsatile flow, a heart-valve leaflet, a bone plate and a pump tube all see repeated loads, and a crack that grows a little in each cycle is a failure mode to check in each. Fatigue is described by a few numbers: the amplitude and mean of the cycle, the number of cycles to failure at that amplitude, and a rule for combining cycles at different levels. This lesson defines the cycle, uses Basquin's law for the S–N curve, corrects for mean stress, sums damage over blocks of different loading, and states what makes fatigue data scatter. All values are synthetic.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute the stress amplitude, mean stress and stress ratio of a cycle.
2. Use Basquin's law to estimate life at a stress amplitude and how it responds to small changes in stress.
3. Apply a mean-stress correction and Miner's rule, and evaluate their limits and the scatter of fatigue data.

## The cycle

A cyclic load swings between a maximum and a minimum stress. The **stress amplitude** is σ_a = (σ_max − σ_min)/2, the **mean stress** is σ_m = (σ_max + σ_min)/2, and the **stress ratio** is R = σ_min/σ_max. **Synthetic cycle:** σ_max = 200 MPa and σ_min = 20 MPa give σ_a = **90 MPa**, σ_m = **110 MPa** and R = **0.1**. A fully reversed cycle has σ_m = 0 and R = −1. Fatigue lives are usually reported against the amplitude, with the mean stress and R stated, because a tensile mean stress shortens life.

## Basquin's law

For many metals and for polymers in a range of lives, the stress amplitude and the number of cycles to failure N_f fall on a straight line in log–log coordinates:

**σ_a = σ_f′ (2N_f)^b,**

with σ_f′ a fatigue strength coefficient and b a negative exponent. **Synthetic values:** σ_f′ = 900 MPa and b = −0.1. Solving for the life, N_f = ½ (σ_a/σ_f′)^(1/b). At σ_a = 300 MPa, N_f = ½ × (1/3)^(−10) = **29,525 cycles**; at 200 MPa, N_f = **1,702,531 cycles**. The exponent is small, so the life is very sensitive to stress: reducing the amplitude by 10% multiplies the life by 0.9^(−10) = **2.87**. This is why small errors in the stress, for example by neglecting a stress concentration, give large errors in life, and why fatigue calculations carry large safety factors on life.

## Mean stress: the Goodman correction

Life data are usually measured at zero mean stress. For a part with a tensile mean stress, the Goodman relation limits the combination of amplitude and mean:

**σ_a/σ_e + σ_m/σ_u = 1/n,**

with σ_e the endurance limit for fully reversed loading, σ_u the ultimate strength and n a safety factor. With σ_e = 150 MPa, σ_u = 600 MPa and σ_m = 200 MPa, the allowable amplitude for n = 1 is σ_a = 150 × (1 − 200/600) = **100 MPa**, instead of 150 MPa at zero mean. Not every material has an endurance limit; many polymers and materials in a corrosive environment continue to lose life at all amplitudes.

## Cumulative damage: Miner's rule

Real loading is a sequence of blocks of different amplitudes. Miner's rule assigns each block the fraction of life it uses, n_i/N_i, and predicts failure when the sum reaches 1:

**D = Σ n_i/N_i.**

For 10,000 cycles at 300 MPa (N = 29,525) and 500,000 cycles at 200 MPa (N = 1,702,531), D = 10,000/29,525 + 500,000/1,702,531 = 0.339 + 0.294 = **0.632**. About 37% of the life remains. The rule ignores the order of the blocks and the interaction of high and low loads, and the sum at failure of real specimens varies widely around 1, so it is a bookkeeping tool and not a precise prediction.

## Scatter, run-outs and the environment

Fatigue lives of nominally identical specimens vary by a factor of several and often by ten or more, and the scatter is approximately log-normal. A fatigue test therefore uses several specimens at each level, reports the mean of log N with its spread, and treats specimens that have not failed at the cutoff (run-outs) as censored observations, not failures: leaving them out biases the estimated life downward, because the longest-lived specimens are the ones dropped, and counting each as a failure at the cutoff still biases it downward, because its true life is longer (see the time-to-event lesson in the statistics course). Humidity, temperature and the test frequency change lives, especially for hydrated polymers, which heat up when cycled quickly.

## Common mistakes

- Using the stress range where the amplitude is needed, or the reverse.
- Using life data from zero mean stress for a part with a large tensile mean stress.
- Neglecting stress concentrations, which multiply the local amplitude.
- Reading Miner's sum of 1 as a precise prediction.
- Dropping run-outs from the analysis.
- Assuming that a material has an endurance limit below which it never fails.

## Worked example

**Problem.** A synthetic material has σ_f′ = 800 MPa and b = −0.12. Find the life at σ_a = 250 MPa and at 200 MPa, the Miner sum for 2,000 cycles at 250 MPa and 15,000 cycles at 200 MPa, and the minimum stress of a cycle with σ_a = 60 MPa, σ_m = 90 MPa.

**Step 1: lives.** N_f(250) = ½ (250/800)^(1/−0.12) = 8,101; N_f(200) = 52,016 cycles.

**Step 2: Miner sum.** D = 2,000/8,101 + 15,000/52,016 = 0.247 + 0.288 = 0.535.

**Step 3: cycle.** σ_max = σ_m + σ_a = 150 MPa and σ_min = σ_m − σ_a = 30 MPa, so R = 0.20.

**Step 4: reading the result.** The two blocks use 54% of the life, so the remaining life is 46%; with the scatter of fatigue data, the margin should be wide.

## Limits of this lesson

All numbers are synthetic. Basquin's law is an empirical fit over a range of lives, the Goodman line is a conservative engineering relation, and Miner's rule is an approximation; real components need tests of the actual geometry and environment. Nothing here is a design check for any part.
