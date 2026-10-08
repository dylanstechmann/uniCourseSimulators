# Protein folding and stability: two-state thermodynamics, denaturant m-values and marginal stability

A protein is useful only in its folded form, and the folded form is held together by a free-energy margin that is surprisingly small: a few tens of kilojoules per mole, about the energy of a handful of hydrogen bonds, separates the functional structure from the unfolded chain. That small margin explains why single mutations can disable a protein, why cells invest heavily in chaperones and degradation machinery, and why the proteostasis theme of the geroscience course matters. This lesson develops the thermodynamics of a two-state protein, shows how a chemical denaturant is used to measure stability, and quantifies what a destabilizing mutation does. All stabilities are synthetic and round.

## Learning objectives

By the end of this lesson, you should be able to:

1. Convert between the free energy of unfolding, the equilibrium constant and the fraction of protein that is folded for a two-state protein.
2. Use the linear dependence of unfolding free energy on denaturant concentration to find a stability in water and a denaturation midpoint.
3. Evaluate how a mutation, temperature or aggregation changes stability, and explain why marginal stability matters for proteostasis.

## A two-state model

In the simplest description, a protein exists as folded (native, N) or unfolded (U) with no populated intermediates: N ⇌ U. The equilibrium constant and the free energy of unfolding are

**K_u = [U]/[N],** **ΔG_unfold = −RT ln K_u,**

so a stable protein has a positive ΔG_unfold (and a small K_u). At 25 °C, RT = 2.479 kJ/mol. The fraction of protein in the folded state is f_N = 1/(1 + K_u). A ΔG_unfold of 10 kJ/mol gives K_u = e^(−10/2.479) = 0.0177 and f_N = 0.983: about 1.7% of the molecules are unfolded at any moment. A ΔG_unfold of 25 kJ/mol gives K_u = 4.2×10⁻⁵ and essentially all molecules folded, but the unfolded molecules never vanish: they are the ones that can aggregate or be degraded.

Typical globular proteins have ΔG_unfold of a few tens of kJ/mol, small compared with the sum of the favorable and unfavorable contributions that produce it. This is called **marginal stability**.

## Measuring stability with a denaturant

Urea and guanidinium chloride unfold proteins in a concentration-dependent way. Over the transition region, the unfolding free energy falls approximately linearly with denaturant concentration [D]:

**ΔG_unfold([D]) = ΔG_H₂O − m [D],**

where ΔG_H₂O is the stability extrapolated to zero denaturant and the **m-value** is the slope, which tends to increase with the amount of surface exposed on unfolding. The **midpoint** is the concentration at which half the protein is unfolded, where ΔG_unfold = 0, so C_m = ΔG_H₂O/m.

**Synthetic protein:** ΔG_H₂O = 25 kJ/mol and m = 10 kJ/mol per M. Then C_m = 25/10 = 2.5 M. At 2.0 M, ΔG_unfold = 25 − 10 × 2.0 = 5.0 kJ/mol, K_u = 0.133 and f_N = 0.883. At 3.0 M, ΔG_unfold = -5.0 kJ/mol, K_u = 7.52 and f_N = 0.117. The folded fraction falls from nearly 1 to nearly 0 over about a 1.5 M range, a sharp transition because a given change in [D] shifts the exponent in K_u by m/RT = 4.0 per M.

The two-state model is an assumption. A protein with a populated intermediate does not give a single, symmetric transition, and different probes (fluorescence, circular dichroism) then report different midpoints. Agreement among probes supports the two-state model.

## What a mutation does

A single amino-acid change shifts the unfolding free energy by ΔΔG. A destabilizing mutation with ΔΔG = −8 kJ/mol lowers ΔG_unfold from 25 to 17 kJ/mol and multiplies K_u by e^(8/2.479) = 25.2: the unfolded population rises about 25-fold, from 4.2×10⁻⁵ to 1.1×10⁻³. Yet the protein is still 99.90% folded. That contrast matters: small equilibrium populations can change by orders of magnitude, so a mutation can leave a protein looking fine in a test tube while greatly raising the supply of unfolded molecules that a cell has to handle, and the effect is larger if the protein started with a lower margin.

## Temperature, aggregation and the cell

- **Temperature.** Heating increases the unfolded population and eventually unfolds the protein at a melting temperature T_m. A protein with lower stability has a lower T_m.
- **Aggregation.** Unfolded or partly unfolded molecules expose hydrophobic surfaces and can form aggregates. This makes the unfolded population dangerous even when it is small.
- **The cell.** Chaperones help folding and refolding, and proteins that cannot fold are tagged for degradation. A larger load of unfolded protein, from mutation, stress or a declining quality-control system, can overwhelm these systems. The geroscience lesson on proteostasis describes the quality-control systems and the evidence about their decline with age.

## Common mistakes

- Mixing up the sign: ΔG_unfold is positive for a stable protein, ΔG_fold is negative.
- Using RT at 37 °C (2.579 kJ/mol) for an in-vitro experiment at 25 °C.
- Reading the denaturant midpoint as the stability in water; the stability is ΔG_H₂O = m × C_m.
- Assuming that an equally stable protein has an equal midpoint, when the m-value differs between proteins.
- Treating a 99.9% folded protein as unaffected by a mutation that raises its unfolded fraction 25-fold.
- Applying the two-state formulas to a protein with a stable intermediate.

## Worked example

**Problem.** A second synthetic protein has ΔG_H₂O = 18 kJ/mol and m = 12 kJ/mol per M. Find its midpoint, and the fraction unfolded at 1.0 M denaturant.

**Step 1: midpoint.** C_m = 18/12 = 1.5 M.

**Step 2: stability at 1.0 M.** ΔG_unfold = 18 − 12 × 1.0 = 6 kJ/mol.

**Step 3: populations.** K_u = e^(−6/2.479) = 0.089, so f_N = 0.918 and the unfolded fraction is 0.082.

**Step 4: comparison.** At the same 1.0 M the first protein (ΔG = 15 kJ/mol) is 0.0023 unfolded, so the second protein, with the lower stability in water, shows far more unfolding at the same concentration.

## Limits of this lesson

All stabilities and m-values are synthetic. The linear extrapolation can fail far from the transition region, real unfolding often has intermediates, and in a cell chaperones, crowding and binding partners change the stability. The lesson gives no laboratory protocol.
