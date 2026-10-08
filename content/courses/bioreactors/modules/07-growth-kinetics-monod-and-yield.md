# Growth kinetics: Monod saturation, yield and what limits a batch

The growth of a culture on a plentiful nutrient is exponential, and for a first estimate of a doubling time that is enough. It is not enough to say how far a culture can grow in a batch, how its rate changes as the nutrient runs down, or when a different design is needed. This lesson adds two ideas to the exponential model: that the specific growth rate saturates with the concentration of a limiting nutrient (Monod kinetics), and that a nutrient supports a fixed amount of new biomass (the yield). Together they bound how much biomass a batch can make and how quickly. All values are synthetic and chosen for round numbers; they describe no particular cell line.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute the specific growth rate from Monod kinetics and the nutrient level that gives a target fraction of the maximum rate.
2. Compute the yield-limited maximum cell density and the minimum time to reach it.
3. Evaluate what the single-nutrient Monod model and a constant yield leave out for animal cell culture.

## Monod kinetics

The specific growth rate μ (per hour) depends on the concentration S of the limiting nutrient as

**μ = μ_max S / (K_s + S),**

where μ_max is the rate at saturating S and K_s the concentration at which μ is half of μ_max. **Synthetic values:** μ_max = 0.04 per hour (a doubling time of ln 2/0.04 = 17.3 h) and K_s = 0.5 mM glucose. At S = 5 mM, μ = 0.04 × 5/(0.5 + 5) = **0.0364 per hour**, 91% of the maximum, and the doubling time is 19.1 h. To reach a fraction f of μ_max the nutrient must be S = f K_s/(1 − f), so 90% of the maximum needs S = 9 K_s = **4.5 mM**. The curve is steep at low S and flat at high S: a culture fed well above K_s grows at nearly its maximum rate, and its rate falls only when the nutrient is almost gone.

## Yield and the maximum cell density

The nutrient consumed builds biomass in a roughly fixed ratio, the **yield** Y_X/S. With a synthetic yield of 1.5 × 10⁵ cells/mL for every mM of glucose consumed, the cell density a batch can reach is

**X_max = X₀ + Y (S₀ − S_min),**

where S₀ is the starting concentration and S_min the concentration at which growth stops. With X₀ = 2.0 × 10⁵ cells/mL, S₀ = 20 mM and S_min = 1 mM, X_max = 2.0 × 10⁵ + 1.5 × 10⁵ × 19 = **3.05 × 10⁶ cells/mL**, a 15.25-fold increase. If growth stayed at μ_max throughout, that would take t = ln(15.25)/0.04 = **68.1 h**; because μ falls near the end and a real culture also has a lag phase, this is a lower bound. Doubling the starting glucose to 40 mM would raise the yield-limited X_max to 6.05 × 10⁶ cells/mL, about double, but the culture reaches it only if nothing else stops growth first; lactate and ammonia accumulation are common reasons that it does not.

## The shape of a batch

A batch passes through a **lag** phase while cells adapt, an **exponential** phase near μ_max, a **deceleration** as nutrients fall or products accumulate, a **stationary** phase and a **decline**. The yield-limited X_max is the density at which the nutrient would be gone. In animal cell culture, growth often stops earlier for another reason: lactate and ammonia accumulate, the pH falls, or a second nutrient (glutamine, for example) runs out. Then X_max is an upper bound, not a prediction, and the model with one limiting nutrient and a constant yield cannot say which factor limits. Yields also change with conditions, and cells consume nutrients for maintenance even when not growing, which the simple model ignores. That is why a batch curve is measured, not computed, and why the model's use is to see how rates and limits scale.

## Common mistakes

- Treating the growth rate as proportional to the nutrient concentration at all concentrations.
- Using a doubling time measured at saturating nutrient for a culture near depletion.
- Taking X_max from the yield as a prediction when another factor stops growth first.
- Forgetting the cells already present (X₀) when computing the final density.
- Mixing mM and mol/L, or cells/mL and cells/L, in the yield.
- Counting the lag phase as part of the exponential growth time.

## Worked example

**Problem.** A synthetic culture has μ_max = 0.05 per hour, K_s = 1.0 mM, Y = 1.0 × 10⁵ cells/mL per mM, S₀ = 10 mM, X₀ = 3.0 × 10⁵ cells/mL and stops growing at S_min = 0.5 mM. Find μ at 2 mM, the nutrient level for 80% of μ_max, the maximum density and the minimum time.

**Step 1: growth rate.** μ = 0.05 × 2/(1.0 + 2) = 0.0333 per hour.

**Step 2: 80% of the maximum.** S = 0.8 K_s/0.2 = 4 K_s = 4.0 mM.

**Step 3: maximum density.** X_max = 3.0 × 10⁵ + 1.0 × 10⁵ × (10 − 0.5) = 1.25 × 10⁶ cells/mL.

**Step 4: minimum time.** t = ln(4.17)/0.05 = 28.5 h at the maximum rate throughout, a lower bound.

## Limits of this lesson

All numbers are synthetic. Monod kinetics describes growth on a single limiting nutrient with a constant yield; animal cells have several nutrients, inhibitory products and changing yields, and the curve is usually measured. The lesson says nothing about any real cell line or process.
