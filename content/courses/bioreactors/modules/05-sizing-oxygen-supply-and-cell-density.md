# Sizing oxygen supply in a culture: kLa, driving force and the cell density a reactor can support

A culture is limited by its scarcest input, and for dense mammalian cell cultures that is usually oxygen. Oxygen dissolves poorly in water, so the supply has to be engineered: through the surface of a dish, through bubbles in a stirred reactor, or through a membrane. This lesson turns that into arithmetic. It computes the maximum oxygen transfer rate of a vessel, converts it to the cell density the vessel can support, and discusses what raising the supply costs.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute the maximum oxygen transfer rate and the cell density it can support from kLa, saturation concentration, a critical dissolved-oxygen level and specific uptake.
2. Compare strategies for raising oxygen supply with their side effects.
3. Evaluate an empirical kLa correlation's domain of validity.

## Transfer and demand

Oxygen moves from gas to liquid at a rate

**OTR = kLa (C* − C)**

where C* is the dissolved-oxygen concentration in equilibrium with the gas phase, C is the actual dissolved concentration, and **kLa** (units of 1/time) is the volumetric mass-transfer coefficient, the product of the liquid-side coefficient and the gas-liquid interfacial area per liquid volume. Demand is the **oxygen uptake rate**

**OUR = q_O₂ × X**

with q_O₂ the specific uptake per cell and X the cell density. Steady operation needs OTR ≥ OUR. Cells need dissolved oxygen above some critical level C_crit for normal metabolism, so the largest supply the vessel can deliver without dropping below that level is

**OTR_max = kLa (C* − C_crit),**

and the largest cell density it can support is X_max = OTR_max / q_O₂. The supply is limited by two things: how fast oxygen is transferred (kLa) and how much driving force exists (C* − C_crit). The driving force is bounded by the gas composition, since C* is proportional to the oxygen partial pressure in the gas.

## Ways to raise supply, and their costs

- **Raise kLa** by faster agitation, higher gas flow or finer bubbles. Costs: more shear stress on cells, more foam and bubble damage, and more carbon dioxide stripping, which changes pH.
- **Raise C\*** by enriching the gas with oxygen. Costs: higher dissolved oxygen can generate oxidative stress, and the oxygen level that cells experience is itself a variable of the experiment.
- **Lower demand** by operating at a lower cell density or a lower temperature, at the price of productivity.
- **Change the format.** Static dishes depend on diffusion through a layer of medium, so deeper medium lowers oxygen at the cells; thin layers, gas-permeable membranes and perfusion shorten the path.

## Empirical correlations and their limits

Reactors are often characterized by a correlation of the form kLa = a (P/V)^b (v_s)^c, where P/V is the specific power input and v_s is the superficial gas velocity. The constants a, b and c are fitted to measurements in a particular vessel geometry, medium and range of operating conditions. They carry no guarantee elsewhere: changing the sparger, the impeller, the scale or the medium (which affects bubble coalescence) can change them. A correlation is safe inside the range of the data it was fitted to, and a measurement of kLa in the actual system, for example by tracking the rise of dissolved oxygen after a step change in gas supply, is the check before relying on it.

## Static cultures: oxygen through a layer of medium

In an unstirred dish, oxygen reaches cells on the bottom by diffusion through the medium depth *h*. Oxygen arrives from the surface at C\*, the cells use it at a rate per area equal to the specific uptake times the surface density ρ, and at steady state the bottom concentration stays above C_crit only if

**h ≤ D (C\* − C_crit) / (q_O₂ ρ).**

Deeper medium holds more total oxygen but lengthens the diffusion path, so the supply rate falls with depth; this is why dense monolayers are cultured under thin layers or on gas-permeable membranes. With D = 3×10⁻⁹ m²/s (a typical value for oxygen in culture medium at 37 °C), C\* − C_crit = 0.15 mol/m³, q_O₂ = 2.0×10⁻¹⁰ mmol per cell per hour and a density of 2×10⁵ cells/cm², the largest depth is 4.05 mm. The estimate is for a uniform monolayer at steady state and ignores convection in the medium and any oxygen stored in plastic.

## Synthetic parameters

**Synthetic teaching values:** kLa = 5.0 h⁻¹, C* = 0.2 mmol/L (air-saturated medium), C_crit = 0.05 mmol/L, q_O₂ = 2.0×10⁻¹⁰ mmol per cell per hour.

## Common mistakes

- Sizing cell density from the total oxygen in the vessel instead of the rate at which oxygen can be transferred.
- Using C* − C rather than C* − C_crit as the driving force for the largest supply.
- Raising kLa without counting the costs in shear, foam and carbon dioxide stripping.
- Applying a kLa correlation outside the range of the data it was fitted to.
- Assuming that deeper medium gives cells at the bottom of a dish more oxygen, when it lengthens the diffusion path.
- Treating oxygen enrichment as free, when the dissolved-oxygen level is itself an experimental variable.

## Worked example

OTR_max = 5.0 × (0.2 − 0.05) = 0.75 mmol/(L·h). X_max = 0.75 / (2.0×10⁻¹⁰) = 3.75×10⁹ cells/L = 3.75×10⁶ cells/mL. Doubling kLa doubles this to 7.50×10⁶ cells/mL. Enriching the gas to 50% oxygen (C* = 0.5 mmol/L here) gives OTR_max = 5.0 × (0.5 − 0.05) = 2.25 mmol/(L·h) and X_max = 1.125×10⁷ cells/mL. A culture at 8×10⁶ cells/mL has OUR = 1.60 mmol/(L·h), which is above the 0.75 mmol/(L·h) this vessel can deliver.

## Limits of this lesson

The numbers are synthetic and the arithmetic is steady-state. The lesson is not an operating procedure for any bioreactor and does not cover carbon dioxide, pH, shear thresholds or scale-up beyond oxygen.
