# Surface flux and the divergence theorem

## Learning objectives

1. Construct an oriented area element for a parameterized or graph surface.
2. Compute selected surface fluxes directly and by a volume divergence integral.
3. Interpret negative outward transfer, closed boundaries and field regularity.

## Density versus total transfer

A vector flux J describes amount crossing unit area per unit time in each spatial direction. Its normal component J·n is a signed flux density, with n a unit normal. Total transfer rate is ∫_S J·n dA. Multiplying a density by area changes its units to amount per time. A negative result for an outward normal indicates net inward transfer, not a negative amount stored inside the region.

For a parameterized surface r(u,v), the oriented area vector is (r_u×r_v)du dv. Its magnitude gives unsigned area. The flux integral is ∫∫J(r)·(r_u×r_v)du dv with order chosen to match orientation. If a unit normal and scalar area are used instead, the same geometry appears as n dA. These are two equivalent conventions; do not normalize the cross product and then forget its area magnitude, or multiply its magnitude in twice.

## A sloped graph

For z=g(x,y), the graph r(x,y)=(x,y,g) has upward area vector (−g_x,−g_y,1)dx dy. Its unsigned area factor is √(1+g_x²+g_y²). The synthetic patch z=x+y over the unit square has area √3. Its upward unit normal is (−1,−1,1)/√3.

For J=(0,0,z), the flux through that patch is ∫₀¹∫₀¹(x+y)dx dy=1. The graph slope factor cancels appropriately through the oriented-vector representation; it must not be multiplied into this expression a second time. For the constant field J=(2,0,5), the dot product with (−1,−1,1) is 3, so the flux is 3 over the unit square. The horizontal component contributes because the surface is tilted.

Reversing the normal changes the flux sign while leaving surface area unchanged. “Upward” is appropriate for this graph because its normal has a positive z component. A closed surface instead uses the outward direction relative to its enclosed region, which can have positive or negative coordinate components on different faces.

## Divergence and a closed boundary

For a continuously differentiable vector field on a neighborhood of a bounded volume V with a suitable piecewise smooth closed boundary, the divergence theorem gives ∫_(∂V)J·n dA=∭_V∇·J dV with outward orientation. The boundary must include every enclosing piece. Applying the theorem to an open patch without its closing surfaces computes a different quantity.

For J=(x,y,z), divergence is 3. On the unit sphere, direct outward normal density is 1 everywhere and area is 4π, giving flux 4π. The volume calculation gives 3 times 4π/3, the same result. The constant divergence does not make the sphere's area and volume interchangeable; the field and geometry supply the conversion.

For J=(x²,y,z) on the box 0≤x≤2, 0≤y≤1, 0≤z≤1, divergence is 2x+2. Its volume integral is ∫₀²(2x+2)dx=8 because the other two coordinate widths are one. Direct face contributions give 4 on the x=2 face, 2 on y=1 and 2 on z=1. Each zero-coordinate face contributes zero. The sum is also 8. Face area matters: the x face has area 1, while each y and z face has area 2. The varying x derivative cannot simply be evaluated at one arbitrary interior point and multiplied by volume.

## Diffusion sign

For the synthetic field C=10+x²+y²+z² with consistent concentration and coordinate scales, and constant diffusivity D=0.5, the diffusive flux J=−D∇C is (−x,−y,−z) in the corresponding flux units. On a sphere of radius 2, the outward density is −2, area is 16π and total transfer is −32π. The divergence is −3 and volume is 32π/3, again giving −32π. This is net inward supply because concentration increases outward.

If D varies spatially, divergence of −D∇C includes derivatives of D. Treating it as merely −D times the Laplacian requires constant D. An irregular boundary can still be suitable for the theorem if it is closed and meets the regularity conditions; irregularity by itself is not a reason to discard it. Singular fields inside the region require an additional analysis.

## Worked example

For the sloped patch z=x+y, compute the cross product of (1,0,1) and (0,1,1) to get (−1,−1,1). Its magnitude is √3, establishing area √3 over a unit parameter square. Dot the vertical field (0,0,z) into that area vector to obtain integrand x+y and total 1. For the diffusion sphere, use the outward normal r/2, so J·n=−2. Integrate over area 16π to obtain −32π and compare with the divergence-volume result. The first surface is open and oriented upward; the second is closed and oriented outward.

## Common mistakes and checks

Do not add unsigned face magnitudes when calculating net flux. Do not omit a closing face in a divergence-theorem argument. Track flux-density versus transfer-rate units. Check the entire enclosed volume for singularities and smoothness. Verify an oriented area vector by its normal direction as well as its magnitude.

## Limits of this lesson

All fields, diffusivities and geometries are synthetic teaching constructions, with no real tissue parameter, oxygen experiment or device specification. The lesson covers selected regular surfaces and constant scalar diffusivity, not general tensor transport. Practice checks calculations and conditions rather than a written theorem proof. Original content was developed with substantial AI assistance. The package remains partial, unreviewed and formative-only.
