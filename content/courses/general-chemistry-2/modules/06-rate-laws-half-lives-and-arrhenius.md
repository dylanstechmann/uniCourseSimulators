# Rate laws in practice: integrated forms, half-lives, Arrhenius temperature dependence and how to tell the order

Reactions that matter in biology and in the lab, from drug and reagent breakdown to protein unfolding and the slow chemical damage that accumulates in long-lived molecules, are described by rate laws. This lesson uses the integrated rate laws to predict how much remains after a time, shows how to determine reaction order from data, and uses the Arrhenius equation to extract an activation energy and predict rates at other temperatures, including why cold storage works.

## Learning objectives

By the end of this lesson, you should be able to:

1. Use integrated first- and second-order rate laws to compute remaining concentration and half-life.
2. Determine reaction order from concentration-time data by choosing the transformation that gives a straight line.
3. Calculate an activation energy from rate constants at two temperatures and predict a rate constant at a third temperature.

## Integrated rate laws

For a **first-order** reaction, rate = k[A], and [A] = [A]₀ e^(−kt). The half-life is t½ = ln 2 / k, independent of starting concentration: every half-life halves what remains. With k = 0.0231 min⁻¹, t½ = 30.0 min, and after 60 minutes 25.0% remains.

For a **second-order** reaction in one reactant, rate = k[B]², and 1/[B] = 1/[B]₀ + kt. Its half-life, t½ = 1/(k[B]₀), depends on the starting concentration: at lower concentration the reaction slows more. With k = 0.5 L mol⁻¹ s⁻¹ and [B]₀ = 0.02 M, t½ = 100 s.

A **zero-order** process, rate = k, falls linearly with time. Enzyme-catalyzed reactions at saturating substrate behave this way, which is why the concentration curve in such cases is a straight line until the substrate falls toward Km.

## Finding the order from data

**Synthetic data** for the decomposition of a compound A (concentration in mM):

| t (min) | [A] (mM) |
|---|---|
| 0 | 1.0 |
| 10 | 0.794 |
| 20 | 0.63 |
| 40 | 0.397 |
| 60 | 0.25 |

Plot three transformations against time: [A] (zero order), ln[A] (first order) and 1/[A] (second order). The one that is straight identifies the order, and its slope gives k. Here ln[A] falls by 0.0231 per minute at every interval: ln(0.794) − ln(1.0) = -0.2307 over 10 min, and the same per-minute slope holds for each later interval to rounding. The constant half-life is a quick check: about 30 minutes from 1.00 to 0.50 mM, as from 0.50 to 0.25 mM would be. Data that span less than one half-life can look straight in all three plots, so a test of order needs the reaction followed far enough.

## Temperature and the Arrhenius equation

Rate constants usually rise steeply with temperature:

**k = A e^(−Ea/RT),** so **ln(k₂/k₁) = (Ea/R)(1/T₁ − 1/T₂).**

**Synthetic measurements:** k = 1.0×10⁻³ s⁻¹ at 25 °C and 2.6×10⁻³ s⁻¹ at 37 °C. Then

Ea = 8.314 × ln(2.6) / (1/298.15 − 1/310.15) = 61.2 kJ/mol.

A related summary used in biology is Q₁₀, the factor by which a rate rises for a 10 °C increase. Here Q₁₀ = (2.6)^(10/12) = 2.22. Q₁₀ is not a constant; for a fixed Ea it changes with the temperature range.

## Using Ea to predict storage

With Ea known, the rate at another temperature follows. At 4 °C, k = 1.0×10⁻³ × exp[−(61.2 × 10³/8.314)(1/277.15 − 1/298.15)] = 1.54×10⁻⁴ s⁻¹, and the first-order half-life rises from 11.6 min at 25 °C to 75 min. This is the logic of refrigerating reagents and of accelerated stability testing at high temperature. Both depend on the mechanism staying the same across the temperature range; a process with a different pathway at high temperature, such as protein unfolding, invalidates the extrapolation.

## Common mistakes

- Using Celsius instead of kelvin in the Arrhenius equation, which gives a meaningless activation energy.
- Assuming every half-life is ln 2 / k; only first-order reactions have a constant half-life.
- Fitting order from data that cover only a small fraction of the reaction, where every model looks straight.
- Treating Q₁₀ as a property of the reaction rather than of the reaction over a stated temperature range.

## Worked example

**Problem.** A reagent loses 20% of its activity in 30 days at 25 °C by first-order decay. How long until it has lost 50%, and what would change at a higher temperature?

**Step 1: rate constant.** 0.80 = e^(−30k), so k = −ln(0.80)/30 = 0.00744 per day.

**Step 2: half-life.** ln 2 / 0.00744 = 93 days.

**Step 3: temperature.** With Ea of about 61 kJ/mol from the measurement above, warming from 25 °C to 37 °C would multiply k by 2.6, cutting the half-life to about 36 days. The answer depends on Ea, so a measured value for the specific compound is needed.

## Limits of this lesson

All rate constants and data are synthetic. Real reactions may follow mixed or changing order, and Arrhenius behavior can fail when mechanisms change with temperature.
