# Substitution mechanisms and stereochemistry: predicting SN1 versus SN2 and tracking what happens at a stereocenter

Many reactions in synthesis and in metabolism replace one group on a carbon with another. Two limiting mechanisms, SN2 and SN1, make different predictions about rate, about which substrates react, and about what happens to the three-dimensional arrangement at that carbon. Because biological molecules are chiral, and their mirror images can behave differently, those stereochemical predictions matter. This lesson uses substrate, nucleophile, solvent and leaving group to choose a mechanism, writes the rate law each implies, and quantifies stereochemical outcomes with stereoisomer counts and enantiomeric excess.

## Learning objectives

By the end of this lesson, you should be able to:

1. Use substrate structure, nucleophile strength, solvent and leaving group to predict whether substitution follows SN1 or SN2, and write each rate law.
2. Predict the stereochemical outcome at a stereocenter (inversion or racemization) and count possible stereoisomers.
3. Calculate enantiomeric excess and composition from optical rotation, and explain why stereochemistry matters for biological activity.

## Two mechanisms

**SN2** (substitution, nucleophilic, bimolecular) happens in one step: the nucleophile attacks the carbon from the side opposite the leaving group as the leaving group departs. Rate = k[substrate][nucleophile]. Because the nucleophile must reach the back of the carbon, crowding matters: methyl > primary > secondary, and tertiary carbons essentially do not react this way. Strong nucleophiles and polar aprotic solvents (which do not cage the nucleophile with hydrogen bonds) favor SN2.

**SN1** (unimolecular) happens in two steps: the leaving group departs first to form a carbocation, which the nucleophile then captures. Rate = k[substrate], independent of the nucleophile. Carbocation stability controls it: tertiary > secondary ≫ primary, and resonance (allylic, benzylic) helps. Polar protic solvents, which stabilize the ions, and weak nucleophiles favor SN1.

Both need a good **leaving group**: a weak base that can carry away the electrons, such as iodide, bromide or a sulfonate. Hydroxide is a poor leaving group, which is why biology converts alcohols into phosphates or diphosphates before substitution.

**Synthetic rate data:** an SN2 reaction with k = 2×10⁻³ L mol⁻¹ s⁻¹ at [substrate] = 0.1 M and [Nu] = 0.2 M has rate 4.0×10⁻⁵ mol L⁻¹ s⁻¹. Doubling the nucleophile doubles the rate to 8.0×10⁻⁵. For an SN1 reaction, doubling the nucleophile would leave the rate unchanged; this is a direct experimental test of mechanism.

## Stereochemistry at the reacting carbon

A carbon bearing four different groups is a **stereocenter**; the molecule and its mirror image are non-superimposable **enantiomers**, labeled R and S by the Cahn–Ingold–Prelog priority rules.

- **SN2 inverts configuration**: the back-side attack flips the other three groups like an umbrella in the wind. An R substrate gives the product with inverted geometry (often, but not always, labeled S; the label depends on priorities, the geometry does not).
- **SN1 tends to racemize**: the planar carbocation can be attacked from either face, giving both enantiomers, often with a slight excess of inversion because the departing group briefly shields one face.

A molecule with n stereocenters can have up to 2ⁿ stereoisomers. With 3 stereocenters, up to 8. (Internal symmetry can reduce the count, giving meso forms.)

**Regiochemistry** asks where on a molecule a reaction occurs. In substitutions the leaving group usually fixes the site; in related eliminations and additions, more substituted alkenes (Zaitsev) or anti-Markovnikov products can dominate depending on mechanism, so the same mechanistic reasoning predicts site as well as stereochemistry.

## Measuring stereochemical purity

Enantiomers rotate plane-polarized light by equal and opposite amounts. If a pure enantiomer has specific rotation [α] = -11.5° and a sample shows -9.2°, the **enantiomeric excess** is ee = |-9.2/-11.5| × 100 = 80%. The composition is (100 + ee)/2 = 90% of the major enantiomer and 10% of the minor. A racemic mixture (50:50) has ee = 0 and no net rotation. Chiral chromatography gives the same information more reliably.

## Why it matters biologically

Enzymes and receptors are chiral, so they often bind one enantiomer much better than the other. Nearly all amino acids in proteins are the L form, and sugars in nucleic acids are D. Enantiomers of a drug can differ in potency, metabolism and side effects, which is why stereochemical purity is reported and controlled.

## Common mistakes

- Expecting SN2 at a tertiary carbon, or SN1 at a primary carbon without resonance stabilization.
- Assuming inversion of geometry always changes the R/S label; the label follows priorities.
- Using 2ⁿ without checking for meso compounds.
- Confusing ee with the fraction of the major enantiomer.

## Worked example

**Problem.** (R)-2-bromobutane, a secondary bromide, reacts with a high concentration of iodide in acetone. Predict mechanism, rate law and stereochemistry.

**Step 1.** Secondary substrate, strong nucleophile, polar aprotic solvent: SN2 is favored.

**Step 2.** Rate = k[2-bromobutane][I⁻]; doubling iodide doubles the rate.

**Step 3.** Back-side attack inverts the stereocenter. Iodine and bromine both have the highest priority in their compounds, so the product is (S)-2-iodobutane. The same substrate in water without a strong nucleophile would lean toward SN1 and give a largely racemic alcohol.

## Limits of this lesson

Rate constants and rotations are synthetic. Real substitutions can show mixed mechanisms, and elimination often competes, especially at higher temperature and with strong bases.
