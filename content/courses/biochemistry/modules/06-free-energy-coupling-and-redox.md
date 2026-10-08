# Free energy in the cell: actual ΔG, coupled reactions and redox potential

Metabolism runs on reactions that would not proceed alone, driven by others that release free energy. Two quantities are easy to confuse here: the standard free-energy change ΔG°′, a property of the reaction under defined standard conditions, and the actual ΔG, which depends on the concentrations in the cell and decides the direction of net flux. This lesson computes both, couples an unfavorable step to ATP hydrolysis, and converts redox potentials into free energy for the electron-transport chain.

## Learning objectives

By the end of this lesson, you should be able to:

1. Calculate the actual free-energy change of a reaction from its standard value and the concentrations of reactants and products.
2. Compute the standard free-energy change and equilibrium constant of a reaction coupled to ATP hydrolysis.
3. Convert a difference in reduction potential into a free-energy change and interpret where energy is released in electron transport.

## Standard and actual free energy

For a reaction A + B ⇌ C + D,

**ΔG = ΔG°′ + RT ln Q,** with Q = [C][D] / ([A][B]).

ΔG°′ refers to 1 M of each species (except water, and with pH 7 for the biochemical standard state). R = 8.314 J/(mol·K), and at 37 °C (310 K) RT = 2.577 kJ/mol. A reaction proceeds net forward when ΔG < 0, is at equilibrium when ΔG = 0, and ΔG°′ = −RT ln K′eq.

ΔG°′ says nothing by itself about whether a reaction runs in a cell. A reaction with a positive ΔG°′ runs forward when products are removed fast enough to keep Q small, and a reaction with a negative ΔG°′ stops when products accumulate.

## ATP hydrolysis in a cell

ATP + H₂O → ADP + Pᵢ has ΔG°′ ≈ -30.5 kJ/mol (the exact value depends on Mg²⁺ and ionic strength). **Synthetic cell concentrations:** ATP 3.0 mM, ADP 0.3 mM, Pᵢ 3.0 mM. Then Q = (3.0×10⁻⁴)(3.0×10⁻³) / (3.0×10⁻³) = 3.0×10⁻⁴, ln Q = -8.11, and

ΔG = -30.5 + 2.577 × (-8.11) = -51.4 kJ/mol.

Cells keep the ATP/ADP ratio far from equilibrium, which is why the energy available from each ATP in a cell is substantially larger in magnitude than the standard value. The ratio itself is an important readout of cellular energy status.

## Coupling

Phosphorylation of glucose by Pᵢ alone (glucose + Pᵢ → glucose-6-phosphate + H₂O) has ΔG°′ ≈ +13.8 kJ/mol; its equilibrium constant is exp(−13.8/2.577) = 4.73×10⁻³, so very little product would form. Hexokinase couples the phosphorylation to ATP hydrolysis through a shared mechanism (direct phosphoryl transfer), and the standard free-energy changes add:

ΔG°′(glucose + ATP → glucose-6-phosphate + ADP) = 13.8 + (-30.5) = -16.7 kJ/mol.

Coupling is a property of the enzyme mechanism, not of two reactions happening in the same cell. Free energies add only because the overall reaction is the sum of the two half-reactions.

## Redox reactions and the electron-transport chain

For electron transfer, ΔG°′ = −n F ΔE°′, where n is the number of electrons, F = 96.485 kJ/(V·mol) and ΔE°′ = E°′(acceptor) − E°′(donor). For electrons from NADH (E°′ ≈ −0.320 V) to oxygen (E°′ ≈ +0.815 V for ½O₂/H₂O), ΔE°′ = 1.135 V and

ΔG°′ = −2 × 96.485 × 1.135 = -219 kJ/mol.

The respiratory chain releases this energy in steps between carriers of increasing reduction potential, and three of those steps pump protons. The proton gradient, not the redox reaction directly, drives ATP synthase. The ratio of NAD⁺ to NADH in a compartment sets the actual potential of the couple in the same way Q sets the actual ΔG; NAD⁺ metabolism is studied in aging research, and this lesson's arithmetic is the background for reading that work, not an evaluation of it.

## Worked example

**Problem.** A synthetic isomerization A ⇌ B has ΔG°′ = +5 kJ/mol. In a cell, the next enzyme keeps [B]/[A] at 0.05. Does the step run forward, and at what ratio would it stop?

**Step 1: actual ΔG.** ΔG = 5 + 2.577 × ln(0.05) = 5 + 2.577 × (-3.00) = -2.72 kJ/mol. It is negative, so net flux is forward.

**Step 2: the stopping point.** Net flux stops when ΔG = 0, which is when [B]/[A] equals K′eq = exp(−5/2.577) = 0.144. If downstream consumption slowed and B accumulated past that ratio, the step would reverse.

**Step 3: interpret.** Steps with ΔG near zero are readily reversible and are set by mass action. Steps with large negative actual ΔG, such as those catalyzed by hexokinase or phosphofructokinase, are effectively one-way and are where pathways are usually regulated.

## Limits of this lesson

Concentrations are synthetic and treated as activities. Real cells compartmentalize metabolites, bind much of their ADP and Mg²⁺, and differ between tissues and states, so free-energy values for any specific cell require measured, compartment-specific concentrations.
