# First-order frequency response: an RC low-pass filter for a biological signal

Biological signals are measured alongside noise: electrical interference, thermal noise in amplifiers, and fast fluctuations unrelated to the biology. The simplest defense is a resistor and capacitor arranged as a low-pass filter. Its behavior is fully described by one number, the time constant, which sets a cutoff frequency, and by a frequency response that tells how much each frequency is passed and delayed. This lesson computes those quantities for a synthetic recording front end and shows why a single RC stage is often not enough to prevent aliasing.

## Learning objectives

By the end of this lesson, you should be able to:

1. Derive the transfer function of an RC low-pass filter and compute its time constant and cutoff frequency.
2. Calculate the gain (as a ratio and in decibels) and the phase shift at a given frequency.
3. Evaluate whether a first-order filter adequately suppresses noise and aliasing for a chosen sampling rate.

## The circuit and its transfer function

A resistor R in series with the signal and a capacitor C from the output to ground form a voltage divider whose lower element has impedance 1/(jωC). The ratio of output to input voltage is

**H(jω) = 1 / (1 + jωRC).**

The **time constant** τ = RC sets the step response, V_out(t) = V_in(1 − e^(−t/τ)), and the **cutoff frequency** f_c = 1/(2πRC) is where the output power falls to half (amplitude to 1/√2). **Synthetic front end:** R = 10 kΩ and C = 10 nF give τ = 0.10 ms and f_c = 1591.5 Hz.

## Gain and phase

The magnitude and phase of H are

**|H| = 1/√(1 + (f/f_c)²),** **φ = −arctan(f/f_c).**

- At the signal frequency 100 Hz: |H| = 0.9980 (essentially unchanged), φ = -3.60°.
- At f_c: |H| = 0.707 (−3 dB) and φ = -45°.
- At 10 kHz interference: |H| = 0.1572, which is -16.1 dB.

Well above f_c, the gain falls in proportion to 1/f: a factor of 10 per decade of frequency, or −20 dB per decade. Decibels for amplitude are 20 log₁₀|H|.

Phase matters when timing matters. A filter delays different frequencies by different amounts, which distorts the shape of signals with sharp features. Comparing the time of a peak before and after filtering, or between channels filtered differently, can mislead.

## Sampling and aliasing

A digitizer sampling at f_s can represent frequencies only up to f_s/2 (the Nyquist frequency). Anything above it folds back and appears as a false lower frequency, indistinguishable from real signal once sampled. An analog filter before the converter must therefore reduce content above f_s/2 to below the converter's resolution.

With f_s = 2000 Hz, f_s/2 = 1000 Hz, where this filter still passes 0.847 of the amplitude: almost no protection. Even at 10 kHz it passes 16% of the interference, which would alias to a false low-frequency component. A first-order filter rolls off too gently for this job. Options are a higher-order filter (each additional pole adds −20 dB per decade), a lower cutoff (at the cost of distorting the signal), or sampling faster and filtering digitally.

## Designing the cutoff

Choosing f_c is a compromise between three things: keeping the signal band (here up to a few hundred hertz) nearly flat in gain and phase, attenuating noise and anything above the Nyquist frequency, and keeping component values practical. A common starting point is to set f_c a few times above the highest frequency of interest, then check gain and phase at that frequency. If that leaves too much at the Nyquist frequency, a single RC stage cannot meet both goals, and the remedy is more filter order or a higher sampling rate, not a different single R or C.

Real components have tolerances: a 5% resistor and a 10% capacitor give a cutoff that can be off by roughly 15%, so the design should not depend on f_c being exact.

## Common mistakes

- Using ω (rad/s) and f (Hz) interchangeably; f_c = 1/(2πRC), but ω_c = 1/RC.
- Computing decibels as 10 log₁₀ for an amplitude ratio (that formula is for power).
- Assuming a filter removes everything above its cutoff; at the cutoff it passes 70.7%.
- Forgetting that aliasing cannot be undone after sampling.

## Worked example

**Problem.** You need the 10 kHz interference reduced to 1% of its amplitude with a single RC stage. What cutoff is required, and what happens to the 100 Hz signal?

**Step 1.** For f ≫ f_c, |H| ≈ f_c/f, so f_c ≈ 0.01 × 10000 = 100 Hz.

**Step 2.** At 100 Hz with f_c = 100 Hz, |H| = 1/√(1 + 1) = 0.707 and the phase is −45°.

**Step 3.** The interference requirement costs 29% of the signal amplitude and a large phase shift. The first-order filter cannot separate signals only two decades apart without harming the signal, which is why recording systems use sharper filters.

## Limits of this lesson

Component values are synthetic. The analysis assumes ideal components, a source with negligible resistance and a load with very high impedance; otherwise source and load resistances shift the cutoff (see the sensor-loading lesson).
