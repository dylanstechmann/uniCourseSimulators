# Taylor polynomials and integrated error

## Learning objectives

1. Build Taylor polynomials with the correct center, factorial and degree.
2. Compare Lagrange and alternating-series bounds with actual approximation errors.
3. Carry a pointwise remainder into an accumulated integral and select a sufficient order.

## Coefficients from local derivatives

The degree-n Taylor polynomial centered at a is Pₙ(x)=Σ_(j=0)^n f^(j)(a)(x−a)ʲ/j!. Degree and number of terms are distinct. A cubic exponential polynomial has four terms, while a sine polynomial of degree five has three nonzero terms. Zero coefficients still matter when describing the degree and the derivative order needed by an error theorem.

For e^(−x) at zero, P₃=1−x+x²/2−x³/6. At x=0.4 the value is 0.669333. The true e^(−0.4) is about 0.670320, so the polynomial is low by about 0.000987. Because the exponential series alternates with decreasing term magnitudes at this positive argument, the first omitted term gives a bound 0.4⁴/24=0.001067. The error sign agrees with the positive omitted fourth-degree term.

For eˣ at x=0.5, all terms are positive, so the alternating theorem does not apply. The cubic polynomial is 1.645833. A Lagrange bound uses the fourth derivative eˣ, whose maximum on [0,0.5] is e^0.5. The error is at most e^0.5(0.5)⁴/24, about 0.004294. The actual error is about 0.002888. Substituting the derivative only at the center would give a smaller number without establishing that it bounds the remainder.

## Lagrange's remainder and assumptions

If f has the required derivatives on the interval connecting a and x, and |f^(n+1)(s)|≤M throughout that interval, then |f(x)−Pₙ(x)|≤M|x−a|^(n+1)/(n+1)!. This is a sufficient bound. It may be conservative, and failure of the bound to meet a target does not prove that the actual approximation error exceeds that target.

For sin x, the fifth-degree polynomial x−x³/6+x⁵/120 evaluated at 0.6 is 0.564648. The first omitted magnitude 0.6⁷/5040 is about 5.554 × 10⁻⁶, bounding the alternating remainder. This uses the sine series' odd-power structure. A generic degree-five Lagrange bound would involve a sixth derivative and need its own bound; it is not interchangeable with the sharper series-specific argument without explanation.

Changing the center can improve a local approximation without increasing degree. For ln x around a=1, write x=1+h and expand ln(1+h). Real logarithms require x>0; a polynomial being defined at negative x does not extend the original function's domain. The expansion radius is constrained by the singularity at x=0, even though the function remains defined far to the right.

## Integrating an approximation

Suppose an integrand satisfies |f(x)−P(x)|≤B(x) on [a,b]. Then the accumulated error satisfies |∫ₐᵇ(f−P)dx|≤∫ₐᵇB(x)dx. A uniform bound E gives the simpler estimate (b−a)E. Integrating a variable bound often produces a sharper result than multiplying the largest pointwise error by the whole interval length.

For the synthetic dimensionless accumulation ∫₀^0.4 e^(−x)dx, integrating P₃ gives x−x²/2+x³/6−x⁴/24 at 0.4, or 0.3296. The exact accumulation is 1−e^(−0.4), about 0.329680. Since the pointwise alternating bound is x⁴/24 for every x in this interval, the integrated error is at most 0.4⁵/120, about 8.5333 × 10⁻⁵. The actual error is about 7.9954 × 10⁻⁵. Using the endpoint pointwise bound times 0.4 would also be safe but less sharp.

The integral's output units include interval units. If a rate approximation error is bounded in amount per hour and integrated over hours, the accumulated error is in amount. A dimensionless exponential argument requires a rate constant times time. Missing this normalization can turn an apparently small numerical remainder into a dimensionally meaningless statement.

## Selecting order

At x=0.8, a degree-n exponential-decay polynomial has alternating bound 0.8^(n+1)/(n+1)! because term magnitudes decrease. For tolerance 0.0001, n=5 gives about 0.000364, while n=6 gives about 0.00004161. Degree six is therefore the first sufficient degree under this bound. This choice includes seven terms, indices zero through six. The arithmetic should retain enough precision to distinguish the neighboring orders.

## Worked example

Approximate the accumulation ∫₀^0.4 e^(−x)dx by integrating the cubic polynomial. The result is 0.3296. Establish the pointwise error x⁴/24 using alternating terms decreasing throughout [0,0.4], then integrate that bound to get 8.5333 × 10⁻⁵. Compare the exact value 0.329680 only after constructing the certificate. The actual error falls below the guarantee. This sequence separates an approximation, a theorem-based error statement and a reference check; knowing the reference value was not necessary for the bound.

## Common mistakes and checks

Do not omit factorials or confuse the first omitted degree with the number of included nonzero terms. Do not apply an alternating bound to eˣ at positive x. Do not use a bound at one point as though it held throughout an integration interval. Keep truncation, numerical rounding, input uncertainty and model discrepancy separate; only the first is covered by these remainder formulas.

## Limits of this lesson

All numerical targets are synthetic mathematical examples. The lesson does not guarantee that an arbitrary infinitely differentiable function equals its Taylor series, nor does it assess physical-model validity. Automated items check numbers and interpretations instead of grading derivations. Original content was developed with substantial AI assistance. The course remains partial, unreviewed and formative-only, with accessibility and qualified mathematical review outstanding.
