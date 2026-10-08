# Homeostasis as balance: mass balance, energy balance and the gain of negative feedback

Physiology keeps variables such as blood volume, solute concentrations and body temperature close to their usual values while eating, exercising, resting and meeting disturbances. Two ideas explain most of how this works. First, every regulated quantity is the net result of inputs and outputs, so balance equations say what must change for the quantity to stay put. Second, regulation is feedback: a sensor detects an error and an effector reduces it, and how well that works can be measured by a single number, the loop gain. This lesson develops both with synthetic values, covering steady states and time constants, heat balance and the strength of correction.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute the steady state, time constant and approach time of a well-mixed compartment from a mass balance.
2. Estimate heat production from oxygen uptake and the rate of temperature rise from an energy imbalance.
3. Calculate closed-loop deviation and loop gain, and distinguish a shifted set point from a failure of regulation.

## Mass balance and the time constant

For a solute X in a well-mixed volume V with production (or intake) rate P and clearance CL (the volume of fluid cleared of X per unit time), the balance is

**V dC/dt = P − CL · C.**

At steady state the left side is zero, so **C_ss = P / CL**. The concentration then approaches this value exponentially, C(t) = C_ss (1 − e^(−t/τ)) from an empty start, with **time constant τ = V / CL**. After one τ the concentration has covered 63% of the way, and after τ ln 10 it has covered 90%.

**Synthetic values:** V = 14 L, CL = 7 L/h and P = 35 mmol/h. Then C_ss = 35/7 = 5 mmol/L, τ = 14/7 = 2 h, and the level reaches 90% of its steady state in 2 × 2.303 = 4.6 h.

Now halve the clearance to 3.5 L/h with production unchanged. The new steady state is 35/3.5 = 10 mmol/L, twice as high, and τ doubles to 4 h, so it takes 9.2 h to cover 90% of the way. A halved clearance therefore doubles the level and also slows the approach, which is why a deficit in removal can take hours or days to show fully. The same bookkeeping applies to any compartment, from a hormone in plasma to sodium in body water.

## Energy balance and heat

The body is not a perfect engine: most of the chemical energy it uses ends up as heat, and the rest leaves as external work. Because oxygen use and energy release are tightly coupled, metabolic power can be estimated from oxygen uptake, using about **20 kJ per liter of oxygen** (a value that varies a little with the fuel being burned). At rest with V̇O₂ = 0.25 L/min, power is 0.25 × 20 = 5.0 kJ/min, about 7 MJ per day.

The heat balance is **S = M − W − H_loss**, where S is the rate of heat storage, M metabolic power, W external mechanical work and H_loss heat dissipated to the environment. If S is not zero, body temperature changes at S divided by the body's heat capacity, mass times the specific heat of tissue, about 3.5 kJ/(kg·°C).

**Synthetic exercise example:** a 70 kg person raises V̇O₂ to 1.5 L/min, so M = 30 kJ/min. If 20% becomes external work (W = 6 kJ/min), then 24 kJ/min must be dissipated. If heat loss is still at its resting value of 5 kJ/min, storage is 19 kJ/min and temperature would rise at 19/(70 × 3.5) = 0.078 °C per minute, about 4.7 °C per hour. Nothing prevents that rise except the effectors of thermoregulation: skin blood flow and sweating raise heat loss within minutes. Small imbalances compound when they persist, which is why a regulated system needs effectors with a range much larger than the typical disturbance.

## Negative feedback and loop gain

A feedback controller measures the error between a variable and its set point and drives an effector that opposes it. For a disturbance that would shift the variable by **d** with no control (the open-loop deviation), a proportional controller with **loop gain G** (the correction produced per unit of remaining error) leaves a closed-loop deviation

**e = d / (1 + G).**

With d = 10 units and G = 4, e = 10/5 = 2 units: the controller removes 80% of the disturbance, yet an error remains. A proportional controller needs an error to produce its correction, so a nonzero **steady-state error** is built in. Gain can be measured from a pair of experiments: **G = (open-loop deviation / closed-loop deviation) − 1**. If a disturbance moves the variable 12 units with the feedback pathway blocked and 3 units with it intact, G = 12/3 − 1 = 3.

Some physiological controls behave like **integral** controllers, which keep acting for as long as any error persists. Long-term control of body sodium and fluid by the kidney is often described in this way: excretion adjusts until intake and output match again, so the long-run error can approach zero even though fast, proportional reflexes leave residual error in the short run.

## A shifted set point is not a failure

In a fever, core temperature rises and is then defended at the higher value. The feedback loop is working, with a changed set point: while the body is below the new set point, it shivers and constricts skin vessels, and when the set point falls again it sweats. In heat stroke, by contrast, the effectors are overwhelmed and temperature climbs past any set point. The distinction matters when reading data: a regulated variable at an unusual value can mean a changed target or a failed loop, and the pattern of effector activity tells the two apart.

## Delays and oscillation

Real feedback has delays: a sensor must detect, a signal must travel, an effector must act. High gain with a long delay overshoots and can oscillate, as in some forms of periodic breathing. Higher gain gives tighter regulation only up to the limit set by the delay.

## Common mistakes

- Reading a normal concentration as normal production and clearance, when a different pair of values could give the same ratio.
- Forgetting that a lower clearance both raises the steady state and lengthens the approach to it.
- Using only the resting oxygen uptake for heat production during exercise, or forgetting that external work leaves the body as work and not as heat.
- Treating feedback as removing a disturbance entirely, when a proportional controller leaves d/(1 + G).
- Calling a fever a failure of regulation, when the loop is defending a higher set point.
- Assuming that more gain is always better, when delays can make a high-gain loop oscillate.

## Worked example

**Problem.** A synthetic hormone has V = 10 L, clearance 5 L/h and production 20 mmol/h. A change in metabolism halves production to 10 mmol/h. What happens to the concentration, and how long does it take to cover 90% of the change?

**Step 1: before and after.** C_ss = 20/5 = 4.0 mmol/L before and 10/5 = 2.0 mmol/L after.

**Step 2: the time constant.** τ = V/CL = 10/5 = 2.0 h, unchanged because clearance did not change. The level falls by 90% of the 2.0 mmol/L change in 2.0 × 2.303 = 4.6 h.

**Step 3: compare with the clearance case.** Halving clearance instead of production changes the steady state by a factor of two as well (up, not down) but doubles the time constant, so the two causes can be told apart by how fast the new level is reached, not only by where it ends.

## Limits of this lesson

All values are synthetic and round. One well-mixed compartment, a constant energy equivalent of oxygen and a proportional controller are simplifications: real solutes distribute among compartments, heat is not uniformly stored, and controllers combine proportional, integral and anticipatory actions. The lesson explains how to reason about regulation and gives no medical advice.
