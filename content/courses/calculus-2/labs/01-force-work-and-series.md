# Virtual lab 1: force integration, geometric tails and sensor offset

**Status:** public formative practice with unlimited retries. Points are feedback, not a course grade. All observations and model values are constructed. Prerequisites are the lessons on integration methods, sampled accumulation and power-series domains.

## Learning objectives

1. Summarize synthetic readings and calculate work using trapezoidal and Simpson rules.
2. Integrate a geometric force approximation and bound its remaining positive tail.
3. Separate systematic offset, sampling, rounding and series-truncation effects.

## Scenario and data dictionary

An abstract actuator model has force F(x)=10x/(1−0.2x) N on 0≤x≤2 m, with x entered numerically in metres. The coefficient 10 represents 10 N/m and 0.2 represents 0.2 m⁻¹; hence the denominator is dimensionless. A synthetic sensor adds a known constant 1 N offset. At each of five positions, F(x)+1 is rounded to four decimal places and three readings are placed at this central value minus 0.05 N, the central value itself and the central value plus 0.05 N. The offsets deliberately balance; they are not random independent observations or evidence for a real noise law.

[Download the synthetic CSV](https://raw.githubusercontent.com/dylanstechmann/uniStemCourseSimulators/main/content/courses/calculus-2/labs/force-samples.csv). Column `position` is the stable group code p0 through p4, `metres` is displacement, `replicate` identifies a constructed reading, `force_N` is force including offset, and `offset_N` is the independently supplied exact offset. Repeated replicate identifiers do not establish independent experiments. CSV values define the sampled numerical-rule answers; the exact generating formula defines the separate mathematical series answers.

| Position | Metres | Readings | Mean raw force (N) | Mean minus offset (N) |
|---|---:|---:|---:|---:|
| p0 | 0.0 | 3 | 1.0000 | 0.0000 |
| p1 | 0.5 | 3 | 6.5556 | 5.5556 |
| p2 | 1.0 | 3 | 13.5000 | 12.5000 |
| p3 | 1.5 | 3 | 22.4286 | 21.4286 |
| p4 | 2.0 | 3 | 34.3333 | 33.3333 |

## Work sequence

Open Practice gradebook and select **Virtual lab 1: force integration, geometric tails and sensor offset (ungraded practice)**. Group rows by position and upload the exact header `position,replicates,mean_force` with the five group codes. The upload checks five counts and five mean raw forces, using a 0.005 N mean tolerance. It does not grade a written uncertainty discussion. Verify that each group has three rows before averaging.

Subtract the known offset from each mean and use the equally spaced positions with h=0.5 m. Composite trapezoids give T=h[F₀/2+F₁+F₂+F₃+F₄/2]. Composite Simpson gives S=(h/3)[F₀+4F₁+2F₂+4F₃+F₄]. There are four panels, an even number as required for these Simpson weights. Work has units N·m, equivalent to J. Keeping the offset would add its integral, 1 N×2 m=2 J, to either rule. Averaging repeats does not remove a common offset.

Next expand the exact rational force: F(x)=10xΣ_(n=0)∞(0.2x)ⁿ. On the whole integration interval, 0≤0.2x≤0.4<1. The expansion therefore converges there, and its tail can be uniformly bounded. Include indices zero through three and integrate each polynomial term. These four terms produce W₃=20+16/3+1.6+0.512 J. Do not confuse geometric index three with force-polynomial degree three: multiplying by x shifts the last force power to degree four.

The exact remaining force is 10x(0.2x)⁴/(1−0.2x). It is nonnegative. Since the denominator is at least 0.6, its integral is bounded above by (10×0.2⁴/0.6)∫₀²x⁵dx. This is a series-truncation certificate for the exact model. It does not include sensor offset uncertainty, physical-model mismatch or the sampling error in T or S.

## Worked calculation

The corrected CSV means give trapezoidal work 28.075425 J and Simpson work 27.711683 J. The exact rational primitive is −50x−250 ln(1−0.2x), with the chosen units carried by its coefficients. Evaluate it from zero to two to obtain −100−250 ln 0.6=27.706406 J. This value is a reference from the constructed model, not a separately measured work observation.

The integrated four-term geometric approximation gives 27.445333 J. Its exact error is 0.261073 J, positive because all omitted terms are positive on this interval. The integrated tail bound is 0.284444 J and contains that error. The Simpson estimate is close to the exact construction, but closeness here does not validate a real actuator model. The trapezoidal estimate is high, consistent with positive curvature of the exact force. Four-decimal input rounding is an additional small effect that should be identified separately.

## Discussion criteria

| Criterion | Evidence to discuss |
|---|---|
| Data summary | Position grouping, three readings per group and arithmetic means |
| Numerical work | Offset correction, proper endpoint weights, panel spacing and J units |
| Series validity | Dimensionless 0.2x, interval wholly inside radius 5 m and correct final index |
| Error certificate | Positive tail, lower denominator bound 0.6 and integration of the bound |
| Interpretation | Separate mathematical reference, constructed observations and real model validation |

These criteria support discussion; the software checks selected numbers and choices, not a written derivation. If the offset were estimated rather than known exactly, its uncertainty would influence every corrected point and the integrated work. Increasing replicate count could reduce some random effects under justified assumptions, but would not automatically remove a shared calibration error.

## Limits and provenance

The force curve has a pole at x=5 m. It is intentionally used only over [0,2] and supplies no claim about physical behavior near that pole. Extending the geometric expansion beyond its radius is invalid even though a finite truncation remains a polynomial. No actual device specification, experiment, independent noise distribution or experimental protocol is established. This single virtual lab is not a laboratory sequence. Original lab and synthetic CSV are CC BY 4.0 with substantial AI assistance. Existing source references supply scope; no third-party dataset or teaching text was reproduced. The package remains partial, unreviewed and formative-only.
