# Sampling, aliasing and a discrete-time PI controller

A controller that runs on a microcontroller does not see the temperature, it sees numbers taken at fixed instants, and it commands the heater with numbers held constant between instants. Two things follow. First, anything in the signal that varies faster than half the sampling rate is not lost but folded back to a lower frequency, where it looks like a real signal; once sampled, it cannot be told apart from one. Second, holding the output between samples is a delay that the loop must tolerate. This lesson explains aliasing and the anti-alias filter, estimates the phase cost of sampling, chooses a sampling period and writes the PI controller as a difference equation. All values are synthetic.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute the apparent frequency of a sampled component and the attenuation of a first-order anti-alias filter.
2. Estimate the phase margin lost to the zero-order hold and choose a sampling period for a loop.
3. Write the discrete PI update and the discrete form of a first-order plant, and compute them for given values.

## Sampling and aliasing

A signal x(t) sampled every T seconds gives x[k] = x(kT), at the sampling frequency f_s = 1/T. The sampling theorem says that a component at frequency f is represented faithfully only if f < f_s/2, the Nyquist frequency. A component above f_s/2 appears at the **alias frequency** |f − n f_s|, where n is the integer that brings the result into the range from 0 to f_s/2. **Synthetic example:** with f_s = 80 Hz, mains interference at 50 Hz appears at |50 − 80| = **30 Hz**, and a component at 140 Hz appears at |140 − 2 × 80| = **20 Hz**.

| Input frequency (Hz) | Alias (Hz) |
|---|---|
| 10 | 10 |
| 30 | 30 |
| 50 | 30 |
| 70 | 10 |
| 100 | 20 |
| 140 | 20 |

Filtering after sampling cannot remove an alias, because it has been moved into the band of interest. The defense is an **anti-alias filter** before the converter, a low-pass filter that attenuates everything above f_s/2. A first-order RC filter with a corner at f_c = 20 Hz has an amplitude ratio of 1/√(1 + (f/f_c)²), which at 50 Hz is **0.3714** (−8.6 dB). That is gentle, which is why anti-alias filters are often of higher order, or the converter samples much faster than the signal needs (oversampling) and the samples are then reduced digitally.

## The cost of holding

A digital-to-analog output holds each value for a whole period (a zero-order hold). Compared with a smooth signal it lags on average by half a period, T/2, which is a pure delay and so costs a phase of ω T/2 at frequency ω. For the PI-controlled incubator of the previous lesson, ω_gc = 0.3333 rad/min and the phase margin is 70.9°. With a sampling period of T = 0.5 min, the hold delay is 0.25 min and costs 0.3333 × 0.25 = 0.0833 rad = **4.77°**, reducing the margin to 66.1°. A common rule is to sample at least ten times per closed-loop time constant: here 1/ω_gc = 3 min, so T should not exceed **0.3 min**.

## The discrete PI controller

Approximating the integral by a sum gives the incremental form of the PI controller:

**u[k] = u[k−1] + K_p (e[k] − e[k−1]) + K_p (T/T_i) e[k].**

The proportional term responds to the change of the error and the last term adds the integral over one period. With K_p = 6.667 W/°C, T_i = 10 min, T = 0.25 min, e[k−1] = 1.2 °C, e[k] = 0.9 °C and u[k−1] = 22.0 W, the new command is 22.0 + 6.667 × (0.9 − 1.2) + 6.667 × (0.25/10) × 0.9 = **20.15 W**. Written this way, anti-windup is easy: clamp u[k] to the actuator limits before storing it as u[k−1], so that the stored value is what the heater actually did.

## The discrete plant

A first-order lag τ dy/dt = −y + K u with an input held constant over each period has the exact discrete form y[k+1] = a y[k] + K(1 − a) u[k] with **a = e^(−T/τ)**. For τ = 10 min and T = 0.25 min, a = **0.97531**. After n samples of a constant input u, the output is K u (1 − aⁿ): for K = 0.5 °C/W and u = 20 W, n = 40 samples (10 min) gives 6.3212 °C, which is 63.2% of the final 10 °C. A delay of 1 min is 4 samples of 0.25 min, so the output does not start to move for 4 samples.

## Common mistakes

- Placing the anti-alias filter after the converter, or omitting it.
- Assuming that a sample rate just above twice the signal frequency is enough once noise is included.
- Forgetting the phase cost of the hold and of the computation delay.
- Writing the integral term without the factor T/T_i, or using the period in the wrong unit.
- Letting the stored controller output exceed the actuator limits, which winds up the integral.
- Using a sampling period that is long compared with the closed-loop time constant.

## Worked example

**Problem.** A synthetic system is sampled at 100 Hz with 60 Hz interference and a first-order anti-alias filter with a corner at 15 Hz. The closed-loop time constant is 5 min. A PI controller has K_p = 0.833, T_i = 5 min and T = 0.5 min. Find the alias, the filter attenuation at 60 Hz, the longest sampling period by the ten-per-time-constant rule and the next controller output.

**Step 1: alias.** |60 − 100| = **40 Hz**.

**Step 2: attenuation.** 1/√(1 + (60/15)²) = **0.2425**.

**Step 3: sampling period.** 5/10 = **0.5 min**; the chosen T = 0.5 min just meets the rule.

**Step 4: update.** With e[k−1] = 2.0, e[k] = 1.5 and u[k−1] = 3.0: u[k] = 3.0 + 0.833 × (1.5 − 2.0) + 0.833 × (0.5/5) × 1.5 = **2.7083**.

## Limits of this lesson

All numbers are synthetic. The lesson treats uniform sampling, a zero-order hold and a linear plant, and the half-period delay is an average; it does not cover quantization noise, computation delay, jitter, multirate sampling or the design of the anti-alias filter beyond its first-order attenuation, and the ten-per-time-constant rule is a rule of thumb.
