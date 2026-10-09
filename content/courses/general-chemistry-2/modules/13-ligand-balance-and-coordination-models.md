# Ligand balance and coordination models

## Learning objectives

1. Distinguish free ligand concentration, analytical total and coordination number.
2. Solve a stipulated one-to-one complexation balance without assuming all ligand is free.
3. Compare limited octahedral electron-count and energy models without asserting an actual material property.

## Donor atoms are the coordination count

A metal's coordination number counts directly attached donor atoms, not necessarily separate ligand molecules. Three bidentate ligands can supply six donor atoms, while six monodentate ligands can do the same. Denticity describes how many donor atoms one ligand contributes in a specified binding mode. It is not the same as ionic charge, formal metal oxidation state or number of unpaired electrons.

For a constructed complex with metal M²⁺, two singly charged X⁻ ligands and two neutral L ligands, overall charge is zero. If every ligand is monodentate, the donor count is four. Four donor atoms alone do not uniquely establish tetrahedral versus square-planar geometry. Electron configuration, ligand behavior and structural evidence matter beyond counting.

An oxidation-state assignment is electron bookkeeping under a convention, not a direct map of actual electron density. Likewise, a coordination diagram does not by itself establish exchange kinetics or binding affinity. Keep the structural, electronic, equilibrium and kinetic questions separate, even when one notation is used to describe the same complex.

## Free ligand versus total ligand

In a stipulated one-to-one equilibrium M+L⇌ML, let the conditional concentration-form constant be K_f=[ML]/([M][L]). With M_T=[M]+[ML] and L_T=[L]+[ML], set x=[ML]. Then x=K_f(M_T−x)(L_T−x). A positive root must obey 0≤x≤min(M_T,L_T). The algebraic second root of the resulting quadratic generally violates those amount bounds.

Use synthetic K_f=10⁴ L/mol, M_T=0.0010 mol/L and L_T=0.0015 mol/L. Solving gives x≈8.64110 × 10⁻⁴ mol/L. Free metal is approximately 1.35890 × 10⁻⁴ mol/L and free ligand 6.35890 × 10⁻⁴ mol/L. The bound fraction of total metal is about 0.864110. Inserting the analytical L_T directly into a free-ligand binding formula would overstate the ligand available after binding.

When free ligand l is independently held fixed, the same simple binding model gives fraction bound K_fl/(1+K_fl). At l=0.0001 mol/L and K_f=10⁴ L/mol, that fraction is 0.5. This is a different boundary condition from the closed analytical-total example. A large ligand excess can justify approximating free ligand by total, but the depletion should be checked rather than assumed.

## Conditional constants and missing species

A conditional constant can incorporate a declared pH, ligand protonation fraction or other fixed convention. It is not automatically transferable to different pH or additional competing ions. If the unprotonated binding form has fraction α_L, a simple stipulated conditional relation can be K'_f=α_LK_f when the remaining assumptions apply. An actual coupled solution needs proton and ligand balances as well as metal balance.

Several complexes, hydrolysis, precipitation or multiple ligand protonation states can invalidate the one-complex equation. A real chelator may also form species with different stoichiometry. The positive quadratic root is an exact solution of this selected ideal model, not evidence that a real sample contains only M, L and ML. Disagreement would motivate broader speciation rather than arbitrary changes to a single constant.

## A limited octahedral model

In the elementary octahedral crystal-field picture, three lower d orbitals lie at −0.4Δ_o and two upper d orbitals at +0.6Δ_o relative to the barycenter. The [OpenStax coordination-property section](https://openstax.org/books/chemistry-2e/pages/19-3-spectroscopic-and-magnetic-properties-of-coordination-compounds) is a link-only reference for splitting and spin distinctions. Our energy parameters are synthetic, and no measured complex is assigned a splitting from these calculations.

For d⁶, a high-spin occupation has four lower electrons and two upper electrons, producing crystal-field energy −0.4Δ_o and four unpaired electrons. A low-spin occupation has six lower electrons, producing −2.4Δ_o and zero unpaired electrons. Electron counts sum to six in both, but pairing differs. Coordination number six alone does not tell us which electronic state applies.

Count one electron pair in the high-spin occupation and three in the low-spin occupation within this simple model. With stipulated Δ_o=200 kJ/mol and pairing cost P=150 kJ/mol per pair, low-minus-high energy is −2Δ_o+2P=−100 kJ/mol. The model favors low spin. These energies omit bonding, covalency, entropy and other effects; the result is a limited bookkeeping comparison rather than a universal spin-transition prediction.

## Evidence and interpretation

Magnetic or spectroscopic observations can constrain electronic models, but one signal does not automatically reveal every ligand, geometry and oxidation state. Geometry can also change with ligand exchange or environment. A formation constant measures an equilibrium relationship rather than the speed at which the complex rearranges. Strong binding and slow exchange are distinct properties.

The combination of balances and model labels helps avoid overinterpretation. A donor count can delimit candidate structures; amount conservation can reject impossible complex concentrations; the simple energy calculation can compare two stipulated occupations. Each conclusion has its own assumptions and would need different evidence before being applied to an actual material.

## Worked example

Set complex concentration x and subtract it from both analytical totals. Solve x=10⁴(0.0010−x)(0.0015−x), retain the bounded root and reconstruct both free species. Check K_f and both totals. Separately count six donors from three bidentate ligands. For the distinct d⁶ model, compare lower/upper occupations and add the pairing-cost difference to obtain −100 kJ/mol. These examples do not identify one real complex.

## Common mistakes

Do not substitute total ligand for free ligand without checking depletion. Do not confuse denticity, charge, oxidation state and spin. Reject inadmissible roots and unsupported geometric assignments.

## Limits of this lesson

All constants and energy parameters are synthetic; no chelation treatment, material recommendation or handling procedure is supplied. Original instruction has substantial AI assistance. The course remains partial, unreviewed and formative-only.
