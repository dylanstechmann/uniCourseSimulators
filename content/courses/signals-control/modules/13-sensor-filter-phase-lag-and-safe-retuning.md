# When a sensor filter makes a fast loop oscillate: phase lag, crossover and a safe retuning sequence

This lesson works through the course case. A temperature controller tracks its setpoint quickly. A noisy sensor reading then prompts someone to add a low-pass filter to the measurement, and afterwards the loop oscillates. Nothing about the heater or the incubator has changed, and the filter even does what it was meant to do. The cause is in the loop, not the parts: every lag in a feedback path costs phase at the crossover frequency, and the margin that was adequate before is not afterwards. The questions are how to see this from numbers you already have, which changes restore the margin, and in what order to make and test them. The course case has a three-criterion self-assessment checklist; try it first, then compare your answer with the analysis below. All values are synthetic.

## Learning objectives

By the end of this lesson, you should be able to:

1. Explain, with the phase and the crossover frequency, why a measurement filter can turn a well-damped loop into an oscillatory one.
2. Compute the phase margin before and after the filter, the gain that restores a target margin, and the trade-off with noise.
3. Outline a retuning sequence that changes one thing at a time and verifies the measured margin, saturation and disturbance behavior before deployment.

## The synthetic loop

The plant is the incubator of the earlier lessons (time in minutes): G(s) = 0.5 e^(−s)/(10s + 1), with a PI controller tuned by cancelling the plant lag. With the aggressive setting λ = 0.5 min, K_p = 10/(0.5 × (0.5 + 1)) = 13.33 W/°C and T_i = 10 min. The loop is an integrator with a delay, L₀(s) = 0.6667 e^(−s)/s. Its gain crossover is **ω_gc = 0.6667 rad/min**, and the phase margin is 90° − 38.20° = **51.8°**. By the rule ζ ≈ PM/100 the closed loop has an overshoot of about 15%: fast and reasonably damped.

## What the filter does

The probe is noisy, so a first-order filter F(s) = 1/(τ_f s + 1) with τ_f = 1 min is added in the feedback path. The loop is now L₁ = L₀ F, and the filter has two effects at the old crossover frequency. Its phase is −atan(0.6667 × 1) = **−33.69°**, almost 34° more lag, and its magnitude is below 1, which moves the crossover down. Solving 0.6667/(ω√(1 + ω²)) = 1 gives the new crossover **ω_gc = 0.5774 rad/min**, where the phase is −90° − 33.08° − 30.00° = −153.08°. The **phase margin falls from 51.8° to 26.9°** and the rule of thumb predicts an overshoot of about 42%. The loop is not unstable, but it rings, and with a plant whose gain is 30% higher than modelled the margin would be only 14.2°. The delay margin is 0.4698/0.5774 = 0.81 min.

## The trade-off

The filter is not a mistake; it removes noise. With the original gain, the effect of the filter time on the margin and on the noise passed at 6 rad/min (a period of about 1 min) is:

| τ_f (min) | ω_gc (rad/min) | Phase margin | Noise amplitude ratio at 6 rad/min |
|---|---|---|---|
| 0 | 0.667 | 51.8° | 1.000 |
| 0.25 | 0.658 | 43.0° | 0.555 |
| 0.5 | 0.635 | 36.0° | 0.316 |
| 1 | 0.577 | 26.9° | 0.164 |
| 2 | 0.481 | 18.6° | 0.083 |

A faster filter (τ_f = 0.25 min) keeps a margin of 43.0° but passes 3.4 times more of the noise than the 1 min filter. There is no free choice: either the filter is slow and the gain is lower, or the filter is fast and the noise is passed. Three options restore the margin: lower the gain, shorten the filter, or add phase lead (a derivative term), which amplifies exactly the noise the filter was added to remove. A fourth option is to move the filter out of the loop: smooth the logged or displayed signal and leave the control signal with its original, faster sensor.

## Lowering the gain

To restore a phase margin of 45° with τ_f = 1 min, the phase at the crossover must be −135°: 90° + 57.30 ω + atan(ω) = 135° gives **ω_gc = 0.4026 rad/min**. The loop gain needed is 0.4340 = ω√(1 + ω²), so K_p = 0.4340 × 10/0.5 = **8.68 W/°C**, a reduction of **35%** from 13.33. The loop is slower (a crossover of 0.40 instead of 0.67 rad/min) but well damped, and with a plant gain 30% higher than modelled the margin is still 34.4°.

## A safe retuning sequence

1. **Record the baseline.** Before changing anything, log a small setpoint step (about 1 °C, small enough that the heater does not saturate): the overshoot, the settling time, the heater power and the fraction of time at its limits.
2. **Predict before acting.** Compute the phase lost to the filter at the present crossover and the new margin. Do not leave the old gain in place with the new filter.
3. **Change one thing at a time.** Lower K_p in stages (here 13.3, then about 11.0, then 8.7 W/°C), each time repeating the small step.
4. **Measure the margins.** Check the phase margin and the gain margin with a frequency test (small sinusoids in the heater power, as in the Bode lesson) or a relay test, and accept a stage only if the phase margin is at least 45° and the gain margin at least 2.
5. **Test saturation and disturbances.** Run a large start-up step with the anti-windup clamp active and watch the overshoot, then apply a disturbance (open the door, change the room temperature) and confirm the loop recovers without oscillation.
6. **Check robustness and log it.** Repeat with the plant gain varied by ±30% if the plant can be changed, and record the final settings, margins and tests.

## Common mistakes

- Adding a filter to the feedback path and leaving the gain unchanged.
- Judging a filter only by the noise it removes, not by the phase it adds at the crossover.
- Restoring the margin by adding derivative action without checking the noise it passes.
- Retuning without a baseline measurement, so that no change can be attributed.
- Changing the gain and the filter in the same step.
- Accepting a tuning on a small-step test alone, without testing saturation and a disturbance.

## Worked example

**Problem.** A synthetic plant has K = 1.2, τ = 5 min and θ = 2 min, with a PI controller tuned by cancellation with λ = 2 min. A filter with τ_f = 1.5 min is added. Find the phase margin before and after, and the gain that restores 45°.

**Step 1: tuning.** K_p = 5/(1.2 × (2 + 2)) = 1.0417, loop gain K_pK/τ = 0.2500, so ω_gc = 0.2500 rad/min and PM = 90° − 28.65° = **61.4°**.

**Step 2: with the filter.** Solving 0.2500/(ω√(1 + (1.5ω)²)) = 1 gives ω_gc = 0.2357 rad/min, and the phase margin is **43.5°**, a loss of 17.8°.

**Step 3: restoring 45°.** The crossover for a phase of −135° is 0.2280 rad/min, which needs a loop gain of 0.2409, so K_p = 0.2409 × 5/1.2 = **1.004**, compared with 1.0417.

## Limits of this lesson

All numbers are synthetic. The lesson treats a lag-plus-delay plant tuned by cancellation and a first-order filter; the rule ζ ≈ PM/100 is an approximation, and the retuning sequence is an outline of how to reason, not a procedure for any real incubator or process, whose limits, alarms and safety interlocks come first.
