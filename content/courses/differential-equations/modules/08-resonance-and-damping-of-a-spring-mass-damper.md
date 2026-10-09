# Resonance and damping: free decay and forced oscillation of a spring–mass–damper

A great deal of laboratory and biological mechanics reduces to a mass on a spring with some friction: a balance pan, a cantilever probe, a micropipette holder, the chest wall in breathing, a shaker platform for culture flasks. The second-order equation m x″ + c x′ + k x = F(t) describes how such a system rings down after a disturbance and how it responds when it is driven periodically. Driving near the natural frequency produces a large response, called resonance, which can be a useful amplifier or a hazard, and the damping decides how large it is. This lesson solves the free and the forced equation, defines the logarithmic decrement and the quality factor, and works the numbers for a synthetic balance pan. All values are synthetic.

## Learning objectives

By the end of this lesson, you should be able to:

1. Solve the free second-order equation and compute the natural frequency, damping ratio and damped period.
2. Use the logarithmic decrement to relate decay to damping, and the amplitude of successive oscillations.
3. Compute the steady-state amplitude of the forced oscillation across frequency and evaluate the resonance and its bandwidth.

## The free response

With x measured from equilibrium, m x″ + c x′ + k x = 0. Trying x = e^(λt) gives m λ² + c λ + k = 0, with roots λ = −c/(2m) ± √((c/2m)² − k/m). Define the **natural frequency** ωn = √(k/m) and the **damping ratio** ζ = c/(2√(km)); the critical damping coefficient is c_c = 2√(km). Three cases follow. If ζ < 1 (underdamped), λ = −ζωn ± jωd with ωd = ωn√(1 − ζ²), and x = A e^(−ζωn t) cos(ωd t − φ): an oscillation under a decaying envelope. If ζ = 1, there is a double real root and the fastest return without oscillation. If ζ > 1, two real negative roots give a slow, non-oscillating return.

**Synthetic balance pan:** m = 0.2 kg, k = 80 N/m and c = 1.2 N·s/m. Then ωn = √(80/0.2) = **20 rad/s** (3.18 Hz), c_c = 2√(80 × 0.2) = 8 N·s/m, and ζ = 1.2/8 = **0.15**. The roots are λ = −3.0 ± j19.77 s⁻¹, the damped frequency is ωd = 19.774 rad/s, and the damped period is 2π/ωd = **0.3178 s**.

## The logarithmic decrement

Successive peaks of the free oscillation are one damped period apart, and the ratio of consecutive peak heights is constant: x_n/x_(n+1) = e^δ with **δ = 2πζ/√(1 − ζ²)**. Measuring the decay of a ringing system therefore gives its damping without knowing the mass or the stiffness. Here δ = 2π × 0.15/√(1 − 0.15²) = **0.9533**. After three cycles the peak height is e^(−3δ) = **0.0573** of its starting value, and after ten cycles it is 0.007% of it. A system with ζ = 0.01 would need many more cycles to settle, which is why lightly damped probes and balances need an added damper or a long wait.

## Forced oscillation and resonance

Now drive the system with a force F cos ωt. After the free transient has decayed (a few times 1/(ζωn)), the displacement oscillates at the driving frequency with amplitude

**X = (F/k) / √((1 − r²)² + (2ζr)²),  r = ω/ωn.**

The static deflection is F/k = 0.5/80 = 6.25 mm. At r = 1, X = (F/k)/(2ζ) = **20.83 mm**, which is the static deflection multiplied by the quality factor Q = 1/(2ζ) = 3.33. A peak at nonzero frequency exists only for ζ < 1/√2. Here the maximum amplitude occurs slightly below the natural frequency, at r = √(1 − 2ζ²) = 0.9772, where X = 21.07 mm. For ζ ≥ 1/√2 the amplitude instead decreases from its static value as frequency rises. At r = 0.5 (half the natural frequency) the response is only X = **8.17 mm**, and well above resonance it falls toward zero. The width of the resonance peak at half power (amplitude 1/√2 of the peak) is approximately 2ζωn = **6.0 rad/s** for light damping; a narrow peak means a large Q and a sharp tuning.

The phase lag of the response relative to the force goes from near 0° at low frequency, through 90° at ω = ωn, to near 180° at high frequency. The 90° crossing is at the natural frequency, rather than the slightly lower amplitude peak. At high frequency the displacement caused by a fixed force becomes small. Vibration isolation also uses a soft support with a natural frequency well below the disturbance frequency, but motion imposed through the base of a mount has a different transfer function from the direct-force response derived here.

## Common mistakes

- Using the damped frequency ωd where ωn belongs in the amplitude formula.
- Confusing the damping coefficient c with the damping ratio ζ.
- Computing the log decrement from the ratio of peak heights over several cycles without dividing by the number of cycles.
- Treating the peak of the forced response as the natural frequency (it is at √(1 − 2ζ²) ωn, which is lower).
- Applying the steady-state amplitude before the free transient has died out.
- Mixing units: millimetres and metres in F/k.

## Worked example

**Problem.** A synthetic mount has m = 0.05 kg, k = 20 N/m and c = 0.4 N·s/m, and a force of 0.2 N is applied. Find ωn, ζ, ωd, the log decrement, the amplitude at resonance and Q.

**Step 1: frequencies.** ωn = √(20/0.05) = **20 rad/s** and ζ = 0.4/(2√(20 × 0.05)) = **0.2**, so ωd = 20 × √(1 − 0.2²) = 19.596 rad/s.

**Step 2: decay.** δ = 2π × 0.2/√(1 − 0.2²) = **1.2825**.

**Step 3: resonance.** The static deflection is 0.2/20 = 10.0 mm. At r = 1, X = 10.0/(2 × 0.2) = **25.0 mm**, and Q = 1/(2 × 0.2) = 2.5.

## Limits of this lesson

All numbers are synthetic. The lesson treats a single linear mass with viscous damping and a sinusoidal force; real structures have several modes, friction that is not viscous and forces that are not sinusoidal, and the amplitude formulas hold only in steady state.
