# Molecular shape, polarity and where a molecule goes: solubility, partitioning and the energy of dissolving

Whether a molecule dissolves in water, sticks in a lipid membrane, or heats or cools a solution as it dissolves follows from its bonds and shape. Bond polarity and molecular geometry decide whether a molecule has a net dipole; intermolecular forces decide what it mixes with; an equilibrium constant summarizes how it distributes between water and an oily phase; and energy conservation measures the heat of dissolving. This lesson connects those ideas with synthetic numbers.

## Learning objectives

By the end of this lesson, you should be able to:

1. Predict whether a molecule is polar from bond polarity and geometry and relate polarity and hydrogen bonding to solubility.
2. Use a partition coefficient (an equilibrium constant) to compute how a solute distributes between octanol and water.
3. Apply energy conservation in a simple calorimeter to obtain an enthalpy of solution, and predict how temperature shifts the dissolution equilibrium.

## Polarity from bonds and shape

A bond between atoms of different electronegativity is polar. Whether the molecule has a net dipole depends on geometry, because bond dipoles add as vectors. Carbon dioxide has two polar C=O bonds, but it is linear, so the dipoles cancel and the molecule is nonpolar. Water has two polar O–H bonds in a bent shape (about 104.5°), so the dipoles add and water is strongly polar. VSEPR theory predicts these shapes from the number of electron domains around the central atom: two bonding domains and two lone pairs on oxygen give a bent molecule.

Polar molecules, and especially those that can donate or accept hydrogen bonds (O–H, N–H groups and lone pairs on O or N), dissolve well in water. Molecules dominated by C–H bonds are nonpolar and mix with oils and the interior of lipid membranes. "Like dissolves like" is a summary of the free-energy balance between breaking and making intermolecular interactions.

## Partitioning: an equilibrium between two phases

When a solute is shaken with water and octanol (a standard model of a lipid-like phase) and allowed to settle, its concentrations reach a fixed ratio:

**K_ow = [solute]_octanol / [solute]_water,** often reported as log P = log₁₀ K_ow.

For a synthetic solute with K_ow = 100 (log P = 2), equal volumes of the two phases leave a fraction 1/(1 + K) = 0.0099 in the water. With unequal volumes, the amount (not the concentration) matters: in 100 mL water and 10 mL octanol the water fraction is V_w/(V_w + K V_o) = 100/(100 + 100 × 10) = 0.0909. Log P is used to anticipate whether a molecule can cross membranes passively, whether it will be lost into plastics or lipids in a culture, and how it will behave in extraction steps.

## Energy of dissolving: calorimetry

In a coffee-cup calorimeter (an insulated cup at constant pressure), heat that leaves or enters the solution comes from the dissolution itself. Energy conservation gives **q_solution = m c ΔT**, and the reaction's heat is q_rxn = −q_solution.

**Synthetic run:** 5.35 g of ammonium chloride (M = 53.49 g/mol, so 0.1000 mol) dissolves in 100 g water. The temperature falls by 3.30 °C. With c ≈ 4.18 J/(g·°C) and the total mass 105.35 g, q_solution = 105.35 × 4.18 × (-3.3) = -1453 J. The dissolution absorbed 1453 J, so ΔH_soln = +1453 J / 0.1000 mol = +14.5 kJ/mol: endothermic. Cold packs use this effect.

## Temperature and the dissolution equilibrium

For an endothermic process, Le Chatelier's principle (and, quantitatively, the van 't Hoff equation) says raising the temperature shifts the equilibrium toward products: solubility increases with temperature. For exothermic dissolutions, solubility falls with temperature. Gases dissolving in water are usually exothermic, which is why warm medium holds less oxygen than cold medium.

## Common mistakes

- Concluding a molecule is polar because it has polar bonds, without checking symmetry.
- Using the mass of water alone instead of the total solution mass in the calorimetry (a small error here, larger for concentrated solutions).
- Getting the sign wrong: a temperature drop means the dissolution absorbed heat (positive ΔH).
- Treating log P as a percent or confusing concentration ratios with amount fractions when volumes differ.

## Worked example

**Problem.** A culture medium contains a synthetic compound with log P = 3. If a 10 mL plastic-and-lipid phase in contact with 100 mL of medium behaved like octanol, what fraction of the compound would remain in the medium?

**Step 1.** K = 10³ = 1000.

**Step 2.** Fraction in medium = 100/(100 + 1000 × 10) = 0.0099, about 1%.

**Step 3.** The model is crude, but the arithmetic warns that strongly lipophilic compounds can be depleted from medium by small lipid-rich or plastic volumes, so measured, not nominal, concentrations should be reported.

## Limits of this lesson

All values are synthetic. Octanol is only a model of membranes; ionizable molecules partition depending on pH (see the buffers lesson), and calorimetry here ignores heat lost to the cup.
