# Convolution and impulse response: why a sensor blurs and delays what it measures

No sensor responds instantly. An oxygen probe, a temperature sensor or a fluorescent reporter integrates its input over some time, so the recorded signal is a smoothed and delayed version of the real one. For linear time-invariant systems, one function describes this completely: the impulse response. The output is the input convolved with it. This lesson computes a discrete convolution by hand, connects a first-order sensor's impulse response to its step and ramp responses, and shows how to correct, or at least account for, the lag.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute the output of a discrete linear time-invariant system by convolving an input sequence with an impulse response.
2. Relate a first-order sensor's impulse response to its step response and time constant, and to its transfer function.
3. Quantify the lag and error a first-order sensor introduces for step and ramp inputs, and evaluate strategies to correct them.

## Linearity, time invariance and the impulse response

A system is **linear** if scaling and adding inputs scales and adds outputs, and **time-invariant** if delaying the input simply delays the output. For such a system, if h is its response to a brief unit impulse, the response to any input x is the **convolution**

**y[n] = Σₖ h[k] x[n − k]** (discrete), or y(t) = ∫ h(τ) x(t − τ) dτ (continuous).

Each output sample is a weighted sum of current and past inputs, with h supplying the weights.

**Synthetic discrete example.** A sampled sensor has impulse response h = [0.5, 0.3, 0.2] (weights for the current sample and the two before it; they sum to 1, so a constant input is reproduced exactly). The input x = [0, 0, 1, 1, 1, 0, 0] is a three-sample pulse. Convolving gives y = [0.0, 0.0, 0.5, 0.8, 1.0, 0.5, 0.2, 0.0, 0.0]. The pulse is spread over five samples, its edges are softened, and its peak is lower only where the window overlaps the pulse edges. The output is longer than the input by len(h) − 1 samples.

## The first-order sensor

Many sensors behave like a first-order system: τ dy/dt = x − y, with transfer function **H(s) = 1/(τs + 1)**. Its impulse response is h(t) = (1/τ) e^(−t/τ): a recent input matters most, and older inputs fade with time constant τ. With τ = 2 s, h(0) = 0.5 s⁻¹ and h at 1, 2 and 3 s is 0.3033, 0.1839 and 0.1116 s⁻¹.

The **step response** is the integral of the impulse response: y(t) = 1 − e^(−t/τ). After one τ the sensor shows 63% of a sudden change, after 2τ = 4 s it shows 86.5%, and only after about 5τ is it within 1%.

## Lag on a ramp

If the true signal rises steadily at rate a (a ramp), a first-order sensor eventually follows it with the same slope but a constant **lag of τ seconds**, so its reading is too low by a × τ. For a signal rising at 0.5 units/s and τ = 2 s, the steady error is 1.0 units. In a fast-changing experiment (an oxygen drop when cells are added, a temperature transient when a door opens) the sensor can miss the true extreme and report events late.

## Correcting for the sensor

- **Choose a faster sensor**, with τ well below the time scale of interest.
- **Model-based correction (deconvolution):** for a first-order sensor, x ≈ y + τ dy/dt. This recovers the input but amplifies noise, because it differentiates; it needs smoothing and a well-known τ.
- **Report the response time with the data**, so readers know which features could not have been resolved.
- **Compare like with like:** two sensors with different τ will report different peak values for the same event.

## Common mistakes

- Treating a sensor's reading during a transient as the true value.
- Forgetting that convolution makes the output longer than the input.
- Deconvolving noisy data without filtering, which amplifies noise.
- Using a step response time from the datasheet that was measured under different conditions (flow, temperature, membrane condition).

## Worked example

**Problem.** A dissolved-oxygen sensor with τ = 2 s reads 60% of saturation 4 s after a sudden change from 100% to 20%. What was the true value, and how should the reading be interpreted?

**Step 1.** For a step, the reading is y = 20 + (100 − 20)e^(−t/τ). At t = 4 s, y = 20 + 80 × e^(−2) = 30.8%.

**Step 2.** The observed 60% is higher than this prediction, which would mean either τ is longer than stated or the change was not instantaneous.

**Step 3.** Either way, the true level has already reached 20% (if the step was sudden), and the sensor is lagging. Waiting 5τ = 10 s before reading, or fitting the exponential to estimate the final value, gives a value that reflects the medium rather than the sensor.

## Limits of this lesson

The sensor model is a synthetic first-order system; real sensors can have dead time, nonlinearity and drift. Convolution applies only to linear time-invariant behavior.
