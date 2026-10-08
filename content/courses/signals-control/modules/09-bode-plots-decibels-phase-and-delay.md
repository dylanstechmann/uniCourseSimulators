# Reading Bode plots: gain in decibels, phase, corner frequencies and the cost of a delay

A heater, a sensor or a controller responds differently to a slow change than to a fast one. If a sinusoid of angular frequency ω goes into a linear system, a sinusoid of the same frequency comes out, with a different amplitude and shifted in time. The ratio of the amplitudes, as a function of ω, and the phase shift are the **frequency response** G(jω), and plotting them against frequency on logarithmic axes gives the Bode plot. The plot shows at a glance which frequencies a system passes, how much time it loses to lags and delays, and how close a feedback loop around it is to oscillating, which the next lesson turns into numbers. All values are synthetic.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute the magnitude in decibels and the phase of a first-order lag with a time delay at a given frequency.
2. Combine the magnitudes and phases of cascaded elements and convert a phase lag into a time lag.
3. Interpret the corner frequency, slopes and phase of a Bode plot and what a delay does to them.

## Magnitude, decibels and phase

For G(s), the frequency response is G(jω), a complex number with magnitude |G(jω)| and phase φ(ω). A gain is usually quoted in **decibels**, 20 log₁₀|G|: a factor of 2 is +6.02 dB, a factor of 10 is +20 dB, and a factor of 0.5 is −6.02 dB. The reason is that elements in series multiply their magnitudes and add their phases, so their decibel gains and phases simply add.

## The first-order lag

For G(s) = K/(τs + 1), the magnitude is |G| = K/√(1 + (ωτ)²) and the phase is φ = −atan(ωτ). The **corner frequency** is ω = 1/τ: there the magnitude is K/√2, which is 3.01 dB below the DC gain, and the phase is −45°. Well below the corner the magnitude is flat at K and the phase near 0°. Well above it the magnitude falls at 20 dB for every factor of ten in frequency (**−20 dB/decade**) and the phase approaches −90°.

## A pure delay

A delay of θ has transfer function e^(−θs), whose magnitude is exactly 1 at every frequency and whose phase is −ωθ radians, or −57.30 ωθ degrees. A delay therefore does not change the gain but removes phase in proportion to frequency; on a plot with a logarithmic frequency axis its phase falls faster and faster. This is why a delay, even a small one, limits how fast a feedback loop can be made.

## An incubator-like plant

**Synthetic plant (time in minutes):** G(s) = K e^(−θs)/(τs + 1) with K = 0.5 °C/W, τ = 10 min and θ = 1 min. The DC gain is 0.5 = **−6.02 dB** and the corner frequency is 1/τ = **0.1 rad/min** (a period of 63 min). At the corner, the magnitude is 0.3536, which is −9.03 dB.

At ω = 0.5 rad/min (a period of 12.6 min) the lag term gives |G| = 0.5/√(1 + 5²) = 0.09806, which is **−20.17 dB**, and a phase of −atan(5) = −78.69°. The delay adds −0.5 × 1 rad = −28.65°, so the total phase is **−107.34°**. A phase lag of 107.34° at 0.5 rad/min corresponds to a time lag of 1.8734 rad/0.5 = **3.747 min** between the heater power and the temperature.

## Cascades

A temperature probe has its own lag. Adding a probe with transfer function 1/(2s + 1) multiplies the response by 1/√(1 + (0.5 × 2)²) = 0.7071 (−3.01 dB) and adds −45° at ω = 0.5. The cascade has a magnitude of −20.17 + (−3.01) = **−23.18 dB** and a phase of **−152.34°**. The extra lag has pushed the phase well past −90°; in a feedback loop that matters a great deal.

## Slopes and measurement

Between 1 and 10 rad/min the lag term alone changes the magnitude by −19.96 dB, close to the asymptotic −20 dB/decade. A real frequency response is measured by driving the system with sinusoids of several frequencies (small enough to stay within the linear range of the actuator) and recording the output amplitude ratio and the time shift between peaks. The phase in degrees is −360 × (time shift)/(period), and a plot of ratio and phase against frequency is the measured Bode plot.

## Common mistakes

- Using 10 log₁₀ where 20 log₁₀ is needed for an amplitude ratio.
- Mixing hertz and radians per second, or minutes and seconds, in ωτ and ωθ.
- Forgetting that a delay has unit magnitude: it changes only the phase.
- Reporting a lag as a positive angle in one place and a negative angle in another.
- Adding magnitudes of cascaded elements instead of multiplying them (adding decibels).
- Reading the phase of the lag term at the corner as −90° instead of −45°.

## Worked example

**Problem.** A synthetic plant has K = 2, τ = 4 min and θ = 0.5 min. Find the magnitude in decibels, the phase and the time lag at ω = 0.5 rad/min.

**Step 1: magnitude.** |G| = 2/√(1 + (0.5 × 4)²) = 0.8944, which is **−0.97 dB**.

**Step 2: phase.** −atan(2) = −63.43° from the lag and −0.5 × 0.5 rad = −14.32° from the delay, a total of **−77.76°**.

**Step 3: time lag.** 1.3571 rad/0.5 = **2.714 min**.

## Limits of this lesson

All numbers are synthetic. The lesson treats linear time-invariant elements with a single lag and a pure delay; real systems have several lags, delays that vary with flow and nonlinear actuators, and the Bode plot of a real system must be measured, not assumed.
