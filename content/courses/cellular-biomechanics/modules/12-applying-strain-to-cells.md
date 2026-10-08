# Applying strain to cells: engineering and true strain, Poisson contraction and strain rate

Many experiments in mechanobiology stretch a culture substrate and ask how cells respond. A flexible membrane is clamped, pulled and released, perhaps cyclically, and the cells on it are imaged or lysed afterward. The experiment is described by a handful of numbers: how much the membrane is stretched, in which directions, how fast and how often. They are easy to confuse. A stretch of 10% along one axis is a different mechanical condition from an area change of 10%; the membrane also contracts in the transverse direction; the stress and the force are not the same as the strain; and the rate matters for a viscoelastic material. This lesson defines the strain measures, computes the transverse and area strains from the Poisson effect, relates strain to stress and force, and computes the strain rate of a cyclic protocol. All values are synthetic.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute engineering strain, true strain, transverse strain and area strain for a stretched membrane.
2. Compute the stress and total force from a modulus and a strain, and the strain rate of a cyclic stretch.
3. Evaluate what a reported strain does and does not specify about the mechanical condition of the cells.

## Strain measures for a uniaxial stretch

**Synthetic membrane:** a PDMS-like sheet with a gauge length L₀ = 20 mm, width 10 mm and thickness 0.5 mm is stretched by ΔL = 2 mm along its length. The **engineering strain** is ε = ΔL/L₀ = 2/20 = **0.10** (10%). The **true strain** accumulates the stretch in small steps and is ln(1 + ε) = **0.0953** (9.53%); the two agree for small strains and differ by about 5% of their value at 10% strain. A nearly incompressible elastomer (ν = 0.5) contracts in the transverse direction by ε_t = −ν ε = **−0.050** (−5%) at small strain, so the area changes by (1 + ε)(1 + ε_t) − 1 = 1.10 × 0.95 − 1 = **0.045** (4.5%), less than the 10% stretch along the axis. If instead the membrane is stretched **equibiaxially** by 10% in both directions, the area strain is 1.10² − 1 = **0.21** (21%): the same axial strain is a very different condition. A report of "10% strain" is incomplete unless it says uniaxial or equibiaxial, and engineering or true.

## From strain to stress and force

In the linear range the stress is σ = E ε. For E = 1.5 MPa and ε = 0.10, **σ = 150 kPa**. The force on the membrane, whose cross-sectional area is width × thickness = 10 mm × 0.5 mm = 5.0 mm², is F = σ A = 150 × 10³ Pa × 5.0 × 10⁻⁶ m² = **0.75 N**. The stress on the membrane is not the stress on a cell: cells sense the substrate's deformation through their adhesions, and a cell on a membrane follows its strain as long as the adhesions hold, whatever the stress inside the membrane. Strain is therefore the quantity that defines the stimulus. The force matters for the apparatus, which must hold it without slipping, and a membrane that thins under stretch changes the stress and the optical path.

## Rate and cycles

A cyclic stretch with a mean strain of 0.05 and an amplitude of 0.05 at 1 Hz, ε(t) = 0.05 + 0.05 sin(2πft), reaches 10% at its peak and returns to zero. Its peak strain rate is 2π f × amplitude = 2π × 1 × 0.05 = **0.314 per second**. For a viscoelastic membrane or cell, what matters is the rate relative to the relaxation time: a strain applied in much less than the relaxation time is resisted by the instantaneous modulus, and one applied slowly by the long-time modulus (see the rheology lesson). The protocol must therefore report the waveform, the frequency, the minimum and maximum strain, the duration and the number of cycles; an average strain says little.

## What a reported strain leaves unspecified

The strain defined here is the membrane's. The strain that cells experience can be lower if the membrane slips in the clamps, if the coating or the cells' own contractility resists the deformation, or if the strain field is not uniform across the culture area (it is smaller near the clamps and varies across a membrane that is wider than it is long). It is checked by imaging fiducial markers on the membrane and computing the displacement field, not assumed from the clamp displacement.

## Common mistakes

- Reporting a strain without saying uniaxial or equibiaxial.
- Confusing engineering and true strain at large strains.
- Forgetting the transverse contraction of the membrane.
- Treating the stress in the membrane as the stress on the cells.
- Reporting a mean strain for a cyclic protocol without the amplitude, frequency and waveform.
- Taking the clamp displacement as the strain in the culture area.

## Worked example

**Problem.** A synthetic membrane has L₀ = 30 mm, width 12 mm, thickness 0.4 mm and E = 1.0 MPa, and is stretched by 1.5 mm. Find the strain, the transverse and area strains (ν = 0.5), the stress and force, and the peak strain rate of a 0.5 Hz cycle with an amplitude of 0.04.

**Step 1: strain.** ε = 1.5/30 = 0.050.

**Step 2: transverse and area strain.** ε_t = −0.5 × 0.050 = −0.0250; area strain = (1 + 0.050)(1 + (−0.0250)) − 1 = 0.0237.

**Step 3: stress and force.** σ = 1.0 × 10⁶ × 0.050 = 50 kPa; F = 50 × 10³ × 4.8 × 10⁻⁶ = 0.240 N.

**Step 4: strain rate.** 2π × 0.5 × 0.04 = 0.126 per second.

## Limits of this lesson

All numbers are synthetic. The small-strain relations assume a linear elastic, isotropic, nearly incompressible membrane and a uniform strain field; real elastomers are nonlinear at large strains and viscoelastic, and the strain in the culture area needs to be measured. Nothing here is a protocol for stretching cells.
