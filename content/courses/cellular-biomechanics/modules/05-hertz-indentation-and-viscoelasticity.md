# Measuring how stiff a cell is: Hertz indentation, viscoelastic relaxation and what a single modulus hides

Cells sense and respond to mechanical cues, and their own stiffness changes with differentiation, disease and age. Measuring that stiffness is harder than it looks. A cell is soft, heterogeneous, and both elastic and viscous: it springs back like a solid on short time scales and flows like a liquid on long ones. This lesson extracts a Young's modulus from an atomic force microscope (AFM) indentation using the Hertz model, then uses simple spring-and-dashpot models to show why the number depends on how fast you push.

## Learning objectives

By the end of this lesson, you should be able to:

1. Estimate an apparent Young's modulus from an indentation force and depth with the Hertz model for a spherical tip, stating its assumptions.
2. Calculate stress relaxation and the relaxation time for a Maxwell element and the instantaneous and long-time moduli of a standard linear solid.
3. Evaluate why reported cell moduli differ between methods and loading rates, and what must be reported for a value to be comparable.

## The Hertz model for indentation

For a rigid sphere of radius R pressed a depth δ into a flat, homogeneous, linearly elastic, isotropic half-space with Young's modulus E and Poisson's ratio ν, the force is

**F = (4/3) [E / (1 − ν²)] √R δ^(3/2).**

Rearranged: **E = 3F(1 − ν²) / (4 √R δ^(3/2)).** Cells are mostly water and are usually treated as nearly incompressible, ν ≈ 0.5.

**Synthetic AFM measurement:** a bead tip of radius 2.5 μm indents 0.5 μm with a force of 0.3 nN. Then

E = 3 × 3.0×10⁻¹⁰ × (1 − 0.5²) / (4 × √2.5×10⁻⁶ × (5.0×10⁻⁷)^1.5) = 302 Pa,

about 0.3 kPa. Because force grows with δ^(3/2), doubling the indentation to 1.0 μm would need 0.85 nN in a perfectly Hertzian material, not twice the force. Checking that the whole force curve follows the 3/2 power is a basic test of whether the model applies.

The assumptions matter. A cell is not a half-space: if the indentation is more than about 10% of the cell's height, the stiff substrate underneath raises the apparent modulus. The cell is not homogeneous: the nucleus, cortex and cytoplasm differ, so the value depends on where you indent. And the cell is not purely elastic.

## Viscoelasticity: springs and dashpots

A spring (stress = E × strain) stores energy; a dashpot (stress = η × strain rate) dissipates it. Combining them gives simple models.

**Maxwell element** (spring and dashpot in series): under a sudden fixed strain the stress relaxes as σ(t) = σ₀ e^(−t/τ), with relaxation time **τ = η/E**. With synthetic η = 2×10³ Pa·s and E = 10³ Pa, τ = 2.0 s, and a stress of 100 Pa decays to 8.2 Pa after 5 s. The Maxwell element eventually relaxes completely, like a liquid.

**Standard linear solid** (a spring E₁ in parallel with a Maxwell element E₂, η): suddenly strained, it first resists with the **instantaneous modulus E₁ + E₂** = 1200 Pa, then relaxes with τ = η/E₂ = 2 s toward the **long-time modulus E₁** = 400 Pa. Cells often behave like this over limited time ranges, and over wider ranges their relaxation follows a power law instead of a single exponential, meaning there is no single characteristic time.

## Why the "stiffness of a cell" is not one number

Indenting fast probes the instantaneous response; indenting slowly lets the cell relax. A standard-linear-solid cell indented in much less than 2 s appears 3 times stiffer than when indented slowly. Methods differ in time scale and in which structure they load: AFM with a sharp tip probes the cortex locally, a large bead averages over more of the cell, micropipette aspiration and optical stretching deform the whole cell. Published cell moduli therefore span orders of magnitude for the same cell type. A value is comparable only if the method, tip geometry, indentation depth, loading rate, location on the cell, model used and fitting range are reported with it.

## Common mistakes

- Fitting Hertz to indentations that are a large fraction of cell height, which mixes in the substrate.
- Using a cone or pyramid tip with the sphere formula; each geometry has its own expression.
- Comparing moduli measured at different loading rates as if they were the same quantity.
- Reporting a single mean across cells without the spread, which hides real heterogeneity between cells.

## Worked example

**Problem.** Two labs measure the same synthetic cell type. Lab A indents at a rate that completes in 0.5 s and reports 1200 Pa; lab B holds each indentation for 60 s and reports 400 Pa. Are the results contradictory?

**Step 1: time scales.** The relaxation time is 2 s. Lab A's 0.5 s is much shorter, so it sees the instantaneous modulus E₁ + E₂; lab B's 60 s is much longer, so it sees E₁.

**Step 2: model check.** With E₁ = 400 Pa and E₂ = 800 Pa, the standard linear solid predicts exactly these two values.

**Step 3: conclusion.** The results are consistent; they report different parts of one viscoelastic response. A useful comparison reports the relaxation curve or the moduli at stated time scales, not a single "stiffness".

## Limits of this lesson

All forces, depths and material constants are synthetic. The models are idealized; real cells are active, remodel during measurement, and can stiffen with strain.
