# PI control, tuning and integrator windup: removing steady-state error without losing the margin

Proportional control of the incubator left a steady-state error, because a heater that is to deliver power must be commanded by an error. Adding an integral term removes it: the controller keeps adding to the heater power as long as any error remains, so the loop can settle only at the setpoint. The price is another lag in the loop, which costs phase margin, and a new hazard when the heater saturates. This lesson writes the PI controller, tunes it from the plant model, compares that tuning with the classic Ziegler–Nichols rules, adds a note on derivative action and shows how integrator windup arises and is prevented. All values are synthetic.

## Learning objectives

By the end of this lesson, you should be able to:

1. Write a PI controller and compute its tuning for a lag-plus-delay plant by cancelling the plant lag.
2. Compute the crossover frequency and phase margin of the tuned loop, and the Ziegler–Nichols PI settings from the ultimate gain and period.
3. Explain integrator windup and the role of the derivative term, and choose where each is needed.

## Integral action

A PI controller is C(s) = K_p (1 + 1/(T_i s)), or u = K_p e + K_i ∫e dt with K_i = K_p/T_i, where T_i is the integral time. In steady state the integral must be constant, so the error must be zero. With a step change in the setpoint or a constant disturbance (a change in room temperature), the controller moves the heater power to the new value needed and the error returns to zero, provided the loop is stable.

## Tuning by cancelling the lag

For a plant K e^(−θs)/(τs + 1), choose T_i = τ so that the controller's zero cancels the plant's pole. The open loop then becomes an integrator with a delay: L(s) = (K_p K/τ) e^(−θs)/s. Its magnitude is (K_p K/τ)/ω, so the gain crossover is **ω_gc = K_p K/τ**, and its phase is −90° − ωθ, so the phase margin is **PM = 90° − ω_gc θ** (with the angle in degrees). A convenient rule (lambda or internal-model tuning) sets K_p = τ/(K(λ + θ)), where λ is a design parameter: a larger λ gives a lower gain, a slower loop and more margin.

**Synthetic incubator (time in minutes):** K = 0.5 °C/W, τ = 10 min, θ = 1 min. With λ = 2 min, K_p = 10/(0.5 × (2 + 1)) = **6.667 W/°C** and T_i = 10 min, so K_i = 6.667/10 = **0.667 W/(°C·min)**. The loop has ω_gc = 6.667 × 0.5/10 = **0.3333 rad/min** and PM = 90° − 19.10° = **70.9°**; a numerical solution of the full loop gives the same margin (70.9°).

| λ (min) | K_p (W/°C) | ω_gc (rad/min) | Phase margin |
|---|---|---|---|
| 4 | 4.000 | 0.2000 | 78.5° |
| 2 | 6.667 | 0.3333 | 70.9° |
| 1 | 10.000 | 0.5000 | 61.4° |
| 0.5 | 13.333 | 0.6667 | 51.8° |

Smaller λ means a faster loop and less margin. The cancellation has a cost: a disturbance that enters at the plant input still excites the slow plant pole, so for a lag-dominant plant (τ much larger than θ) the disturbance response is slow, and a smaller T_i is often used.

## Ziegler–Nichols closed-loop rules

An older method needs no model. With proportional control only, raise K_p until the loop oscillates steadily; the gain at that point is the ultimate gain K_u and the period of the oscillation is P_u. For this plant K_u = 32.7 W/°C and P_u = 2π/1.632 = 3.85 min (the gain and phase crossover of the previous lesson). The rules give a PI controller with K_p = 0.45 K_u = **14.72 W/°C** and T_i = P_u/1.2 = **3.21 min**, and a PID controller with K_p = 0.6 K_u = 19.6, T_i = P_u/2 = 1.93 min and T_d = P_u/8 = 0.48 min. The rules are aggressive: here the PI loop has a crossover at 0.785 rad/min and a phase margin of only 30.6°, below the 45° target, and the response rings.

## Derivative action

A derivative term K_p T_d de/dt anticipates the error and adds phase lead. It also multiplies measurement noise by a frequency-proportional gain, so it needs a filter, and on a slow thermal plant with a noisy probe it is often left out. PI is enough for most incubator and bioreactor temperature loops; derivative action helps where a fast, lightly damped mode needs to be damped.

## Integrator windup

While the heater is saturated, the error is not reduced as the controller intends, but the integral keeps accumulating it. When the temperature finally reaches the setpoint, the integral term still holds the stored value, and it drives the heater past what is needed: a large overshoot. **Synthetic case:** with K_i = 0.667 W/(°C·min), an error of 1.8 °C for 7 min of saturation stores 0.667 × 1.8 × 7 = **8.4 W** of integral action that the heater could not use. Anti-windup measures stop this: clamp the integral while the output is saturated, or feed back the difference between the commanded and the actual output (back-calculation) so that the integral relaxes.

## Common mistakes

- Choosing T_i much shorter than the plant lag without checking the phase margin.
- Using the phase margin of the proportional loop for a PI loop.
- Applying Ziegler–Nichols settings without checking the margin they produce.
- Adding derivative action to a noisy measurement with no filter.
- Allowing the integral to accumulate while the actuator is saturated.
- Expecting integral action to help a loop that is already close to instability.

## Worked example

**Problem.** A synthetic plant has K = 1.2, τ = 5 min and θ = 2 min. Tune a PI controller with λ = 3 min, find the crossover and phase margin, and the integral stored during 5 min of saturation with an error of 2 °C.

**Step 1: tuning.** K_p = 5/(1.2 × (3 + 2)) = **0.833**, T_i = 5 min and K_i = 0.833/5 = 0.1667.

**Step 2: crossover and margin.** ω_gc = 0.833 × 1.2/5 = 0.200 rad/min and PM = 90° − 22.92° = **67.1°**.

**Step 3: windup.** 0.1667 × 2 × 5 = **1.67** (in the units of the controller output) of stored integral action.

## Limits of this lesson

All numbers are synthetic. The tuning rules assume a stable lag-plus-delay plant and a linear actuator; real loops need a measured model, a check of the margins and a test of the saturation behavior, and the Ziegler–Nichols rules are rules of thumb that are known to leave a lightly damped loop.
