# Noise bandwidth, covariance and uncertainty

## Learning objectives

1. Convert a supplied amplitude noise density into RMS noise using a stated bandwidth model.
2. Propagate selected correlated or independent contributions without confusing variance and amplitude.
3. Evaluate calibration uncertainty, repeatability and unsupported confidence claims.

## Density is not total noise

An amplitude spectral density in volts per square root hertz is not already an RMS voltage. Under a declared one-sided power spectral density, output noise variance is the integral from zero to positive infinity of spectral density squared times squared transfer magnitude. The square and the frequency convention matter: adding amplitude densities as though they were variances changes the result.

Stipulate a synthetic white input amplitude density e_n=6 nV/√Hz and a unity-DC-gain first-order low-pass with cutoff f_c=100 Hz. Its squared magnitude is 1/[1+(f/f_c)²]. The equivalent noise bandwidth is the integral of that squared magnitude, πf_c/2≈157.079633 Hz. It exceeds the cutoff because the gradual response passes noise above f_c rather than stopping there abruptly.

Input-referred RMS after that selected filter is 6√157.079633≈75.198848 nV. A stated constant signal/noise gain of 20 over the modeled band gives output RMS approximately 1.503977 µV. These values are independent constructed parameters, not measured specifications for an actual amplifier or tissue signal. A different gain-versus-frequency relation would need to remain inside the variance integral.

The mathematical one-pole formula integrates a tail to infinity. Real spectra, additional poles and bandwidth limits require their own characterization. A low-frequency excess-noise component cannot be described by the white-density constant merely because one datasheet number is available. Likewise, a density quoted at one frequency does not establish that density everywhere.

## Variances add conditionally

For independent zero-mean contributions with RMS values 3 and 4 µV, combined RMS is √(3²+4²)=5 µV. Directly adding 3+4 gives a different, conservative amplitude bound rather than the independent standard-deviation result. The choice of combination depends on what the numbers represent, not only on their units.

If correlation coefficient is ρ=0.50 instead, variance of their sum is 3²+4²+2ρ×3×4=37 µV². RMS is √37≈6.082763 µV. For their difference, the covariance term changes sign and variance becomes 13 µV². Shared disturbances can therefore reinforce or cancel depending on how channels are combined.

Correlations are not established merely because two numbers were recorded simultaneously. Nor are independently labeled replicates necessarily independent physical preparations. The new lab's balanced variants deliberately reproduce a construction; their count does not justify estimating a real noise law. An uncertainty model needs a defensible account of shared sources and how observations were generated.

## A calibration is a measurement equation

Suppose a separate affine sensor relation is V=gx+b. Inversion gives x=(V−b)/g. With V=2.10 V, b=0.10 V and g=0.50 V per x unit, the inferred x is 4.00 units. Small uncertainties propagate through sensitivities ∂x/∂V=1/g, ∂x/∂b=−1/g and ∂x/∂g=−(V−b)/g², evaluated at the supplied operating point.

Stipulate independent standard uncertainties u_V=0.020 V, u_b=0.010 V and u_g=0.005 V per unit. The three magnitude contributions are 0.040,0.020 and 0.040 x units. Their quadrature sum is 0.060 units. This first-order result includes uncertainty in the calibration parameters rather than treating a fitted slope and intercept as exact by default.

The [NIST combined-standard-uncertainty guidance](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-5-combined-standard-uncertainty) is a link-only reference for measurement-equation sensitivity and covariance concepts. The parameters and arithmetic here are original teaching constructions. No NIST table, example or prose was imported, and an illustrative calculation is not a calibrated real instrument.

If fitted gain and offset are correlated, covariance terms must join the linear propagation. Ignoring them can understate or overstate uncertainty. Close to zero gain, inversion becomes sensitive and the small-error approximation may fail. A nonlinear, clipped or strongly uncertain relation can need a more complete treatment than this local linearization.

## Resolution, uncertainty and bias

Resolution describes a reporting increment; repeatability describes dispersion under specified repeated conditions; standard uncertainty describes an assigned uncertainty in a result under its model. A known bias correction changes the estimate, while uncertainty in that correction remains in the uncertainty budget. These quantities can coexist and should not be collapsed into one number of displayed digits.

A stable common offset does not average away when all observations share it. More repeats can reduce an independent random contribution under suitable assumptions while leaving shared calibration uncertainty largely unchanged. Reporting the standard error of constructed variants as total instrument accuracy would omit the measurement equation and shared sources.

Standard uncertainty is not automatically a hard worst-case bound or a 95% interval. Coverage statements require a distributional model or appropriate coverage method and the relevant degrees of freedom or assumptions. The synthetic examples supply standard uncertainties for algebraic practice, without a real coverage claim. A small propagated number also does not prove the model omitted no important effect.

## Worked example

Integrate squared first-order response for equivalent noise bandwidth, then multiply its square root by the supplied density. Apply the declared constant gain to RMS, not to variance without squaring. Combine 3 and 4 µV first under independence and then under ρ=0.5 to expose the covariance term. For the separate affine inversion, compute all three sensitivities and recover 0.060 x units.

## Common mistakes

Do not treat cutoff as an abrupt bandwidth, add independent RMS contributions linearly or infer independence from labels. Do not ignore gain/offset uncertainty, turn standard uncertainty into a guaranteed bound or assume displayed resolution demonstrates accuracy. State spectral, covariance and measurement-equation assumptions.

## Limits of this lesson

Every density, bandwidth, gain and uncertainty is synthetic. Selected white-noise and local-linear models do not certify a real instrument's precision or coverage. No hardware procedure is supplied. Original instruction has substantial AI assistance. Qualified review, accessibility review and workload measurement remain absent; the course stays partial, unreviewed and formative-only.
