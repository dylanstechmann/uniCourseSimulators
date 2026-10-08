# Writing a cell-culture mass balance: substrate use, product accumulation and when a batch runs out

Every culture is a small chemical plant: cells take in glucose and other nutrients, make more cells and secrete products such as lactate. Before choosing a feeding schedule, a medium change interval or a perfusion rate, it pays to write the mass balance. This lesson writes balances for cells, glucose and lactate in a batch culture, integrates them with an exponentially growing population, predicts when glucose runs out, and extends the balance to a continuously perfused vessel.

## Learning objectives

By the end of this lesson, you should be able to:

1. Write mass balances for cells, a consumed substrate and a secreted product in a batch culture using specific rates.
2. Integrate the substrate balance for an exponentially growing population to predict substrate remaining, product formed and the time of exhaustion.
3. Extend the balance to a perfused vessel with dilution, and evaluate the assumptions behind constant specific rates and yields.

## Balances in words and symbols

For any species in a well-mixed vessel: **accumulation = in − out + generation − consumption.** In a closed batch, nothing flows in or out, so for cell density X, glucose concentration G and lactate concentration P:

- dX/dt = μX (growth at specific rate μ)
- dG/dt = −q_G X (each cell consumes glucose at specific rate q_G)
- dP/dt = q_P X (each cell secretes lactate at specific rate q_P)

Specific rates are per cell per unit time. Writing balances this way separates biology (μ, q_G, q_P) from bookkeeping (volume, flows, cell number).

## Integrating with exponential growth

With X(t) = X₀e^(μt), the glucose consumed by time t is

**ΔG = q_G ∫₀ᵗ X dt = q_G X₀ (e^(μt) − 1)/μ.**

**Synthetic culture:** X₀ = 5.0×10⁵ cells/mL, μ = 0.03 h⁻¹ (doubling about every 23 h), q_G = 2.0×10⁻¹⁰ mmol per cell per hour, G₀ = 25 mM. After 48 h the culture holds X = 2.11×10⁶ cells/mL. The integral of cell density is 5.368×10⁷ cell·h/mL, so glucose used is 2.0×10⁻¹⁰ × 5.368×10⁷ × 1000 mL/L = 10.74 mM, leaving G = 14.26 mM. The factor 1000 converts per mL to per L, a common source of thousandfold errors.

If lactate is made at about 1.6 mol per mol of glucose consumed (a synthetic yield; the theoretical maximum from glycolysis alone is 2), lactate reaches 17.2 mM, enough to acidify a weakly buffered medium (see the buffers lesson in general chemistry 2).

## When does the glucose run out?

Set ΔG = G₀ and solve: e^(μt) = 1 + G₀μ/(q_G X₀ × 1000), so

t_exhaust = ln(1 + 25 × 0.03 / (2.0×10⁻¹⁰ × 5.0×10⁵ × 1000)) / 0.03 = 71 h.

Because consumption grows with the population, most of the glucose is used near the end: the culture consumes as much in its last doubling as in all previous ones combined. This is why cultures can look comfortable one day and be starved the next.

## Perfused vessels

If fresh medium at G_in flows in and spent medium flows out at the same rate, with dilution rate D = flow/volume, the glucose balance gains two terms:

**dG/dt = D(G_in − G) − q_G X.**

At steady state with a fixed cell density X, G = G_in − q_G X/D. For a perfusion rate of 0.5 vessel volumes per day (D = 0.0208 h⁻¹) and a retained density of 5.0×10⁶ cells/mL, steady glucose would be 25 − 2.0×10⁻¹⁰ × 5.0×10⁶ × 1000 / 0.0208 = -23.0 mM: negative, meaning that perfusion rate cannot support that density. The minimum D for glucose to stay above zero is q_G X/G_in = 0.040 h⁻¹, about 0.96 volumes per day. Cells must also be retained in the vessel for this to be a perfusion rather than a washout.

## Assumptions to check

Specific rates are rarely constant. Cells often consume glucose faster and make more lactate when glucose is plentiful and switch to consuming lactate when glucose is low. Growth slows as nutrients fall or waste rises, so exponential growth is an approximation for the early culture. Yields depend on cell type, oxygen and pH. A balance with constant rates is a planning estimate to be checked against measured concentrations.

## Common mistakes

- Mixing per-mL cell densities with per-L concentrations without the factor of 1,000.
- Using the final cell density times time instead of the integral of cell density.
- Treating a lactate yield above 2 mol/mol as plausible from glucose alone.
- Forgetting that perfusion needs cell retention.

## Worked example

**Problem.** Starting density is doubled to 1.0×10⁶ cells/mL with everything else unchanged. When does glucose run out?

**Step 1.** t = ln(1 + 25 × 0.03 / (2.0×10⁻¹⁰ × 1.0×10⁶ × 1000)) / 0.03.

**Step 2.** The argument is 1 + 3.75 = 4.75, so t = 52 h.

**Step 3.** Doubling the seed shortens the batch by about one doubling time (19 h), not by half. Exponential bookkeeping rewards writing the balance rather than guessing.

## Limits of this lesson

All rates and concentrations are synthetic. The balances assume a well-mixed vessel, constant specific rates and no cell death; real cultures need measured rates.
