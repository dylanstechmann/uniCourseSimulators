# Separating substrate stiffness from ligand density: factorial design, interaction effects and traction forces

A widely reproduced observation is that many cell types spread more, build stronger adhesions and change their gene expression on stiffer substrates. But in many materials, making a gel stiffer also changes how much adhesive ligand is presented, how porous the gel is and how tightly the ligand is tethered. An experiment that varies stiffness without controlling those can attribute to stiffness an effect that belongs to ligand density. This lesson designs an experiment that separates the two, analyzes a synthetic factorial result including the interaction, and estimates the forces cells exert.

## Learning objectives

By the end of this lesson, you should be able to:

1. Design a factorial experiment that varies stiffness and ligand density independently, with the measurements needed to confirm each factor.
2. Calculate main effects and an interaction effect from a 2×2 factorial and interpret them.
3. Convert a surface ligand density into molecules per area and spacing, and estimate total traction force from traction stress and adhesion area.

## Why stiffness and ligand are confounded

In polyacrylamide gels, stiffness is tuned by crosslinker and monomer concentration, and ligands are coupled afterward. Changing the network can change how many coupling sites are available and how much protein ends up on the surface. In other systems, ligands bound loosely to a soft surface can be pulled off by cells, so the cell "feels" a different effective tether. If stiff gels also carry more ligand, a correlation between stiffness and spreading tells us nothing about which caused it. Mechanotransduction pathways (integrin clustering, focal-adhesion growth, actomyosin tension, and downstream transcriptional regulators that shuttle to the nucleus on stiff matrices) respond to both.

## A factorial design

Vary the two factors independently in all combinations: soft and stiff gels, each at low and high ligand density. Each condition is made and measured independently, with replicates from separate gel batches. Two confirmations are part of the design, not extras:

- **Measure stiffness** of each gel batch (for example by indentation), not just the nominal recipe.
- **Measure surface ligand** on each gel (for example by fluorescent labeling of the ligand with a standard curve), and adjust coupling so that the "low" and "high" levels match across stiffness.

## Analyzing a 2×2 result

**Synthetic mean spread area (μm²):**

| | low ligand | high ligand |
|---|---|---|
| soft | 900 | 1300 |
| stiff | 1400 | 2600 |

- **Main effect of stiffness** (average of stiff minus soft across ligand levels): ((1400 + 2600) − (900 + 1300)) / 2 = 900 μm².
- **Main effect of ligand**: ((1300 + 2600) − (900 + 1400)) / 2 = 800 μm².
- **Interaction**: half the difference between the ligand effect on stiff gels (2600 − 1400 = 1200) and on soft gels (1300 − 900 = 400): (1200 − 400) / 2 = 400 μm².

A nonzero interaction means the effect of one factor depends on the level of the other: here, extra ligand helps much more on stiff gels. That pattern is consistent with a requirement for both adhesion sites and resistance to pull before adhesions mature, but these are synthetic numbers, and an interaction in data is a statement about the measurement, not proof of a mechanism. With replicate-level data, the effects come with standard errors and are usually tested with a two-way analysis of variance.

## Ligand density in physical terms

Surface densities are often reported per area in moles. A synthetic coupling of 10⁻¹² mol/cm² equals 10⁻¹² × 6.022×10²³ / 10⁸ = 6022 molecules per μm² (1 cm² = 10⁸ μm²). If evenly spread on a square lattice, the spacing is 1/√(density) = 13 nm. Integrin-based adhesion is sensitive to ligand spacing on the scale of tens of nanometers, so spacing can matter more than total amount, and clustered and evenly spread presentations of the same average density can behave differently.

## Traction forces

Cells pull on their substrate. Traction force microscopy tracks beads embedded in a gel of known stiffness and calculates the traction stress field. A total force is the integral of traction stress over area. With a synthetic average traction of 300 Pa over 1000 μm² of adhesive area: F = 300 N/m² × 1000 × 10⁻¹² m² = 300 nN. The calculation depends on knowing the gel's modulus, which is another reason to measure it.

## Common mistakes

- Comparing gels of different stiffness without measuring ligand on each.
- Treating wells from one gel as independent replicates.
- Reporting only main effects when the interaction is large, which hides that the stiffness effect depends on ligand level.
- Calling the nominal recipe modulus the measured modulus.

## Worked example

**Problem.** A study reports that cells spread 1,500 μm² more on stiff gels than soft gels, but stiff gels in that study carried twice the ligand. Using the synthetic factorial above, how much of that difference could ligand alone explain?

**Step 1.** Compare soft-high with soft-low: 1300 − 900 = 400 μm² from ligand at fixed (soft) stiffness.

**Step 2.** The confounded comparison is stiff-high versus soft-low: 2600 − 900 = 1700 μm², which includes stiffness, ligand and their interaction.

**Step 3.** Without the factorial, this comparison cannot separate those contributions. The factorial shows that stiffness alone at low ligand adds 500 μm², ligand alone on soft gels adds 400 μm², and the remaining 800 μm² is the extra benefit of having both, the difference of differences (twice the interaction effect as defined above).

## Limits of this lesson

All numbers are synthetic. Real substrates also differ in porosity, viscoelasticity and protein adsorption from serum, which require their own controls.
