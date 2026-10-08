# Strength of brittle materials: flaws, scatter and the Weibull distribution

A ductile metal has a yield strength that repeats from specimen to specimen within a few percent. A ceramic, a glass or a bone cement does not. Ten nominally identical bars broken in bending can give strengths that differ by a factor of two, and a large part is, on average, weaker than a small one made of the same material. Failure begins at the most severe flaw in the stressed region, and the size and position of that flaw are random. For such materials a single strength number is not enough: the strength is described by a probability distribution, and a design chooses an acceptable probability of failure instead of a safety factor on one number. This lesson uses the two-parameter Weibull distribution for that purpose. All values are synthetic.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute the probability of failure of a brittle part under uniform stress from the Weibull distribution and invert it to find a design stress.
2. Estimate the Weibull modulus from ranked strength data and interpret it as a measure of scatter.
3. Evaluate how the stressed volume changes the strength (the weakest-link size effect) and when the model does not apply.

## Why strength scatters

Brittle fracture starts from a flaw: a pore, a crack from machining, a cluster of large grains or an inclusion. A flaw of size a in a material of fracture toughness K_Ic fails under a stress of about σ_f = K_Ic/(Y √(π a)), where Y is a geometry factor near 1. **Synthetic values:** K_Ic = 1.0 MPa√m and Y = 1.12 give σ_f = **71.2 MPa** for a 50 μm flaw and **112.6 MPa** for a 20 μm flaw. The strength is controlled by the largest flaw that happens to lie in the highly stressed region, and different specimens contain different largest flaws. It is the same idea as the stress concentration of the earlier lesson: the flaw tip multiplies the local stress.

## The two-parameter Weibull distribution

If the stress is uniform over a volume V, and the part fails when its weakest element fails, the probability of failure at stress σ is

**P_f = 1 − exp[−(V/V₀)(σ/σ₀)^m].**

The scale parameter σ₀ is the stress at which a specimen of the reference volume V₀ fails with probability 1 − 1/e = **0.632**. The **Weibull modulus** m measures the scatter: the larger m, the narrower the distribution. Many ceramics have m of roughly 5 to 20, while the yield strength of a ductile metal repeats within a few percent. **Synthetic material:** σ₀ = 100 MPa and m = 10, with V = V₀. Then P_f(80 MPa) = 1 − exp(−0.8^10) = **0.1018** and P_f(60 MPa) = 0.0060. Because of the high power, the probability changes by a factor of about 17 between 60 and 80 MPa. Inverting the formula gives the stress for a chosen failure probability, σ = σ₀ [−ln(1 − P_f)]^(1/m): for 1% this is σ = **63.13 MPa**, about 63% of σ₀. A design that wants a failure probability of 1% must work at a stress far below the average strength.

## Estimating the modulus from data

To estimate m and σ₀, break N specimens and rank the strengths from lowest to highest. Assign the i-th strength the probability P_i = (i − 0.5)/N, and plot ln[−ln(1 − P_i)] against ln σ. For the Weibull distribution this is a straight line of slope m, and σ₀ is the stress at which the line crosses y = 0. From two points, m = (ln[−ln(1 − P_B)] − ln[−ln(1 − P_A)])/(ln σ_B − ln σ_A). With (σ, P_f) = (70 MPa, 0.1) and (90 MPa, 0.6), m = **8.61**.

A small illustration with N = 6: strengths 62, 71, 77, 83, 88, 96 MPa, with P_i = 0.083, 0.250, 0.417, 0.583, 0.750, 0.917. A least-squares line through the 6 points has m = 7.6 and σ₀ = 84.4 MPa. With only 6 specimens the estimate of m is very uncertain; standards for ceramics call for tens of specimens, and a design should not rely on a modulus from six.

## The size effect

For the same failure probability, a larger volume has a lower strength, because it holds more potential flaws: σ₂/σ₁ = (V₁/V₂)^(1/m). For eight times the volume and m = 10, the factor is 8^(−1/10) = **0.8123**, so the stress for 1% failure falls from 63.13 MPa to **51.28 MPa**. For a more scattered material (m = 5) the same increase in volume gives a factor of 0.660. At m = 5 with the same σ₀, P_f(80 MPa) rises from 0.102 to **0.2794**. This is why the strength measured on small laboratory bars does not transfer directly to a larger part, and why a material with a lower Weibull modulus is penalized much more heavily.

## When the model does not apply

The Weibull model describes brittle fracture that starts at flaws. It does not apply to ductile yielding, where the strength is set by the plastic flow of the whole section. It assumes one population of flaws, a uniform stress (for a beam in bending the stress varies, and an effective volume is used), and that no flaw grows during the load. In moist or physiological environments, many ceramics and glasses show slow crack growth, so that strength falls with the time under load. A proof test, which breaks the weakest parts before they enter service, truncates the distribution, but only if it is a faithful test. Bone, polymer composites and lattices have several kinds of flaw and different scatter. The lesson is a model of random strength, not a prediction of any real material.

## Common mistakes

- Treating the mean strength as a design strength.
- Reading a high Weibull modulus as a high strength; it measures only scatter.
- Applying the Weibull size effect to a ductile material.
- Estimating m from a handful of specimens as though it were exact.
- Forgetting that the failure probability refers to a specified stressed volume.
- Mixing the volume ratio: the stress ratio is the volume ratio to the power −1/m, not −m.

## Worked example

**Problem.** A synthetic ceramic has σ₀ = 120 MPa and m = 8 for the reference volume. Find the failure probability at 90 MPa, the stress for a failure probability of 0.5%, and that stress for a part with 27 times the volume.

**Step 1: probability.** P_f = 1 − exp(−(0.75)^8) = 1 − exp(−0.1001) = 0.0953.

**Step 2: design stress.** σ = 120 × [−ln(0.995)]^(1/8) = 120 × 0.5158 = 61.9 MPa.

**Step 3: size effect.** The factor is 27^(−1/8) = 0.6623, so the allowable stress for the larger part is 61.9 × 0.6623 = 41.0 MPa.

**Step 4: reading the result.** A part with 27 times the volume must be loaded to about 66% of the stress allowed for the reference volume, to keep the same failure probability.

## Limits of this lesson

All numbers are synthetic. The two-parameter Weibull model, with a uniform stress and a single flaw population, is a simplification; real data show scatter in the estimates of both parameters and often need a threshold stress, several flaw populations or a time-dependent strength. Nothing here is a design basis for any device.
