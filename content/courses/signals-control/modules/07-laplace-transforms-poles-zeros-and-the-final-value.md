# From a transfer function to a time response: Laplace transforms, poles, zeros and the final value

A heated chamber, a sensor and a perfusion line are each described by a differential equation, and the question that a control engineer asks of the equation is rarely the exact solution. It is how fast the output moves, where it ends up, whether it overshoots and whether anything can make it grow without bound. The Laplace transform turns a linear differential equation into algebra, and the result, the transfer function, answers those questions from the location of a few numbers called poles and zeros. This lesson defines the transfer function, reads the time constants and the DC gain from it, builds a step response by partial fractions, uses the final value theorem and shows what a zero in the wrong half of the plane does. All values are synthetic.

## Learning objectives

By the end of this lesson, you should be able to:

1. Find the poles, the DC gain and the dominant time constant of a transfer function.
2. Use partial fractions to write and evaluate the step response of a stable system with real poles.
3. Apply the final value theorem and interpret zeros and poles in the right half-plane.

## Transforms and transfer functions

The Laplace transform of a signal f(t) is F(s) = ∫ f(t) e^(−st) dt from 0 to infinity. Three pairs are enough for this lesson: a unit step has transform 1/s, a decaying exponential e^(−at) has transform 1/(s + a), and the derivative rule is L{dy/dt} = sY(s) − y(0). For a system that starts at rest, differentiation in time becomes multiplication by s, and a linear differential equation becomes a ratio of polynomials. The **transfer function** is G(s) = Y(s)/U(s), the output transform divided by the input transform.

For the incubator of the earlier lesson, τ dy/dt = −y + K u with K = 0.5 °C/W and τ = 10 min becomes (τs + 1)Y(s) = K U(s), so G(s) = K/(τs + 1). A step of u₀ watts has U(s) = u₀/s, so Y(s) = K u₀/(s(τs + 1)), which is a sum of a constant and a decaying exponential: y(t) = K u₀ (1 − e^(−t/τ)). Time in this example is in minutes, and the single pole is at s = −1/τ = −0.1 per minute.

## Poles, zeros and the DC gain

The **poles** are the roots of the denominator of G(s), and the **zeros** are the roots of the numerator. Each real pole at s = −p contributes a term e^(−pt) to the response, with time constant 1/p, so poles farther from the origin in the left half-plane correspond to faster terms. The pole closest to the origin is the slowest, and for times well after the fast terms have died out it sets the shape of the response. A pole with a positive real part contributes a term that grows without bound, so a system with any pole in the right half-plane is unstable. The **DC gain** is G(0), the ratio of the final output to a constant input.

**Synthetic example (time in seconds):** G(s) = 20/((s + 2)(s + 10)) has poles at s = −2 and s = −10 and a DC gain of 20/(2 × 10) = **1**. The slowest pole has a time constant of 1/2 = 0.5 s.

## Step response by partial fractions

For a unit step, Y(s) = G(s)/s = 20/(s(s + 2)(s + 10)). Writing this as A/s + B/(s + 2) + C/(s + 10), the coefficient of each term is found by covering its factor and evaluating the rest at the pole: A = 20/(2 × 10) = 1, B = 20/((−2)(−2 + 10)) = **−1.25** and C = 20/((−10)(−10 + 2)) = **0.25**. Therefore

**y(t) = 1 − 1.25 e^(−2t) + 0.25 e^(−10t).**

At t = 0.5 s, y = 1 − 1.25 e^(−1) + 0.25 e^(−5) = **0.5418**. The fast term has almost vanished by t = 0.4 s, so after that the response is the slow exponential 1 − 1.25 e^(−2t), and the time to settle within 2% of the final value is close to four time constants of the slow pole: 4 × 0.5 = 2 s (the exact value for this response is 2.07 s).

## The final value theorem

If every pole of sY(s) lies in the left half-plane, the final value of the output is y(∞) = lim as s → 0 of sY(s). For a step input of size u₀ this reduces to y(∞) = G(0) u₀. **Synthetic example:** for Y(s) = 5(s + 4)/(s(s² + 6s + 10)), the roots of s² + 6s + 10 are −3 ± j, in the left half-plane, so y(∞) = 5 × 4/10 = **2.0**. The condition matters: for a transfer function with a pole at s = +1 the limit exists as a number but the output never reaches it, and using the theorem there gives a confident wrong answer.

## Zeros and the wrong-way start

A zero shapes how the output starts. A zero in the left half-plane makes the response faster; a zero in the **right half-plane** makes the step response begin in the opposite direction before it turns around. **Synthetic example:** G(s) = (1 − 0.5s)/(s + 1)² has a zero at s = +2 and a step response y(t) = 1 − e^(−t) − 1.5 t e^(−t), which at t = 0.5 is **−0.0614**: negative, although the final value is +1. Plants of this kind (the water level in a boiler drum, which first swells when steam demand rises, or a reactor whose outlet briefly moves the wrong way) limit how fast a feedback loop can be made, because a controller that reacts to the early wrong-way motion pushes in the wrong direction.

## Common mistakes

- Reading the pole value as the time constant instead of its reciprocal.
- Applying the final value theorem when a pole of sY(s) is in the right half-plane or on the imaginary axis.
- Assuming the fastest pole dominates; the slowest stable pole controls the long-time behaviour.
- Forgetting that a transfer function describes a system at rest, with zero initial conditions.
- Taking the DC gain as the final value for an input that is not a constant.
- Mixing units: poles in per-second and time in minutes.

## Worked example

**Problem.** For G(s) = 12/((s + 1)(s + 4)), find the poles, the DC gain, the step response, its value at t = 2 s and the 2% settling time.

**Step 1: poles and gain.** The poles are −1 and −4, and G(0) = 12/(1 × 4) = **3**.

**Step 2: partial fractions.** Y(s) = 12/(s(s + 1)(s + 4)): A = 3, B = 12/((−1)(3)) = −4 and C = 12/((−4)(−3)) = 1, so y(t) = 3 − 4e^(−t) + e^(−4t).

**Step 3: value at 2 s.** y(2) = 3 − 4 × 0.1353 + 0.0003 = **2.459**.

**Step 4: settling.** The slow pole is −1, with a time constant of 1 s, so four time constants is 4 s; the exact 2% time is 4.20 s.

## Limits of this lesson

All numbers are synthetic. The lesson covers linear systems with rational transfer functions, starting at rest, and real poles or the simplest complex pair; it does not cover repeated poles in general, time delays, nonlinearity or saturation, and the settling-time rule of four time constants is an approximation for systems with one dominant pole.
