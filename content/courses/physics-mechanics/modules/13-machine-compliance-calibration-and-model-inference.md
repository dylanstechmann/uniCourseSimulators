# Machine compliance, calibration and model inference

## Learning objectives

1. Separate baseline displacement, machine compliance and specimen elongation in a stated series model.
2. Convert a corrected specimen stiffness to a geometry-defined modulus.
3. Compare orientation claims using independent calibration and explicit uncertainty limits.

## The observed displacement has a model

An actuator or crosshead can move while both the machine and specimen deform. In a synthetic series model, report displacement d_rep=d₀+C_mF+F/k_s, where d₀ is an additive reporting offset, C_m is machine compliance and k_s specimen stiffness. All series elements share the same force under the stated quasistatic constraint. The two force-dependent displacement terms add; their stiffnesses do not add as though they were parallel.

Take synthetic k_s=1000 N/m, C_m=0.0010 m/N and d₀=0.0020 m. At force F=0.30 N, machine displacement is 0.00030 m and specimen elongation 0.00030 m. Reported total is 0.00260 m, or 2.60 mm. Subtracting only the zero-load offset leaves both physical deformation terms, not a pure specimen displacement.

## Intercept and slope answer different questions

A zero-load observation constrains d₀ in this stipulated model. The slope of reported displacement versus force is C_total=C_m+1/k_s=0.0020 m/N. Its reciprocal is apparent stiffness 500 N/m. Removing a constant offset changes the intercept but leaves that slope unchanged. A calibrated origin alone therefore does not correct the series-compliance bias.

An independently characterized reference with known specimen compliance C_ref can instead give reference slope C_m+C_ref. Subtract C_ref to infer C_m. The virtual lab stipulates an ideal zero-compliance reference, but an actual finite reference would need its own compliance value. Calling a reference “stiff” does not justify setting its deformation to zero at every accuracy.

For the example, reference slope 0.0010 m/N identifies the machine term. Subtract it from total slope 0.0020 for specimen compliance 0.0010, then invert for k_s=1000 N/m. At 0.30 N, specimen elongation is 0.30 mm. An inferred negative specimen compliance after subtraction is not a negative ordinary tensile spring stiffness in this passive model; it flags incompatible assumptions, calibration or observations.

## Geometry converts stiffness to modulus

With the stipulated uniform axial gauge length L₀=0.020 m and initial area A₀=1.0×10⁻⁶ m², corrected modulus is E=k_sL₀/A₀=20 MPa. Using apparent stiffness 500 N/m instead gives 10 MPa. The difference is caused by the known series measurement construction, not a changed material parameter. The specimen strain at the chosen load is 0.00030/0.020=0.015 under the assigned linear interval.

Geometry itself can be uncertain or nonuniform. If the area convention differs, the inferred modulus differs even with identical force and displacement. A modulus estimate from a corrected stiffness requires the same uniform axial and gauge assumptions used in deriving E=kL/A. It is not automatically a full multiaxial material characterization.

## Directional differences can survive correction

The synthetic lab supplies two orientations of an invented linear specimen with shared L₀=20 mm and A₀=1 mm². Their assigned stiffnesses are 2000 and 1000 N/m, so corrected moduli are 40 and 20 MPa. A shared machine compliance 0.00050 m/N compresses their apparent stiffness ratio from two to one and a half. Correcting that common term recovers the stipulated directional difference rather than removing it.

The example shows that a real mechanical difference and a measurement bias can coexist. Neither “all instrument error” nor “all material behavior” follows from two raw slopes alone. Independent reference information and geometry provide distinguishing constraints. In a real tissue, recruitment, nonlinear response, rate dependence or changing boundary conditions could also affect an orientation comparison.

## Inference can be sensitive

Specimen compliance is a difference of measured or inferred slopes. When machine compliance dominates, that difference can be small, making its relative uncertainty large. Inverting it for stiffness magnifies the consequence. A visually straight total-displacement plot does not establish precise specimen stiffness, because a straight line is compatible with many partitions of the same total compliance.

For example, doubling specimen stiffness with a fixed machine compliance halves only the specimen term, not the entire observed displacement. In the limit of an infinitely stiff specimen, apparent stiffness approaches 1/C_m rather than infinity. That limiting case is a useful test of a proposed correction formula. In the limit C_m→0, apparent and specimen stiffness coincide.

An additive offset can also vary between groups or drift with time. The present construction assumes one shared offset and compliance; balanced repeats do not establish those conditions for a real system. A one-dimensional calibration cannot remove every possible grip slip, force-channel gain, geometry error or nonlinear machine response.

## Evidence for the preserved case

The preserved tendon self-assessment case asks for orientation, geometry, hydration, temperature, strain rate and modulus definition. The lab addresses only a subset: fixed geometry, assigned orientation and a declared linear machine/reference model. It does not validate an actual tendon experiment or prove that a direction-dependent apparent modulus has one universal cause.

Discussion should separate what was supplied independently from what was fitted to the same observations. The reference supplies machine information under a stipulated zero-compliance assumption; specimen slopes then supply corrected directional stiffness. Reporting more digits cannot replace missing calibration or specimen metadata. These distinctions connect the earlier force, energy and material models to the observation used to test them.

## Worked example

At 0.30 N, add offset 2.0 mm, machine elongation 0.30 mm and specimen elongation 0.30 mm for reported 2.60 mm. Fit total compliance independently of the intercept, subtract the known reference contribution to obtain machine compliance and remove it before inversion. Convert corrected 1000 N/m to 20 MPa with the stated geometry, versus apparent 10 MPa. In the separate lab orientation pair, recover the two-to-one corrected ratio while preserving the shared reporting terms.

## Common mistakes

Do not add series stiffnesses, treat an intercept correction as a slope correction or assume a finite reference is perfectly rigid without a declared model. Check positive corrected compliance, consistent geometry and sensitivity before interpreting a modulus. A residual difference after calibration is not automatically a uniquely identified material cause.

## Limits of this lesson

All dimensions, compliances, orientations and reports are synthetic. Quasistatic, uniform axial and linear assumptions do not establish an actual testing frame, tendon property or validated measurement method. No apparatus or biological experiment procedure is supplied. Original instruction has substantial AI assistance. The course remains partial, unreviewed and formative-only.
