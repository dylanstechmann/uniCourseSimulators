# Virtual lab 1: oriented boundary flux and a steady volume balance

**Status:** public formative practice, with unlimited retries and public answers. Points are study feedback, not a course grade. All observations are constructed. Prerequisites are the lessons on surface flux, divergence and spatial balance signs.

## Learning objectives

1. Summarize signed outward-normal densities and calculate area-weighted net transfer.
2. Compare boundary and divergence integrals, then use explicitly stated steady assumptions.
3. Explain orientation, shared calibration effects and limits of sink identification.

## Scenario and units

A fixed rectangular region occupies 0≤x≤2 m,0≤y≤1 m,0≤z≤1 m. It has volume 2 m³. A synthetic concentration field is C=10+x²+1.5y²+2z² in arbitrary amount/m³ units when coordinates are inserted numerically in metres. The quadratic coefficients carry the corresponding concentration per squared-length units. With constant scalar diffusivity D=1 m²/s, the constructed flux is J=−D∇C=(−2x,−3y,−4z) amount/(m²·s), with the coefficients interpreted consistently.

The field is smooth and has divergence −9 amount/(m³·s). A steady version with no volumetric source can be paired with uniform sink 9 in the same units. This source/storage assumption is supplied for the exercise. The concentration and flux do not establish actual tissue oxygen demand or a biological mechanism.

At each face the true outward-normal component is constant. A synthetic reporting system adds a known +1 amount/(m²·s) offset to that signed normal density. Three readings are then placed at the central reported value minus 0.1, the central value and the central value plus 0.1. The offsets deliberately balance. They are not independent random experiments or evidence for a Gaussian error distribution.

## Data dictionary and geometry

[Download the synthetic CSV](https://raw.githubusercontent.com/dylanstechmann/uniStemCourseSimulators/main/content/courses/calculus-3/labs/boundary-flux.csv). Column `face` is the stable group code. `nx,ny,nz` give the outward unit normal. `area_m2` is face area in m²; `replicate` identifies a constructed reading; `normal_flux` is the signed reported normal density in amount/(m²·s), including calibration offset; `offset` is that known offset in the same units. These are already normal components, so do not apply an additional normal-vector sign to them.

| Face | Outward normal | Area (m²) | Raw mean density | Corrected density | Corrected transfer (amount/s) |
|---|---|---:|---:|---:|---:|
| x0 | (−1, 0, 0) | 1 | 1.0 | 0.0 | 0.0 |
| x2 | (1, 0, 0) | 1 | −3.0 | −4.0 | −4.0 |
| y0 | (0, −1, 0) | 2 | 1.0 | 0.0 | 0.0 |
| y1 | (0, 1, 0) | 2 | −2.0 | −3.0 | −6.0 |
| z0 | (0, 0, −1) | 2 | 1.0 | 0.0 | 0.0 |
| z1 | (0, 0, 1) | 2 | −3.0 | −4.0 | −8.0 |

The two x faces each have area 1. Each y or z face has area 2. Their total boundary area is 10 m². The zero-coordinate faces have zero true normal density because the corresponding component of the linear field vanishes there. They still belong to the physical boundary and to the calibration calculation.

## Work sequence

Open Practice gradebook and select **Virtual lab 1: oriented boundary flux and a steady volume balance (ungraded practice)**. Group rows by `face` and upload a summary with exact columns `face,replicates,mean_normal_flux` and six row codes x0,x2,y0,y1,z0,z1. The upload checks six counts and six raw arithmetic means, with mean tolerance 0.005 in the stated density scale. It does not evaluate a written report.

First calculate Q_raw=Σarea×mean_normal_flux. Retain the signs; summing magnitudes would compute an unsigned crossing measure instead of net outward transfer. Second subtract the known density offset from every mean and calculate Q_corrected using the same areas. Third compare it with divergence −9 times volume 2. Finally use storage balance dM/dt=integrated source minus sink minus Q_out. Under the supplied steady and zero-source assumptions, solve for a uniform sink.

For a prediction task, enlarge only the x extent to 3 m while retaining the same exact field. Its divergence remains −9 and volume becomes 3, predicting outward transfer −27 amount/s. A separate boundary calculation gives contributions −6,−9,−12 on the positive-coordinate faces. This prediction is a mathematical consequence of the stipulated field, not an observation that validates it.

## Worked calculation

The raw face means are 1,−3,1,−2,1,−3. Their area-weighted sum is −8 amount/s. Subtracting the offset gives densities 0,−4,0,−3,0,−4 and transfer −18 amount/s. The correction changes transfer by 10 amount/s, exactly offset times total boundary area. Inward supply is therefore 18 under the outward-normal convention.

The divergence-volume calculation gives −9×2=−18, matching the boundary sum. At steady state with no source, 0=−2r−(−18), so r=9. If storage were changing or a source were present, this sink would not follow from boundary transfer alone. The theorem relates integrals of the supplied smooth field; conservation and the source/storage assumptions support the additional sink interpretation.

## Discussion criteria

| Criterion | Evidence to discuss |
|---|---|
| Summary | Face grouping, three readings per group and signed arithmetic means |
| Geometry | All six normals, unequal areas and a closed outward boundary |
| Transfer | Corrected density times area, with negative outward rate interpreted as inward supply |
| Balance | Fixed volume, source/storage assumptions and rate versus volumetric-rate units |
| Uncertainty | Shared offset effect and distinction between construction and real inference |

These criteria guide discussion; numeric and structured checks do not grade written proofs. A common estimated offset can correlate errors across face means. Averaging more repeats may reduce some random effects under justified assumptions but does not automatically remove a shared calibration error. Nonuniform normal density would require surface integration or a justified quadrature, rather than one constant mean times area.

## Limits and provenance

The box, field and repeats are synthetic and unusually orderly. No real sensor calibration, tissue uptake parameter, experimental protocol or uniform-sink identification is established. An irregular real boundary would require its own geometry and normal fields; a singular interior field could invalidate the ordinary theorem. One virtual lab is not a laboratory sequence. Original lab and CSV are CC BY 4.0 with substantial AI assistance. Existing multivariable and transport references provide scope only; no third-party data or teaching text was reproduced. The package remains partial, unreviewed and formative-only.
