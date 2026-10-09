# Stokes' theorem and spatial balances

## Learning objectives

1. Relate oriented boundary circulation to curl flux through a spanning surface.
2. Apply volume balance signs to net boundary transfer, sources, sinks and storage.
3. Check smoothness, singularities and modeling assumptions before choosing a vector-field theorem.

## A boundary and its spanning surface

Stokes' theorem states ∮_(∂S)F·dr=∫_S(∇×F)·n dA for an appropriately oriented smooth or piecewise smooth surface, with the field continuously differentiable on a neighborhood of that surface. The boundary direction follows the right-hand rule with the chosen normal. Reversing the normal requires reversing the boundary direction and changes both signs.

For the synthetic field F=(−y/2,x/2,z), curl is (0,0,1). On the upward unit disk in the xy plane, curl flux equals its area π. The compatible boundary is the counterclockwise unit circle when viewed from above. A disk of radius 2 gives circulation 4π. The z component of F does not contribute to this horizontal circle's work, but its presence must still be included when computing the field derivatives.

Stokes relates circulation to curl flux, while the divergence theorem relates a vector field's outward transfer across a closed boundary to its divergence inside a volume. An open surface can serve as a Stokes spanning surface; it cannot by itself be the full closed boundary needed for the divergence theorem. The integral's type and geometry determine which theorem applies.

## A tilted triangle

Let a triangle have vertices A=(0,0,0), B=(1,0,0), C=(0,1,1), traversed A to B to C to A. The oriented edge cross product (B−A)×(C−A) is (0,−1,1), with positive z component. Its oriented triangle area vector is half that, (0,−1/2,1/2). Dotting constant curl (0,0,1) into this vector gives circulation 1/2.

The triangle's unsigned area is √2/2, yet its curl flux is 1/2 because only the projected area normal to the curl direction contributes. Substituting the full unsigned area would omit the angle factor. A direct integral along the three straight edges supplies another route to the same result and checks the boundary orientation.

## Storage, sources and sinks

For a fixed volume V, let M be stored amount, Q_out=∫_(∂V)J·n dA be net outward transfer, and s and r be volumetric source and sink rates. Conservation gives dM/dt=∫_V(s−r)dV−Q_out. Outward transfer removes stored amount; a negative Q_out represents inward supply and therefore adds to storage in this equation.

At steady state, storage derivative is zero, so Q_out equals integrated source minus sink. If no source is present and a uniform sink r consumes amount inside, Q_out is negative. The local smooth form is ∂C/∂t+∇·J=s−r. At steady state with no source, ∇·J=−r. This sign follows from conservation and does not depend on calling an incoming transfer “negative uptake.”

For the synthetic field J=(−2x,−3y,−4z) on [0,2]×[0,1]×[0,1], divergence is −9 and volume is 2. Net outward transfer is −18 amount units per second in the stated coordinate and flux scale. With zero storage change and no source, a uniform sink of 9 amount units per cubic metre per second balances that inward supply. This is a stipulated steady mathematical model, not an inferred biological oxygen-consumption measurement.

If the same boundary transfer remains −18 but the sink becomes 12 throughout the volume and source stays zero, storage derivative is −24−(−18)=−6 amount units per second. The volume loses stored amount despite inward supply because consumption exceeds it. A source of 2 and sink of 9 at steady state would instead require Q_out=(2−9)×2=−14. These calculations separate boundary transfer from reaction and storage terms.

## Singularities and theorem scope

The radial field F=r/|r|³ is smooth away from the origin and has divergence zero there, yet its outward flux through the unit sphere is 4π. The origin lies inside and is singular, so applying the ordinary divergence theorem to the entire ball is invalid. On a shell excluding a small inner ball, both outer and inward-facing inner boundaries belong to the shell boundary; their fluxes cancel, consistent with zero divergence in that shell.

Likewise, a spanning surface crossing a field singularity does not satisfy Stokes' smoothness assumptions merely because its boundary integral exists. An alternative spanning surface must remain in a valid region and carry the same oriented boundary. Conditions are part of the result, not a footnote that can be dropped after obtaining a plausible number.

## Worked example

For J=(−2x,−3y,−4z), the three positive-coordinate faces of the box contribute −4, −6 and −8; the zero-coordinate faces contribute zero. Their sum is −18, matching divergence −9 times volume 2. Insert this signed result into storage balance. A uniform sink 9 gives steady storage, while sink 12 gives storage loss 6. For the tilted triangle and the separate circulation field F, use its oriented area vector rather than unsigned area to obtain 1/2. Transfer and circulation use related geometric machinery but represent different integrals.

## Common mistakes and checks

Do not infer a sink from flux alone without specifying storage and source assumptions. Do not switch a boundary's orientation independently of its surface normal. Distinguish a local divergence density from its volume-integrated transfer. Keep amount/time units separate from amount/volume/time units. Check for singularities throughout the theorem region, not only on its outer boundary.

## Limits of this lesson

All fields and balance rates are synthetic. They establish no tissue oxygen demand, experimental protocol or unique reaction mechanism. Moving boundaries, nonsmooth conservation laws and variable diffusion tensors are outside this increment. Practice checks numbers and selected assumptions rather than written proofs or causal identification. Original material has substantial AI assistance; the package remains partial, unreviewed and formative-only.
