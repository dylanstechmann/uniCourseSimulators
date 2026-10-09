# Power series, radius and endpoints

## Learning objectives

1. Determine the radius of convergence and test boundary points separately.
2. Differentiate and integrate power series on justified interior intervals.
3. Track centers, indices and domain restrictions in transformed expansions.

## A series of functions

A power series Σ_(n=0)∞aₙ(x−c)ⁿ depends on the evaluation point x and center c. It converges absolutely inside a radius R and diverges outside that radius. R may be zero or infinite. At x=c only the constant term remains, so the center is always included. Behavior at distance exactly R must be checked separately; the radius alone does not specify whether either endpoint belongs to the convergence interval.

For Σ_(n=1)∞(x−2)ⁿ/(n3ⁿ), the absolute ratio of successive terms tends to |x−2|/3. Interior convergence requires |x−2|<3, hence −1<x<5. At x=−1 the series becomes Σ(−1)ⁿ/n, conditionally convergent. At x=5 it becomes the harmonic series and diverges. The full real convergence interval is therefore [−1,5), with radius 3 centered at 2. The midpoint and radius must be distinguished from endpoint inclusion.

At x=2.5, the effective argument is (x−2)/3=1/6. Using the logarithm series identity Σzⁿ/n=−ln(1−z) for |z|<1 gives the value −ln(5/6), about 0.182322. The identity is justified in the interior; endpoint conclusions above came from separate numerical-series tests.

## Geometric functions and substitution

The expansion 1/(1−x/2)=Σ_(n=0)∞(x/2)ⁿ has radius 2 around zero. Its quadratic truncation is 1+x/2+x²/4. At x=0.5 this gives 1.3125, while the exact function is 4/3. The positive tail is (0.25)³/(1−0.25)=0.020833. A finite polynomial is defined for every real x, but its agreement with this infinite series is restricted to |x|<2.

The rational function itself is defined at x=3, where it equals −2. The series there diverges because terms grow in magnitude. A function's domain can extend beyond the convergence interval of a particular expansion. Substituting x=3 into a truncated polynomial gives a number but does not supply a valid infinite-series approximation. At x=2 the function has a pole; at x=−2 the rational function is finite, yet the series terms alternate with fixed magnitude and fail to tend to zero.

Centering changes coefficients and the usable neighborhood. A series in x−c is not evaluated by substituting x directly into each power unless c=0. If a scientific variable has units, normalize it with a scale so each power-series argument is dimensionless. Coefficients then restore the output units. These bookkeeping steps prevent addition of incompatible dimensions across different powers.

## Differentiation and integration

Inside the radius, a power series can be differentiated and integrated term by term. The differentiated and integrated series retain the same radius, but their endpoint behavior may change. The compact-interval justification is important: on every closed interval strictly inside the radius, convergence is sufficiently controlled for these operations. Merely observing pointwise convergence at an endpoint is not a general license to interchange every limit and integral there.

Differentiating Σxⁿ gives Σ_(n=1)∞n x^(n−1)=1/(1−x)² for |x|<1. At x=0.5 the derivative-series value is 4. Integrating from 0 to x gives Σ_(n=0)∞x^(n+1)/(n+1)=−ln(1−x) for |x|<1. At x=0.5 the value is ln 2. The integrated series also converges at x=−1 by the alternating-series test, while at x=1 it becomes harmonic and diverges. Its radius remains 1 despite the additional endpoint.

The integration constant is fixed by the chosen lower bound. If an indefinite antiderivative is written instead, it needs an arbitrary constant. An index shift should preserve the first term and exponent: Σ_(n=0)∞x^(n+1)/(n+1) can be rewritten as Σ_(m=1)∞xᵐ/m, but not as a sum starting at m=0 with a zero denominator.

## Worked example

Analyze Σ_(n=1)∞(x−2)ⁿ/(n3ⁿ). The ratio calculation gives a radius of 3. Substitute x=−1 to obtain an alternating harmonic series and x=5 to obtain a positive harmonic series. The resulting interval is [−1,5). Evaluate x=2.5 using the dimensionless argument z=1/6 and the identity −ln(1−z), giving 0.182322. These are three separate tasks: finding the radius, classifying endpoints and computing an interior value. A single ratio inequality solves only the first task.

## Common mistakes and checks

Do not automatically attach closed brackets to a radius inequality. Check each endpoint with its own series. Do not claim that a finite polynomial diverges outside the radius; divergence belongs to the infinite series limit. Compare the first several terms before and after an index shift to catch off-by-one errors.

When integrating an approximation over an interval, ensure the entire interval lies in the justified expansion range or provide an additional endpoint argument. The largest argument magnitude on that interval often controls a uniform error bound. A series that is accurate near its center may converge slowly near its radius. Increasing the number of terms can improve truncation error inside the radius but cannot rescue an evaluation outside it.

## Limits of this lesson

These synthetic algebraic examples cover selected geometric and logarithmic expansions. Complex-variable analyticity and a full proof of uniform convergence are outside this increment. Practice verifies numerical values and endpoint classifications, not symbolic series manipulation or written proofs. Original material was developed with substantial AI assistance using existing calculus scope references. The package remains partial, unreviewed and formative-only.
