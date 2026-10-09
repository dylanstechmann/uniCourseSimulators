# Forced first-order systems: steps, ramps, sinusoids and decaying inputs in a perfused chamber

A well-mixed chamber that is perfused with medium is a first-order system driven by whatever concentration is in the feed. In the earlier lesson the feed was constant, and the chamber relaxed to it with a time constant. Real feeds change: a new medium is switched in (a step), a nutrient is ramped up, the supply varies with a pump or a daily cycle (a sinusoid), or a bolus of drug is washed through (a pulse or a decay). The same linear equation covers all of these, and the answers come in a handful of closed forms that tell you how much of a feed change the culture actually sees, how late it sees it and how long it lasts. This lesson derives them by the integrating factor, checks the limiting cases and uses linearity to build a pulse from steps. All values are synthetic.

## Learning objectives

By the end of this lesson, you should be able to:

1. Write the chamber equation for a time-varying feed and solve it by an integrating factor.
2. Compute the response to a step, a ramp, a sinusoid and a decaying input, including the lag and attenuation.
3. Use linearity to build the response to a pulse and to interpret how long a feed change takes to reach the culture.

## The equation and the integrating factor

For a chamber of volume V perfused at a flow Q with feed concentration c(t), the amount balance is V dC/dt = Q(c − C), or

**τ dC/dt + C = c(t),  τ = V/Q.**

**Synthetic chamber:** V = 20 mL and Q = 0.5 mL/min, so τ = **40 min**. Multiplying the equation by e^(t/τ)/τ turns the left side into the derivative of C e^(t/τ), and integrating gives

**C(t) = e^(−t/τ) [ C(0) + (1/τ) ∫ from 0 to t of e^(s/τ) c(s) ds ].**

Every response below is this integral for a particular c(s), with C(0) = 0 unless stated.

## A step

For c = c₀ from t = 0, the integral gives C = c₀(1 − e^(−t/τ)). After 60 min the chamber has reached 1 − e^(−60/40) = **0.7769** of the new concentration, and the time to reach 95% is −τ ln 0.05 = **119.8 min**, about three time constants. A culture therefore sees a medium change only gradually; two hours after the switch it has covered only 95% of the change.

## A ramp

For c = a t, C = a (t − τ + τ e^(−t/τ)). Once the exponential has died away, C = a(t − τ): the chamber follows the ramp with the same slope but trails it by the time τ, a constant offset of a τ. For a feed that rises at a = 0.02 mM/min, the offset is 0.02 × 40 = **0.8 mM**, so a culture sees a nutrient ramp 40 minutes late.

## A sinusoid

For c = A sin ωt, after the transient has decayed, C = A sin(ωt − φ)/√(1 + (ωτ)²) with φ = atan(ωτ). The chamber attenuates the oscillation and delays it. For a feed that cycles with a period of 120 min, ω = 2π/120 = 0.05236 rad/min and ωτ = 2.094, so the amplitude is multiplied by **0.4309**, the phase lag is 64.5° and the time lag is φ/ω = **21.5 min**. Fast variations are filtered out much more strongly than slow ones; a cycle with a period of 10 min would be attenuated to 0.040 of its amplitude.

## A decaying input and a pulse

When the feed concentration decays as c = c₀ e^(−t/T), for example a drug that is being cleared upstream, and T ≠ τ, the integral gives C = c₀ T/(T − τ) (e^(−t/T) − e^(−t/τ)). With T = 100 min the chamber concentration first rises, peaks at t = ln(T/τ)/(1/τ − 1/T) = **61.1 min** at 0.5429 c₀, then falls: the chamber never sees the full feed concentration, because the feed has already dropped.

Linearity gives pulses. A pulse of height c₀ lasting 30 min is a step at t = 0 minus the same step delayed by 30 min. At t = 30 min the chamber has reached 0.5276 c₀, and at t = 60 min it has fallen to c₀ [(1 − e^(−60/40)) − (1 − e^(−30/40))] = c₀ (e^(−0.75) − e^(−1.5)) = **0.2492 c₀**.

## Common mistakes

- Using V/Q with V in millilitres and Q in microlitres per minute, which gives a time constant that is wrong by a factor of 1000.
- Expecting the culture concentration to equal the feed concentration immediately.
- Applying the sinusoidal steady-state formulas before the transient has decayed (about 3τ).
- Forgetting that a ramp is followed with a constant lag aτ, not with a constant ratio.
- Adding the responses of nonlinear terms by superposition; it holds only for linear equations.
- Reading the peak of the decaying-input response as the feed concentration.

## Worked example

**Problem.** A synthetic chamber has V = 15 mL and Q = 0.4 mL/min. Find τ, the fraction reached 50 min after a step, and the amplitude ratio, phase lag and time lag for a feed cycle with a period of 90 min.

**Step 1: time constant.** τ = 15/0.4 = **37.5 min**.

**Step 2: step.** 1 − e^(−50/37.5) = **0.7364**.

**Step 3: sinusoid.** ω = 2π/90 = 0.06981 rad/min, ωτ = 2.618, so the amplitude ratio is 1/√(1 + 6.854) = **0.3568**.

**Step 4: lag.** φ = atan(2.618) = 69.1° and the time lag is φ/ω = **17.3 min**.

## Limits of this lesson

All numbers are synthetic. The lesson treats a perfectly mixed chamber with constant volume and flow and a linear first-order equation. Real chambers have mixing delays, dead volumes and consumption of the substance, and the amplitude and lag formulas hold only after the transient has decayed.
