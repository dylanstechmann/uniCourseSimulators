# Water, pH, and noncovalent interactions

## The solvent is part of the system

Cells are aqueous mixtures, not collections of dry molecules. Water is polar: its oxygen atom carries partial negative character and its hydrogens partial positive character. Water molecules form a rapidly rearranging hydrogen-bond network. A molecular group that can donate or accept hydrogen bonds often interacts favorably with water; a nonpolar surface cannot make those same interactions. Solute behavior reflects both solute-solute and solute-water interactions.

Several interactions stabilize biological assemblies. Hydrogen bonds are directional attractions involving a donor and acceptor. Electrostatic interactions depend on charge, separation, and the surrounding dielectric environment. Van der Waals interactions are individually weak but can sum across tightly packed surfaces. The hydrophobic effect is not a new covalent bond or a simple attraction between nonpolar groups: burying nonpolar surface can release water molecules whose orientations were constrained around that surface. The size of the contribution depends on geometry, temperature, and the rest of the system.

Electrostatic interactions are screened in water and become shorter-ranged as ionic strength increases. In a dilute solution, two oppositely charged side chains may contribute a favorable interaction; added salt can weaken the contribution of that pair. The same salt can also affect protein solubility, conformation, or other interactions, so an observed response to salt is not automatically proof of a single “salt bridge.” A perturbation and readout should isolate the mechanism as far as practical.

## Protonation links pH to charge

Many functional groups can gain or lose a proton. For the pair HA ⇌ H⁺ + A⁻, the Henderson–Hasselbalch relation is:

`pH = pKa + log10([A⁻]/[HA])`

When pH equals pKa, the two forms are present in equal amounts in the model. One pH unit above pKa gives a tenfold excess of deprotonated form; one unit below gives a tenfold excess of protonated form. This is an equilibrium relationship, not a claim that every molecule has a fixed half-charge or that pKa never changes with environment.

### Worked calculation: a histidine-like group

Assume an ionizable group has solution pKa 6.0 and is in a well-mixed buffer at pH 7.4. Then `[A⁻]/[HA] = 10^(7.4 − 6.0) ≈ 25`. Under this two-state model, the protonated fraction is `1/(1 + 25) ≈ 0.038`, or about 4%. At pH 6.0 the model predicts 50% in each state. The calculation predicts the relative population for the stated pKa and solution conditions. A protein interior, nearby charges, hydrogen bonds, or ligand binding can shift an amino-acid side chain's pKa, so a measured protein environment may differ from this simple solution example.

## From interactions to a protein prediction

Imagine that a histidine on a protein surface is near a negatively charged partner. Lowering buffer pH toward the side-chain pKa increases the protonated, positively charged population in the simple model and could strengthen electrostatic attraction. If the group becomes buried, its pKa may shift; if the protein changes conformation, the partner's position may also change. Therefore “lower pH strengthens binding” is a testable hypothesis, not a guaranteed result.

A useful experiment compares a pH series at constant salt and protein concentration, checks that the protein remains folded and soluble, and includes a no-protein or reference condition for instrument drift. A separate salt series can probe sensitivity to electrostatic screening. Replicates estimate variability; a mutation that removes the candidate ionizable group can test mechanism, but may itself change folding. A plot should show the measured response, units, replicate values, and uncertainty. Do not infer direct contact from a pH-dependent curve alone.

## Distinguish cause, measurement, and interpretation

For any molecular-interaction claim, state which variable is changed, which signal is measured, and which alternatives remain. A pH titration can change many groups at once. A salt titration can alter both screening and protein solubility. A fluorescence signal may depend on concentration as well as conformation. Use matched buffer composition where possible, verify protein integrity, and avoid claiming that a model parameter is a molecular constant when the model assumptions are unmet.

## Check your understanding

1. For a group with pKa 5.0, is its protonated form more or less abundant at pH 4 than at pH 6? Explain with the ratio, not a memorized label.
2. If a protein's apparent pH response shifts after a nearby charge is mutated, what additional control would help separate a pKa shift from protein destabilization?
3. Predict one way added salt could alter a charge-mediated interaction and one alternative explanation for a measured change in soluble protein concentration.

## Provenance

Original instructional text, released under CC BY 4.0. MIT OpenCourseWare 7.01SC and 7.28x are topic-level, link-only curriculum comparators; no course text, figure, question, or exam was copied or adapted. See the package [source map](../source-map.json) and the repository [source registry](../../../sources/registry.json).
