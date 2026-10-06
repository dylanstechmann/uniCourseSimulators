# Cell fractionation: enrichment, contamination, and recovery

Microscopy preserves spatial context but can be limited by resolution, labeling, and optical background. Biochemical fractionation separates material from a disrupted sample so that it can be measured in different fractions. A fraction is an experimentally produced mixture. Calling it “mitochondrial,” “nuclear,” or “pure” requires marker evidence, recovery measurements, and a definition of the claim.

## Learning objectives

By the end of this lesson, you should be able to:

1. Explain what differential centrifugation separates and why a pellet is not automatically a purified organelle.
2. Calculate recovery of a marker across fractions and distinguish recovery from enrichment and purity.
3. Interpret marker recovery and contamination across fractions, and identify the additional denominator needed to calculate concentration-based enrichment.
4. Design controls that separate a fractionation artifact from a change in protein abundance, integrity, or biological localization.

## What the centrifuge separates

In a simplified differential-centrifugation workflow, cells are disrupted under conditions intended to release subcellular components while retaining relevant structures. At a selected force and time, faster-sedimenting material forms a pellet; smaller or less dense material remains in the supernatant. Repeating the process on the supernatant produces additional pellets and a final soluble fraction. The actual sedimentation rate depends on particle size, shape, density difference from the medium, viscosity, rotor geometry, and applied force. RPM alone does not specify the force experienced at every position in a rotor.

Differential centrifugation separates overlapping populations by sedimentation behavior; it does not sort each organelle into a single pure tube. A low-speed pellet can contain nuclei, unbroken cells, and large debris. Mitochondria and other dense structures may overlap in an intermediate pellet. Small membrane fragments can sediment into a microsomal fraction, while soluble proteins remain in a supernatant. Density-gradient methods can provide additional separation based on buoyant density, but no separation method eliminates the need for marker and recovery measurements.

Fraction labels describe the intended target or its measured marker distribution, not the complete composition. The starting homogenate, each pellet, and each supernatant should be tracked. If the claim depends on an organelle remaining intact, include a measurement of membrane integrity or topology rather than relying only on a marker band.

## A synthetic marker panel

The table below is **synthetic teaching data**. Each cell is the percentage of the starting amount of that marker recovered in the named fraction. Values are constructed, not observed from cells. `P1`, `P2`, and `P3` represent successive pellets; `S1` is the final supernatant.

| Marker measured | P1: coarse pellet | P2: organelle-rich pellet | P3: small-membrane pellet | S1: final supernatant | Total recovered |
|---|---:|---:|---:|---:|---:|
| Nuclear marker | 78% | 9% | 2% | 4% | 93% |
| Mitochondrial marker | 12% | 76% | 5% | 1% | 94% |
| ER marker | 4% | 18% | 68% | 5% | 95% |
| Soluble cytosolic marker | 2% | 3% | 4% | 86% | 95% |

P2 contains the largest measured share of the starting mitochondrial marker among the collected fractions. It also contains 18% of the starting ER marker and 9% of the nuclear marker, so it is not a pure mitochondrial preparation. These recovery percentages describe partitioning; they do not calculate a concentration-based enrichment factor because fraction volume and total protein are not supplied. To estimate enrichment relative to total protein or volume, measure that denominator in every fraction and compare with the input.

For a marker `M`, percent recovery across the collected fractions is:

`recovery(M) = 100 × (amount of M in all collected fractions) / (amount of M in the starting input)`

For the synthetic ER marker, `4 + 18 + 68 + 5 = 95%` recovery. The missing 5% could reflect assay uncertainty, uncollected material, degradation, or measurement error. It is not evidence that 5% of ER was biologically destroyed. Recovery is an accounting check on the experiment; it is not the same as purity or enrichment.

**Enrichment** is a concentration or specific-activity comparison and needs a denominator such as total protein, fraction volume, or a documented input. The table supports a statement about marker partitioning and recovery, not a normalized enrichment factor. **Purity** asks what else is present and usually requires several independent markers or orthogonal characterization. **Yield** asks how much target material was retained. Increasing purity can reduce yield, and an unreported loss can make fractions appear selectively depleted.

## Controls and normalization

Measure marker amounts or activities in the starting input and in every collected fraction. Use matched starting-cell numbers or a documented input amount, record volumes, and avoid comparing raw band intensity from unequal loads as if it were total recovery. A marker panel should include positive markers for the compartments of interest and markers for likely contaminants. Validate marker behavior in the cell type and conditions used; proteins sometimes occupy more than one compartment or change distribution after perturbation.

Other controls depend on the claim:

- A **starting-homogenate aliquot** gives the denominator for recovery and confirms the marker was present before fractionation.
- **Input and fraction volume records** allow total amounts to be compared instead of equal-volume aliquots alone.
- A **membrane-integrity or protease-protection test** addresses whether a membrane compartment remained intact; a marker distribution by itself does not.
- A **spike or recovery standard** can identify losses during transfer, extraction, or detection.
- An **orthogonal microscopy or imaging measurement** checks whether a fractionation pattern agrees with intact-cell spatial evidence.
- A **matched cell count, total protein, or other normalization** helps distinguish a change in starting material from a change in partitioning.

Normalize activity claims to an explicit denominator: total cells, total protein, fraction volume, or amount of a measured enzyme. A higher activity per milligram of protein in P2 may show enrichment of that activity; it does not by itself prove that the enzyme acts in mitochondria in an intact cell. Homogenization can rupture membranes, release soluble contents, and redistribute associations. A perturbation can also change organelle abundance, marker expression, cell viability, or recovery.

## Bounded conclusions from a fraction

If P2 gains candidate-protein signal after a perturbation, first ask whether the starting homogenate changed, whether the mitochondrial marker recovery changed, whether ER or nuclear markers also shifted, and whether total protein loaded was matched. An increase in P2 alone may reflect more candidate protein overall, greater mitochondrial abundance, altered breakage, or a contaminating fraction. A rescue, an orthogonal localization measurement, and recovery across all fractions can help distinguish these alternatives.

**Worked interpretation.** Suppose a candidate signal rises in P2 while the mitochondrial marker's total recovery falls from 94% to 65%. The fraction-specific increase cannot be read directly as increased mitochondrial localization: altered recovery is a competing explanation. Repeat the fractionation with matched input, measure the complete marker panel and candidate abundance in every fraction, and check the organelle-integrity control. A conclusion should name the fraction and the measured distribution rather than silently converting it into an in-cell mechanism.

### Check your reasoning

In the table, identify the fraction containing the largest measured share of the mitochondrial marker and calculate ER-marker recovery. Which contaminants prevent a “pure mitochondria” claim? What protein or volume denominator would be needed for a concentration-based enrichment factor, and what additional measurement would test whether mitochondrial membranes stayed intact?

## Provenance

This is original explanatory text and original synthetic data under the course's CC BY 4.0 content license. Claude's 1946 differential-fractionation paper and the linked NCBI cell-biology methods chapter are bibliographic or methods references only; no source text, figure, or data is reproduced or adapted.
