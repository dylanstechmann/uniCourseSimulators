# Controlling dissolved oxygen: the required kLa, the capacity limit and the control cascade

The lesson on sizing oxygen supply computed the largest cell density a vessel can support at a given kLa. A real culture does not sit at one density. It grows, its oxygen demand rises along with it, and the vessel's capacity stays fixed, so a controller that holds the dissolved oxygen at a setpoint has to raise the supply steadily until it runs out of ways to do so. This lesson computes how much kLa the culture requires over time, when a vessel reaches its limit, what each way of extending the limit costs, and how fast the dissolved oxygen can respond, which decides whether a probe and a controller can follow it. All values are synthetic.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute the oxygen uptake rate and the kLa required to hold a dissolved-oxygen setpoint as a culture grows.
2. Find the time at which a vessel reaches its capacity and compare the options for extending it.
3. Evaluate a dissolved-oxygen control cascade, the oxygen time constant and the role of sensor lag.

## Demand rises as the culture grows

The oxygen uptake rate is OUR = q X, with q the specific uptake per cell and X the cell density. **Synthetic values:** q = 2.0 × 10⁻¹⁰ mmol/(cell·h), and a culture that starts at X₀ = 5.0 × 10⁵ cells/mL (5.0 × 10⁸ cells/L) has OUR₀ = 2.0 × 10⁻¹⁰ × 5.0 × 10⁸ = **0.100 mmol/(L·h)**. If the culture grows exponentially at μ = 0.03 per hour, OUR rises as e^(μt). To hold the dissolved oxygen at a setpoint C_set, the transfer must match the uptake, kLa (C* − C_set) = OUR, so the required kLa is

**kLa_req = OUR / (C* − C_set).**

With C* = 0.2 mmol/L (air saturation at 37 °C, rounded) and C_set = 0.1 mmol/L (half of air saturation), the driving force is 0.10 mmol/L and kLa_req = 0.100/0.10 = **1.0 per hour** at the start.

## Reaching the limit

A vessel has a ceiling on kLa. Above some agitation and gas flow, cells are damaged by shear and bubbles, or the foam becomes unmanageable; take kLa_max = 5.0 per hour. The requirement grows by a factor of 5 before it reaches that ceiling, which takes t = ln(5)/μ = ln 5/0.03 = **53.6 h**, at a cell density of 5.0 × 10⁵ × 5 = **2.5 × 10⁶ cells/mL**. After that, the dissolved oxygen falls below the setpoint, however the controller acts.

## Extending the limit

- **Oxygen-enriched gas** raises C*. With C* = 0.5 mmol/L, the driving force at the setpoint is 0.40 mmol/L, the capacity is kLa_max × 0.40 = 2.0 mmol/(L·h), the supportable density is **10.0 × 10⁶ cells/mL**, and the requirement reaches the ceiling at t = ln(20)/0.03 = **99.9 h**. Pure oxygen costs gas, and high local oxygen levels can themselves stress cells.
- **A lower setpoint** raises the driving force. Lowering C_set to 0.05 mmol/L (a quarter of air saturation) gives a capacity of 5.0 × (0.2 − 0.05) = 0.75 mmol/(L·h), which supports 3.75 × 10⁹ cells/L = 3.75 × 10⁶ cells/mL, half again as much, but leaves less margin above the level at which respiration is limited.
- **A higher kLa** needs more power or gas flow, which costs shear and foam (see the lessons on scale-up and on shear).

Each option moves the limit but also moves a hazard.

## The control cascade

A typical dissolved-oxygen controller works as a cascade. When the measured value falls below the setpoint, the controller first raises the agitation (the cheapest actuator) up to a limit, then the gas flow, then the oxygen fraction in the gas; when the value rises, it reverses the sequence. A PID controller computes the output from the error, its integral and its rate of change, whereas an on/off controller drives a limit cycle around the setpoint. The cascade extends the range of control, and the order of the stages is chosen to put the least harmful actuator first.

## Time constant and sensor lag

In a lumped model, the dissolved oxygen relaxes toward its steady value with the time constant 1/kLa. At kLa = 5.0 per hour, 1/kLa = 1/5.0 h = **12 min**. A dissolved-oxygen probe has its own response time, perhaps 30 s, and the sensor lag matters when the product kLa × τ_p is not small. Here it is 5.0 × 30/3600 = **0.042**, so the probe follows the process well. The steady value when uptake is below the ceiling is C_ss = C* − OUR/kLa: for OUR = 0.6 mmol/(L·h) it is 0.2 − 0.6/5.0 = 0.08 mmol/L, and for OUR = 0.75 it is 0.05 mmol/L, the critical level used in this lesson, which is why the controller can no longer hold the setpoint.

## Common mistakes

- Treating the vessel's capacity as a constant to be compared with a single demand.
- Using the saturation concentration C* where the driving force C* − C_set is needed.
- Expecting oxygen enrichment to be free of hazards.
- Setting the setpoint at the critical level and leaving no margin.
- Ignoring probe lag when kLa is large.
- Forgetting that the required kLa grows exponentially when the culture does.

## Worked example

**Problem.** A synthetic culture has q = 1.5 × 10⁻¹⁰ mmol/(cell·h), X₀ = 4.0 × 10⁵ cells/mL, μ = 0.025 per hour, C* = 0.2 and C_set = 0.12 mmol/L, and the vessel's ceiling is kLa_max = 4 per hour. Find the starting requirement, the time to the ceiling, the density then and the oxygen time constant.

**Step 1: demand and requirement.** OUR₀ = 1.5 × 10⁻¹⁰ × 4.0 × 10⁸ = 0.060 mmol/(L·h); kLa_req = 0.060/(0.2 − 0.12) = 0.75 per hour.

**Step 2: time to the ceiling.** The requirement must rise by 4/0.75 = 5.33, so t = ln(5.33)/0.025 = 67.0 h.

**Step 3: density.** 4.0 × 10⁵ × 5.33 = 2.13 × 10⁶ cells/mL.

**Step 4: time constant.** 1/kLa = 60/4 = 15 min.

## Limits of this lesson

All numbers are synthetic. The model assumes exponential growth, a constant specific uptake, a perfectly mixed liquid and a single first-order oxygen balance; real cultures change their uptake with the state of the cells, gradients appear in large vessels (see the capstone), and the controller's tuning matters. The lesson is not a control design.
