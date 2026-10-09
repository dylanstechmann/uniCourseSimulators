# Geometry, parametric curves and radial amounts

## Learning objectives

1. Set up area, volume and arc-length integrals from geometry and parameter bounds.
2. Use annular area elements to calculate a radial total and area average.
3. Check multiplicity, units and model assumptions before interpreting an integral.

## Build the small element

An integral begins with a small contribution and a limiting sum. A vertical strip between y=x and y=x² on [0,1] has area approximately (x−x²)dx, so the total is 1/6. The top-minus-bottom order follows from the curves on that interval. If their order changes, split the interval rather than allowing signed contributions to cancel when the requested quantity is geometric area.

Rotating y=x², 0≤x≤1, around the x-axis gives disks with radius x² and area πx⁴. The volume is π∫₀¹x⁴dx=π/5. The radius is squared to obtain the disk area; using πx² would rotate a different profile. Washers subtract an inner disk area from an outer one, while shells use circumference times height times thickness. Either method can work, but bounds and dimensions must refer to the chosen slices.

These coordinates are dimensionless in the abstract examples. If x and y describe lengths, specify length scales consistently before interpreting a numerical volume in cubic units. A one-dimensional integral can compute a three-dimensional amount because the cross-sectional factor already contains the other geometric dimensions.

## Parametric motion and arc length

For a smooth planar curve x=x(t), y=y(t), a short displacement has length approximately √((x′)²+(y′)²)dt. Therefore its traced length is ∫√((x′)²+(y′)²)dt over the stated parameter range. The parameter need not be physical time. If it is time, the square-root factor is speed and integrating it gives distance traveled, which can exceed endpoint displacement.

For x=3t and y=4t over 0≤t≤2, speed is 5 in the chosen coordinate scale, so length is 10. The endpoint displacement also equals 10 because the curve is a straight segment traversed once without reversal. A circle x=2 cos t, y=2 sin t has speed 2. From t=0 to π it traces a semicircle of length 2π. Extending the range to 2π gives the full circumference 4π, while extending to 4π traces that same geometric circle twice and gives traveled length 8π.

Parametric area can be computed by ∫y(t)x′(t)dt for appropriately oriented regions, but signs and traversal matter. For x=t² and y=t on [0,1], x′=2t, and the area under the curve from x=0 to x=1 is ∫₀¹2t²dt=2/3. This also follows from y=√x. Omitting x′ would confuse parameter increments with horizontal widths.

## Polar sectors and annuli

A polar sector of small angle dθ and radius r has area approximately r²dθ/2. Thus a region described once by nonnegative r=r(θ) has area (1/2)∫r(θ)²dθ over the proper angular bounds. For constant r=2 and 0≤θ≤π/2, the quarter-disk area is π. Integrating over a wider range changes the swept region or its multiplicity; bounds are part of the geometry.

For a radially symmetric density c(r), a thin annulus at radius r and thickness dr has area approximately 2πr dr. This factor weights outer radii more heavily because they occupy longer circles. The total amount per unit cylinder length, when c is an amount per cross-sectional area, is Q=∫₀ᴿc(r)2πr dr. If c instead denotes a volumetric concentration, the same cross-sectional integral is amount per length and a cylinder length is needed for total amount.

The preserved course case gives c(r)=c₀(1−r²/R²) for 0≤r≤R. The profile is nonnegative, equals c₀ at the center and vanishes at the edge. Its cross-sectional integral is πc₀R²/2. Dividing by area πR² yields an area average c₀/2. The center-value approximation c₀πR² is twice the integral, so it overestimates by 100% relative to the true total, while the true total is 50% of that approximation. Those percentage statements use different denominators and must be distinguished.

## Worked example

Use synthetic R=2 cm and c₀=6 arbitrary amount units per cm². Then Q=∫₀²6(1−r²/4)2πr dr. Integrate 12π(r−r³/4) to obtain 12π[r²/2−r⁴/16]₀²=12π, about 37.699112 amount units. The disk area is 4π cm², giving average density 3 amount units per cm². The center-density shortcut gives 24π amount units and doubles the correct total. An unweighted radial average would answer a different question because each radius would receive equal weight despite occupying unequal area.

The same calculation can be checked by changing variable s=r²/R². Then 2r dr=R² ds, and Q=πc₀R²∫₀¹(1−s)ds. This gives the same half factor and reveals why normalizing the radius simplifies the shape dependence. It also verifies the annular Jacobian without repeating the original polynomial integration.

## Common mistakes and checks

Do not integrate c(r)dr and call the result a disk amount. Its units and weighting differ. Do not insert a cylinder length unless the requested quantity and concentration units require it. Confirm that a parametric curve is traced the intended number of times. For nonnegative density bounded by c₀, the integral cannot exceed c₀ times area, which supplies a useful scale check.

## Limits of this lesson

The radial profile, geometries and numerical values are synthetic. They do not establish a tissue distribution, experimental sampling protocol or biological transport mechanism. More general surfaces and multivariable Jacobians belong to Calculus III. The case remains a public self-assessment checklist; practice does not grade written reasoning or certify mastery. Original content was developed with substantial AI assistance. The package remains partial, unreviewed and formative-only.
