# Polymer degradation by chain scission: molecular weight, mass loss and erosion mode

The lesson on hydrogel degradation described mass loss as a first-order process. That is a useful summary of what a balance reads, but it hides what happens inside the material. A polymer does not lose mass when a bond breaks; it loses mass only when the pieces are small enough to dissolve and leave. Long before that, every break shortens a chain, and the properties that depend on chain length, such as strength and toughness, change first. This lesson models random chain scission, computes how the average molar mass falls and when mass loss begins, and uses a critical thickness to decide whether a device degrades throughout or from its surface. All rate constants and sizes are synthetic and chosen for round numbers, not measured on any real polymer.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute the fraction of bonds cleaved and the number-average molar mass for random chain scission.
2. Estimate when chains become small enough to dissolve and the mass remaining under a lag model.
3. Classify erosion as bulk or surface using a critical thickness and evaluate which measurements show degradation.

## Random scission and the number-average molar mass

Suppose every bond in the backbone is cleaved at random by hydrolysis with a first-order rate constant k per bond. The fraction of bonds cleaved after time t is

**p(t) = 1 − e^(−kt).**

Each break creates one new chain, so the number of chains per unit mass grows with p, and the number-average molar mass follows

**1/Mn(t) = 1/Mn0 + p(t)/M_u,**

where Mn0 is the starting value and M_u the molar mass of the repeat unit. **Synthetic values:** Mn0 = 100 kDa, M_u = 72 g/mol (so a chain has about 1,389 bonds) and k = 0.0002 per day. After 28 days p = **0.56%** and Mn = **11.4 kDa**; after 56 days p = 1.11% and Mn = 6.1 kDa. Breaking about one bond in 179 has already cut the average chain length by 89%, because every break splits a long chain in two. Strength, toughness and the ability to hold a suture depend on chain length, so they can be lost while the device looks and weighs the same.

## From molecular weight to mass loss

Mass is lost when fragments become soluble. Take a synthetic critical molar mass of 5 kDa. The fraction of bonds that must be cleaved is p_crit = M_u (1/M_crit − 1/Mn0) = 72 × (1/5000 − 1/100000) = 0.0137, which takes t_c = −ln(1 − p_crit)/k = **68.9 days**. Until then the mass is essentially unchanged. A simple **lag model** then lets the mass fall first-order with a rate k_m = 0.02 per day: M(t)/M₀ = e^(−k_m (t − t_c)), so 53.7% remains at day 100 and half the mass is gone at t_c + ln 2/k_m = 103.5 days. A balance reading at day 60 would show 100% of the mass remaining, and the chains would already be 18 times shorter. A design for mechanical support must therefore track a chain-length or mechanical measurement, not mass alone.

## Bulk or surface erosion?

The simple picture of the earlier lesson can be made quantitative with a time-scale comparison. Water and oligomers cross a thickness L in about τ_D = L²/D, while a bond reacts in about 1/k. If τ_D is much shorter than 1/k, water saturates the device before many bonds have broken and degradation takes place throughout (**bulk erosion**); if τ_D is much longer, bonds break in a surface layer before water penetrates (**surface erosion**). Setting τ_D = 1/k gives a critical thickness

**L_c = √(D/k).**

With a synthetic effective diffusion coefficient D = 0.009 mm²/day, L_c = √(0.009/0.0002) = **6.7 mm**. A 1 mm wall has τ_D = 111 days against 1/k = 5,000 days (τ_D k = 0.02), so it degrades in bulk; a 10 mm block has τ_D = 11,111 days (τ_D k = 2.2) and degrades more from the surface inward. The heuristic ignores a real complication: in thick polyester devices, acidic end groups can be trapped inside and speed up degradation there, so the interior can degrade faster than the surface.

## Which measurements show degradation?

- **Molar mass** (by size-exclusion chromatography) shows scission directly and early.
- **Mass** shows loss of soluble fragments and lags.
- **Mechanical properties** show the loss of function, often between the two.
- **Medium pH and degradation products** show what the surroundings receive.

No single measurement tells the whole story, and rate constants measured in buffer at 37 °C are starting estimates for a tissue where enzymes and cells may speed degradation. When specimens are tested, the independent unit is the specimen, not the repeated measurements on it.

## Common mistakes

- Reading unchanged mass as unchanged material.
- Equating the fraction of bonds cleaved with the fraction of mass lost.
- Using the weight-average where the number-average is needed in the scission formula.
- Applying a rate constant per day to a time in weeks without converting.
- Assuming that a thick device degrades from its surface because a thin one degrades in bulk.
- Treating a rate measured in buffer as the rate in tissue.

## Worked example

**Problem.** A synthetic polymer has Mn0 = 60 kDa, M_u = 58 g/mol and k = 0.0004 per day, and chains dissolve below 4 kDa. Find Mn at day 30 and the time at which mass loss begins.

**Step 1: bonds cleaved at day 30.** p = 1 − e^(−0.0004 × 30) = 1.19%.

**Step 2: molar mass.** 1/Mn = 1/60000 + 0.0119/58, so Mn = 4498 g/mol (4.5 kDa), a fall of 93%.

**Step 3: onset of mass loss.** p_crit = 58 × (1/4000 − 1/60000) = 0.0135, so t_c = −ln(1 − 0.0135)/0.0004 = 34.1 days.

**Step 4: reading the result.** Chain length has already fallen by 93% at day 30, yet no mass has been lost; mass loss begins at about day 34.

## Limits of this lesson

All numbers are synthetic. Random scission with a single rate constant is a first model. Real polymers have crystalline regions that degrade more slowly, rate constants that change as acid accumulates, end-group effects, and enzymatic degradation in tissue. The critical-thickness argument is a heuristic. Nothing here is evidence about the degradation of any real polymer or implant.
