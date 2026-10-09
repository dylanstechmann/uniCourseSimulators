# Oscillations, damping and energy balance

## Learning objectives

1. Calculate natural and damped frequencies under a stated mass–spring model.
2. Relate the damped solution to initial conditions and an energy-loss balance.
3. Distinguish decay, critical damping and driven-response claims.

## A restoring law and an equilibrium

Let x measure displacement from a supplied equilibrium of a synthetic point mass on a linear spring. The restoring force is −kx and an ideal linear drag is −c dx/dt. With no external drive after the initial displacement, the model equation is m d²x/dt²+c dx/dt+kx=0. Gravity can already be accounted for in the equilibrium coordinate; do not add its static offset again without redefining x.

Stipulate m=0.50 kg, k=50 N/m and c=0.80 N·s/m. These are teaching parameters rather than measured device or tissue properties. The undamped natural angular frequency is ω₀=√(k/m)=10 rad/s. The damping decay parameter is δ=c/(2m)=0.80 s⁻¹. Angular frequency and ordinary frequency differ by 2π; radians per second should not be read as cycles per second.

## Underdamped time dependence

The selected parameters satisfy δ<ω₀, so damped angular frequency is ω_d=√(ω₀²−δ²)=√99.36≈9.967949 rad/s. The damped period is 2π/ω_d, approximately 0.63034 s. The [OpenStax damped-oscillation section](https://openstax.org/books/university-physics-volume-1/pages/15-5-damped-oscillations) is a link-only reference for the basic regime distinction; all numerical examples here are constructed independently.

For initial displacement x₀=0.020 m and initial velocity zero, the solution is x=x₀exp(−δt)[cos(ω_dt)+(δ/ω_d)sin(ω_dt)]. The sine term ensures zero initial derivative even though the exponential is already decaying. Writing only x₀exp(−δt)cos(ω_dt) would instead imply initial velocity −δx₀, a different initial condition.

The envelope coefficient decays with exp(−δt). Its half-time is ln2/δ≈0.866434 s. That envelope half-time is not a period, and it is not necessarily the time of a particular signed displacement crossing. Oscillation can carry x through zero many times while the envelope remains positive. State whether an observed quantity is displacement, absolute peak amplitude, velocity or energy before fitting a decay.

## Mechanical energy provides a second check

Instantaneous mechanical energy is E=0.5m(dx/dt)²+0.5kx². Initially the mass is at rest, so E₀=0.5×50×0.020²=0.0100 J. Multiplying the differential equation by velocity yields dE/dt=−c(dx/dt)². For positive c, the energy is nonincreasing and the integral of drag dissipation equals the mechanical-energy reduction in this selected unforced model.

Energy is not generally an exact simple exponential at every instant for an arbitrary underdamped initial condition. Its slope depends on instantaneous velocity, becoming zero at displacement turning points even while the overall motion decays. An envelope or cycle-averaged approximation can have a simpler decay, but that should be labeled rather than substituted for the exact instantaneous balance.

This energy identity also checks sign conventions. A force +c dx/dt would add energy and produce a different unstable model, not passive damping. If a numerical trajectory gains energy with the declared negative drag and no drive, investigate the calculation, step size or implementation before assigning a physical explanation.

## The damping boundary

Critical damping in this constant-parameter model occurs at c_crit=2√(mk)=10 N·s/m. At that boundary the characteristic equation has a repeated negative root. Larger positive c gives two real negative modes rather than an underdamped sinusoid. Substituting such parameters into the underdamped frequency formula and ignoring an imaginary result would apply the wrong solution family.

Critical damping is a particular mathematical regime; it is not a universal design recommendation or proof of fastest response under every performance metric. Initial conditions, constraints and the quantity being optimized matter. The model provides neither a real device's allowed displacement nor a clinical interpretation of a measured oscillation.

## Forcing changes the question

With a sinusoidal applied force, a driven response depends on forcing frequency as well as m,k,c. The displacement response can peak near but not exactly at ω₀ when damping is nonzero. Different observed quantities, such as velocity or transmitted force, can have different peaks. A frequency at which one plotted signal is largest does not uniquely identify stiffness without mass, damping and observation information.

A transient after a step or release also differs from the final steady driven response. Observation offset or gain can alter an amplitude estimate without changing the actual displacement equation. Conversely, a change in mass or boundary conditions can change the true natural frequency. Distinguishing these possibilities needs independent evidence, continuing the calibration/model separation in the lab.

## Worked example

Calculate ω₀=10 and δ=0.80, confirm the underdamped inequality and obtain ω_d from their squared difference. Divide 2π by ω_d for period and ln2 by δ for envelope half-time. Use the zero-velocity initial condition to retain the sine term. Independently compute initial energy 0.0100 J and verify that any integrated trajectory loses exactly the modeled drag energy. Compare c with 10 N·s/m before deciding which regime formula applies.

## Common mistakes

Do not confuse radians with cycles, decay half-time with period or envelope loss with exact instantaneous energy decay. Check initial velocity as well as displacement. Do not use an underdamped sinusoid beyond its regime or infer a unique material property from a response peak alone.

## Limits of this lesson

All parameters and motions are synthetic. Linear spring, linear drag and point-mass assumptions establish no real damping law, device stability limit or biological diagnosis. No apparatus or measurement procedure is supplied. Original instruction has substantial AI assistance. The package remains partial, unreviewed and formative-only.
