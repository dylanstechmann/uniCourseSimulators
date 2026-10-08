# Virtual lab 1: oxygen depth profiles in cell-laden slabs

**Activity type:** synthetic-data analysis with public, ungraded formative checks
**Course package:** Thermodynamics & Transport in Bioengineering. **Estimated learner time:** 2–3 hours
**Data status:** all measurements are constructed for instruction. They describe no real tissue, sensor or experiment, and nothing here is evidence about any construct or cell.
**Dataset:** [synthetic oxygen profiles (CSV)](https://raw.githubusercontent.com/dylanstechmann/uniStemCourseSimulators/main/content/courses/transport/labs/oxygen-depth-profiles.csv).

## Experimental question

A cell-laden slab is bathed on one face at a fixed oxygen concentration (C₀ = 0.2 mol/m³) and sealed at the other face. A microsensor records the oxygen concentration at depths of 25 μm steps from the supplied face to the sealed face. Three slab thicknesses (100, 200 and 300 μm) are measured, with three independent constructs each. The lab asks for the consumption rate, the critical thickness, the thickness of the anoxic zone of the thickest slab, and the limits of the zero-order interpretation. It describes the logic of the measurement, not an operating procedure.

## Learning objectives

1. Summarize replicate oxygen profiles by slab thickness at chosen depths.
2. Estimate the consumption rate from the curvature of a profile and the critical thickness from it.
3. Interpret a profile that reaches zero oxygen, including the thickness of the anoxic zone, and state the limits of the model.

## Data dictionary

| Column | Meaning |
|---|---|
| thickness_um | slab thickness, μm |
| replicate | 1 to 3, an independent construct |
| depth_um | depth from the supplied face, μm |
| o2_mol_m3 | dissolved oxygen, mol/m³ |

## The synthetic data

**100 μm slab**

| Depth (μm) | Profile 1 | Profile 2 | Profile 3 | Mean |
|---:|---:|---:|---:|---:|
| 0 | 0.204 | 0.198 | 0.198 | 0.200 |
| 25 | 0.175 | 0.182 | 0.177 | 0.178 |
| 50 | 0.162 | 0.160 | 0.166 | 0.163 |
| 75 | 0.157 | 0.151 | 0.151 | 0.153 |
| 100 | 0.147 | 0.154 | 0.149 | 0.150 |

**200 μm slab**

| Depth (μm) | Profile 1 | Profile 2 | Profile 3 | Mean |
|---:|---:|---:|---:|---:|
| 0 | 0.197 | 0.204 | 0.199 | 0.200 |
| 25 | 0.152 | 0.151 | 0.156 | 0.153 |
| 50 | 0.116 | 0.110 | 0.110 | 0.112 |
| 75 | 0.075 | 0.082 | 0.077 | 0.078 |
| 100 | 0.049 | 0.048 | 0.053 | 0.050 |
| 125 | 0.028 | 0.028 | 0.028 | 0.028 |
| 150 | 0.012 | 0.012 | 0.012 | 0.012 |
| 175 | 0.003 | 0.003 | 0.003 | 0.003 |
| 200 | 0.000 | 0.000 | 0.000 | 0.000 |

**300 μm slab**

| Depth (μm) | Profile 1 | Profile 2 | Profile 3 | Mean |
|---:|---:|---:|---:|---:|
| 0 | 0.199 | 0.198 | 0.203 | 0.200 |
| 25 | 0.157 | 0.151 | 0.151 | 0.153 |
| 50 | 0.110 | 0.116 | 0.112 | 0.113 |
| 75 | 0.077 | 0.076 | 0.081 | 0.078 |
| 100 | 0.054 | 0.048 | 0.048 | 0.050 |
| 125 | 0.028 | 0.028 | 0.028 | 0.028 |
| 150 | 0.012 | 0.012 | 0.012 | 0.012 |
| 175 | 0.003 | 0.003 | 0.003 | 0.003 |
| 200 | 0.000 | 0.000 | 0.000 | 0.000 |
| 225 | 0.000 | 0.000 | 0.000 | 0.000 |
| 250 | 0.000 | 0.000 | 0.000 | 0.000 |
| 275 | 0.000 | 0.000 | 0.000 | 0.000 |
| 300 | 0.000 | 0.000 | 0.000 | 0.000 |

## Work sequence

To use the software checks, open **Practice gradebook** and select **Virtual lab 1: oxygen depth profiles in cell-laden slabs (ungraded practice)**. The points are practice feedback only.

1. **Summarize.** Count the profiles and average the oxygen at depth 0, at 100 μm and at the sealed face for each thickness. Upload a table with columns `thickness`, `profiles`, `c_surface`, `c_100` and `c_end`.
2. **Consumption rate.** From the sealed-face concentration of the 100 μm slab, solve C_end = C₀ − qL²/(2D) for q (D = 2.0 × 10⁻⁹ m²/s).
3. **Critical thickness.** Compute √(2DC₀/q) and compare it with the depth at which the 200 μm and 300 μm profiles reach zero.
4. **Anoxic zone.** Find the thickness of the anoxic zone of the 300 μm slab.
5. **Interpret.** Explain why the 200 μm and 300 μm profiles coincide down to the critical depth, and state what zero-order uptake assumes.

## Worked calculation

At the sealed face of the 100 μm slab the mean oxygen is 0.150 mol/m³, so q = 2 × 2.0 × 10⁻⁹ × (0.2 − 0.150)/(100 × 10⁻⁶)² = 0.0200 mol/(m³·s), which rounds to 0.02. The critical thickness is √(2 × 2.0 × 10⁻⁹ × 0.2/0.02) = 200 μm. The 200 μm slab reaches zero exactly at its sealed face, and the 300 μm slab reaches zero at 200 μm and is anoxic over the remaining 100 μm, one third of its thickness. The profiles of the two thicker slabs coincide down to 200 μm because the supply and the consumption, not the thickness, determine how far oxygen penetrates. The zero-order model assumes that uptake does not depend on the oxygen level; real uptake saturates, so the edge of the anoxic zone would be softer, and oxygen above zero does not prove that cells are functioning.

## Analytic rubric for discussion

| Criterion | Evidence for full credit |
|---|---|
| Summary table | Reports the number of profiles and the mean oxygen at the chosen depths for each thickness |
| Consumption | Obtains q from the sealed-face concentration with consistent units |
| Critical thickness | Computes it and relates it to the depth at which the profiles reach zero |
| Anoxic zone | Finds its thickness for the thickest slab and explains why the profiles coincide |
| Scope | States that zero-order uptake is an idealization and that a profile is not a viability measurement |

## Limits and provenance

This is an original exercise with constructed data and round parameters. Real profiles are noisier, depend on the sensor tip size and position, and are measured in constructs whose cells are not uniform. Original lab text and dataset: CC BY 4.0.
