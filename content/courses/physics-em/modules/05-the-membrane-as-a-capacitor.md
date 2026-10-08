# The cell membrane as a capacitor: charge, ions, fields and the membrane time constant

A lipid bilayer is a thin insulator separating two salt solutions, which is the definition of a capacitor. That single observation explains several facts that otherwise seem surprising: why so few ions need to move to change a cell's voltage, why the electric field across a membrane is enormous, and why membranes respond to current with a characteristic delay. This lesson applies capacitor physics to an idealized spherical cell.

## Learning objectives

By the end of this lesson, you should be able to:

1. Calculate a cell's membrane capacitance from specific capacitance and area, and relate it to the dielectric constant and thickness with C = εA/d.
2. Compute the charge and number of ions needed to change membrane potential and compare it with the ions present in the cell.
3. Calculate the electric field across the membrane and the membrane RC time constant, and interpret both.

## Capacitance of a membrane

For a parallel-plate capacitor, **C = ε₀ε_r A / d**, where A is area, d the separation and ε_r the relative permittivity of the insulator. Cell membranes are so thin that curvature can be ignored, and their capacitance per area, the **specific capacitance**, is close to 1 μF/cm² (0.01 F/m²) across many cell types. Inverting the formula with a thickness of 5 nm gives the implied relative permittivity: ε_r = C_m d / ε₀ = 0.01 × 5×10⁻⁹ / 8.854×10⁻¹² = 5.6, a plausible value for a hydrocarbon layer with polar head groups.

**Synthetic cell:** a sphere of radius 10 μm has area 4πr² = 1.257×10⁻⁹ m², so C = 0.01 × 1.257×10⁻⁹ = 1.257×10⁻¹¹ F = 12.6 pF.

## How many ions change the voltage?

Charge on a capacitor is **Q = CV**. To change the membrane potential by 100 mV (roughly the swing of an action potential), Q = 1.257×10⁻¹¹ × 0.1 = 1.257×10⁻¹² C. Dividing by the elementary charge, that is 7.84×10⁶ monovalent ions.

Compare that with the potassium inside. At about 140 mM in a cell volume of (4/3)πr³ = 4.189×10⁻¹² L, the cell contains 3.53×10¹¹ potassium ions. The ions that cross to produce the full swing are about 2.2×10⁻⁵ of them, roughly two thousandths of one percent. This is why a single action potential barely changes intracellular concentrations, and why pumps can restore gradients over much longer times. It is also why the bulk solutions on either side remain electrically neutral to an excellent approximation; the net charge sits in a thin layer against the membrane.

## The field across the membrane

A resting potential of 70 mV across 5 nm gives a field **E = V/d** = 0.070 / 5×10⁻⁹ = 1.4×10⁷ V/m. This is comparable to the field at which many insulators break down. Voltage-gated channels have charged segments that move in this field, which is how a change of tens of millivolts can open or close them. Applying external fields large enough to raise this voltage by several hundred millivolts can transiently permeabilize the membrane, the principle behind electroporation.

## The membrane time constant

Ion channels make the membrane a leaky capacitor: a resistor in parallel with the capacitance. For a patch of membrane, the time constant is **τ = R_m C_m**, the product of specific resistance (Ω·m²) and specific capacitance (F/m²), and so does not depend on the cell's size. With a synthetic R_m = 10 kΩ·cm² = 1 Ω·m², τ = 1 × 0.01 = 10 ms. A step of injected current changes the voltage as V(t) = IR(1 − e^(−t/τ)), reaching 63% of its final value after τ. Opening more channels lowers R_m and shortens τ, so the cell responds faster but integrates inputs over a shorter window.

## Common mistakes

- Confusing specific capacitance (per area) with total capacitance (multiplied by area).
- Forgetting the 10⁴ factor between cm² and m², or the 10³ between L and m³.
- Concluding that an action potential depletes intracellular potassium.
- Using the cell diameter as the radius when computing area or volume.

## Worked example

**Problem.** A synthetic neuron's soma is a sphere of radius 20 μm. How do its capacitance, the ions needed for a 100 mV swing, and its time constant change relative to the 10 μm cell?

**Step 1: capacitance.** Area scales with r², so C is four times larger: 50.3 pF.

**Step 2: ions.** Q = CV is four times larger, 3.14×10⁷ ions; but volume scales with r³, so the fraction of the cell's potassium involved halves, to 1.1×10⁻⁵.

**Step 3: time constant.** τ = R_m C_m is unchanged at 10 ms, because both total resistance and total capacitance scale with area, in opposite directions. Size changes how much current is needed, not how fast the membrane responds.

## Limits of this lesson

All values are synthetic and round. Real cells have complex shapes, dendrites, and membrane regions with different properties; the uniform-sphere model ignores them.
