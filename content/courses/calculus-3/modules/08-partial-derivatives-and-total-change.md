# Partial derivatives and total change

## Learning objectives

1. Calculate partial and mixed derivatives while stating which variables are held fixed.
2. Use tangent planes and the multivariable chain rule for local change along a path.
3. Distinguish differentiability from isolated partial derivatives and bound a local remainder.

## Holding a coordinate fixed

For a scalar function f(x,y), f_x measures change in x while y stays fixed; f_y does the converse. Neither automatically gives the change along a path where both coordinates vary. For the synthetic dimensionless field f(x,y)=x²y+sin y, the derivatives are f_x=2xy and f_y=x²+cos y. At (2,0) they are 0 and 5. A zero x partial at this point does not mean the field is constant in a whole neighborhood; the y direction still has a nonzero slope.

The mixed derivatives are f_xy=f_yx=2x, hence 4 at (2,0). Their equality here follows from the smooth polynomial and sine terms. A common sufficient condition for equality is continuity of the mixed second partials in a neighborhood. Equality is not obtained simply by swapping symbols without checking whether the needed derivatives exist and satisfy the theorem's conditions.

The gradient collects coordinate slopes. It acts on a displacement h=(h_x,h_y) through the dot product ∇f·h. Coordinates need a consistent physical scale if a Euclidean gradient norm is interpreted as slope per distance. When variables represent different kinds of inputs, such as time and temperature, their partials have different units and should not be combined into an unqualified spatial magnitude.

## Differentiability and a tangent plane

Differentiability at a point means there is a linear approximation with remainder small compared with |h| as h approaches zero through every direction. For a differentiable field, f(a+h)=f(a)+∇f(a)·h+o(|h|). The tangent-plane approximation is therefore a statement about simultaneous small changes, not only coordinate-axis limits.

At (2,0), f is zero and the tangent approximation is 5h_y. For h=(0.1,0.02), it predicts 0.1. The exact value is (2.1)²(0.02)+sin(0.02), approximately 0.108199. The difference arises from terms beyond the first-order plane. A linear approximation need not have zero error merely because one partial derivative happens to vanish.

The function g(x,y)=xy/(x²+y²) away from the origin, extended by g(0,0)=0, illustrates a failure. Along either coordinate axis it is zero, so both origin partial derivatives exist and equal zero. Along y=x away from the origin it equals 1/2, so it is not continuous at the origin and cannot be differentiable there. Axis data alone miss the problem. Testing a few paths can disprove a limit but cannot prove a general two-variable limit without a broader argument.

## A path makes both coordinates change

For a differentiable f and differentiable path x(t),y(t), the chain rule gives df/dt=f_x x′+f_y y′. Evaluate partials at the point on the path, not at an unrelated center. For x=1+t and y=t², at t=1 the point is (2,1), with x′=1 and y′=2. In the synthetic field above, f_x=4 and f_y=4+cos 1. Thus df/dt=12+2 cos 1, approximately 13.080605.

The two contributions have distinct meanings. The first records horizontal motion through the x slope; the second records vertical motion through the y slope. Neglecting either moving coordinate changes the derivative. Directly substituting the path into f and differentiating the resulting one-variable expression provides a separate check.

If the scalar field also depends explicitly on time, f(x(t),y(t),t), add f_t. Motion through a static field and evolution of the field at a fixed location are different mechanisms. Their sum is often called the material derivative for a specified velocity field, but the mathematical chain rule does not establish that a physical process follows that velocity.

## A bounded quadratic remainder

For q(x,y)=x²+y², the Hessian is 2I everywhere. The tangent approximation at (1,2) is 5+2h_x+4h_y. The exact remainder is h_x²+h_y². With h=(0.1,−0.2), the predicted value is 4.4, the true value is 4.45 and the error is 0.05.

More generally, if the Hessian operator norm is at most M throughout the line segment from a to a+h, a second-order argument gives absolute linearization error at most M|h|²/2. For this quadratic M=2, so the bound equals 0.05 exactly. A Hessian value at one point alone does not certify a bound throughout a neighborhood for an arbitrary function.

## Worked example

For f=x²y+sin y, compute coordinate derivatives before evaluating them. At (2,0), f_x=0, f_y=5 and f_xy=4. The displacement (0.1,0.02) gives a tangent prediction of 0.1. Along the different path x=1+t,y=t² at t=1, evaluate the partials at (2,1) and include both path velocities, giving 13.080605. These values differ because the derivative questions differ. One concerns a local plane near (2,0), and the other concerns a moving point at (2,1).

## Common mistakes and checks

Do not infer continuity or differentiability solely from existing coordinate partials. Do not omit a chain-rule contribution from a changing variable. Keep angles in radians when differentiating sine. Distinguish exact finite change, tangent prediction and an error guarantee. A second-order bound controls mathematical linearization under its assumptions, not input uncertainty or physical-model mismatch.

## Limits of this lesson

All fields and paths are synthetic. The lesson develops selected smooth examples and a counterexample, not a full proof of every multivariable limit theorem. Practice checks numerical derivatives and chosen interpretations, not written proofs. Original content has substantial AI assistance. Mathematical accessibility and qualified review remain outstanding; the course remains partial, unreviewed and formative-only.
