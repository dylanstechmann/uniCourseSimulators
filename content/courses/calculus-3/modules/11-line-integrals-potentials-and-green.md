# Line integrals, potentials and Green's theorem

## Learning objectives

1. Distinguish scalar arc-length integrals from oriented vector work integrals.
2. Calculate potential differences and test when a field is conservative.
3. Relate planar circulation to a curl integral while checking orientation and domain holes.

## Two kinds of path accumulation

For a scalar C on a curve r(t), the arc-length integral is ∫C(r(t))|r′(t)|dt. It weights by nonnegative length. For a vector field F, work or circulation is ∫F(r(t))·r′(t)dt. It weights by directed displacement. Reversing a single traversal preserves the scalar integral but changes the sign of the vector integral. A physical work interpretation also needs compatible force and displacement units.

For the synthetic straight path r(t)=(3t,4t), 0≤t≤1, and scalar C(x,y)=x, the speed is 5 and C=3t. Thus the scalar integral is ∫₀¹15t dt=7.5 in the corresponding scalar-times-length units. Omitting speed would integrate with respect to the parameter instead of distance. Replacing it with an endpoint displacement is valid only if the chosen calculation actually matches this straight one-way path.

## A potential supplies endpoint values

The field F=(2xy,x²) is the gradient of φ=x²y. Along a smooth path, F·r′ is dφ(r(t))/dt by the chain rule. Consequently ∫F·dr=φ(end)−φ(start), independent of the particular path within the potential's domain. From (0,0) to (2,1), the work is 4. Along r(t)=(t,t²) from t=0 to 1, the integrand is 4t³, whose integral is 1, matching the different endpoint potential difference.

Path independence does not mean that all endpoints give the same work. It means that fixed endpoints give the same result across admissible paths. A closed loop in this globally defined potential field has zero circulation. A vector field may also have a potential only on a restricted domain; that domain belongs to the claim.

For a continuously differentiable planar field F=(P,Q), a necessary local condition for a potential is Q_x−P_y=0. On a simply connected open region with the usual smoothness conditions, this condition is also sufficient. A hole can obstruct the global conclusion. “Curl zero” must therefore be paired with domain information, rather than used as a universal path-independence certificate.

## Circulation and Green's theorem

For a positively oriented, simple, closed planar boundary around a suitable region D, Green's circulation theorem gives ∮P dx+Q dy=∬_D(Q_x−P_y)dA, assuming the field is continuously differentiable on an open neighborhood of the region and boundary. Positive orientation means counterclockwise around an ordinary outer boundary so the region stays on the left. Inner boundaries of holes have the opposite orientation under the same left-side convention.

For F=(−y,x), the scalar curl is 2. The counterclockwise unit circle therefore has circulation 2π. Direct parameterization r=(cos t,sin t) gives F·r′=1, integrated from zero to 2π, confirming the result. For the rectangle [0,2]×[0,1], circulation is 2 times area 2, or 4. Reversing orientation negates either answer.

The geometric region used by Green's theorem must match the boundary. A self-crossing curve or a repeatedly traced circle needs an explicitly appropriate treatment; the simple-boundary statement cannot be applied by silently ignoring multiplicity. A finite numerical line integral can be computed for many paths, but that does not establish the hypotheses of a theorem converting it to a region integral.

## A hole changes the conclusion

The vortex field F=(−y/(x²+y²),x/(x²+y²)) is smooth away from the origin and has zero scalar curl there. On the counterclockwise unit circle its work integrand is again 1, so circulation is 2π. This does not contradict Green's theorem: the field is undefined at the origin inside the disk, so its required smoothness neighborhood is missing.

On an annulus excluding the origin, the theorem applies with both outer and inner boundaries. The counterclockwise outer-circle circulation is 2π, while the clockwise inner-circle circulation is −2π, giving net zero, consistent with zero curl throughout the annulus. Omitting the inner boundary would change the region's boundary and break the calculation.

## Worked example

Compare the gradient field (2xy,x²) and rotation field (−y,x). For the first, identify φ=x²y and use endpoint differences, obtaining 4 for (0,0) to (2,1). For the second, a counterclockwise unit circle has curl integral 2 times disk area, or 2π, and a direct parameter calculation agrees. Now change to the vortex field: the circle integral still equals 2π, although local curl is zero away from the origin. The missing origin prevents using the disk as a smooth theorem region. Formula, orientation and domain all contribute to the answer.

## Common mistakes and checks

Do not substitute ds for dr in work, or drop |r′| from a scalar line integral. Do not infer a global potential from zero curl without domain conditions. Specify the loop's orientation and each hole's boundary direction. Check a proposed potential by differentiating every component; matching only one component leaves room for an additional variable-dependent term.

## Limits of this lesson

Fields and curves are synthetic. The lesson develops selected smooth planar examples and a domain counterexample, not every generalized form of Green's theorem. It establishes no physical vortex mechanism or force law. Practice checks selected values and conditions, not proof quality. Original instruction has substantial AI assistance; the package remains partial, unreviewed and formative-only.
