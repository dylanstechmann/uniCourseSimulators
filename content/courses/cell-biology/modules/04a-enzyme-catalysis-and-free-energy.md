# Enzyme catalysis, reaction mechanisms, and free energy

An enzyme assay reports a rate. The rate alone does not tell you whether a protein changed the reaction's equilibrium, which chemical step is faster, or whether an observed cellular phenotype is caused by catalytic chemistry. This lesson builds a chain from a reaction mechanism to a bounded interpretation of measurements.

## Learning objectives

By the end of this lesson, you should be able to:

1. Distinguish a change in reaction rate from a change in reaction free energy or equilibrium.
2. Explain how a plausible catalytic strategy changes the activation barrier without claiming that an enzyme supplies net energy.
3. Calculate a rate at half-saturation from active-enzyme concentration and a turnover number.
4. Evaluate whether measured activity reflects enzyme amount, active fraction, or activity per active site.

## Reaction coordinate: rates and equilibria answer different questions

For a reaction A ⇌ B, the free-energy difference between A and B determines the equilibrium ratio under specified conditions. The activation free energy, ΔG‡, describes the barrier separating a starting state from the transition state. A catalyst changes the pathway and lowers the barrier for reaching the transition state. It accelerates approach to equilibrium; it does not change the net ΔG between A and B or the equilibrium constant. A catalyst can accelerate the reverse reaction as well as the forward reaction.

The distinction matters in cells. If an isolated chemical step has an unfavorable ΔG under cellular conditions, simply adding an enzyme does not make that step favorable. Cells can couple reactions through a shared intermediate or another physically linked mechanism. If the coupled reaction has a net negative ΔG under the actual conditions, it can proceed forward. Merely writing two unrelated equations whose free energies sum to a negative number does not establish that one reaction drives the other.

**Worked coupling example.** Suppose a chemical transformation has ΔG = +12 kJ·mol⁻¹ and a one-to-one coupled hydrolysis has ΔG = −21 kJ·mol⁻¹ under the stated conditions. If a mechanism physically couples one event of each reaction, the combined net change is +12 − 21 = −9 kJ·mol⁻¹. This bookkeeping predicts the thermodynamic direction of the coupled process. It does not identify the enzyme mechanism, rate, or coupling efficiency, and the numerical ΔG values are condition-specific rather than universal constants.

## What an enzyme can change

An enzyme creates a chemical environment in which a particular transition state is more accessible. Several strategies can contribute to one reaction:

- **Acid–base catalysis:** a side chain or bound molecule donates or accepts a proton at a useful point in the reaction. Its protonation state depends on the local environment, so a pH profile can change as residues gain or lose protons.
- **Covalent catalysis:** an active-site nucleophile forms a temporary covalent intermediate. The enzyme must later break that bond and regenerate the catalyst.
- **Metal-ion catalysis:** a metal may orient substrate, stabilize charge, participate in redox chemistry, or alter a bound water's reactivity. The exact role depends on the metal and reaction.
- **Proximity, orientation, and preorganization:** the active site can position reacting groups, restrict unproductive motions, exclude or organize water, and stabilize charge distributions that develop in the transition state.

These descriptions are mechanistic hypotheses, not labels to infer from a rate curve. A residue substitution that lowers activity might alter folding, active-site occupancy, chemical catalysis, product release, or the active fraction of purified protein. Evidence should separate these possibilities. Compare soluble protein abundance, folding or stability, substrate binding where appropriate, and activity normalized to a measured amount of active enzyme. A single endpoint assay cannot localize the affected step.

Substrate recognition also does not mean that enzymes bind only one molecule or that every close-fitting substrate is converted efficiently. Binding, chemistry, conformational change, and product release can each contribute to specificity. “Induced fit” describes a possible coupled conformational response; it is not by itself a complete explanation of catalysis or proof that a particular transition state is stabilized.

## A minimal kinetic mechanism

For one substrate, the common starting model is:

`E + S ⇌ ES → E + P`

The enzyme–substrate complex forms and can dissociate; productive chemistry releases product and regenerates enzyme. In a steady-state treatment, the amount of ES is approximately stable during the initial-rate interval. With total active enzyme `Eₜ = [E] + [ES]`, the model gives:

`v₀ = Vmax[S] / (Km + [S])`

`Vmax = kcat Eₜ`

`Km = (k₋₁ + kcat) / k₁`

The equation uses the initial rate `v₀`, substrate concentration `[S]`, and the model parameters `Vmax` and `Km`. At `[S] = Km`, `v₀ = Vmax/2`; at substrate concentrations far below `Km`, rate is approximately proportional to `[S]`; at concentrations far above `Km`, rate approaches `Vmax`.

`Km` is a kinetic parameter, not generally a binding dissociation constant. It approaches the dissociation constant only under a rapid-equilibrium condition in which product-forming chemistry is slow relative to ES dissociation. `kcat` is the turnover number per active site at saturating substrate. `kcat/Km` describes catalytic efficiency in the low-substrate regime for the specified substrate and conditions. None of these values is universal across pH, temperature, cofactors, constructs, or assay formats.

The model is useful only when its assumptions are reasonably matched: a single-substrate mechanism of the represented form, stable enzyme over the measurement interval, initial velocities before substantial substrate depletion or product accumulation, substrate in excess of enzyme, and no unmodeled allostery, cooperativity, substrate inhibition, or coupled-substrate effects. The equation is a testable model, not a definition of every enzyme.

## Worked rate calculation and measurement boundary

An assay contains 50 nM measured active enzyme. Under a defined condition, `kcat = 6 s⁻¹`, so `Vmax = 6 s⁻¹ × 50 nM = 300 nM·s⁻¹`. If `[S] = Km`, the predicted initial rate is `150 nM·s⁻¹`. If `[S]` doubles while enzyme amount and conditions stay fixed, the rate increases but does not double in this saturating regime.

Now suppose a mutant sample gives half the observed total rate. That result does not by itself mean `kcat` was cut in half. The sample might contain half as much soluble enzyme, a smaller fraction might be active, the detector might respond differently, or a required cofactor could be limiting. Measure a time interval with a linear product signal, use a matched enzyme-free blank, calibrate the detector with known product, quantify soluble enzyme, and—when the claim requires it—estimate active-site concentration. State which quantity is normalized and which remains uncertain.

### Check your reasoning

If an enzyme lowers the activation barrier but neither reactant nor product is removed, what should change first: the speed of approach to equilibrium, the equilibrium ratio, or both? Then identify one coupled-reaction measurement that would be needed before claiming that a cell uses the coupling in vivo.

## Provenance

This is original explanatory text and original numerical examples under the course's CC BY 4.0 content license. MIT OpenCourseWare 5.07SC Biological Chemistry I is linked as a topic-scope comparator only. The cited historical papers are link-only research references; no text, figure, problem, or data was copied or adapted.
