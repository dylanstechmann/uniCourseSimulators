# Gradients in a concentration field: partial derivatives, directional derivatives and what a cell can sense

During development and regeneration, cells often read their position from the concentration of a signaling molecule that spreads from a source. Whether a cell can tell which way the source lies depends on how steeply the concentration changes across its own body: the gradient. Multivariable calculus describes that precisely. This lesson computes partial derivatives and the gradient of a synthetic two-dimensional concentration field, finds directional derivatives and the direction of steepest increase, and uses Fick's law to turn the gradient into a diffusive flux.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute partial derivatives and the gradient vector of a two-variable concentration field at a point.
2. Calculate a directional derivative, identify the direction of steepest ascent and interpret the gradient's magnitude.
3. Apply Fick's law J = −D∇C and estimate the fractional concentration difference across a cell to judge whether a gradient is detectable.

## A synthetic concentration field

Suppose a source at the origin maintains the steady field

**C(x, y) = 100 exp(−(x² + y²)/(2s²)) μM,** with s = 50 μm and x, y in μm.

At the point P = (30, 40) μm, 50 μm from the source, C = 100 e^(−0.5) = 60.65 μM.

## Partial derivatives and the gradient

A partial derivative measures change in one coordinate direction while holding the other fixed. By the chain rule,

∂C/∂x = −(2x/(2s²)) C = −(x/s²) C, ∂C/∂y = −(y/s²) C.

At P: ∂C/∂x = −(30/2500) × 60.65 = -0.7278 μM/μm and ∂C/∂y = −(40/2500) × 60.65 = -0.9704 μM/μm. The **gradient** collects them into a vector, ∇C = (-0.7278, -0.9704) μM/μm, with magnitude |∇C| = √(-0.7278² + -0.9704²) = 1.213 μM/μm.

## Directional derivatives and steepest ascent

The rate of change of C in the direction of a unit vector u is the **directional derivative** D_u C = ∇C · u. Moving in the +x direction, u = (1, 0), D_u C = -0.7278 μM/μm: concentration falls, since P lies up and to the right of the source. Along the diagonal u = (1/√2, 1/√2), D_u C = (-0.7278 + -0.9704)/√2 = -1.2009 μM/μm.

Because D_u C = |∇C| cos θ, where θ is the angle between u and ∇C, the largest increase occurs along ∇C itself (θ = 0), with rate |∇C|. Here ∇C points along (−0.6, −0.8), straight back toward the source, as symmetry demands. Directions perpendicular to the gradient follow contour lines of constant concentration, where D_u C = 0.

## From gradient to flux: Fick's law

Molecules diffuse down their gradient. In two or three dimensions, Fick's first law reads

**J = −D ∇C.**

The minus sign says flux points from high to low concentration, opposite to the gradient. With a synthetic diffusion coefficient D = 10 μm²/s, the flux magnitude at P is 10 × 1.213 = 12.13 μM·μm/s, directed away from the source. In a true steady state, the field must also satisfy a balance of diffusion, production and removal; this lesson takes the field as given and looks only at its local geometry.

## What a cell can sense

A cell of length 10 μm aligned with the gradient experiences a concentration difference of about |∇C| × L = 12.1 μM between its ends, which is 20% of the local concentration. Cells that sense chemical gradients by comparing receptor occupancy across their surface are often described as able to detect differences of a few percent across their length, but detection also depends on concentration relative to receptor affinity and on noise in binding. Far from the source, both C and |∇C| fall; the fractional difference |∇C|L/C = (r/s²)L grows with distance r in this particular field, while the absolute concentration becomes too low to bind receptors reliably. Positional information is therefore best in a band of distances, not everywhere.

## Common mistakes

- Forgetting the chain-rule factor when differentiating the exponent.
- Using a non-unit vector in the directional derivative, which scales the answer by its length.
- Dropping the minus sign in Fick's law, so the flux points up the gradient.
- Judging detectability from the absolute gradient alone instead of the fractional difference across a cell.

## Worked example

**Problem.** At Q = (60, 80) μm, twice as far from the source, find C, |∇C| and the fractional difference across a 10 μm cell.

**Step 1.** C = 100 e^(−10000/5000) = 13.53 μM.

**Step 2.** |∇C| = (r/s²) C = (100/2500) × 13.53 = 0.541 μM/μm.

**Step 3.** Fractional difference = 0.541 × 10 / 13.53 = 40%. The relative signal is larger, but the absolute concentration has fallen about 4.5-fold, so whether a cell there reads direction better depends on its receptors.

## Limits of this lesson

The field is synthetic and fixed in time. Real morphogen fields are shaped by production, degradation, binding to matrix and transport by flow; the lesson describes no specific signal or tissue.
