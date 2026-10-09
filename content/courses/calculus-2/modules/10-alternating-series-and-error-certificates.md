# Alternating series and error certificates

## Learning objectives

1. Separate absolute convergence, conditional convergence and divergence.
2. Use the alternating-series theorem only when its magnitude conditions hold.
3. Interpret the first omitted term as an error bound with explicit indexing and sign.

## Signs change the convergence question

Absolute convergence means Σ|aₙ| is finite. It guarantees convergence of Σaₙ. Conditional convergence means the signed series converges while its absolute-value series diverges. These definitions distinguish mathematical mechanisms: one depends on summable magnitudes, while the other can rely on cancellation between signs. Neither definition follows merely from seeing alternating signs in a displayed expression.

For Σ_(n=1)∞(−1)^(n+1)/n, the magnitudes decrease to zero. The alternating-series theorem establishes convergence, while the harmonic series of magnitudes diverges. Thus convergence is conditional. Replacing n by n² gives an absolutely convergent series because the p-series with p=2 converges. Replacing 1/n by a constant magnitude produces terms that do not tend to zero and therefore gives divergence.

Absolute convergence is also what permits arbitrary rearrangement without changing a sum. A conditionally convergent series cannot generally be reordered freely. Finite reordering within a finite sum is ordinary algebra; rearranging infinitely many terms changes how the limiting process is taken. The distinction is another reason to write the partial sum sequence explicitly.

## Conditions and remainder

Write a signed series as Σ_(n=1)∞(−1)^(n+1)bₙ, where bₙ≥0. If bₙ decreases to zero, its partial sums converge, and after N included terms the error magnitude is at most b_(N+1). The exact sum lies between consecutive partial sums S_N and S_(N+1). The remaining error has the sign of the first omitted term when the conditions hold. Eventual decrease can suffice for convergence, but an error certificate for a particular early cutoff requires the needed monotonicity throughout its remaining tail.

The theorem is not a confidence interval. The bound contains no probability or random sampling assumption. It describes a deterministic truncation of an exact mathematical series. Measurement uncertainty, floating-point rounding and model error must be assessed separately when the series approximates a real quantity.

Consider the logarithm expansion ln(1+x)=Σ_(n=1)∞(−1)^(n+1)xⁿ/n for 0<x≤1. Its magnitudes have ratio x n/(n+1)<1 and tend to zero. At x=0.5, four included terms give 0.5−0.5²/2+0.5³/3−0.5⁴/4=0.401042. The next term is positive and has magnitude 0.5⁵/5=0.00625. The exact ln 1.5, about 0.405465, lies between that partial sum and the next one. The actual error, about 0.004423, is smaller than the bound.

## Choosing an order

For the same logarithm at x=0.5, require 0.5^(N+1)/(N+1)≤0.0001. With N=8, the first omitted magnitude is about 0.000217, too large. With N=9 it is 9.765625 × 10⁻⁵, sufficient. Nine included terms therefore give the first certificate at this tolerance. The actual error for eight terms could conceivably be smaller than the tolerance; the question here asks about this specific sufficient bound, not the unknown smallest actual error.

At x=1, the same series approximates ln 2 with bound 1/(N+1). A bound at most 0.01 requires N≥99. This slow convergence contrasts with x=0.5. An expansion may converge at an endpoint yet require many more terms for useful accuracy there. Convergence and computational efficiency are separate properties.

For arctan x, integrate the geometric expansion of 1/(1+x²) inside |x|<1 to obtain x−x³/3+x⁵/5−…. At x=0.5, the three displayed terms give 0.464583. The first omitted magnitude is 0.5⁷/7, about 0.001116. The true arctan value is about 0.463648, so the remainder is negative and within the bound. The exponent 7 and denominator 7 belong together because the expansion has odd powers; counting three terms does not mean stopping at degree three.

## Worked example

Evaluate the four-term logarithm approximation at x=0.5 using exact fractions before rounding. Its value is 77/192, or 0.401042. Add the first omitted term 1/160 to obtain the upper enclosing partial sum. Since the signs start positive and four terms end negative, the omitted fifth term is positive, so the approximation is below ln 1.5. The interval width is 0.00625, and the actual error is 0.004423. This reasoning supplies a sign, a magnitude guarantee and an explicit partial-sum convention; reporting only “approximately 0.4” would omit all three.

## Common mistakes and checks

Do not use the first omitted term for a positive series unless another theorem supplies that bound. In a geometric positive tail, all omitted terms add, so the first one alone is generally too small. Do not claim that every alternating series converges: magnitudes that stay fixed fail the zero-limit condition, and irregular magnitudes require a separate argument.

Retain enough intermediate precision that rounding is smaller than the requested bound. If a truncation certificate is 0.0001, reporting only one decimal place discards its practical value. When comparing actual and guaranteed errors, state which is which. The actual error needs the exact target or a separately reliable reference calculation; the bound can be available even when that target is unknown.

## Limits of this lesson

The logarithm and arctangent examples are synthetic numerical tasks. They do not establish measurement accuracy or an experimental uncertainty distribution. The lesson does not prove the rearrangement theorem or analyze every oscillating series. Public practice evaluates selected values and interpretations, not a written proof. Original content has substantial AI assistance and retains partial, unreviewed and formative-only status.
