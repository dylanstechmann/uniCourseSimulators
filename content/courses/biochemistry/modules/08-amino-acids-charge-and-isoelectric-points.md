# Amino acids, charge and pH: titration, isoelectric points and the charge of a protein

A protein's behavior in solution depends strongly on its electric charge, and that charge comes almost entirely from a few kinds of side chains and the two ends of the chain, each of which gains or loses a proton depending on the pH. Charge decides whether a protein dissolves or precipitates, which way it moves in an electric field, whether it binds to a charged surface or to another protein, and how it buffers a solution. This lesson turns the acid–base chemistry of the general chemistry and organic chemistry courses into the bookkeeping biochemists use: fractional protonation, the isoelectric point and the net charge of an amino acid or a protein at a given pH. All pKa values and the protein composition are synthetic and typical.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute the protonation state and the net charge of an amino acid or a short chain at a given pH from its pKa values.
2. Calculate the isoelectric point of amino acids with and without an ionizable side chain.
3. Predict how a protein's net charge changes with pH and what that implies for solubility, migration and binding to an ion-exchange resin.

## Ionizable groups

An amino acid has an α-carboxyl group (pKa about 2.3) and an α-amino group (pKa about 9.7) that are both free in the isolated amino acid. In a chain these become the C-terminus and N-terminus (pKa about 3.5 and 8.0, shifted because of the neighboring peptide bond), and the backbone itself is neutral across the physiological pH range. The side chains that ionize are aspartate and glutamate (pKa about 4), histidine (about 6), cysteine (about 8.3), tyrosine (about 10), lysine (about 10.5) and arginine (about 12.5). Values in a folded protein can differ by several units because burial and neighboring charges change the local environment.

For an acid HA ⇌ H⁺ + A⁻, the fraction deprotonated (charged, −1) at a given pH is

**f(A⁻) = 1 / (1 + 10^(pKa − pH)),**

and for a base BH⁺ ⇌ H⁺ + B, the fraction protonated (charged, +1) is

**f(BH⁺) = 1 / (1 + 10^(pH − pKa)).**

At pH = pKa the fraction is one half. Thirty-fold or more from the pKa, the group is essentially fully in one form.

**Synthetic values at pH 7.4:** a lysine side chain (pKa 10.5) is 99.92% protonated, so it carries essentially +1. A histidine side chain (pKa 6.0) is 3.8% protonated, so only about one histidine in 26 carries a charge at this pH; the ratio of unprotonated to protonated forms is 10^(7.4 − 6.0) = 25. An aspartate or glutamate side chain (pKa about 4.1) is 99.95% deprotonated and carries −1.

## Net charge and the isoelectric point

The net charge of a molecule is the sum of the fractional charges of its groups. For alanine, which has only the two backbone groups (pKa 2.34 and 9.69), the net charge at pH 7.4 is 0.9949 − 1.0000 = -0.0051, essentially neutral as a zwitterion (−COO⁻ and −NH₃⁺).

The **isoelectric point (pI)** is the pH at which the net charge is zero. For an amino acid whose charge changes between +1, 0 and −1, the pI is the average of the two pKa values that bracket the neutral form. For alanine, pI = (2.34 + 9.69)/2 = 6.015. With an acidic side chain, the bracketing pKa values are the α-carboxyl and the side chain: glutamate (pKa 2.2, 4.25, 9.67) has pI = (2.2 + 4.25)/2 = 3.225. With a basic side chain they are the α-amino and the side chain: lysine (pKa 2.18, 8.95, 10.53) has pI = (8.95 + 10.53)/2 = 9.74, and histidine (1.82, 6.0, 9.17) has pI = (6.0 + 9.17)/2 = 7.585. At pH 7.4, lysine carries a net charge of 0.973 + 0.999 − 1.000 = +0.97.

## The charge of a protein

A protein's net charge is the same sum over all its ionizable groups. **Synthetic protein:** 12 lysine or arginine residues (counted at pKa 10.5), 10 aspartate or glutamate residues (pKa 4.1), 4 histidines (pKa 6.0), and the two termini (pKa 8.0 and 3.5). At pH 7.4 the net charge is +1.9: the basic residues contribute about +12, the acidic ones −10, the histidines +0.15, and the termini nearly cancel. Lowering the pH to 6.0 makes the histidines half protonated and raises the net charge to +4.1. Because net charge falls as the pH rises, this basic protein reaches zero charge near pH 9.5, which is its pI.

Three consequences follow.

- **Solubility** is usually lowest near the pI, because molecules with no net charge repel each other least and aggregate or precipitate more readily.
- **Migration:** a protein with a net positive charge moves toward the negative electrode in an electric field, and a negatively charged protein toward the positive one. Isoelectric focusing exploits this by letting proteins migrate in a pH gradient until each reaches the pH equal to its pI.
- **Ion exchange:** at a pH above its pI a protein is net negative and binds an anion-exchange resin; below its pI it is net positive and binds a cation-exchange resin. Raising the salt concentration releases it.

## Buffering

A group resists pH changes most effectively within about one pH unit of its pKa, where both forms are present in comparable amounts. Histidine side chains, with a pKa near neutral pH, are the main buffering groups of proteins at physiological pH, which is one reason hemoglobin, rich in histidine, is an important buffer of blood.

## Common mistakes

- Using the pKa of the wrong group, or averaging the wrong two pKa values, for the pI of an amino acid with an ionizable side chain.
- Mixing the two fraction formulas, so that an acid's charged fraction is computed with the base formula.
- Treating a pKa from a table as fixed inside a folded protein.
- Assuming that a protein with zero net charge has no charged groups.
- Expecting maximum solubility at the pI.
- Expecting a protein to bind a cation-exchange resin above its pI.

## Worked example

**Problem.** A synthetic protein has pI 5.0. At pH 8.0, what is the sign of its net charge, in which direction does it move in an electric field, and which type of ion-exchange resin binds it at that pH?

**Step 1: sign.** pH 8.0 is above the pI, so groups are on average more deprotonated than at the pI: the net charge is negative.

**Step 2: migration.** A negatively charged protein moves toward the positive electrode.

**Step 3: resin.** A net negative protein binds an anion-exchange resin, which carries positive groups. At pH 3.0 (below the pI) the same protein would be net positive and would bind a cation-exchange resin instead.

**Step 4: caution.** Only the net charge is known. Local patches of the opposite charge can still mediate binding, so the prediction is a first guide that experiments confirm.

## Limits of this lesson

All pKa values are typical textbook-level values and the protein composition is synthetic. Interactions between nearby groups, ionic strength, temperature and burial shift real pKa values, and a simple sum of independent groups cannot capture them. The lesson gives no laboratory protocol.
