# Limits, continuity and the definition of a derivative

A calculation near a point and a claim about what happens at that point are different things. A sensor model may have a removable algebraic hole, a threshold response may jump, and a continuous displacement can have a sharp corner. Calculus starts by distinguishing these situations. This lesson develops limits through algebra and an explicit error criterion, then defines a derivative as a limit of slopes. All numerical examples are synthetic mathematical exercises. A finite table of measurements can suggest a limit, but cannot establish one without assumptions about the function between the observations.

## Learning objectives

1. Evaluate a limit and justify a simple epsilon–delta error criterion.
2. Distinguish a limit, a function value and continuity, including one-sided behavior.
3. Compute a derivative from its difference quotient and recognize failure at a corner.

## A limit is a nearby-value claim

The statement lim_(x→a) f(x) = L means that f(x) becomes arbitrarily close to L when x is sufficiently close to a, with x different from a. It does not prescribe f(a). For g(x) = (x² − 4)/(x − 2), defined away from 2, factoring gives g(x) = x + 2 whenever x ≠ 2. Therefore the limit at 2 is 4 even though the original quotient is undefined there. Defining g(2) = 4 fills the hole continuously. Defining g(2) = 9 leaves the same limit but makes the function discontinuous at 2.

Cancellation in this example is an identity on the punctured domain. It is not permission to substitute into the original zero denominator. Record the domain before simplifying. A graph that omits the point may hide the distinction, and a rounded table may make a discontinuity look smooth. Algebra identifies what the graph alone cannot certify.

## Making closeness precise

For f(x) = 2x + 1 at a = 3, the proposed limit is 7. Let ε be any positive output tolerance. We need a positive input radius δ such that 0 < |x − 3| < δ implies |f(x) − 7| < ε. Here |f(x) − 7| = 2|x − 3|, so choosing δ = ε/2 proves the claim. For ε = 0.1, δ = 0.05 works. Both inequalities are strict: a point exactly at the input boundary is not included in this neighborhood statement.

This is a complete argument for every positive ε, not merely a check at ε = 0.1. More complicated functions may require a preliminary bound on x before choosing δ. The order matters: the desired output accuracy is supplied first; the neighborhood size may depend on it. A limit proof must not choose a fixed neighborhood and then claim arbitrarily small output error inside it.

## Continuity and one-sided limits

A function is continuous at a when it is defined there, its two-sided limit exists, and that limit equals f(a). A two-sided limit requires matching left and right limits. A threshold rate that is 0 below a and 5 above a has left limit 0 and right limit 5. No choice of its value at a makes the two-sided limit exist. For a function defined only on a closed interval, continuity at an endpoint uses the available one-sided limit relative to that domain.

The absolute-value function f(x) = |x| is continuous at 0: |f(x) − 0| = |x|, so δ = ε works. Continuity says nearby values are nearby; it does not say the graph has a unique tangent. Conversely, a derivative can exist only where the function is continuous. If a difference quotient has a finite limit, writing f(a+h) − f(a) as h times that quotient shows the function difference tends to zero.

## Slopes become derivatives

The derivative at a is f′(a) = lim_(h→0) [f(a+h) − f(a)]/h, when this finite two-sided limit exists. The numerator is a change in output and the denominator is a change in input. For f(x) = x² at a = 3, expanding gives [(3+h)² − 9]/h = 6 + h for h ≠ 0. The limit is 6. At h = 0.1 the secant slope is 6.1, whose absolute difference from the derivative is 0.1. To keep this slope error at most 0.01, take |h| at most 0.01, with h nonzero.

For f(x) = |x| at 0, the quotient is |h|/h: it is 1 for h > 0 and −1 for h < 0. The two one-sided slopes disagree, so the derivative does not exist. Reporting an average slope of zero would not repair that failure. The function's continuity and its lack of differentiability are compatible.

## Stable algebra before numerical substitution

For f(x) = √x at 9, the quotient [√(9+h) − 3]/h involves subtracting close values when h is small. Multiplying by the conjugate gives 1/[√(9+h) + 3], for h ≠ 0 and 9+h ≥ 0. Its limit is 1/6. The rationalized expression avoids a subtraction that can lose useful digits in finite-precision arithmetic. Taking ever smaller h in the original expression is not a numerical proof of the derivative; rounding can eventually dominate the difference.

## Worked example

Consider H(x) = (x² − 1)/(x − 1) for x ≠ 1, and H(1) = A. Factoring gives H(x) = x + 1 away from the hole, so its limit at 1 is 2. Continuity requires A = 2. With that choice, [H(1+h) − H(1)]/h = [(2+h) − 2]/h = 1 for every nonzero h, hence H′(1) = 1. If A = 5 instead, the quotient is (h − 3)/h and has no finite two-sided limit. Filling the hole incorrectly changes differentiability even though the nearby formula remains the same.

## Common mistakes

- Substituting into a zero denominator before identifying a removable factor.
- Assuming the value at a point determines its limit.
- Checking only one side of an interior point.
- Equating continuity with differentiability.
- Using a finite table or a very small numerical step as a complete limit proof.

## Limits of this lesson

The proofs concern stated exact functions, not unobserved experimental behavior. Measured data need a model and uncertainty assumptions before a derivative or continuity claim is interpreted physically. This lesson introduces epsilon–delta reasoning for simple functions; it is not a complete course in real analysis or a validated sensor model.
