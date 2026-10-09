# Improper integrals, singularities and comparison

## Learning objectives

1. Define improper integrals through limits at infinite bounds and singular endpoints.
2. Apply power and comparison criteria with the correct endpoint conditions.
3. Distinguish convergent integrals, divergent totals and principal-value cancellation.

## An integral with a limit attached

A finite interval and a familiar antiderivative are not enough to guarantee an ordinary definite integral. An integrand may become unbounded near an endpoint or inside the interval. An infinite integration range also requires a limit. Define ∫₁∞ f(x)dx as lim_(b→∞)∫₁ᵇ f(x)dx when this limit exists as a finite real number. Define ∫₀¹ f(x)dx for an endpoint singularity as lim_(a→0⁺)∫ₐ¹ f(x)dx. These definitions specify which part of the calculation is ordinary and which requires convergence.

The distinction matters for accumulated rates. A synthetic release can continue forever while having a finite total if its tail decays sufficiently fast. Conversely, a rate can approach zero and still accumulate an infinite total. For f(x)=1/x, the tail integral is ln b and diverges, despite f(x) tending to zero. Small instantaneous values alone do not settle total accumulation.

## Two power criteria

For p≠1, ∫₁ᵇ x^(−p)dx=(b^(1−p)−1)/(1−p). The limit is finite exactly when p>1, giving 1/(p−1). At p=1 the logarithmic tail diverges. For p=2 the total from 1 to infinity is 1. The omitted tail from b to infinity is 1/b, so cutting off at b=100 leaves 0.01. That is a rigorous tail amount for this exact model, not a numerical integration error estimate for an arbitrary function.

At the other endpoint, ∫ₐ¹ x^(−p)dx=(1−a^(1−p))/(1−p), converging exactly when p<1. Thus ∫₀¹ x^(−1/2)dx=2, even though the integrand is unbounded at zero. The criterion reverses because the relevant limit changes from large x to small positive x. Using the infinity criterion at zero incorrectly classifies this integrable singularity.

If both endpoints are improper, treat them separately. For ∫₀∞ f, split at a finite interior point, such as 1, and require convergence of both pieces. The split point is arbitrary when both integrals converge. It cannot be adjusted to force divergent positive and negative pieces to cancel.

## Comparison and positive tails

Suppose 0≤f(x)≤g(x) beyond a finite point. If the integral of g over the tail converges, the integral of f converges. If the integral of f diverges, the integral of g diverges. The other directions are inconclusive. A large divergent upper bound does not prove that a smaller function diverges.

For f(x)=1/(x²+1) and x≥1, f(x)≤1/x². Since the comparison tail converges, so does f's tail. Its exact value from 1 to infinity is π/4, using arctangent. Limit comparison provides a closely related tool: if f/g tends to a finite strictly positive constant and both functions are nonnegative on the tail, they have the same convergence behavior. Here f divided by x^(−2) tends to 1.

A shift does not change the power criterion at infinity. For the constructed rate q(t)=6/(1+t)² in amount units per hour, with t expressed numerically in hours and the scale 1 representing one hour, the total from 0 to infinity is 6 amount units. The amount remaining after t=3 is 6/(1+3)=1.5. The model's rate constant and units must be carried when converting to another time coordinate; replacing hours by minutes without transforming the scale would define a different model.

## Internal singularities and cancellation

For ∫_(−1)¹ 1/x dx, split at zero. The integral from −1 to 0 diverges negatively, and that from 0 to 1 diverges positively. The ordinary improper integral therefore does not exist. Evaluating ln|x| only at −1 and 1 gives zero but skips both divergent endpoint limits.

The symmetric expression lim_(a→0⁺)(∫_(−1)^(−a)1/x dx+∫ₐ¹1/x dx) is zero. This is a Cauchy principal value, a separately defined cancellation rule. It is not the ordinary improper integral. Different nonsymmetric approaches can change the apparent cancellation. State explicitly which quantity is being computed rather than treating opposite infinities as ordinary numbers.

## Worked example

For q(t)=6/(1+t)², integrate first on [0,b]. The antiderivative is −6/(1+t), so the finite total is 6−6/(1+b). Taking b to infinity gives 6. If observations stop at t=3, the observed-window integral is 4.5 and the model-based remaining tail is 1.5. Their sum matches the total. Contrast this with q(t)=6/(1+t), whose finite-window integral is 6 ln(1+b). Its rate also tends to zero, but its unlimited total diverges. The difference comes from the tail exponent, not from whether the curve appears nearly flat on a finite plot.

## Common mistakes and checks

Never substitute infinity as an ordinary endpoint number. Write the finite primitive evaluation and then take its limit. Inspect the original integrand for every singularity before cancellation or numerical quadrature. A finite computed value from a truncated window establishes only that window's integral; it does not demonstrate tail convergence.

For a positive integrand, accumulated amounts increase with the cutoff. A claimed finite total smaller than a valid finite-window integral is inconsistent. A tail estimate requires a justified tail model or bound. Real measurements may have backgrounds, changing dynamics or detection limits that violate the assumed asymptotic law. A mathematical comparison is about functions satisfying its hypotheses; it does not prove that a real release follows those functions indefinitely.

## Limits of this lesson

The examples and rates are synthetic. Only selected nonnegative comparisons and elementary singularities are developed; oscillatory integral convergence and specialized regularization are outside this increment. Practice points do not evaluate a written proof or establish a real infinite-time exposure. All content is original with substantial AI assistance, and no third-party dataset was used. The course remains partial, unreviewed and formative-only.
