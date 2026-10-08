# Taylor approximations with an error bound: when "approximately" is good enough

Scientists linearize constantly: e^(−kt) ≈ 1 − kt for short times, ln(1 + x) ≈ x for small changes, sin θ ≈ θ for small angles. Each is the first term or two of a Taylor series, and each comes with an error that can be bounded rather than guessed. This lesson builds Taylor polynomials, bounds their error with the Lagrange remainder, and uses the bound to decide when a simplified formula, such as treating decay as linear or a fold change as a difference of logs, is accurate enough.

## Learning objectives

By the end of this lesson, you should be able to:

1. Construct first- and second-order Taylor polynomials of standard functions about a point.
2. Bound the approximation error with the Lagrange remainder and compare it with the actual error.
3. Decide whether a linearization used in a scientific formula is accurate enough for a stated tolerance.

## Taylor polynomials

If f has enough derivatives at a, its Taylor polynomial of degree n about a is

**Pₙ(x) = f(a) + f′(a)(x − a) + f″(a)(x − a)²/2! + … + f⁽ⁿ⁾(a)(x − a)ⁿ/n!.**

About a = 0 (a Maclaurin polynomial), e^(−x) gives P₁ = 1 − x and P₂ = 1 − x + x²/2; ln(1 + x) gives P₁ = x; sin x gives P₁ = x (and P₂ = x as well, since the second derivative is zero at 0).

## The remainder and its bound

Taylor's theorem says the error Rₙ(x) = f(x) − Pₙ(x) equals f⁽ⁿ⁺¹⁾(c)(x − a)ⁿ⁺¹/(n + 1)! for some c between a and x. Bounding the derivative over that interval bounds the error:

**|Rₙ(x)| ≤ M |x − a|ⁿ⁺¹ / (n + 1)!,** where M ≥ |f⁽ⁿ⁺¹⁾| on the interval.

**Example at x = 0.2.** e^(−0.2) = 0.818731. P₁ = 0.800000, error 0.018731. P₂ = 0.820000, error 0.001269. For P₂, the third derivative of e^(−x) is −e^(−x), whose magnitude on [0, 0.2] is at most 1, so |R₂| ≤ 0.2³/6 = 0.001333. The actual error is below the bound, as it must be. Each extra term here reduces the error by roughly a factor of x/(n + 1), which is why a few terms suffice for small x.

## Using the bound: three common linearizations

**First-order decay.** For a quantity decaying as e^(−kt), the fraction lost by time t is 1 − e^(−kt) ≈ kt. With synthetic k = 0.1 per day over 0.5 day, the linear estimate is 0.0500, the true value 0.04877: the linearization overstates loss by 2.5%. The remainder bound (kt)²/2 = 0.00125 explains why: the relative error is about kt/2, so "linear decay" is fine while kt is small.

**Log ratios.** ln(1 + x) ≈ x means a small fractional change is approximately a difference of natural logs. For a 5% increase, ln(1.05) = 0.04879, versus 0.05: a 2.5% relative error. For a 50% increase, ln(1.5) = 0.4055, and the approximation (0.5) is 23% off. Log scales are used for fold changes partly because they turn ratios into differences exactly, without needing the approximation.

**Small angles.** sin θ ≈ θ (radians) is used in optics and in pendulum and lever problems. At 10°, the relative error is 0.51%; the remainder bound θ³/6 for the next nonzero term predicts it.

## Interpretation: what the bound buys

A bound is a guarantee, not an estimate: the error cannot exceed it. That makes it the right tool when an approximation sits inside a calculation whose result matters, such as the amount of a reagent or a tolerance on a measurement. When the bound is loose, the actual error may be much smaller, but you only know that by computing it.

## Approximations inside larger calculations

An approximation's error does not stay put. If a linearized term is multiplied by a large factor, or subtracted from a nearly equal quantity, its absolute error is carried along and its relative error can grow. A practical habit is to carry the remainder bound through the rest of the calculation, or to compute the final answer once with the exact function as a check. When the check and the approximation agree within the needed tolerance, the simpler formula can be used with confidence; when they do not, the bound tells you which term to keep.

## Common mistakes

- Using degrees in sin θ ≈ θ.
- Forgetting the factorial in the remainder.
- Bounding the derivative at the expansion point instead of over the whole interval.
- Applying a linearization outside the range where its error was checked.

## Worked example

**Problem.** A protocol approximates the fraction of a reagent remaining after time t as 1 − kt. For what kt does this stay within 1% (absolute) of e^(−kt)?

**Step 1.** The error of P₁ is bounded by (kt)²/2, since |f″| = e^(−x) ≤ 1 on [0, kt].

**Step 2.** (kt)²/2 ≤ 0.01 gives kt ≤ √0.02 = 0.141.

**Step 3.** With k = 0.1 per day, the linear formula is guaranteed within 1% for t ≤ 1.41 days. Beyond that, use the exponential.

## Limits of this lesson

All parameters are synthetic. The lesson covers single-variable Taylor polynomials about a point; convergence of the full series and multivariable expansions are not covered.
