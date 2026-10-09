# Superposition, potential and Gauss-law boundaries

## Learning objectives

1. Add signed vector electric fields and scalar potentials from declared point charges.
2. Relate potential gradients, force and energy with consistent reference conventions.
3. Apply spherical symmetry without confusing zero flux with zero local field.

## Describe sources and observation separately

An electric field belongs to an observation location and a stated source distribution. A test charge experiences force q_test E, but the field is defined before choosing that test charge. Reversing the test charge reverses the force without reversing the field produced by fixed sources. This separation prevents a common sign error when interpreting electron motion.

Use a synthetic vacuum model with rounded Coulomb constant k=9.00×10⁹ N·m²/C². Positions are in metres. Place +2.0 nC at x=−0.10 and −2.0 nC at x=+0.10. At the midpoint, the positive source contributes a rightward field away from itself, and the negative source contributes a rightward field toward itself. Each magnitude is 1800 V/m, so total E_x=+3600 V/m.

Field contributions are vectors; add their components rather than absolute magnitudes by default. The two contributions add here because their directions match. A different charge sign or observation point can make them oppose. The point-charge model is singular at a source position, so the field expression must not be evaluated there as though a finite material charge cloud had been supplied.

## Potential uses a reference

Choose potential zero at infinity for these finite point sources. Each source contributes kq/r, a scalar with the source's sign. At the midpoint the two equal and opposite contributions cancel, giving potential zero. Yet the field is nonzero there. A zero potential value describes a chosen reference comparison, while field depends on spatial change of potential.

Potential difference determines electric work for a fixed-charge electrostatic model: work by the field is q(V_initial−V_final). Potential energy change is q(V_final−V_initial). Positive charge tends toward lower potential under electric force alone, but negative charge has the opposite potential-energy relation. Neither statement determines an actual trajectory if additional forces or constraints are present.

For a separate +3.0 nC source at the origin, at radius 0.30 m potential is 90 V and outward field magnitude 300 V/m with the stipulated k. Increasing radius lowers potential and field with different powers: potential scales as inverse distance, field as inverse squared distance. Their numerical equality at some chosen units would not identify them as the same physical quantity.

## A gradient is a local statement

In a smooth electrostatic region, E=−∇V. In one dimension the negative slope gives the component E_x, not necessarily the total magnitude. For the two-source example, differentiating kq/|x−x_source| in the source-free interval yields the same +3600 V/m midpoint component as direct vector addition. A finite-difference estimate can cross-check it if the interval avoids either singular source.

An equipotential surface permits no electrostatic work along its tangent for a fixed test charge, but field can point normal to that surface. The midpoint's zero potential therefore does not mean a nearby region has zero potential gradient. Likewise, adding a constant to every potential leaves all fields and potential differences unchanged.

At the midpoint a +1.0 nC test charge experiences +3.6 µN in x. A negative test charge of the same magnitude experiences the opposite force. The example assumes the test charge is small enough that the prescribed sources remain unchanged. A real movable conductor can redistribute charge, so that response would require solving a different boundary problem.

## Flux and symmetry

Gauss's law relates electric flux through a closed surface to enclosed net charge. Flux integrates E dotted with the outward area vector; it is not simply the field magnitude multiplied by area for every surface. A surface can enclose zero net charge while field enters through some patches and exits through others. Cancellation of total flux does not establish zero field at every patch.

The [OpenStax Gauss-law section](https://openstax.org/books/university-physics-volume-2/pages/6-3-applying-gausss-law) is a link-only reference for the role of charge-distribution symmetry. The sphere's shape alone is insufficient: unequal charges across hemispheres can break spherical symmetry. Only the declared symmetry allows a common radial field component to be taken outside a spherical flux integral.

For a separate uniformly charged insulating sphere, stipulate total Q=3.0 nC and radius R=0.30 m. At r<R, enclosed charge scales as Q(r/R)³. The radial field is therefore kQr/R³, reaching 150 V/m at r=0.15 m. Outside, it is kQ/r²; the inside and outside formulas agree at r=R. A conducting sphere in electrostatic equilibrium has a different interior distribution and cannot use the uniform-volume formula interchangeably.

## Worked example

Draw a one-dimensional source map and label the observation point before assigning signs. At the midpoint add two rightward 1800 V/m fields, but add +180 and −180 V scalar potentials. Multiply the resulting field by the independently chosen test charge for force. For the separate uniform sphere, calculate enclosed charge first and use the interior expression only within its radius.

## Common mistakes

Do not infer zero field from zero potential or zero net flux. Do not put the test charge into a source-field expression twice, discard component directions or choose a Gaussian surface based only on an object's outline. State potential reference, source domain and charge distribution.

## Limits of this lesson

All charges and geometries are synthetic. Vacuum, fixed-source and electrostatic assumptions do not establish tissue fields or a measurement procedure. The rounded k is a stipulated teaching constant. No source text, problem or figure is imported. Original instruction has substantial AI assistance; qualified review and measured workload remain absent. The package stays partial, unreviewed and formative-only.
