# Atoms, amount and photon accounting

## Learning objectives

1. Relate proton, neutron and electron counts to isotope and ion notation.
2. Convert between specified entities, amount and a synthetic isotope average.
3. Calculate photon energies while distinguishing exact constants from uncertain inputs.

## Identity, isotope and charge

The atomic number Z counts protons and identifies an element. The mass number A counts protons plus neutrons in one isotope, so neutron count is A−Z. Electron count changes with ionic charge: a positive ion has lost electrons, and a negative ion has gained them. Changing electron count does not change the nucleus into a different element. A nucleus with Z=12 and A=24 has 12 neutrons; its ion with charge +2 has 10 electrons.

Mass number is an integer count, not the measured atomic mass in unified atomic mass units. Nuclear binding and electron masses prevent treating every isotope's mass as exactly its mass number. In a natural sample, isotope abundances also matter. Specify whether a number is an isotope count, an isotope mass, a relative atomic mass or a molar mass before using it in a conversion.

For a constructed element X, suppose isotope masses are exactly stipulated as 35.0 and 37.0 in the exercise scale, with amount fractions 0.75 and 0.25. The weighted mean is 0.75×35.0+0.25×37.0=35.5. This is a synthetic distribution, not a tabulated atomic weight of chlorine. Fractions must sum to one; using mass fractions as though they were amount fractions would answer a different question.

## What a mole counts

Amount n and entity count N satisfy N=nN_A. The [NIST SI definitions](https://www.nist.gov/pml/special-publication-330/sp-330-section-2) fix N_A at 6.02214076 × 10²³ mol⁻¹. A mole counts specified entities, which might be atoms, molecules or ions. It is not a fixed mass for every substance. A constructed 0.025 mol sample contains 1.50553519 × 10²² of the specified entities. An answer in “particles” should identify what particle is being counted.

For a molecular compound, count atoms from its formula after counting molecules. One mole of molecules containing two hydrogen atoms each contains two moles of those hydrogen atoms. That does not imply the sample contains one mole of free hydrogen gas. Formula accounting describes composition and must be separated from chemical state.

Molar mass converts n to mass by m=nM. The SI amount-count relation is exact, while a measured mass, composition or molar mass generally carries uncertainty. Keeping many calculator digits does not make those measurements exact. Unit cancellation is a stronger first check than the appearance of a plausible decimal: mol times g/mol gives g, while dividing by the wrong conversion can leave incompatible dimensions.

## Electron occupancy as a model

An orbital is a quantum-state description, not a small planet-like trajectory. Each orbital accommodates at most two electrons with opposite spin within the usual independent-electron occupancy model. A shell of principal quantum number n has capacity 2n² when all its allowed orbitals are counted; n=2 therefore has capacity 8. This capacity does not mean that every atom fills shells in a simple sequence without subshell energy considerations.

For the familiar main-group configuration of a neutral Z=12 atom, the occupied sequence is 1s²2s²2p⁶3s². Removing two outer 3s electrons gives the ten-electron closed-shell ion. The lesson uses this simple case rather than proposing a universal transition-metal filling rule. Electron configuration helps interpret periodic structure, but it does not by itself supply every bonding property or a measured ionization energy.

## Photon energy and scale

A photon in vacuum has frequency ν=c/λ and energy E=hν=hc/λ. Use wavelength in metres with SI constants. For a synthetic wavelength of 500 nm, λ=5.00 × 10⁻⁷ m and E≈3.972892 × 10⁻¹⁹ J. Multiplying by N_A gives about 239.253 kJ per mole of photons. The [NIST reference](https://www.nist.gov/pml/special-publication-330/sp-330-section-2) gives exact defining values h=6.62607015 × 10⁻³⁴ J·s and c=299792458 m/s; the chosen wavelength still determines the precision of this example.

A shorter wavelength has higher energy. If the wavelength doubles while the same model applies, energy halves. This inverse relation concerns each photon, not the total energy of a beam, which also depends on photon count. Absorption can require matching allowed energy differences, and the simple energy calculation alone does not predict a complete spectrum of a multielectron molecule.

## Worked example

Take the synthetic 500 nm photon. Convert nanometres to metres before forming hc/λ, producing approximately 3.972892 × 10⁻¹⁹ J. Then multiply by the exact amount-count constant and convert J to kJ to obtain 239.253 kJ per mole of photons. Separately, a 0.025 mol entity sample has 1.50553519 × 10²² entities. These two conversions use the same amount-count relation but concern different specified objects. Neither number establishes an absorption probability, measured spectral line or actual sample composition.

## Common mistakes and checks

Do not use mass number as an exact isotope mass. Do not change proton count when merely forming an ion. Do not substitute 500 directly into a formula expecting metres. Keep photons per mole distinct from joules per photon. An exact conversion constant does not remove uncertainty in a wavelength or sample amount. For an isotope average, verify positive fractions summing to one and a result between the two stipulated masses.

## Limits of this lesson

Sample amounts, isotope distributions and wavelength examples are synthetic. Atomic occupancy is a limited introductory model, not a full quantum calculation or spectroscopy analysis. No measurement procedure or material recommendation is supplied. Original explanation has substantial AI assistance and uses link-only references without copied source text. The course remains partial, unreviewed and formative-only.
