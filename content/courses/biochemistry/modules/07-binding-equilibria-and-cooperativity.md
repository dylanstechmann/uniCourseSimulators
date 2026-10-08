# Binding equilibria: dissociation constants, ligand depletion and cooperative binding

Almost everything a protein does begins with binding: a receptor binds a hormone, an antibody binds an antigen, hemoglobin binds oxygen. A single number, the dissociation constant, summarizes how tightly a ligand binds, and simple equations predict how much is bound at a given concentration. Two complications matter in practice: when the receptor is as concentrated as the ligand, the free ligand is depleted and the simple equation misleads; and when binding sites interact, the binding curve becomes sigmoidal, which is how hemoglobin delivers oxygen efficiently. This lesson computes each with synthetic and textbook-like values.

## Learning objectives

By the end of this lesson, you should be able to:

1. Use the dissociation constant to compute fractional occupancy at a given free ligand concentration and interpret K_d.
2. Account for ligand depletion with the exact quadratic solution and judge when the simple hyperbolic equation is adequate.
3. Use the Hill equation to describe cooperative binding and compare oxygen unloading by cooperative and non-cooperative carriers.

## The dissociation constant

For R + L ⇌ RL, the dissociation constant is K_d = [R][L]/[RL], with units of concentration. Fractional occupancy, the fraction of receptors with ligand bound, is

**θ = [L]_free / (K_d + [L]_free).**

K_d is the free ligand concentration at which half the receptors are occupied. With synthetic K_d = 10 nM and free ligand 30 nM, θ = 30/(10 + 30) = 0.75. Lower K_d means tighter binding. The equation has the same hyperbolic form as Michaelis–Menten kinetics, but K_d is a true equilibrium constant, whereas K_m generally is not.

## Ligand depletion

The equation uses free ligand. In many experiments only the total amount added is known. If the receptor concentration is much smaller than K_d, binding barely depletes the ligand and free ≈ total. If not, the exact solution comes from mass balance and the quadratic formula:

**[RL] = {(R_T + L_T + K_d) − √[(R_T + L_T + K_d)² − 4 R_T L_T]} / 2.**

With R_T = L_T = 50 nM and K_d = 10 nM: [RL] = (110 − √(12100 − 10000))/2 = 32.1 nM. Assuming free = total would predict 41.7 nM, an overestimate of 30%. Ligand depletion also distorts apparent K_d values measured by titration. A practical rule: keep the receptor concentration well below K_d (by tenfold or more) or use the quadratic.

## Cooperative binding and the Hill equation

When a protein has several sites that influence each other, binding at one site can raise affinity at the others. The binding curve then becomes sigmoidal and is often summarized by the Hill equation:

**Y = Pⁿ / (P₅₀ⁿ + Pⁿ),**

with n the Hill coefficient (n = 1 for independent sites; n > 1 for positive cooperativity) and P₅₀ the concentration or partial pressure at half saturation. n is an empirical steepness parameter, not the number of sites; it is at most the number of sites.

**Oxygen delivery.** Using hemoglobin-like values (n = 2.8, P₅₀ = 26 mmHg), saturation is 97.8% at 100 mmHg (lungs) and 77.0% at 40 mmHg (resting tissue), so 20.8% of the carrier's capacity is unloaded. A non-cooperative, myoglobin-like carrier (n = 1, P₅₀ = 2.8 mmHg) is 97.3% saturated at 100 mmHg and 93.5% at 40 mmHg, unloading only 3.8%. The sigmoid curve is steep in exactly the range between lung and tissue pressures, which is what makes cooperative binding effective for transport. Factors such as lower pH, higher CO₂ and 2,3-bisphosphoglycerate shift hemoglobin's P₅₀ to the right, increasing unloading in active tissue.

## Measuring binding in practice

K_d is measured by titrating one partner and recording a signal that reports the bound fraction: fluorescence, radioactivity, a change in heat (isothermal titration calorimetry) or a change in mass on a sensor surface. Each method has its own assumptions. A signal may not be strictly proportional to occupancy, nonspecific binding has to be measured separately and subtracted, and equilibrium must actually be reached: tight binders can take hours to equilibrate at low concentrations. Reporting the receptor concentration, the incubation time and how nonspecific binding was handled lets a reader judge whether a reported K_d is an affinity or an artifact of the assay.

## Common mistakes

- Using total ligand in θ = L/(K_d + L) when the receptor concentration is comparable to K_d.
- Reading the Hill coefficient as the number of binding sites.
- Equating K_m with K_d.
- Comparing saturations at a single pressure instead of the difference between loading and unloading pressures.

## Worked example

**Problem.** If P₅₀ shifts from 26 to 30 mmHg (more acidic tissue) with n unchanged, how much more oxygen is unloaded between 100 and 40 mmHg?

**Step 1.** At 100 mmHg, Y = 100^2.8/(30^2.8 + 100^2.8) = 96.7%.

**Step 2.** At 40 mmHg, Y = 69.1%.

**Step 3.** Unloading is now 27.6%, up from 20.8%: a rightward shift barely affects loading in the lungs but increases delivery to tissue.

## Limits of this lesson

Values are synthetic or rounded textbook-like numbers, and concentrations are treated as activities. Real oxygen binding depends on temperature, pH and allosteric effectors that this summary treats only qualitatively.
