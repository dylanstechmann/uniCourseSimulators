# Virtual lab 1: machine compliance and orientation-dependent stiffness

**Status:** public formative practice with public answers and unlimited retries. Points are study feedback, not course grades. This exercise interprets constructed data; it supplies no specimen preparation, testing procedure or actual experimental result. Prerequisites: free-body diagrams, stress/strain definitions and the series-compliance lesson.

## Learning objectives

1. Summarize grouped displacement reports and distinguish an additive baseline from a compliance slope.
2. Use an independently specified reference to recover machine compliance and specimen stiffness.
3. Evaluate orientation comparisons, passive-model feasibility and the information still needed by the preserved tendon case.

## Model and independently supplied information

Consider two abstract specimen orientations A and B in a hypothetical force/displacement reporting system. Force is supplied as exact for this exercise. Reported displacement includes an additive offset, machine deformation and specimen deformation: d_report=d₀+C_mF+F/k_s. Both elastic parts carry the same force in this series model. Their compliances add, whereas stiffness is the reciprocal of total compliance.

The construction uses d₀=0.001 m and common machine compliance C_m=0.0005 m/N. Orientation A has specimen stiffness 2000 N/m and B has 1000 N/m. These declared construction values explain the public worked answers; the learner recovers them from the report slopes and supplied reference information. They are not measurements of a particular tissue, equipment assembly or material.

An independent ideal reference has zero specimen compliance over the stated force range. Its measured slope therefore equals machine compliance. A real reference would have finite deformation and require an independently known reference compliance. Treating its entire slope as machine compliance would overcorrect the specimens. The ideal reference is a mathematical assumption rather than a claim that a real object cannot deform.

Independently supplied specimen geometry is initial gauge length L=0.020 m and initial area A₀=0.000001 m² for both orientations. With the stipulated linear specimen response, corrected moduli E=k_sL/A₀ are 40 MPa and 20 MPa. At maximum force 0.40 N, specimen extensions are 0.00020 m and 0.00040 m, giving strains 0.010 and 0.020. The model declares that these values remain in its linear domain. No physical material's allowable strain follows from that declaration.

## Data dictionary and report construction

[Download the synthetic CSV](https://raw.githubusercontent.com/dylanstechmann/uniStemCourseSimulators/main/content/courses/physics-mechanics/labs/compliance-reports.csv). The file contains 27 rows. `sample` is the nine-group code, `orientation` is a, b or ref, `force_n` is the supplied force in newtons, `replicate` identifies a constructed report and `reported_displacement_mm` is raw displacement in millimetres.

| Sample | Orientation | Force (N) | Mean raw displacement (mm) |
|---|---|---:|---:|
| a00 | a | 0.00 | 1.000 |
| a02 | a | 0.20 | 1.200 |
| a04 | a | 0.40 | 1.400 |
| b00 | b | 0.00 | 1.000 |
| b02 | b | 0.20 | 1.300 |
| b04 | b | 0.40 | 1.600 |
| ref00 | ref | 0.00 | 1.000 |
| ref02 | ref | 0.20 | 1.100 |
| ref04 | ref | 0.40 | 1.200 |

Each group mean has three report variants with offsets −0.010, zero and +0.010 mm. Their average equals the central value by design. These deterministic variants are not independently sampled measurements and provide no evidence of Gaussian noise, precision or actual confidence intervals. All groups use the same deliberately balanced pattern. Retaining raw values in the summary makes the baseline and force-dependent terms visible before correction.

## Work sequence

Open Practice gradebook and select **Virtual lab 1: machine compliance and orientation-dependent stiffness (ungraded practice)**. Upload exact columns `sample,replicates,mean_displacement_mm` with all nine sample codes. The software checks nine counts and nine arithmetic means, with 0.005 mm tolerance for each mean. It does not automatically grade a written regression, uncertainty budget, free-body drawing or biological explanation.

First calculate each raw arithmetic mean. Use the zero-force reference mean to identify d₀. Next compare reference means at 0 and 0.40 N: their difference divided by force difference is a displacement/force slope. Because reference compliance is stipulated zero, this is C_m. A constant baseline disappears in the difference, but machine deformation remains until its slope is explicitly subtracted.

Then estimate the total compliance for each orientation from its displacement differences over the same force interval. Subtract C_m to recover specimen compliance. Convert millimetres per newton to metres per newton before inverting for stiffness in newtons per metre. Check that the corrected compliance is positive within this passive elastic model. Finally use the independently supplied geometry to convert specimen stiffness to a modulus and compare matched orientations.

## Worked example

The reference means at 0 and 0.40 N are 1.0 and 1.2 mm. Baseline is therefore 1.0 mm, and C_m=(1.2−1.0)/0.40=0.5 mm/N. Orientation A's total slope is (1.4−1.0)/0.40=1.0 mm/N; subtracting 0.5 gives 0.5 mm/N specimen compliance. Conversion yields 0.0005 m/N, whose inverse is 2000 N/m.

Orientation B's total slope is (1.6−1.0)/0.40=1.5 mm/N. Subtraction gives 1.0 mm/N or 0.001 m/N, whose inverse is 1000 N/m. Ignoring machine compliance gives apparent stiffnesses 1000 and approximately 666.667 N/m. Their ratio is 1.5 rather than the corrected ratio 2. A common machine contribution therefore changes the magnitude of the comparison even when its value is identical for both orientations.

## Interpretation criteria

| Criterion | Evidence to discuss |
|---|---|
| Summary | Nine groups, three reports each and correct raw means |
| Baseline | Zero-force intercept separated from force-dependent slope |
| Reference | Independently stipulated reference compliance applied |
| Series model | Equal force and additive compliances justified |
| Geometry | Gauge length, area and specimen extension distinguished |
| Case scope | Orientation, hydration, temperature, loading rate and history recorded |

The preserved tendon case asks why an apparent modulus can change with pull direction and what metadata support comparisons between laboratories. This synthetic lab demonstrates one observation bias and a conditional residual contrast. It does not decide whether a real contrast arises from fiber recruitment, nonlinear behavior, viscoelasticity, gripping, geometry or another mechanism. A calibrated observation model is useful evidence, but it is not complete material identification.

## Limits of this lesson

The common linear machine compliance, exact forces, ideal reference, matched geometry and positive linear specimen stiffnesses are supplied assumptions. Real data could require force calibration, reference uncertainty, nonlinear machine response, slipping or rate-dependent constitutive models. Negative corrected compliance would flag incompatibility with the stated model or inputs rather than establish negative passive stiffness. As machine compliance approaches zero, apparent stiffness approaches specimen stiffness; an infinitely stiff specimen instead leaves apparent stiffness limited by the machine. Original guide and CSV are CC BY 4.0 with substantial AI assistance. No third-party dataset or teaching asset was copied. This single data lab is not a laboratory sequence; workload, accessibility and qualified subject-matter review remain outstanding.
