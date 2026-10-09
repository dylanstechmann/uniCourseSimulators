# Multiple integrals and Jacobian measures

## Learning objectives

1. Set bounds from a geometric region and evaluate selected double and triple integrals.
2. Transform area and volume elements using the absolute Jacobian determinant.
3. Interpret density totals and coordinate domains without counting a region twice.

## A region determines its bounds

A double integral adds small area-weighted contributions. Its iterated form must describe the actual region. For the triangle D with x≥0, y≥0 and x+y≤1, one description is 0≤x≤1, 0≤y≤1−x. Integrating the constant 1 gives area 1/2. Integrating the synthetic density x+y gives total 1/3. Reversing order yields 0≤y≤1, 0≤x≤1−y and the same answers.

The inner bound depends on the outer coordinate because the slanted edge moves. Replacing 1−x by 1 would describe the unit square and give a different integral. Sketching a vertical or horizontal slice, even in words, helps: at fixed x the slice begins at the horizontal axis and ends at the line y=1−x. For a density total, the integrand and area element together supply amount units; integrating the density alone without area does not.

Fubini's theorem supports exchanging iterated integrals under appropriate integrability conditions, for example a continuous function on the bounded regions used here. Arbitrary singular or conditionally integrable examples require more care. An order change is a change in representation of the same region, not permission to retain old bounds with new differential symbols.

## Polar area

The transformation x=r cosθ, y=r sinθ has area element r dr dθ for r≥0. The factor r is the absolute Jacobian determinant. It records how an equal radial-angle coordinate cell expands with radius. An annulus 1≤r≤2 with synthetic density r² has total ∫₀^(2π)∫₁²r³dr dθ=15π/2, approximately 23.561945.

The annulus area itself is 3π. Dividing its density total by that area gives average density 2.5 in the chosen scale, between the minimum density 1 and maximum density 4. These bounds supply a practical check on weighting. An unweighted average over the radial interval gives a different value because it treats radii equally instead of weighting their circular area.

Angles covering a full rotation should describe the region once. Allowing both negative r and a full ordinary angle range can create repeated representations unless the mapping and multiplicity are handled explicitly. At r=0 polar coordinates are not one-to-one, but that single point has zero area and the standard integral can still be valid on a disk with the usual domain.

## Linear coordinate transformations

The ellipse x²/4+y²/9≤1 becomes a unit disk under x=2u,y=3v. Its determinant is 6, so dx dy=6 du dv. The ellipse area is 6π. The determinant has an absolute value in an unsigned measure: an orientation-reversing map would not make geometric area negative. Oriented surface and circulation conventions are a different issue and must be carried separately.

A coordinate transformation needs a usable domain and an appropriate one-to-one description except possibly on negligible boundary sets. A Jacobian factor by itself does not repair a map that covers the same region several times. Check the transformed region, factor and multiplicity together. Coefficients also carry scale when coordinates have units; a transformation from a unit disk to a physical ellipse restores the corresponding area units.

## Cylindrical and spherical volume

Cylindrical coordinates give dV=r dr dθ dz. A cylinder with radius 1 and height 2 has volume ∫₀²∫₀^(2π)∫₀¹r dr dθ dz=2π. The height bounds are separate from the radial area factor. A spatial density may depend on z as well as r; radial symmetry in a slice does not imply uniformity along the whole cylinder.

Use spherical coordinates with radius ρ≥0, polar angle φ from the positive z axis in [0,π], and azimuth θ in [0,2π]. The volume element is ρ² sinφ dρ dφ dθ. Naming the angle convention prevents switching the sine factor to the wrong angle. A ball of radius 2 has volume 32π/3. The integral of the synthetic density ρ² over that ball is 4π∫₀²ρ⁴dρ=128π/5, approximately 80.424772. Dividing by volume gives average squared radius 12/5, within the range zero to four.

## Worked example

For the elliptical region, substitute x=2u,y=3v, find determinant 6 and transform the boundary into u²+v²≤1. Integrate 6 over the unit disk to obtain 6π. For the ball, integrate the spherical angular factor sinφ from zero to π, giving 2, and azimuth over a full turn, giving 2π. The remaining radial integrals are ∫₀²ρ²dρ for volume and ∫₀²ρ⁴dρ for the density total. The common angular factor is 4π, while the different radial powers answer different questions.

## Common mistakes and checks

Do not omit r in polar or cylindrical coordinates, or ρ²sinφ in spherical coordinates. Do not retain triangle bounds when reversing the order without reconstructing slices. Check that a density average lies between its known extrema. Distinguish the absolute Jacobian for unsigned measure from the oriented area vector used in flux. A total's units must include all integrated spatial dimensions.

## Limits of this lesson

Regions and densities are synthetic. The lesson develops selected regular coordinate changes rather than a full measure-theoretic treatment or arbitrary singular transformations. No measured tissue density or spatial sampling protocol is established. Practice checks selected totals and domain choices, not a written geometric derivation. Original content was developed with substantial AI assistance. The package remains partial, unreviewed and formative-only.
