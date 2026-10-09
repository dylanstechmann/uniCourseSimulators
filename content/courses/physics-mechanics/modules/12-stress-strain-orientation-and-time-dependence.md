# Stress, strain, orientation and time dependence

## Learning objectives

1. Calculate engineering stress, strain and a declared linear modulus from specimen geometry.
2. Solve a stipulated spring–dashpot stress or creep balance with matching units.
3. Distinguish orientation, time dependence, measurement geometry and modulus definitions.

## Force and displacement are not material properties

A specimen's stiffness relates force to elongation for a supplied geometry and loading condition. Engineering tensile stress divides axial force by the initial cross-sectional area A₀, while engineering strain divides specimen elongation by initial gauge length L₀. A linear relation σ=Eε then gives E=kL₀/A₀ for a uniform axial model. Changing geometry can change stiffness without changing the assigned modulus.

For synthetic F=10 N, A₀=2.0×10⁻⁶ m², L₀=0.020 m and specimen elongation 0.00020 m, engineering stress is 5.0 MPa and strain 0.010. Their ratio is E=500 MPa. These values are a constructed calculation, not measured properties of an actual polymer or tendon. They assume uniform axial loading and a valid linear interpretation over the stated interval.

The [OpenStax stress/strain section](https://openstax.org/books/university-physics-volume-1/pages/12-3-stress-strain-and-elastic-modulus) is a link-only reference for the basic definitions. Stress units are pressure units, whereas strain is dimensionless. A value in percent must be converted to a fraction before forming E. Dividing 5 MPa by the displayed percent value one rather than 0.010 would understate the modulus by a factor of one hundred.

## Specify the deformation measure

Engineering stress uses initial area; a true stress uses an appropriate current area. Engineering strain uses initial gauge length; other finite-deformation measures differ when extension is large. The current example supplies the initial geometry and a small modeled strain, without a measured current area. It therefore does not claim a true-stress curve or a universal large-strain modulus.

A slope at one point is a tangent modulus, a ratio from a chosen reference is a secant modulus, and a fitted slope over an interval is another explicitly defined estimate. They can differ in a nonlinear material. Calling all three “the modulus” without specifying interval and reference can create apparent contradictions between laboratories that used different definitions.

Crosshead or actuator displacement may include deformation in grips and the testing frame. Dividing that total by L₀ does not automatically yield specimen strain. The next lesson and virtual lab introduce a series-compliance model to demonstrate this measurement distinction rather than blaming every orientation difference on instrument error.

## A parallel spring–dashpot construction

To represent a restricted time-dependent model, place an ideal linear spring and an ideal linear viscous element in parallel in the scalar stress relation σ=Eε+η dε/dt. η has units Pa·s, so both terms have stress units. This is a stipulated constitutive equation for a teaching system, not a claim that a particular tissue follows it.

Take synthetic E=100000 Pa and η=50000 Pa·s. At strain ε=0.020 and strain rate 0.010 s⁻¹, stress is 2000+500=2500 Pa. The viscous contribution depends on rate while the elastic term depends on current strain. Two tests at equal strain but different rates can therefore report different stresses within this selected model even with identical E.

Under a suddenly imposed constant stress σ₀=3000 Pa with initial strain zero, the equation gives dε/dt=(σ₀−Eε)/η. Its time constant is τ=η/E=0.50 s and asymptotic strain σ₀/E=0.030. At t=τ, strain is 0.030(1−exp(−1))≈0.018964. The response approaches its limit rather than jumping instantaneously to the elastic ratio.

The ideal discontinuous stress step is a mathematical input, not an apparatus command. A real loading ramp, inertia or additional modes can change the early response. This simple parallel model also has restricted relaxation behavior under imposed strain and cannot be used interchangeably with every series spring–dashpot model merely because both include a spring and a viscous element.

## Orientation needs a declared model

In an orientation-dependent material, stiffness or modulus can differ along different directions. Fiber recruitment or structural arrangement can also change the response with strain. The preserved tendon case asks why a direction-dependent apparent modulus need not be a measurement error. A generic scalar E represents one selected orientation and condition, not a complete anisotropic constitutive law.

Supplying two directional linear moduli for a synthetic comparison does not specify all shear, coupling or transverse responses. A full anisotropic model needs more components and symmetry assumptions. Similarly, one fitted creep time does not identify every relaxation mechanism. Independent orientation and geometric metadata constrain interpretation without pretending the selected equations are comprehensive.

At minimum, compare initial dimensions, gauge region, orientation, hydration/temperature conventions, preload, loading history, rate and the definition of the reported modulus. The need for that metadata does not prescribe a biological experiment here. It states which quantities would have to be comparable before attributing a numerical difference to one material parameter.

## Worked example

Divide 10 N by 2.0×10⁻⁶ m² for 5 MPa, then divide 0.00020 by 0.020 for strain 0.010 and form 500 MPa. For the independent spring–dashpot construction, add Eε and η times strain rate for 2500 Pa. Under the stipulated constant stress, solve the first-order balance for τ=0.50 and limiting strain 0.030, then evaluate its fraction at one time constant. Keep geometry-based stiffness, orientation and time-dependent model parameters distinct.

## Common mistakes

Do not use percent strain as a decimal fraction, mix current and initial geometries without a definition or treat actuator motion as specimen elongation automatically. Do not infer a full anisotropic or viscoelastic model from one scalar slope or time constant. State conditions before comparing reported moduli.

## Limits of this lesson

All geometry, stresses and constitutive parameters are synthetic. The selected scalar laws establish no actual tendon modulus, failure threshold or biological recommendation. Qualified subject-matter and accessibility review and workload measurement remain absent. Original instruction has substantial AI assistance. The package remains partial, unreviewed and formative-only.
