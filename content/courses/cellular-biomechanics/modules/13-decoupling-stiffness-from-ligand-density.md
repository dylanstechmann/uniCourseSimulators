# Decoupling stiffness from ligand density and mobility: redesigning the experiment

The package's case describes a stiff hydrogel that increases a differentiation marker. Stiffness was raised by adding crosslinker, and the crosslinker also reduced the mobility of the adhesive ligand. The result is the classic confounded experiment: more crosslinker means a stiffer gel and a less mobile ligand at the same time, so a rise in the marker could be due to either. This lesson quantifies how much a confounded design costs, shows how to measure the quantity that was not controlled (ligand mobility, by photobleaching recovery), proposes a crossed design that separates the factors, and counts the independent units that such a design really has. All values are synthetic and the plan is a way of reasoning, not a protocol.

## Learning objectives

By the end of this lesson, you should be able to:

1. Quantify the loss of precision caused by two correlated explanatory variables.
2. Compute a diffusion coefficient from a photobleaching recovery time and use it to characterize ligand mobility.
3. Plan a crossed design and its replication, with the gel as the independent unit.

## What a confounded design costs

Suppose stiffness and ligand mobility change together across the gels, with a correlation of r = 0.95 between them (on a logarithmic scale of stiffness). Regressing the marker on both explanatory variables gives estimates whose variance is inflated by the **variance inflation factor**

**VIF = 1/(1 − r²) = 1/(1 − 0.95²) = 10.26,**

so the standard error of each effect is **3.20 times** as large as it would be if the two were uncorrelated, and the same precision would need about 10 times as many gels. With r = 1 (exactly proportional) the effects cannot be separated at all, and the data say only that the marker rises with crosslinker. A design in which the two are varied independently, so that their correlation is zero, has VIF = 1.

## Measuring the quantity that was not controlled: ligand mobility

Mobility of a tethered ligand can be measured by fluorescence recovery after photobleaching: a fluorescently labeled ligand is bleached in a circular spot of radius w, and the time t½ for the fluorescence to recover to half of its final level gives a diffusion coefficient. For a circular spot, D ≈ 0.224 w²/t½. **Synthetic example:** with w = 5 μm, a lightly crosslinked gel recovers with t½ = 12 s, so D = 0.224 × 5²/12 = **0.467 μm²/s**, and a gel with more crosslinker recovers with t½ = 30 s, so D = 0.187 μm²/s, a ratio of **2.5**. The mobility differs by a factor of 2.5 between the gels, and it must be reported as a characteristic of each formulation, together with the storage and loss moduli at culture conditions (see the rheology lesson) and the ligand density measured on the gel.

## A crossed design

The redesigned experiment varies the two factors independently. It crosses three stiffness levels (spaced logarithmically, for example 1, 10 and 100 kPa, adjusted without changing the ligand density or mobility, perhaps by changing the polymer content or the chemistry of the crosslinks) with two ligand densities (low and high, measured on the gels), and adds the control of a non-adhesive surface and a ligand-scrambled peptide. Each combination is made on several independent gels. With three gels per combination there are 18 gels. If 20 cells are imaged on each, there are 360 cells, but only 18 independent units, and the analysis is done on gel means, as the statistics lessons explain.

## The unit of analysis, with numbers

Suppose the SD between gels is 6 points and the SD between cells within a gel is 15 points. The mean of 20 cells on a gel has SD √(6² + 15²/20) = **6.87**. A main effect is a difference between two arms of 9 gels each, with standard error 6.87 × √(2/9) = **3.24** points. Treating the 180 cells in each arm as independent would use the total SD √(6² + 15²) = 16.16 and give a standard error of 16.16 × √(2/180) = **1.70** points, which is 1.90 times too small. More cells per gel would not rescue the comparison, since the between-gel part of the variation remains; more gels would.

## Common mistakes

- Raising stiffness by crosslinker alone and attributing the result to stiffness.
- Reporting stiffness without the ligand density and mobility of the same gels.
- Analyzing cells as independent when the gels are the units.
- Adding more cells per gel instead of more gels.
- Omitting a non-adhesive and a scrambled-ligand control.
- Spacing the stiffness values linearly over a wide range.

## Worked example

**Problem.** Two explanatory variables are correlated with r = 0.9. Gels have a between-gel SD of 5 and a within-gel cell SD of 12, with 15 cells per gel and 6 gels per arm. Find the VIF, the standard error of a difference between arms using gel means and using cells, and the diffusion coefficient for a spot of radius 4 μm with t½ = 20 s.

**Step 1: VIF.** 1/(1 − 0.9²) = 5.26.

**Step 2: gel-level SE.** The SD of a gel mean is √(5² + 12²/15) = 5.88, and SE = 5.88 × √(2/6) = 3.40.

**Step 3: naive cell-level SE.** √(5² + 12²) = 13.00, and SE = 13.00 × √(2/90) = 1.94, which is 1.75 times too small.

**Step 4: mobility.** D = 0.224 × 4²/20 = 0.179 μm²/s.

## Limits of this lesson

All numbers are synthetic. The variance inflation factor is the large-sample result for two predictors in a linear model; real gels differ in more than two properties, and orthogonal control of stiffness, ligand density and mobility is hard to achieve chemically. The recovery formula assumes free diffusion in a circular spot. The design is an outline of how to reason, not a protocol.
