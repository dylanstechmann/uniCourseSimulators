# Floating-point arithmetic in scientific code: rounding, cancellation and comparing numbers safely

Computers store most numbers in binary floating point with about 16 significant decimal digits. That is plenty for almost any measurement, yet scientific code still produces wrong answers from rounding: a variance computed as zero, a test that fails because 0.1 + 0.2 is not 0.3, a difference of two large numbers with no correct digits. These failures are predictable. This lesson explains machine precision, shows how subtracting nearly equal numbers destroys accuracy, and gives safe ways to compute and compare.

## Learning objectives

By the end of this lesson, you should be able to:

1. Explain machine epsilon and compute the spacing between representable floating-point numbers near a given value.
2. Diagnose catastrophic cancellation, estimate the digits lost, and choose a numerically stable formula.
3. Write comparisons and tests with appropriate absolute and relative tolerances.

## Machine precision

Double-precision (64-bit) floating point stores a number as a sign, a 53-bit binary significand and an exponent. **Machine epsilon**, ε ≈ 2.220×10⁻¹⁶, is the gap between 1 and the next larger representable number. Near any value x, representable numbers are spaced by roughly |x| ε, so every stored value has a relative rounding error up to about ε/2. Near 10⁸ the spacing is about 2.2×10⁻⁸.

Many decimal fractions have no exact binary representation, just as 1/3 has none in decimal. In Python, `0.1 + 0.2 == 0.3` is `False`, because the sum is stored as 0.30000000000000004. The error is tiny in relative terms, but an exact equality test notices it.

## Catastrophic cancellation

Subtracting two nearly equal numbers keeps their absolute error but shrinks the result, so the relative error explodes. If a and b each carry a relative error δ, a − b can carry a relative error of about δ × |a| / |a − b|. With a = 1.0000001, b = 1.0 and δ = 10⁻¹², the difference 10⁻⁷ has a relative error near 10⁻⁵: five digits lost.

**A real example: variance.** The textbook shortcut var = mean(x²) − mean(x)² subtracts two large, nearly equal numbers when the mean is large compared with the spread. For the synthetic values 100000001, 100000002, 100000003 (say, a timestamp in microseconds), the true population variance is 0.6667. In double precision the shortcut returns **0.0**: mean(x²) ≈ 10¹⁶, and the variance is about 10¹⁶ times smaller, more than the 16 digits available. The number of digits lost is roughly log₁₀(x̄²/s²) = 16.2.

```python
xs = [1e8 + 1, 1e8 + 2, 1e8 + 3]
m = sum(xs) / len(xs)
naive = sum(x * x for x in xs) / len(xs) - m * m        # 0.0
two_pass = sum((x - m) ** 2 for x in xs) / len(xs)      # 0.6666666666666666
```

The **two-pass** formula subtracts the mean first, so the squared terms are small and exact. Welford's one-pass algorithm achieves the same stability when data arrive as a stream. Library functions (statistics.pvariance, numpy.var) use stable methods; writing the shortcut by hand is where the bug enters. Centering data before fitting (subtracting the mean of x) helps regression for the same reason.

## Comparing floating-point numbers

Replace exact equality with a tolerance:

- **Relative tolerance** scales with magnitude: |a − b| ≤ rtol × max(|a|, |b|). Good for most quantities.
- **Absolute tolerance** handles values near zero, where a relative test would demand impossible precision: |a − b| ≤ atol.
- Python's `math.isclose(a, b, rel_tol=1e-9, abs_tol=0.0)` and NumPy's `np.isclose` combine both. Choose tolerances from the problem: a quantity computed by a method with error 10⁻⁶ cannot be tested at 10⁻¹².

Tolerances belong in tests (see the testing lesson), in convergence checks for iterative solvers, and anywhere code branches on a computed number.

## Other traps

- **Summation order:** adding many small numbers to one large one can lose them all; summing small values first, or using compensated summation (math.fsum), keeps them.
- **Integer conversions:** integers above 2⁵³ cannot all be represented exactly as doubles, which matters for large identifiers read as floats from spreadsheets.
- **Overflow and underflow:** products of many probabilities underflow to zero; work with sums of logarithms instead.

## Common mistakes

- Testing floats with ==.
- Computing variance with mean(x²) − mean(x)².
- Using a fixed absolute tolerance for quantities that span many orders of magnitude.
- Multiplying many small probabilities directly.

## Worked example

**Problem.** A likelihood is the product of 500 probabilities, each about 0.01. What happens, and what is the fix?

**Step 1.** The product is about 10⁻¹⁰⁰⁰, far below the smallest positive double (about 10⁻³⁰⁸): it underflows to 0.

**Step 2.** Sum logs instead: 500 × ln(0.01) = -2302.6, a perfectly ordinary number.

**Step 3.** Compare models by differences of log-likelihoods, which are what statistical tests use anyway.

## Limits of this lesson

Examples use IEEE 754 double precision as in standard Python. Other types (32-bit floats on GPUs, decimal or arbitrary-precision arithmetic) have different limits.
