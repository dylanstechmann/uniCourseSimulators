# Traction forces from micropillars: force from deflection, and what the substrate really is

Cells pull on what they attach to, and the size and pattern of those forces tell how they sense stiffness. A microfabricated array of flexible pillars turns the measurement into one of geometry: each pillar bends like a cantilever, and its tip deflection, which a microscope can resolve, gives the force on it through Hooke's law. This lesson derives the stiffness of a pillar from beam theory, converts deflections into forces and stresses, shows how strongly the stiffness depends on the pillar's diameter and height, and states what an array of pillars is and is not as a model of a substrate. All values are synthetic.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute the bending stiffness of a cylindrical pillar and the force and traction stress from a measured deflection.
2. Use the scaling of the stiffness with the pillar's diameter and height to design an array.
3. Evaluate the limits of the beam model and of pillars as a model of a continuous substrate.

## The pillar as a cantilever

A cylindrical pillar of Young's modulus E, diameter d and height L, loaded sideways at its tip, behaves as an Euler–Bernoulli cantilever of second moment of area I = πd⁴/64. The tip stiffness is

**k = 3EI/L³ = 3πE d⁴ / (64 L³),**

and a deflection x at the tip corresponds to a force F = k x. **Synthetic values:** a PDMS-like pillar with E = 2.0 MPa, d = 2 μm and L = 6 μm has k = 3π × (2.0 × 10⁶) × (2 × 10⁻⁶)⁴/(64 × (6 × 10⁻⁶)³) = **0.0218 N/m = 21.8 nN/μm**. A tip deflection of 0.2 μm therefore means a force of 21.8 × 0.2 = **4.36 nN**, and spread over the pillar's top area π d²/4 = 3.14 μm² it is a stress of 1389 Pa (1 nN/μm² = 1 kPa; the stress is an average over the contact area, which is smaller than the top area for a real focal adhesion). A cell that deflects 40 pillars by 0.1 μm on average applies a total force of 40 × 21.8 × 0.1 = **87 nN**.

## Designing an array: the powers of d and L

Because k ∝ d⁴/L³, small changes in geometry change the stiffness a great deal. Doubling the diameter makes the pillar **16 times** stiffer, and halving the height makes it **8 times** stiffer. A thin, tall pillar with d = 1.5 μm and L = 8 μm has k = 2.91 nN/μm, about 7 times softer than the pillar above. This is how arrays of different effective stiffness are made from the same material: by changing the geometry, not the chemistry. The beam formula assumes deflections small compared with the height (a common limit is about 10% of L, here 0.6 μm), a uniform modulus, and pillars that do not interact; at larger deflections the force is not proportional to the deflection, and the measurement needs a calibrated nonlinear correction.

## Pillars are not a continuous substrate

An array of pillars gives each focal adhesion a spring of known stiffness, which is an advantage for interpretation, but the cell sees a different substrate from a continuous gel. Forces are applied only at discrete points, the cell can bridge between pillars and sag between them, and the stiffness that the cell experiences also depends on the pillar spacing and on how much of the cell's adhesive area lies on pillar tops. An effective stiffness of the array in kPa is therefore a model-dependent number, and a comparison with a hydrogel needs the same quantity measured in the same way. The deflection is measured against a reference position found from the unloaded pattern, and the error of that reference sets the smallest detectable force; with a localization error of 20 nm the force resolution of the pillar above is 0.44 nN.

## Common mistakes

- Using the diameter to the first power or the height to the first power in the stiffness.
- Mixing nanometres, micrometres and metres in the formula.
- Reporting the stress as force divided by the area of the whole cell instead of the adhesion.
- Using the beam formula for large deflections.
- Treating the stiffness of the pillar array as the modulus of a gel.
- Forgetting that the reference position has an error.

## Worked example

**Problem.** A synthetic pillar has E = 1.5 MPa, d = 1 μm and L = 4 μm. Find k, the force at a deflection of 0.05 μm, the stress over the top area, and the total force on 25 such pillars.

**Step 1: stiffness.** k = 3π × (1.5 × 10⁶) × (1 × 10⁻⁶)⁴/(64 × (4 × 10⁻⁶)³) = 0.0035 N/m = 3.45 nN/μm.

**Step 2: force.** F = 3.45 × 0.05 = 0.17 nN.

**Step 3: stress.** The top area is 0.785 μm², so the stress is 220 Pa.

**Step 4: total.** 25 × 0.17 = 4 nN.

## Limits of this lesson

All numbers are synthetic. The cantilever formula assumes a uniform pillar of circular section and small deflections; real pillars taper, their modulus varies with processing, and the force of a cell is not applied at the tip. Nothing here is a measurement of any real cell or array.
