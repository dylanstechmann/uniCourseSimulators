# Holding a culture at 37 °C: first-order plants, proportional control, steady-state error and saturation

Incubators, perfusion heaters, and bioreactor pH and oxygen loops all hold a variable near a setpoint by feedback. The simplest version, a heater driven in proportion to the temperature error, already shows the central trade-offs of control: higher gain means faster response and smaller steady-state error, until the actuator saturates or noise is amplified. This lesson models an incubator as a first-order system, closes a proportional loop around it, computes its steady-state error and speed, and shows why integral action and limits matter.

## Learning objectives

By the end of this lesson, you should be able to:

1. Model a heated chamber as a first-order system with a gain and a time constant, and write its transfer function.
2. Compute the closed-loop steady-state error and time constant under proportional control for a given gain.
3. Evaluate the effects of actuator saturation and integral action, and choose a gain with attention to noise and limits.

## The plant

Let y be the chamber temperature above ambient and u the heater power. Heat balance with loss proportional to y gives

**τ dy/dt = −y + K u,** with transfer function **G(s) = K / (τs + 1).**

K is the steady-state gain (°C per W) and τ the time constant. **Synthetic incubator:** K = 0.5 °C/W and τ = 600 s. Holding 37 °C in a 22 °C room needs y = 15 °C, so steady heater power u = y/K = 30 W.

## Proportional control

A proportional controller sets u = K_p (r − y), where r is the setpoint. The closed loop is

τ dy/dt = −y + K K_p (r − y), so **τ dy/dt = −(1 + KK_p) y + KK_p r.**

The loop gain L = KK_p sets everything:

- **Steady state:** y = L/(1 + L) × r, so the **steady-state error** is e = r/(1 + L).
- **Speed:** the closed-loop time constant is **τ/(1 + L)**.

With K_p = 20 W/°C, L = 10: the chamber settles at 13.64 °C above ambient, an error of 1.36 °C, with time constant 54.5 s. With K_p = 100 W/°C, L = 50: the error falls to 0.294 °C and the time constant to 11.8 s.

Why the error? A proportional controller produces heater power only if there is an error to multiply. Holding the chamber warm requires 30 W, so some error must remain to command it.

## Saturation

Real heaters have a maximum power. Suppose u is limited to 50 W. Starting from ambient, K_p = 20 demands 300 W, far beyond the limit: the heater runs flat out and the chamber warms with the open-loop time constant, not the fast closed-loop one, until the error is small enough for the demand to fall below 50 W. Linear predictions of speed hold only within the actuator's range. A gain chosen from the linear formula alone may simply mean "always saturated" during large changes.

## Integral action and windup

Adding a term proportional to the integral of the error, u = K_p e + K_i ∫e dt, removes the steady-state error: the integral keeps growing until the error is zero, and then holds whatever power is needed. The cost is a new risk. During saturation the integral keeps accumulating error that the heater cannot act on (**integrator windup**), and when the temperature finally reaches the setpoint the stored integral drives an overshoot. Practical controllers clamp or stop the integral while the actuator is saturated.

## Noise and gain

A temperature sensor's noise is multiplied by K_p before reaching the heater. At K_p = 100 W/°C, 0.05 °C of sensor noise becomes ±5 W of heater chatter. Higher gain trades a smaller steady-state error for more actuator activity, and in systems with delays (a thick chamber wall, a slow sensor) high gain can produce oscillation. The first-order model has no delay and so cannot show that instability; adding one is the next step in a control course.

## Common mistakes

- Expecting proportional control alone to reach the setpoint exactly.
- Predicting response time from the linear closed-loop formula while the actuator is saturated.
- Forgetting that loop gain is the product of controller and plant gains, with units that must cancel.
- Raising gain without considering sensor noise and delay.

## Worked example

**Problem.** What proportional gain keeps the steady-state error below 0.2 °C for the 15 °C rise, and what heater demand does it make at start-up?

**Step 1.** Need r/(1 + L) < 0.2, so 1 + L > 75, L > 74.

**Step 2.** K_p > 74/0.5 = 148 W/°C.

**Step 3.** At start-up the demand would be 148 × 15 = 2220 W, against a 50 W heater: deeply saturated. Integral action would meet the accuracy requirement with a much lower K_p, provided windup is handled.

## Limits of this lesson

Parameters are synthetic. The model treats the chamber as one well-mixed thermal mass without delay; real incubators have walls, door openings and humidity effects, and their controllers are tuned and tested by the manufacturer.
