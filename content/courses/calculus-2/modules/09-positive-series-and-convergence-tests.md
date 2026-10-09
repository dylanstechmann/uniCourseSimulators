# Positive series and convergence tests

## Learning objectives

1. Distinguish a sequence limit from convergence of its infinite series.
2. Choose geometric, power, comparison, integral or ratio tests with their hypotheses.
3. Bound a positive-series tail and select a sufficient truncation length.

## Terms and partial sums answer different questions

A sequence aₙ is an ordered list. Its series is defined through partial sums S_N=Σ_(n=1)^N aₙ. The infinite series converges when S_N approaches a finite limit. If aₙ does not approach zero, the series diverges, because aₙ=Sₙ−S_(n−1) would otherwise approach zero. The converse fails: terms tending to zero are necessary, but not sufficient.

The harmonic terms 1/n approach zero. Their series diverges. Group terms from n=2^(k−1)+1 through 2^k. There are 2^(k−1) terms, each at least 1/2^k, so each group adds at least 1/2. Infinitely many such groups cannot produce a finite sum. This grouping supplies a reason for divergence rather than merely assigning a test name.

For nonnegative terms, partial sums increase. If a valid comparison bounds them above, they converge. This monotonic structure explains why comparison is effective. Negative or alternating terms require extra care because monotonicity no longer applies directly to their partial sums.

## Geometric series and exact tails

For Σ_(n=0)∞ rⁿ, the finite sum through index N is (1−r^(N+1))/(1−r) when r≠1. It converges for |r|<1 to 1/(1−r). The remaining tail after N is r^(N+1)/(1−r). For r=0.4 and N=3, the four included terms sum to 1.624, the infinite sum is 1.666667 and the positive tail is about 0.042667.

The indexing is part of the answer. A sum beginning at n=1 omits the constant term. A phrase such as “four terms” means indices 0 through 3 for this series, not 0 through 4. At r=1 every term is 1 and the series diverges. At r=−1 terms alternate between 1 and −1 but do not tend to zero, so the series still diverges. Having both signs is not sufficient for convergence.

For the synthetic geometric accumulation with r=0.4, requiring the tail after N to be at most 0.001 means 0.4^(N+1)/0.6≤0.001. Index N=7 gives about 0.001092, too large; N=8 gives about 0.000437, sufficient. Thus nine terms are required for this exact guarantee. Testing both the selected index and the previous one verifies minimality.

## Power series of numbers and comparison

The numerical p-series Σ_(n=1)∞1/nᵖ converges exactly for p>1. The integral test explains the criterion when the corresponding function is positive, continuous and decreasing on the relevant tail. At p=2, after N terms the remaining tail lies between ∫_(N+1)∞x^(−2)dx and ∫_N∞x^(−2)dx, or 1/(N+1) and 1/N. These bounds do not require knowing the exact infinite sum.

For N=100, the upper bound is 0.01. If the requirement is “at most 0.01,” this is sufficient. If the requirement were strictly less than 0.01, the stated bound alone would suggest choosing N>100. Pay attention to whether a tolerance is strict and to whether the inequality is a bound rather than an equality for the actual tail.

For aₙ=1/(n²+n), comparison with 1/n² establishes convergence. Algebra gives a stronger result: aₙ=1/n−1/(n+1). Summing through N cancels internal terms, yielding S_N=1−1/(N+1). The infinite sum is 1 and its exact tail is 1/(N+1). This telescoping structure is worth checking before applying a generic estimate.

## Ratio tests and inconclusive outcomes

For nonzero terms eventually, evaluate L=lim|a_(n+1)/aₙ| when that limit exists. L<1 establishes absolute convergence; L>1 implies divergence, as terms cannot tend to zero. L=1 is inconclusive. Both harmonic and square-reciprocal terms have ratio limit 1, yet one series diverges and the other converges.

For aₙ=3ⁿ/n!, the ratio is 3/(n+1) and tends to zero, establishing convergence. The first few ratios can exceed one; the test concerns eventual behavior. For aₙ=n/2ⁿ, the ratio is (n+1)/(2n) and tends to 1/2. The terms' initial size does not determine the convergence of the infinite tail. Likewise, a finite prefix can alter the sum but cannot turn a convergent tail into a divergent one.

## Worked example

Suppose a constructed repeated contribution is 0.4ⁿ for n beginning at zero. Add four terms to get 1+0.4+0.16+0.064=1.624. The exact remainder is 0.4⁴/0.6=0.042667. For a tighter tolerance of 0.001, compare N=7 and N=8: their tail bounds straddle the target. Keep terms through N=8, meaning nine contributions. Unlike a measurement uncertainty estimate, this tail comes entirely from the specified geometric mathematical model. Unmodeled changes in the ratio would require a separate argument.

## Common mistakes and checks

Do not conclude convergence from a zero term limit or from a finite calculator sum. Do not call a ratio limit of one a divergence result. When applying the integral test, check positivity and eventual decrease, and use the correct N versus N+1 endpoints. Compare quantities with matching signs; inequalities can reverse when negative terms are introduced.

## Limits of this lesson

All accumulations are synthetic, and the tests cover selected standard series. Convergence establishes existence of a mathematical sum, not an experimental process continuing indefinitely or a biological mechanism. Practice checks numbers and test choices rather than grading proof quality. Original explanations were developed with substantial AI assistance, with no imported third-party text. This package remains partial, unreviewed and formative-only.
