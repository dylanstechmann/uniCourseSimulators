# Numerical ODEs and error control

Forward Euler updates xₙ₊₁=xₙ+h f(tₙ,xₙ); it is first-order accurate globally and can be unstable for a step size that is too large. Higher-order Runge-Kutta methods improve accuracy per step but still require convergence checks. Compare solutions at h and h/2, monitor units and conserved quantities, and document solver tolerances. For stiff biochemical systems, explicit methods may need impractically small steps; implicit solvers can be more stable.
