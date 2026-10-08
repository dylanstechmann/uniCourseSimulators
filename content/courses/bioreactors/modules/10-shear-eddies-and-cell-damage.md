# Shear, eddies and cells: the Kolmogorov scale and when stirring becomes damage

Stirring a culture is a trade: enough to mix, suspend and supply oxygen, but not so much that it damages the cells. Animal cells have no cell wall, and the question "how much shear can they take?" has no single answer, because the stress that matters depends on the size of the cell or aggregate compared with the smallest eddies in the flow. This lesson introduces the eddy picture of turbulence, computes the smallest eddy size (the Kolmogorov scale) and the stress at that scale from the power per volume, compares it with the size of a cell and of a microcarrier, and explains why a stirrer's tip speed is a poor proxy for hydrodynamic stress on small particles. All values are synthetic and the thresholds are empirical in real systems.

## Learning objectives

By the end of this lesson, you should be able to:

1. Convert power per volume into an energy dissipation rate, a Kolmogorov scale and a stress at that scale.
2. Compare the eddy scale with the size of a cell or microcarrier and compute a stirring level that keeps eddies above a chosen size.
3. Evaluate why average power per volume, tip speed and local dissipation give different pictures of shear.

## Dissipation and the smallest eddies

The power input of a stirrer is dissipated as heat by viscosity, in the smallest eddies. The dissipation rate per mass is

**ε = (P/V)/ρ.**

For the lab vessel of the lesson on scale-up, P/V = 21.6 W/m³ and ρ = 1000 kg/m³, so ε = **0.0216 W/kg**. Turbulence transfers energy from large eddies (of the size of the impeller) to smaller and smaller ones until viscosity removes it. The size of the smallest eddies is the Kolmogorov microscale

**η_K = (ν³/ε)^(1/4),**

where ν = μ/ρ = 0.70 × 10⁻⁶ m²/s is the kinematic viscosity. Here η_K = ((0.70 × 10⁻⁶)³/0.0216)^(1/4) = **63.1 μm**. A cell of 10 to 20 μm is much smaller than these eddies and sees mainly the viscous shear of the local flow, which at the Kolmogorov scale has the stress τ = μ (ε/ν)^(1/2) = 0.00070 × (0.0216/(0.70 × 10⁻⁶))^(1/2) = **0.123 Pa**. A microcarrier or an aggregate of 150 μm is larger than the Kolmogorov scale, so eddies of its own size collide with it and exert more severe stress; the rule of thumb in the microcarrier literature compares η_K with the particle size, with damage becoming likely when the eddies are smaller than the particle or a fraction of it, although the threshold is empirical and depends on cell line, carrier and medium.

## Average and local dissipation

The average ε understates what cells near the impeller see. The dissipation is concentrated in the impeller region, where it is higher than the average by a factor that depends on geometry; an illustrative factor of 100 gives ε_local = **2.16 W/kg**, a Kolmogorov scale of **20.0 μm** (smaller by 100^(1/4) = 3.16) and a stress of 1.23 Pa. Against a 150 μm microcarrier, the ratio η_K/d falls from 0.42 (average) to **0.13** (local). A cell passing through the impeller zone sees this local value for a short time and then returns to the bulk, so the damage depends on the stress and on how long and how often the cell is exposed.

To keep local eddies above one third of the carrier diameter (50 μm), the local dissipation must not exceed ν³/η⁴ = 0.0549 W/kg, which with the factor of 100 corresponds to an average power per volume of only **0.55 W/m³**, hundreds of times lower than the lab vessel's 21.6 W/m³. This is why microcarrier cultures are stirred gently and why aeration by sparging is often avoided or separated from the cells.

## Tip speed is a poor proxy

In geometrically similar vessels the maximum local dissipation is proportional to P/V, because it scales as (tip speed)³/D = π³ N³D². At constant power per volume the tip speed rises on scale-up (the lesson on scale-up found a factor of 2.15) while the Kolmogorov scale in the impeller region stays unchanged. Tip speed describes the large-scale velocity difference, and what matters to a particle smaller than the large eddies is the dissipation. Scale-up can still change the exposure, since cells circulate through the impeller zone less often in a large vessel. Rising bubbles are a separate source of damage: bubbles bursting at the surface kill cells in their film, and surfactants such as Pluronic F-68 are commonly added to protect them, which is an additional reason that oxygen transfer and shear must be considered together.

## Common mistakes

- Using the tip speed as a measure of the stress on a cell.
- Applying the average dissipation where the local value near the impeller matters.
- Quoting a damage threshold from one system as a property of cells in general.
- Comparing the Kolmogorov scale with the size of a single cell when cells are on microcarriers or in aggregates.
- Forgetting that bubble bursting damages cells independently of stirring.
- Ignoring the exposure time and frequency, and looking only at the peak stress.

## Worked example

**Problem.** A synthetic vessel has P/V = 50 W/m³ and microcarriers of 100 μm. Taking a local factor of 50, find the average and local Kolmogorov scales and the local stress, and judge them against the carrier size.

**Step 1: average dissipation.** ε = 50/1000 = 0.050 W/kg and η_K = 51.2 μm.

**Step 2: local dissipation.** ε_local = 50 × 0.050 = 2.50 W/kg, giving η_K = 19.2 μm and τ = 1.32 Pa.

**Step 3: comparison.** The average η_K/d = 0.51, and the local value is 0.19: eddies near the impeller are well below the carrier size.

**Step 4: reading the result.** Whether this damages the culture cannot be computed; it points to the impeller region as the place to look and to a lower P/V as the first thing to test.

## Limits of this lesson

All numbers are synthetic. The Kolmogorov scale and the stress formula assume homogeneous, isotropic turbulence, which is not true near an impeller; the local factor is an illustrative number, damage thresholds are empirical and specific to the system, and bubbles, sparging and cell sensitivity are not modeled. Nothing here is a design or a statement about any real cell line.
