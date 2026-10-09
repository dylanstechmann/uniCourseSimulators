# Integration methods and domain checks

## Learning objectives

1. Select substitution, integration by parts or partial fractions from an integrand's structure.
2. Evaluate definite integrals while carrying bounds and domain conditions.
3. Check an antiderivative by differentiation and diagnose missing factors or singularities.

## Structure before calculation

An integration method is a way to expose a derivative relationship. Before choosing one, inspect products, compositions, rational denominators and the interval. Substitution reverses the chain rule. Integration by parts reverses the product rule. Partial fractions separates rational expressions into simpler terms after any necessary polynomial division. Trigonometric identities can expose useful substitutions, but there is no guarantee that every elementary-looking integrand has an elementary antiderivative. Numerical integration remains a valid option when its assumptions and error are stated.

For a synthetic rate f(t)=2t/(1+t²), the denominator's derivative appears in the numerator. Set u=1+t², du=2t dt. On t from 0 to 2, the new bounds are u=1 and u=5. Thus the integral is ln 5, about 1.609438. The logarithm is dimensionless when the original denominator is dimensionless. If t carries physical time units, a scale must first make the expression dimensionally consistent. Here t is explicitly a dimensionless coordinate, so adding 1 and t² is meaningful.

Substitution can also simplify a trigonometric expression. For ∫₀^(π/2) sin³θ cosθ dθ, choose u=sinθ. The bounds become 0 and 1, and the integral of u³ is 1/4. The radians convention supports the ordinary derivative of sine. This substitution does not require treating sin³θ as an independent function without its accompanying cosine factor.

## Products and integration by parts

From d(uv)=u dv+v du, obtain ∫u dv=uv−∫v du. The minus sign is essential. For ∫₀¹ x eˣ dx, choose u=x and dv=eˣ dx. Then du=dx and v=eˣ. The boundary contribution is e, and the remaining integral is e−1, so the result is 1. Differentiating (x−1)eˣ gives xeˣ, checking both the product and subtraction.

For ∫₁ᵉ ln x dx, take u=ln x and dv=dx. The antiderivative is x ln x−x. At e it is zero, while at 1 it is −1, so the definite integral is again 1. Logarithms require x>0 in this example. A formula containing ln|x| can apply on separate negative and positive intervals, but it cannot authorize integrating through a singularity without an improper-integral analysis.

A poor choice of parts can make the remaining integral harder. That is a reason to reconsider the choice, not evidence that the original integral has no value. Repeated parts can terminate for a polynomial times an exponential because each polynomial derivative lowers its degree. For other products it can generate a relation involving the original integral, which must then be solved algebraically.

## Rational functions

Consider ∫₀¹ 1/((x+1)(x+2)) dx. Both denominator factors stay positive on this interval. Seek A/(x+1)+B/(x+2). Multiplying by the denominator gives 1=A(x+2)+B(x+1), hence A=1 and B=−1. The integral becomes ln(x+1)−ln(x+2), evaluated at the two bounds, yielding ln(4/3), about 0.287682. Both numerator and denominator inside that final ratio are positive.

Repeated factors require a separate term for each power. A denominator (x+1)² does not permit only A/(x+1); it generally needs an additional B/(x+1)². An irreducible quadratic generally needs a linear numerator. If the rational numerator degree is at least the denominator degree, perform division first. These rules come from algebraic decomposition, not a memorized guess that all factors produce logarithms.

The standard integral ∫₀¹ 1/(1+x²) dx equals arctan(1)−arctan(0)=π/4. Its derivative check is especially useful because substituting u=1+x² would introduce an x factor that is absent. Recognizing that mismatch prevents a spurious logarithm answer.

## Worked example

Compare the three structures 2t/(1+t²), xeˣ and 1/((x+1)(x+2)). The first matches a derivative divided by its original function and gives ln 5 on [0,2]. The second combines a polynomial and exponential; parts gives 1 on [0,1]. The third separates into reciprocal linear terms and gives ln(4/3) on [0,1]. Different numerical results are expected because these are three different integrands. For each, differentiate the proposed primitive, verify every denominator on the interval and only then evaluate the endpoints. A calculator value alone would not reveal a missing chain factor or an interval crossing a pole.

## Common mistakes and checks

Do not change the variable while retaining incompatible endpoint values. Either transform both bounds or return to the original variable before evaluation. Do not multiply separate integrals to integrate a product. Do not cancel a denominator factor and forget that the original expression remains undefined at its zero. A removable expression can have a continuous extension, but that extension must be stated when interpreting the original function.

For a dimensional rate, the definite integral has rate times time units. A negative definite integral can represent signed change even when geometric area would be nonnegative. Checking scale and sign is part of method selection: a positive integrand on a positive-width interval cannot have a negative integral. A numerical quadrature check provides another calculation route, though agreement between two calculations does not establish the validity of a physical model.

## Limits of this lesson

All rate and coordinate examples are synthetic mathematical constructions. The lesson does not present a universal algorithm for elementary antiderivatives, a complete catalog of trigonometric substitutions or a symbolic grader for logarithmic and exponential expressions. Practice checks selected numbers and method choices. It does not automatically assess a written derivation or certify integration mastery. Original explanation and examples were developed with substantial AI assistance, using existing calculus scope references without reproducing third-party text. The course remains partial, unreviewed and formative-only.
