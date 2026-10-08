# Membrane potential: the Nernst potential, the Goldman–Hodgkin–Katz equation and why extracellular potassium matters

Every living cell maintains different ion concentrations inside and outside, and its membrane lets some ions cross much more easily than others. The result is a voltage across the membrane, the membrane potential, which is the basis of nerve signalling, muscle contraction and many cell-sorting and signalling processes. This lesson derives the voltage that a single permeant ion would set, combines several ions into the resting potential, and uses the model to predict what a change in extracellular potassium does. All concentrations and permeabilities are synthetic and round.

## Learning objectives

By the end of this lesson, you should be able to:

1. Calculate the Nernst equilibrium potential of an ion from its concentrations on either side of the membrane.
2. Compute a resting membrane potential from relative permeabilities with the Goldman–Hodgkin–Katz equation, and as a conductance-weighted average of reversal potentials.
3. Predict how a change in extracellular potassium shifts the resting potential, and explain why it changes less than the potassium equilibrium potential does.

## The Nernst potential

If a membrane were permeable to one ion only, that ion would diffuse down its concentration gradient until the resulting voltage exactly opposed further net movement. That voltage is the **Nernst (equilibrium) potential**:

**E_ion = (RT / zF) ln([ion]_out / [ion]_in).**

At 37 °C, RT/F = 26.73 mV, and converting to base-10 logarithms gives 61.5 mV per tenfold ratio for a monovalent ion (divide by z for other valences). The sign convention is inside relative to outside.

**Synthetic concentrations (mM):** K⁺ 5 outside and 140 inside; Na⁺ 145 outside and 12 inside. Then

- E_K = 61.5 × log₁₀(5/140) = -89.1 mV;
- E_Na = 61.5 × log₁₀(145/12) = +66.6 mV.

The two are far apart: a membrane that was permeable only to potassium would sit near -89 mV, and one permeable only to sodium near +67 mV.

## From currents to the resting potential

For each ion the current across the membrane is I_i = g_i (V − E_i), where g_i is the membrane's conductance to that ion and E_i its Nernst potential. At rest, the net current is zero, so the voltage is a conductance-weighted average of the reversal potentials:

**V = Σ g_i E_i / Σ g_i.**

With synthetic relative conductances g_K = 1.0 and g_Na = 0.15, V = (1.0 × -89.1 + 0.15 × 66.6)/1.15 = -68.8 mV. The voltage sits close to E_K because potassium dominates the conductance. During an action potential, voltage-gated sodium channels open and g_Na rises sharply; if g_Na were 20 times g_K, V would be (-89.1 + 20 × 66.6)/21 = +59 mV. The real peak is lower than E_Na because sodium channels inactivate and potassium channels open within a millisecond or two.

The **Goldman–Hodgkin–Katz (GHK) equation** expresses the same balance in terms of permeabilities rather than conductances, using concentrations directly:

**V = 61.5 log₁₀[(P_K [K]_out + P_Na [Na]_out) / (P_K [K]_in + P_Na [Na]_in)]** (mV, 37 °C, monovalent cations).

With relative permeabilities P_K : P_Na = 1 : 0.04 and the concentrations above,

V = 61.5 × log₁₀[(1 × 5 + 0.04 × 145) / (1 × 140 + 0.04 × 12)] = -68.6 mV.

Chloride contributes in many cells; with a chloride permeability added, the same equation gains a [Cl]_in term in the numerator and a [Cl]_out term in the denominator, and the resting potential moves toward E_Cl.

## Why extracellular potassium matters

Raise extracellular potassium from 5 to 8 mM. The potassium Nernst potential changes from -89.1 to -76.5 mV, a shift of 12.6 mV. The GHK resting potential changes from -68.6 to -62.0 mV, a shift of only 6.6 mV. The cell depolarizes less than E_K because the small sodium permeability pulls the voltage toward E_Na, and the effect of a given change in [K]_out is damped by that fixed pull.

Depolarization of that size moves the cell toward the threshold for firing, but it is not simply "more excitable": a sustained depolarization also inactivates voltage-gated sodium channels, which reduces excitability. The direction of the net effect depends on how large and how prolonged the shift is, which is why disturbances of extracellular potassium are studied in physiology and managed by clinicians; this lesson explains the arithmetic only and gives no medical advice.

## Common mistakes

- Using concentration ratios with the wrong orientation, which flips the sign of the Nernst potential.
- Forgetting that the factor is 61.5 mV per decade only for monovalent ions at 37 °C.
- Treating the resting potential as equal to E_K, when sodium permeability pulls it above E_K.
- Expecting the resting potential to follow E_K one-for-one when extracellular potassium changes.
- Mixing conductances with permeabilities: conductance depends on concentrations as well as on the channels.
- Assuming that depolarization always raises excitability.

## Worked example

**Problem.** In a second synthetic cell, [K]_out = 4 mM, [K]_in = 150 mM, [Na]_out = 140 mM and [Na]_in = 10 mM, with P_K : P_Na = 1 : 0.05. Find E_K and the GHK resting potential.

**Step 1: Nernst.** E_K = 61.5 × log₁₀(4/150) = -96.9 mV.

**Step 2: GHK.** Numerator 4 + 0.05 × 140 = 11.0; denominator 150 + 0.05 × 10 = 150.5; V = 61.5 × log₁₀(11.0/150.5) = -69.9 mV.

**Step 3: compare.** V is about 26.9 mV above E_K, the pull from sodium.

## Limits of this lesson

The values are synthetic. The GHK equation assumes a constant electric field and independent ions; real channels have voltage-dependent and time-dependent permeabilities, pumps contribute a small direct current, and cell volume and ion concentrations change over time. Excitability depends on channel kinetics and cable properties, which this lesson does not cover.
