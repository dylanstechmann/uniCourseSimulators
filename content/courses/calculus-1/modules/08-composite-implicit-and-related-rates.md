# Composite functions, implicit curves and related rates

A response may depend on concentration while concentration depends on time. A geometric constraint may connect two moving coordinates without giving either as an explicit function of the other. Derivatives track these dependencies only when the variable with respect to which we differentiate remains clear. This lesson develops the chain rule, implicit differentiation and related rates through synthetic response and geometry models. It separates a total time derivative from a derivative that holds another variable fixed. The numerical models are teaching examples, not operating instructions for a device or biological experiment.

## Learning objectives

1. Differentiate composite and product functions while keeping their dependencies and units explicit.
2. Differentiate an implicit curve and identify where its slope formula is valid.
3. Calculate a related rate when more than one geometric quantity changes.

## Composition and the chain rule

Suppose a synthetic response is R(c) = 100c/(2+c), where c is a concentration expressed in one chosen unit and R is in signal units. Let c(t) = 1 + 0.5t with t in hours. Differentiate the outer function first: the quotient rule gives R′(c) = [100(2+c) − 100c]/(2+c)² = 200/(2+c)². Then dR/dt = R′(c(t))c′(t). At t = 2, c = 2, R = 50, R′ = 12.5 signal units per concentration unit, and c′ = 0.5 concentration units per hour. Their product is 6.25 signal units per hour.

The derivative 12.5 is not the time rate 6.25. The intermediate concentration units cancel in the chain-rule product. If concentration stopped changing at that moment, dR/dt would be zero even though R′(2) is not zero. If a sensor's response also depended directly on temperature, and temperature varied in time, a further dependency would be needed. The single-variable chain rule cannot silently represent an omitted changing input.

## Products describe competing changes

Let F(t) = t²e^(−t), with t a dimensionless model coordinate. Product and chain rules give F′(t) = 2te^(−t) − t²e^(−t) = e^(−t)(2t − t²). At t = 3, F′ = −3e^(−3) = −0.149361. The polynomial factor is increasing for positive t, yet the entire product is decreasing after t = 2 because the exponential decrease wins. Differentiating only the increasing factor would give the wrong sign.

For y = (3x+1)⁴, differentiating the outer fourth power gives 4(3x+1)³ and differentiating its inner argument gives 3. Thus y′ = 12(3x+1)³. The chain factor belongs in the answer even if the inner expression looks simple. Derivative rules are consequences of the difference-quotient definition; they reduce repeated expansions rather than replacing the dependency argument.

## An implicit curve

On the circle x² + y² = 25, treat y as a local function of x. Differentiating gives 2x + 2y(dy/dx) = 0, so dy/dx = −x/y where y ≠ 0. At (3, 4), the slope is −3/4. On the lower branch at (3, −4), it is +3/4. The same x-coordinate can correspond to different points and different slopes, so the branch or full point must be stated.

At (5, 0), division by y fails. The circle has a vertical tangent there; it does not have a finite dy/dx at that point. One can instead locally express x in terms of y and obtain dx/dy = −y/x = 0. This change of coordinate resolves the representation issue, but it does not turn the vertical tangent into a finite slope in the original coordinates.

If x and y both depend on time, differentiate the same circle constraint with respect to time: 2x x′ + 2y y′ = 0. At (3, 4) with x′ = 2 length units per second, y′ = −(3/4) × 2 = −1.5 length units per second. The implicit slope and the horizontal speed combine through the chain rule.

## Geometry rates need a constraint first

For a sphere of radius r, V = (4/3)πr³. If the radius changes at r′ = 0.1 cm/min when r = 2 cm, then V′ = 4πr²r′ = 1.6π = 5.026548 cm³/min. The radius itself must be evaluated at the same time as its rate. Substituting r = 2 into V before differentiating would produce a constant and erase the changing radius.

For a cylinder, V = πr²h. If both r and h vary, V′ = π(2r r′h + r²h′). At r = 2 cm, h = 3 cm, r′ = 0.1 cm/min and h′ = −0.2 cm/min, the two terms inside π are 1.2 and −0.8, so V′ = 0.4π = 1.256637 cm³/min. Ignoring the falling height would overestimate the volume increase. Holding h fixed computes a different hypothetical rate from the actual total rate.

## Worked example

Use the same response R(c) but let c(t) = 4e^(−0.2t). At t = 0, c = 4 and c′ = −0.8 concentration units per hour. The response slope is 200/(2+4)² = 50/9, so dR/dt = (50/9)(−0.8) = −40/9 = −4.444444 signal units per hour. The negative sign indicates a falling signal. It does not mean a negative concentration or a negative response. The derivative describes local change in a positive quantity.

## Common mistakes

- Omitting the inner derivative in a composition.
- Differentiating an implicit y² as if y were constant.
- Using an implicit slope formula at a point where its denominator vanishes.
- Substituting an instantaneous radius before differentiating its time dependence.
- Dropping one changing quantity from a product in a related-rate calculation.

## Limits of this lesson

All examples assume differentiable functions and exact stated constraints. Measured rates can be noisy, geometric models can be approximate and unmodeled variables can change. The calculations demonstrate dependency reasoning and dimensional interpretation; they establish no real response curve, growth law or device setting.
