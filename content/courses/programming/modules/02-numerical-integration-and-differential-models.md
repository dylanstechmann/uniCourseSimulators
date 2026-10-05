# Numerical integration and differential models

Numerical integration approximates a continuous process from discrete samples. Forward Euler is transparent but first-order accurate and conditionally stable; higher-order Runge-Kutta improves local approximation at added computation. Step size, solver tolerances, stiffness, and measurement noise all affect the answer. Validate by halving the step, checking limiting cases, and comparing against analytic or conservation-based results when available. A visually smooth curve is not evidence of numerical accuracy.
