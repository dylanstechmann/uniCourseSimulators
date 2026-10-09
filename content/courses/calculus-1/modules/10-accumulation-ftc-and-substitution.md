# Accumulation, the fundamental theorem and substitution

A rate curve answers how quickly a quantity changes at an instant; its integral answers how much change accumulates over an interval. A definite integral is a signed sum with a limiting definition, not simply an instruction to find an antiderivative. This lesson connects those viewpoints, differentiates accumulated quantities with changing bounds and derives substitution from the chain rule. All flows and functions are synthetic. The models teach accumulation and units, not instructions for dosing, infusion or operating a pump.

## Learning objectives

1. Interpret a definite integral through signed sums and recover accumulated change.
2. Differentiate an accumulation function, including changing upper and lower bounds.
3. Change variables in a definite integral and calculate an average rate.

## From small intervals to an integral

Partition [a, b] into intervals of widths Δt_i and choose a sample point t_i* in each. The sum Σv(t_i*)Δt_i approximates the signed accumulation of a rate v. Under appropriate integrability conditions, refining the partition so its largest width tends to zero gives ∫ₐᵇv(t)dt. The units are rate units multiplied by time units. A positive portion adds to the accumulated state and a negative portion subtracts from it.

For a synthetic volume rate v(t) = 6t − t², with t expressed in minutes and coefficients carrying the required units, v is nonnegative on [0, 6]. Its values at 0, 3 and 6 are 0, 9 and 0 mL/min. A single rectangle using the middle rate gives 9 × 6 = 54 mL, which overestimates this curved profile. It is an approximation from one sampled value, not an exact accumulation. The integral provides the limit of suitably refined sums.

## Two parts of the fundamental theorem

If v is continuous, F(t) = ∫ₐᵗv(s)ds is differentiable and F′(t) = v(t). The integration variable s is a dummy variable; t determines the upper boundary. The derivative reads the rate at that boundary. If A is any antiderivative of v, then ∫ₐᵇv(t)dt = A(b) − A(a). The arbitrary constant in A cancels between endpoints; a definite integral does not need an extra constant added to its value.

For v(t) = 6t − t², use A(t) = 3t² − t³/3. Over [0, 6], the accumulated volume is 108 − 72 = 36 mL. If the starting volume is 10 mL and this is the net rate of volume change, the final volume is 46 mL. The integral alone is the change, not the final state. At t = 3, accumulation from zero is 27 − 9 = 18 mL, and its derivative is v(3) = 9 mL/min.

## Average rate and an existence statement

The average rate over [a, b] is (1/(b−a))∫ₐᵇv(t)dt. For this profile it is 36/6 = 6 mL/min. A continuous rate reaches its average value somewhere in the interval. Solving 6t − t² = 6 gives t = 3 ± √3, both within [0, 6]. There need not be a unique time at which the average occurs. The theorem concerns existence; it does not say that the rate at the midpoint is the average.

An average rate is not generally the arithmetic mean of unevenly spaced measured rates. A long interval should contribute more accumulated weight than a short one. Numerical integration of observations therefore needs their time coordinates, not only a list of rate values. The later numerical-calculus lesson develops this distinction.

## Moving bounds add chain factors

Let H(t) = ∫₀^(t²)e^(−s)ds. The fundamental theorem and chain rule give H′(t) = e^(−t²) × 2t. At t = 1, H′ = 2/e = 0.735759. The expression H(t) = 1 − e^(−t²) provides an independent differentiation check. Omitting the derivative of t² would miss the factor 2t.

When both bounds move, M(t) = ∫_(a(t))^(b(t))v(s)ds has derivative v(b(t))b′(t) − v(a(t))a′(t), provided the stated smoothness conditions hold. For M(t) = ∫ₜ^(2t)s²ds, M′ = (2t)² × 2 − t² × 1 = 7t². At t = 2 this is 28. The subtraction comes from the moving lower boundary; the extra factor 2 comes from the upper boundary. Equivalently M(t) = 7t³/3, which differentiates to the same result.

## Substitution is reversed composition

In ∫₀² [2t/(1+t²)]dt, choose u = 1+t², so du = 2t dt. The bounds become u = 1 and u = 5. Thus the integral is ∫₁⁵(1/u)du = ln 5 = 1.609438. Because u is positive throughout this interval, the logarithm has no domain problem. For an indefinite integral the corresponding result is ln(1+t²) plus a constant. Differentiate it to check the chain factor.

Changing variables requires changing both the differential and the bounds. Keeping the old bounds 0 and 2 after replacing t with u would evaluate a different integral. For ∫₀³(2s+1)²ds, set u = 2s+1 and ds = du/2. The new bounds are 1 and 7, giving (1/2)∫₁⁷u²du = (343−1)/6 = 57.

## Worked example

Let a synthetic state satisfy x′(t) = 2t/(1+t²), with x(0) = 4. Integrating from 0 to 2 gives the change ln 5, so x(2) = 4 + ln 5 = 5.609438. The average rate is ln 5/2 = 0.804719 over that interval. Differentiating x(t) = 4 + ln(1+t²) recovers the specified rate. Initial state, accumulated change and average rate are three related but distinct quantities.

## Common mistakes

- Treating accumulation as final state without an initial value.
- Adding an arbitrary constant to a definite integral's numerical value.
- Losing a chain factor or the lower-bound subtraction.
- Changing an integrand's variable while retaining incompatible bounds.
- Assuming the midpoint rate equals the time average.

## Limits of this lesson

The fundamental-theorem calculations assume continuous rates and differentiable bounds as stated. Real sampled signals require interpolation and uncertainty decisions. An integral of a constructed model establishes neither a measured volume nor the accuracy of a real process.
