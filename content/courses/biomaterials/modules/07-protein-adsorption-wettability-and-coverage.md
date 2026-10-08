# Protein adsorption: wettability, coverage and the layer that cells actually meet

Within seconds of contact with blood, serum or culture medium, a material is coated with proteins. Cells then never meet the bare material; they meet this adsorbed layer, and which proteins it holds, how many, in what orientation and how tightly bound depend on both the surface and the fluid. This lesson quantifies three things with simple models: how wettability relates to the work of adhesion, how much protein a surface can hold, and how fast protein arrives. It then states what the models leave out. All values are synthetic and illustrative, of a plausible order of magnitude but not measurements of any real material.

## Learning objectives

By the end of this lesson, you should be able to:

1. Use Young's equation and the work of adhesion to compare the wettability of surfaces.
2. Apply the Langmuir isotherm and a molecular footprint to compute coverage, the concentration for a target coverage and the monolayer capacity.
3. Estimate diffusion-limited protein arrival and evaluate what a measurement of adsorbed protein does and does not show.

## Wettability and the work of adhesion

A drop of water on a surface makes a contact angle θ that balances three surface tensions, as in Young's equation:

**cos θ = (γ_sv − γ_sl) / γ_lv,**

where γ_sv is the solid–vapor, γ_sl the solid–liquid and γ_lv the liquid–vapor tension. With synthetic values γ_sv = 35, γ_sl = 10 and γ_lv = 72 mN/m, cos θ = 0.347 and θ = **69.7°**. The work of adhesion between water and the surface is

**W_a = γ_lv (1 + cos θ).**

For θ = 65° this is 72 × (1 + 0.4226) = **102.4 mN/m**, and for a more hydrophobic surface with θ = 110° it is 47.4 mN/m. A larger contact angle means water adheres less strongly. Hydrophobic surfaces tend to adsorb more protein and to hold it more tightly, because proteins expose hydrophobic patches that are driven out of water, but contact angle is only a screening measure: charge, roughness, chemistry and the particular protein all contribute, and two surfaces with equal angles can behave differently.

## How much protein: coverage and capacity

If protein adsorbs reversibly onto equivalent sites without interacting, the amount per area follows the Langmuir isotherm

**Γ = Γ_max C / (K_d + C),**

with Γ_max the monolayer capacity and K_d the concentration at half coverage. **Synthetic values:** Γ_max = 3.0 mg/m² and K_d = 0.05 mg/mL. At C = 0.2 mg/mL, coverage is C/(K_d + C) = 0.80 and Γ = 2.4 mg/m². Raising C to 1.0 mg/mL increases coverage only to 0.95, because the isotherm saturates: reaching 90% coverage needs C = 9 K_d = **0.45 mg/mL**.

The capacity itself comes from molecular size. A molecule of molar mass M that occupies a footprint A covers the surface at Γ_max = M / (N_A A). For a 66 kDa protein (66 kg/mol) lying side-on with A = 50 nm², Γ_max = 66 / (6.022 × 10²³ × 50 × 10⁻¹⁸) = **2.19 mg/m²**; standing end-on with A = 20 nm² it could hold 5.48 mg/m². Orientation changes both the mass held and which parts of the protein, including cell-binding sites, face the solution.

## How fast: diffusion-limited arrival

For a surface that captures every protein that reaches it from a still solution of concentration C, the adsorbed amount grows as

**Γ(t) = 2 C √(D t / π).**

With D = 60 μm²/s and C = 0.2 mg/mL, Γ(1 s) = **1.75 mg/m²**, which is already 58% of the capacity above, and half of the capacity (1.5 mg/m²) is reached after t = π (Γ / 2C)² / D = **0.74 s**. Transport to the surface is therefore rarely the slow step for a concentrated solution: within seconds the surface is crowded, and what happens next is rearrangement and exchange.

In a mixture, each protein arrives at a rate proportional to C √D. Using illustrative plasma-like values, albumin at 40 mg/mL with D = 61 μm²/s arrives (40/3) × √(61/20) = **23.3 times** faster than fibrinogen at 3 mg/mL with D = 20 μm²/s. Yet proteins with higher affinity can displace the early arrivers over time (the **Vroman effect**), so the composition of the layer at one second differs from that at one hour. The models above do not describe this competition.

## What a measurement of adsorbed protein shows

Techniques such as ellipsometry, surface plasmon resonance, quartz crystal microbalance and labeled-protein counting report an amount or a thickness, each with its own assumptions (a quartz crystal microbalance, for example, also senses coupled water). An amount per area does not say whether the protein is folded, which side faces the cells or whether cell-binding sites are accessible, and results in a single-protein buffer do not transfer to serum. Cells respond to the layer that forms in their own medium, so adhesion should be measured under the conditions of use.

## Common mistakes

- Treating the contact angle as a direct measure of how much protein adsorbs.
- Treating a monolayer as a fixed number, when orientation changes the capacity.
- Expecting coverage to rise in proportion to concentration after the isotherm saturates.
- Taking the most abundant protein in solution as the one that stays on the surface.
- Reading adsorbed mass as biological activity.
- Concluding from a single-protein result that the same layer forms in serum.

## Worked example

**Problem.** A synthetic 45 kDa protein has a side-on footprint of 30 nm², K_d = 0.1 mg/mL and D = 80 μm²/s. At C = 0.3 mg/mL, what is the capacity, the equilibrium amount and the diffusion-limited time to reach it?

**Step 1: capacity.** Γ_max = 45/(6.022 × 10²³ × 30 × 10⁻¹⁸) = 2.49 mg/m².

**Step 2: equilibrium amount.** Coverage = 0.3/(0.1 + 0.3) = 0.75, so Γ = 2.49 × 0.75 = 1.87 mg/m².

**Step 3: arrival time.** With Γ = 1.87 mg/m² = 1.87 × 10⁻⁶ kg/m², C = 0.3 mg/mL = 0.3 kg/m³ and D = 80 μm²/s = 8.0 × 10⁻¹¹ m²/s, t = π (Γ / 2C)² / D = π × (1.87 × 10⁻⁶ / 0.6)² / (8.0 × 10⁻¹¹) = 0.38 s.

**Step 4: reading the result.** Transport takes well under a second here, so any slower change in the layer comes from rearrangement or exchange, not from delivery of protein.

## Limits of this lesson

All values are synthetic. The Langmuir model assumes reversible adsorption on identical sites without lateral interaction, while real protein adsorption is often partly irreversible and changes with time; the diffusion-limited formula assumes a perfectly absorbing surface and still solution, and ignores convection, which matters in flow. This lesson says nothing about the response of any real cell or tissue to any real material.
