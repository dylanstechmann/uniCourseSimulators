# A washout curve: semilog slopes, background and model checks

The course case gives a concentration sensor reporting C(t) = C₀e^(−kt) after washout. It asks how a semilog plot estimates k, what units k has and why observations might depart from a straight line. This capstone connects those questions to derivatives, logarithms, accumulation and numerical uncertainty. It also distinguishes an additive sensor background from a sum of decay processes. Every concentration, rate and observation here is synthetic. The models establish no clearance rate, biological mechanism or operating protocol for a real system.

## Learning objectives

1. Estimate exponential decay rates from dimensionless logarithms and interpret their units.
2. Diagnose how background offsets and mixed rates change a semilog curve.
3. Specify independent checks while separating descriptive fit from mechanism.

## Logarithms turn a ratio into a slope

For a positive exponential C(t) = C₀e^(−kt), divide by the reference C₀ and take the natural logarithm: ln(C/C₀) = −kt. The logarithm's argument is dimensionless. A straight line of this quantity against time has slope −k; its intercept is zero if C₀ is the true concentration at time zero. If the reference is a different positive constant, the intercept changes while the slope remains −k. The exponent must be dimensionless, so k has inverse-time units.

For the synthetic curve C(t) = 20e^(−0.1t), with time in hours, k = 0.1 h⁻¹. At 10 h, C = 20/e = 7.357589 and C′ = −2/e = −0.735759 concentration units per hour. The rate of concentration change is not k itself: C′ = −kC. The magnitude of the derivative falls as concentration falls, even though the fractional decay rate k stays constant.

If the plot uses common logarithms instead, log₁₀(C/C₀) = −kt/ln 10. Its slope is −0.043429 per hour for this example. Multiply the magnitude of that slope by ln 10 to recover k. Reading a base-10 slope directly as k gives an error by a factor of ln 10. State the logarithm base and the time unit with the estimate.

## Half-life and accumulation answer different questions

The half-life solves C(t)/C₀ = 1/2, giving t_half = ln 2/k = 6.931472 h. It is the same for each successive halving under this model. The concentration-time accumulation over [0, T] is (C₀/k)(1 − e^(−kT)); over 0 to 20 h it is 172.932943 concentration-unit hours. This integral is not an amount removed unless an additional relationship, such as a known fixed volume and a specified flux, supplies the required conversion.

From any two positive exact concentrations at times t₁ and t₂, k = ln(C₁/C₂)/(t₂−t₁). Two points determine this apparent rate but cannot test whether the decay was exponential between them. More time points provide a shape check; independently held-out observations provide a prediction check after the model and fitting choices have been fixed.

## An additive background bends the semilog curve

Suppose the sensor reports Y(t) = C(t) + B with fixed background B = 2 concentration units. Then Y(0) = 22 and Y(20) = 4.706706. Taking logarithms of Y does not remove B: ln(C+B) is not ln C + ln B. The apparent two-point decay rate from those uncorrected endpoints is ln(22/4.706706)/20 = 0.077103 h⁻¹, below the true 0.1.

The instantaneous semilog slope is Y′/Y = −kC/(C+B). Its magnitude at 10 h is 0.078627 h⁻¹ and tends toward zero as the decaying concentration becomes small relative to the background. The second derivative of ln Y is k²BC/(C+B)², positive for positive B and C. Thus the logarithmic curve flattens even though the underlying C is a single exponential. Subtracting an independently established constant background before logging recovers the ideal line in this exact construction.

Background correction has an uncertainty cost. If the estimate of B is noisy, all corrected observations can share that uncertainty. A corrected value that is zero or negative cannot be logged as a positive real ratio. Deleting such points silently or adding an arbitrary positive constant changes the analysis and may bias the fitted slope. Report the correction and the usable range, and account for the common background error.

## Several rates can also cause curvature

Consider C_mix(t) = 12e^(−0.2t) + 8e^(−0.05t), with no background. Its instantaneous fractional decay rate is −C_mix′/C_mix, a concentration-weighted average of the two rates. At t = 10 this is approximately 0.087615 h⁻¹. At late times the slower component dominates and the apparent rate approaches 0.05. A flattening semilog curve therefore has multiple possible explanations: a background, mixed rates, sensor dynamics or failure of the assumed process model.

Curvature alone does not identify which explanation is correct. A blank measurement tests background; independently known input changes can probe sensor response; a wider observation window can test a persistent plateau against continued slow decay. These are proposed evidence distinctions for a synthetic case, not a real experimental procedure. Fits with more free parameters can imitate the same short window, so compare predictions on data reserved from tuning.

## Worked example

At 0 and 20 h, background-corrected concentrations are 20 and 2.706706. Their ratio gives k = ln(20/2.706706)/20 = 0.1 to the displayed precision. The uncorrected estimate 0.077103 predicts Y(40) ≈ 22e^(−0.077103×40) = 1.006958, while the actual constructed sensor reading is 20e^(−4)+2 = 2.366313. The discrepancy exposes failure of the zero-background model's extrapolation. It does not by itself prove that background is the only possible cause; the known construction supplies that explanation here.

## Common mistakes

- Logging a dimensional value without stating a reference ratio.
- Confusing concentration change per hour with a fractional decay rate per hour.
- Reading a base-10 slope as the natural-log rate.
- Treating two points as evidence for a unique process model.
- Logging an uncorrected background or assigning a mechanism from curvature alone.

## Limits of this lesson

The examples use positive exact model values and a known constant background. Real signals may have correlated noise, detection limits, changing calibration and process variation. The original course case remains a self-assessment checklist; no written capstone is graded and no instructor review is claimed.
