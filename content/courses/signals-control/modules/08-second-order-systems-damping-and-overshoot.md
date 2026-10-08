# Second-order systems: damping, overshoot and ringing in a pressure transducer

Many measuring and mechanical systems store energy in two ways at once and so respond like a mass on a spring: a fluid-filled catheter connected to a pressure transducer (the fluid has inertia, the tubing and diaphragm have compliance), a cantilever probe, a micropipette holder, a balance pan. Such a system is second-order. Depending on its damping it creeps to the new value, reaches it as fast as it can without overshoot, or rings around it, and the ringing can distort a measured waveform badly. This lesson gives the standard second-order model, the formulas for overshoot, peak time and settling time, the link between damping and the frequency response, and what these mean for a measuring line. All values are synthetic.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute the poles, damped frequency, overshoot, peak time and settling time of an underdamped second-order system.
2. Choose a damping ratio for a given overshoot specification.
3. Evaluate how damping and natural frequency shape the amplitude ratio of a measuring system at the frequencies of its signal.

## The standard model

The second-order transfer function with unit DC gain is

**G(s) = ωn² / (s² + 2ζωn s + ωn²),**

with the **natural frequency** ωn (in rad/s) and the **damping ratio** ζ (dimensionless). The poles are s = −ζωn ± jωn√(1 − ζ²) for ζ < 1. The real part −ζωn sets how fast oscillations decay; the imaginary part ωd = ωn√(1 − ζ²) is the **damped frequency** at which the response rings. For ζ = 1 (critical damping) there is a double real pole and no overshoot; for ζ > 1 (overdamped) there are two real poles and the response is a slow creep. From the polynomial s² + 12s + 100, ωn = √100 = 10 rad/s and 2ζωn = 12, so ζ = 12/(2 × 10) = **0.6**.

## Step response measures

For 0 < ζ < 1, the unit step response is y(t) = 1 − e^(−ζωn t) sin(ωd t + φ)/√(1 − ζ²) with cos φ = ζ. Three numbers summarize it:

- **Overshoot** M_p = exp(−πζ/√(1 − ζ²)), the fraction by which the first peak exceeds the final value;
- **Peak time** t_p = π/ωd, when the first peak occurs;
- **Settling time** (to within 2%) t_s ≈ 4/(ζωn), the time for the decaying envelope to fall to 2%.

**Synthetic catheter and transducer:** natural frequency 20 Hz, so ωn = 2π × 20 = 125.7 rad/s, and damping ratio ζ = 0.25. The poles are −31.4 ± j121.7, the damped frequency is ωd = **121.67 rad/s**, the overshoot is **44.43%**, the peak time is **25.82 ms** and the settling time is **127.3 ms**. A pressure step is overshot by almost half before the ringing dies away.

## Choosing the damping

A specification of the form "overshoot no more than 10%" fixes the damping ratio: solving M_p = exp(−πζ/√(1 − ζ²)) for ζ gives ζ = −ln M_p/√(π² + (ln M_p)²). For M_p = 0.10, ζ = **0.5912**, and for the s² + 12s + 100 system the overshoot is 9.48%. More damping removes ringing but slows the response, so the choice is a compromise; for second-order measuring systems a damping ratio near 0.64 to 0.7 gives the flattest amplitude response up to a large fraction of ωn.

## Damping and the frequency response

For a sinusoidal input of frequency f, the amplitude ratio of the second-order system is

**|G| = 1 / √((1 − r²)² + (2ζr)²),  r = f/f_n.**

At the natural frequency (r = 1), |G| = 1/(2ζ), which is **2.0** for ζ = 0.25: a signal at 20 Hz is doubled. A blood-pressure-like waveform at 1.2 Hz has harmonics at multiples of that frequency, and the tenth is at 12 Hz, where r = 0.6. For ζ = 0.25 the amplitude ratio is 1.415, so that harmonic is exaggerated by 41% and the waveform shows spurious peaks; for ζ = 0.64 it is 1.0003, which is flat. The remedy is not to filter the displayed waveform but to add damping or raise the natural frequency, for example by a shorter, stiffer line.

## Common mistakes

- Using the natural frequency in place of the damped frequency to compute the peak time.
- Reading the damping ratio as a percentage, or using ζ and ωn interchangeably.
- Applying the overshoot formula to an overdamped system (ζ ≥ 1), which has none.
- Applying the settling-time formula to a system whose poles are not a single complex pair.
- Forgetting to convert hertz to radians per second (a factor of 2π).
- Assuming that more damping always improves a measurement; it slows the response.

## Worked example

**Problem.** A synthetic measuring line has natural frequency 10 Hz and damping ratio 0.4. Find the damped frequency, overshoot, peak time, settling time and the amplitude ratio at 6 Hz.

**Step 1: frequencies.** ωn = 2π × 10 = 62.83 rad/s and ωd = 62.83 × √(1 − 0.4²) = 57.59 rad/s.

**Step 2: overshoot.** M_p = exp(−π × 0.4/√(1 − 0.4²)) = 25.38%.

**Step 3: times.** t_p = π/57.59 = 0.0546 s = 54.55 ms and t_s = 4/(0.4 × 62.83) = 0.1592 s = 159.2 ms.

**Step 4: amplitude ratio.** At 6 Hz, r = 0.6 and |G| = 1/√((1 − 0.36)² + (2 × 0.4 × 0.6)²) = **1.250**. The value at the natural frequency is 1/(2 × 0.4) = 1.25.

## Limits of this lesson

All numbers are synthetic. The lesson treats a linear second-order model with unit DC gain; it does not cover air bubbles or other changes in a real line that alter its damping, nonlinear damping, or higher-order dynamics, and a real measuring line must be tested (for example by a fast flush) to find its natural frequency and damping.
