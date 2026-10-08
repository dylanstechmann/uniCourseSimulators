# Redox direction and metal centers: the Nernst equation, electron flow and why ligands matter

Electrons flow from one molecule to another along gradients of reduction potential, and many of the molecules that pass them along hold a metal ion in a carefully shaped pocket. This lesson puts numbers on both ideas. The Nernst equation shows how a couple's actual potential depends on the ratio of oxidized to reduced forms, which sets the direction of electron transfer. Coordination chemistry explains how the geometry and ligands around a metal tune what it does, and how a chelator can strip metal ions from a solution.

## Learning objectives

By the end of this lesson, you should be able to:

1. Use the Nernst equation to compute the actual reduction potential of a couple from its standard potential and the ratio of oxidized to reduced forms.
2. Predict the direction of electron transfer between two couples and compute the free-energy change from their potential difference.
3. Explain coordination number, geometry and ligand effects for biological metal centers, and calculate the free metal ion left after chelation.

## Reduction potentials and the Nernst equation

A half-reaction is written as a reduction, Ox + n e⁻ → Red, with a standard potential E°′ (biochemical standard state, pH 7). The higher the potential, the stronger the tendency to accept electrons. The actual potential depends on concentrations:

**E = E°′ + (2.303 RT / nF) log₁₀([Ox]/[Red]).**

At 37 °C, 2.303 RT/F = 0.06155 V, so each tenfold change in the ratio shifts a one-electron couple by about 62 mV and a two-electron couple by about 31 mV.

**Synthetic example:** the NAD⁺/NADH couple (E°′ = -0.32 V, n = 2) in a compartment where [NAD⁺]/[NADH] = 10 has E = -0.32 + (0.06155/2) × log₁₀(10) = -0.2892 V. A more oxidized pool (higher ratio) makes NADH a weaker electron donor, which is why the redox state of a compartment matters, not only the standard potential.

## Which way do electrons go?

Electrons flow spontaneously from the couple with the lower actual potential to the couple with the higher one. The free-energy change for transferring n electrons is

**ΔG = −nF ΔE,** with ΔE = E(acceptor) − E(donor).

For electrons from the NADH pool above to a synthetic quinone-like acceptor at E = 0.045 V: ΔE = 0.045 − (-0.2892) = 0.3342 V and ΔG = −2 × 96485 × 0.3342 = -64.5 kJ/mol. A negative ΔG confirms the direction. In the respiratory chain, this is the first step of a descent through carriers of increasing potential to oxygen.

## Metal centers: coordination number, geometry and ligands

A metal ion in a protein is held by **ligands**, atoms with lone pairs that donate into the metal's empty orbitals. The **coordination number** is the number of donor atoms bound; common geometries are tetrahedral (4), square planar (4) and octahedral (6). Examples:

- In heme, iron sits in a porphyrin ring that supplies four nitrogen ligands in a plane. A histidine from the protein binds below, and the sixth site above binds O₂ in hemoglobin and myoglobin: an octahedral, six-coordinate iron. Only Fe²⁺ binds O₂ reversibly; oxidized Fe³⁺ (as in methemoglobin) does not.
- Zinc in many structural motifs is tetrahedral, held by cysteine sulfurs and histidine nitrogens; it does not change oxidation state, which suits a structural role.
- Copper and iron centers that do change oxidation state carry electrons. The ligands and geometry shift their reduction potentials by hundreds of millivolts, which is how one metal serves at different steps of a chain.

Ligands also split the energies of the metal's d orbitals (ligand-field splitting). The size of the split determines which wavelengths are absorbed, which is why heme proteins change color when they bind oxygen or change oxidation state.

## Chelation

A **chelator** binds a metal through several donor atoms at once. EDTA, a hexadentate ligand, wraps a metal ion with six donors and binds far more strongly than six separate monodentate ligands would (the chelate effect). That is why EDTA-containing solutions are used to detach adherent cells: they remove Ca²⁺ and Mg²⁺ needed by adhesion proteins.

With a synthetic conditional formation constant K_f = 10⁷ M⁻¹ at the working pH, [CaY] = 1 mM and excess free EDTA [Y] = 1 mM, the free calcium is [Ca²⁺] = [CaY]/(K_f [Y]) = 0.1 μM, roughly ten-thousandfold below the bound amount.

## Common mistakes

- Writing the Nernst ratio upside down; for a reduction written Ox + ne⁻ → Red, a higher Ox/Red ratio raises E.
- Using standard potentials to predict direction when the actual ratios are far from 1.
- Forgetting n in both the Nernst slope and ΔG = −nFΔE.
- Assuming all metal sites do redox chemistry; zinc sites are usually structural.

## Worked example

**Problem.** How much would the NAD⁺/NADH ratio have to rise for the couple's potential to increase by 60 mV at 37 °C?

**Step 1.** For n = 2, each decade of ratio adds 30.8 mV.

**Step 2.** 60 mV / 30.8 mV ≈ 1.95 decades, a factor of 10^1.95 ≈ 89.

**Step 3.** Large shifts in a two-electron couple's potential need large changes in the ratio, which is one reason cells can hold different compartments at substantially different redox states.

## Limits of this lesson

All concentrations and the quinone-like potential are synthetic. Conditional formation constants depend on pH and competing ions, and potentials of protein-bound centers depend on their environment.
