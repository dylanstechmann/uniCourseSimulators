# Fluid exchange across capillaries: Starling forces, filtration, absorption and why edema forms

Blood plasma is constantly filtered out of capillaries into tissue and returned, partly by reabsorption and partly by lymph. The balance is set by four pressures, two pushing fluid out and two pulling it in, together with the wall's permeability. When the balance shifts, fluid accumulates in tissue as edema. The same forces matter for engineered tissues and organ-on-chip devices, where the walls of perfused channels are themselves leaky. This lesson computes net filtration pressure along a capillary with synthetic values and predicts the effect of perturbations.

## Learning objectives

By the end of this lesson, you should be able to:

1. Calculate net filtration pressure from hydrostatic and oncotic pressures with a reflection coefficient using the Starling equation.
2. Compute a filtration rate from the filtration coefficient and net pressure, and predict where along a capillary fluid leaves or returns.
3. Predict how changes in capillary pressure, plasma protein or wall permeability shift fluid balance, and explain the role of lymph.

## The Starling equation

The volume flux across a capillary wall is

**J_v = K_f [(P_c − P_i) − σ(π_c − π_i)],**

- P_c and P_i: hydrostatic pressures in the capillary and the interstitium;
- π_c and π_i: oncotic (colloid osmotic) pressures from proteins, mainly albumin, in plasma and interstitial fluid;
- σ: the reflection coefficient, from 0 (wall fully permeable to protein) to 1 (fully impermeable);
- K_f: the filtration coefficient, combining wall permeability to water and surface area.

Positive J_v means filtration out of the capillary.

## Along a capillary

**Synthetic values:** P_i = 0, π_c = 25, π_i = 5 mmHg, σ = 0.9. The oncotic term is σ(π_c − π_i) = 0.9 × 20 = 18 mmHg, roughly constant along the vessel.

- At the arterial end, P_c = 35 mmHg: net = 35 − 18 = 17 mmHg, so fluid filters out.
- At the venous end, P_c = 15 mmHg: net = 15 − 18 = -3 mmHg, so fluid is reabsorbed.

The classic picture of filtration at one end and reabsorption at the other is a simplification. Measurements in many tissues suggest that, at steady state, most capillaries filter along most of their length and that lymph returns most of the filtered fluid; the interstitial oncotic pressure just outside the wall can be higher than bulk interstitial values suggest. The equation still applies; the inputs are what is debated.

## From pressure to flow

Using a synthetic mean capillary pressure of 25 mmHg, the net pressure is 7 mmHg. With a whole-tissue filtration coefficient of 0.5 mL/min per mmHg, filtration is J_v = 0.5 × 7 = 3.5 mL/min. That fluid must leave the tissue through lymphatics for the interstitial volume to stay constant.

## Perturbations and edema

Edema develops when filtration exceeds lymph drainage. Each Starling term gives a route:

- **Higher capillary pressure** (for example, from raised venous pressure in heart failure, or from standing): raising mean P_c to 30 mmHg raises filtration to 6.0 mL/min.
- **Lower plasma oncotic pressure** (low albumin from liver disease, kidney protein loss or malnutrition): with π_c = 15 mmHg, the arterial-end net pressure rises from 17 to 26 mmHg.
- **Leakier walls** (inflammation): σ falls and K_f rises, so protein leaks out, π_i rises, and the opposing oncotic force collapses.
- **Impaired lymph drainage**: filtration is normal but not removed.

Tissue has safety factors: as interstitial fluid accumulates, P_i rises and π_i falls through dilution and washout, both opposing further filtration. Edema becomes visible when these are exhausted.

## Common mistakes

- Forgetting the reflection coefficient, which overstates the oncotic force.
- Treating the venous-end reabsorption picture as established for all tissues.
- Ignoring lymph flow when asking whether fluid accumulates.
- Mixing up signs: positive net pressure means filtration out.
- Assuming every tissue has the same K_f; lung, kidney and muscle capillaries differ widely.

## Worked example

**Problem.** In a perfused hydrogel channel lined with cells (an organ-on-chip), the medium has no added protein (π_c ≈ 0), channel pressure is 10 mmHg and the gel's fluid pressure is about 0. What happens to fluid, and what changes would reduce leakage?

**Step 1.** Net pressure ≈ 10 − σ(0 − 0) = 10 mmHg: fluid filters into the gel continuously.

**Step 2.** Adding protein (for example albumin) to the medium creates an oncotic force if the cell layer has a meaningful σ; lowering channel pressure reduces the hydrostatic drive.

**Step 3.** Measuring leakage rate against channel pressure gives K_f for the engineered wall, a useful barrier-function readout. The chip is a synthetic example; the same balance governs native tissue.

## Limits of this lesson

All pressures and coefficients are synthetic and round. Real capillaries vary by organ (the kidney glomerulus and lung differ greatly), and the glycocalyx layer modifies the effective oncotic gradient.
