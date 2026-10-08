# Derivatives as rates in growth models: exponential and logistic growth, doubling time and the fastest-growth point

A cell culture, a regenerating tissue and a bacterial infection all grow, and how fast they grow is a derivative. This lesson uses differential calculus to read growth models: what the derivative of an exponential says, how to estimate a growth rate from two counts, why logistic growth is fastest at half its capacity, and how long it takes to approach the limit. The same tools describe decay, from radioactive tracers to drug clearance to the loss of a cell population.

## Learning objectives

By the end of this lesson, you should be able to:

1. Relate the specific growth rate r of an exponential model to its derivative and to doubling time, and predict population size at a later time.
2. Estimate r from two measurements using logarithms and explain why a semi-log plot is linear for exponential growth.
3. Use the derivative of the logistic model to find the population of maximum growth rate and solve for the time to reach a fraction of capacity.

## Exponential growth and its derivative

If each cell divides independently at the same rate, the population grows in proportion to its size:

**dN/dt = rN,** with solution **N(t) = N₀ e^(rt).**

Differentiate the solution and you recover the equation: d/dt(N₀e^(rt)) = rN₀e^(rt) = rN. The quantity r is the **specific** (per-capita) growth rate, with units of 1/time. Doubling time t_d satisfies e^(r t_d) = 2, so **r = ln 2 / t_d**.

**Synthetic culture:** N₀ = 10⁵ cells and t_d = 24 h, so r = 0.02888 h⁻¹. After 72 h (three doublings) N = 10⁵ × e^(0.02888 × 72) = 8×10⁵ cells. The growth rate in cells per hour is not constant: at 4×10⁵ cells it is rN = 11552 cells/h, four times the rate at 10⁵ cells.

## Estimating r from data

Taking logarithms makes exponential growth linear: ln N = ln N₀ + rt. A plot of ln N against t is a straight line with slope r, which is why growth is plotted on a semi-log axis. From two counts, r = ln(N₂/N₁) / (t₂ − t₁).

With 2×10⁵ cells at 10 h and 5×10⁵ at 40 h: r = ln(2.5) / 30 = 0.03054 h⁻¹ and t_d = ln 2 / r = 22.7 h. Two points cannot show whether growth was in fact exponential; more points on the semi-log plot can, by showing whether they fall on a line.

## Logistic growth: a limit to growth

Real cultures run out of space or nutrients. The logistic model adds a carrying capacity K:

**dN/dt = rN (1 − N/K).**

When N ≪ K it behaves exponentially; as N → K, growth stops. To find when growth is fastest, maximize the rate f(N) = rN − rN²/K. Its derivative with respect to N is f′(N) = r − 2rN/K, which is zero at **N = K/2**, and f″(N) = −2r/K < 0 confirms a maximum. The maximum rate is f(K/2) = rK/4. For K = 10⁶ cells and the r above, the fastest growth is 7220 cells/h, reached at 5×10⁵ cells. On a plot of N against t, this is the inflection point of the S-shaped curve.

## Time to approach the limit

The logistic equation has the solution N(t) = K / (1 + ((K − N₀)/N₀) e^(−rt)). Solving for the time to reach a fraction p of K gives

**t = (1/r) ln[ (p/(1 − p)) × ((K − N₀)/N₀) ].**

For p = 0.9 and N₀ = 10⁵: t = ln(9 × 9) / 0.02888 = 152 h. Growth slows sharply near K, so "how long until confluence" depends heavily on what fraction counts as confluent.

## Common mistakes

- Confusing the specific growth rate r (per hour) with the absolute growth rate dN/dt (cells per hour); they differ by a factor of N.
- Using log base 10 for r: ln 2 / t_d uses the natural logarithm, and log₁₀ gives a value 2.3 times too small.
- Reading a doubling time off a late, crowded stage of growth and treating it as the cells' intrinsic rate.
- Assuming the S-curve is symmetric in time around the inflection point for every model; it is for logistic growth, but not for other limits to growth.

## Worked example

**Problem.** In the logistic model above, what is the growth rate at N = 4×10⁵ cells, and how does it compare with the exponential prediction?

**Step 1: logistic rate.** dN/dt = 0.02888 × 4×10⁵ × (1 − 0.4) = 6931 cells/h.

**Step 2: exponential rate.** Without the limit, rN = 11552 cells/h.

**Step 3: interpretation.** Crowding already cuts growth by 40% at 40% of capacity. A doubling time measured late in a culture therefore understates the cells' intrinsic rate, which is why growth rates are estimated during the early, near-exponential phase.

## Limits of this lesson

All parameters are synthetic. Real populations have lag phases, death, heterogeneous cells and nutrient depletion that the logistic model only summarizes.
