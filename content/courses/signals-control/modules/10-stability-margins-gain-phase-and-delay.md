# Stability margins: gain margin, phase margin and how much delay a loop can take

Feedback makes a system faster and less sensitive to its own gain, and the same feedback can make it oscillate. A loop is unstable when the signal, after going around the loop with its gain and its lags and delays, comes back reinforcing itself instead of opposing the error. The Bode plot of the open loop shows how close that is. Two numbers, the gain margin and the phase margin, say how much more gain or how much more phase lag the loop can tolerate before it oscillates steadily, and they predict how much ringing the closed loop has long before it reaches that limit. This lesson defines them, computes them for the incubator-like plant of the previous lesson and uses them to choose a gain. All values are synthetic.

## Learning objectives

By the end of this lesson, you should be able to:

1. Find the gain crossover and phase crossover frequencies of a loop with a lag and a delay.
2. Compute the phase margin, gain margin and delay margin, and the largest gain that keeps the loop stable.
3. Choose a controller gain for a target phase margin and relate the margin to the ringing of the closed loop.

## The open loop and the two crossovers

With the controller C and the plant G in series and the measurement fed back, the **open loop** is L(s) = C(s)G(s). The closed loop is stable if the Nyquist curve of L(jω) does not encircle −1; for a plant that is stable on its own, this reduces to two checks on the Bode plot:

- the **gain crossover frequency** ω_gc is where |L(jω)| = 1 (0 dB). The **phase margin** is PM = 180° + ∠L(jω_gc): how many degrees of additional lag would bring the phase to −180° at that frequency.
- the **phase crossover frequency** ω_pc is where ∠L(jω) = −180°. The **gain margin** is GM = 1/|L(jω_pc)|, the factor by which the gain can grow before |L| reaches 1 at that frequency.

A loop with both margins positive is stable. Common design targets are a phase margin of at least 45° and a gain margin of at least 2 (6 dB); they leave room for the plant to differ from the model.

## The incubator loop with proportional control

**Synthetic plant (time in minutes):** G(s) = 0.5 e^(−s)/(10s + 1), with a proportional controller of gain K_p in W/°C. The loop is L = K_p G. For K_p = 20 W/°C the DC loop gain is 20 × 0.5 = 10.

**Gain crossover.** |L| = 10/√(1 + 100ω²) = 1 gives 1 + 100ω² = 100, so ω_gc = √99/10 = **0.995 rad/min**. The phase there is −atan(9.95) − 0.995 rad = −84.26° − 57.01° = −141.27°, so the **phase margin is 38.7°**.

**Phase crossover.** Solving atan(10ω) + ω = π (in radians) gives ω_pc = **1.632 rad/min**, where |L| = 10/√(1 + 266.3) = 0.6116. The **gain margin is 1.635** (4.27 dB), so the proportional gain can rise to 20 × 1.635 = **32.7 W/°C** before the loop oscillates at a steady period of 2π/1.632 = 3.85 min.

**Delay margin.** The phase margin can also be read as spare delay: DM = PM(rad)/ω_gc = 0.6760/0.995 = **0.679 min**. If the delay in the plant (a slow probe, a longer air path) grew from 1 min by that amount, the loop would be on the edge of instability.

## Margins and ringing

As K_p rises, the crossover moves up to where the delay costs more phase, and the phase margin falls:

| K_p (W/°C) | DC loop gain | ω_gc (rad/min) | Phase margin |
|---|---|---|---|
| 10 | 5 | 0.490 | 73.5° |
| 20 | 10 | 0.995 | 38.7° |
| 30 | 15 | 1.497 | 8.1° |

A common rule of thumb for loops that behave like a second-order system relates damping ratio and phase margin by ζ ≈ PM/100 (PM in degrees, up to about 60°). For PM = 38.7° this gives ζ ≈ 0.39 and an overshoot of about 27%, so the closed loop rings. At K_p = 30 W/°C the phase margin is only 8.1° and the response is close to a sustained oscillation. To reach a phase margin of 45°, the phase at crossover must be −135°: atan(10ω) + ω = 3π/4 gives ω_gc = 0.896 rad/min, which needs a loop gain of √(1 + 100 × 0.896²) = 9.02, so **K_p = 18.04 W/°C**. This gain is only a little below 20 W/°C, yet it buys 6.3° of phase margin.

## Why the margins are needed

A model is never exact. The plant gain depends on the temperature and the air flow, the delay depends on where the probe sits, and the actuator saturates. A gain margin of 1.64 says that a plant with 63% more gain than modelled would already oscillate; a phase margin of 39° says that an extra lag of 0.68 min would. A loop designed to the stability limit has no allowance for either.

## Common mistakes

- Computing the phase margin at the wrong frequency (the phase crossover instead of the gain crossover).
- Mixing degrees and radians when adding the delay phase ωθ to the lag phase.
- Reading a gain margin of 1.2 as comfortable because it is greater than 1.
- Taking the phase margin at face value for a loop that crosses unity gain several times.
- Applying the rule ζ ≈ PM/100 to a loop whose phase falls steeply near the crossover (a long delay).
- Forgetting that the delay margin is in the same time unit as ω.

## Worked example

**Problem.** A synthetic plant is G(s) = 1.2 e^(−2s)/(5s + 1) with time in minutes and K_p = 2. Find the gain and phase crossover frequencies, the phase margin, the gain margin and the delay margin.

**Step 1: gain crossover.** The DC loop gain is 2.4, and 2.4/√(1 + 25ω²) = 1 gives ω_gc = 0.4363 rad/min.

**Step 2: phase margin.** Phase = −atan(2.182) − 0.8727 rad = −65.38° − 50.00° = −115.38°, so the phase margin is **64.6°**.

**Step 3: gain margin.** The phase crossover is ω_pc = 0.8953 rad/min, where |L| = 0.5232, so the gain margin is **1.911** (5.63 dB).

**Step 4: delay margin.** DM = 1.1279/0.4363 = **2.585 min**, compared with the existing delay of 2 min.

## Limits of this lesson

All numbers are synthetic. The lesson treats a stable plant with a single lag and delay and a proportional controller, for which the two margins settle stability; plants with unstable poles, several crossovers or a changing delay need the full Nyquist criterion, and the rule ζ ≈ PM/100 is an approximation.
