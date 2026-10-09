# Vectors, planes and spatial curves

## Learning objectives

1. Compute vector lengths, dot products and cross products in a stated Cartesian frame.
2. Obtain unit tangents, speeds and traced lengths from parameterized curves.
3. Interpret normal directions, point-to-plane distances and coordinate units.

## Coordinates and geometric objects

A point identifies a location; a displacement vector identifies a change between locations. In an orthonormal Cartesian frame, v=(v₁,v₂,v₃) has Euclidean length √(v₁²+v₂²+v₃²). The same physical vector can have different components in a rotated frame. Components require their frame and scale, while length remains invariant under an orthogonal change of frame. These formulas do not apply unchanged to arbitrary nonorthogonal coordinates, whose metric must also be supplied.

For the synthetic displacement v=(1,2,2) m, the length is 3 m. Its unit direction is (1/3,2/3,2/3), dimensionless. Normalization separates magnitude from direction. The zero vector has zero length and cannot be normalized. A direction-only instruction therefore needs a nonzero reference vector; silently dividing by zero is not a geometric convention.

The dot product a·b=Σaᵢbᵢ measures projection and angle. For unit u, v·u is the signed component along u. If a gradient in two dimensions is (3,4) output units per metre, its directional derivative along the vector (3,4) requires first dividing that vector by 5. The resulting slope is 5 output units per metre, the maximum possible unit-direction slope. Using the unnormalized vector would instead compute a derivative per parameter whose speed is 5, producing a different quantity.

## Cross products and orientation

In a right-handed three-dimensional Cartesian frame, a×b is perpendicular to both vectors, has magnitude equal to their parallelogram area, and follows the right-hand orientation. Swapping the order changes its sign. For a=(1,0,0) m and b=(0,2,0) m, the cross product is (0,0,2) m². The z component is 2, and the triangle formed by the vectors has half the parallelogram area, or 1 m².

Parallel vectors have zero cross product, so they cannot define a plane normal by this construction. A normal vector can be scaled by a positive factor without changing its orientation, but a negative factor reverses it. Flux formulas later require either a unit normal with the scalar area element or an oriented area vector that already includes the area factor. Confusing those conventions can multiply the area twice.

The equation 2x−y+2z=6 defines a plane when coordinates are expressed numerically in metres and the coefficients are interpreted consistently. Its normal is n=(2,−1,2), with length 3. The unsigned distance from the origin is |0−6|/3=2 m. A signed distance additionally depends on which normal orientation is chosen. It is useful to distinguish a plane equation from its normalized distance formula: scaling the whole equation does not change the geometric plane.

## Curves and parameters

A spatial curve r(t) has tangent r′(t). Where r′ is nonzero, its unit tangent is T=r′/|r′|. If t is physical time, |r′| is speed. If t is merely a curve parameter, it is length per parameter unit. The traced length over [a,b] is ∫ₐᵇ|r′(t)|dt. This counts repeated traversal and differs from endpoint displacement when the path bends or reverses.

Consider the synthetic helix r(t)=(3 cos t,3 sin t,4t), with coordinates in metres and t a dimensionless parameter. Its derivative is (−3 sin t,3 cos t,4), whose length is √(9+16)=5 m per parameter unit. Over 0≤t≤2 the length is 10 m. The unit tangent's z component is 4/5 at every t. At t=0 the unit tangent is (0,3/5,4/5), while the derivative itself is (0,3,4). Both point in the same direction but carry different magnitude and units.

Reparameterizing with t=2s over 0≤s≤1 doubles the derivative magnitude to 10, while halving the parameter interval. The length remains 10 m. A change of parameter must transform both derivative and bounds. Reversing a traversal changes the tangent orientation and oriented line integrals, while the unsigned traced length remains the same for a single reverse traversal.

## Worked example

For the helix, differentiate all three coordinates rather than treating z as constant. The horizontal contribution to squared speed is 9(sin²t+cos²t)=9, and the vertical contribution is 16. Thus speed is constantly 5 and length over [0,2] is 10. Divide the derivative by 5 to obtain the unit tangent, with vertical component 0.8. For a plane calculation, use the independent normal (2,−1,2), divide its residual by length 3, and obtain an origin-to-plane distance of 2. The same normalization principle supports both calculations, but tangent and plane normal are different geometric objects.

## Common mistakes and checks

Do not call components invariant under rotation. Do not use a nonunit direction in a derivative claimed to be per distance. Do not equate traveled length with the norm of endpoint displacement. Check cross-product order against the chosen right-hand orientation. Verify that dot products of a computed cross product with both original vectors are zero, within numerical precision.

Lengths, areas and normalized directions have different dimensions. A cross product of two length vectors has area units, while a unit tangent is dimensionless. Coordinate differences must use a common scale before the Euclidean norm is meaningful. These checks are especially useful when combining spatial geometry with a rate or flux field.

## Limits of this lesson

All displacements and curves are synthetic teaching constructions. The lesson assumes an orthonormal Cartesian frame and develops selected curve geometry, not a full treatment of curvature, torsion or non-Euclidean metrics. Practice checks numbers and orientation choices rather than a written geometric argument. Original material was developed with substantial AI assistance, using existing scope references without copying third-party text. The package remains partial, unreviewed and formative-only.
