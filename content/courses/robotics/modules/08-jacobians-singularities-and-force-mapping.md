# Jacobians, singularities and force mapping

**Status:** original formative instruction with substantial AI assistance. Arms, speeds, forces and damping values are synthetic. This lesson distinguishes three calculations that are often conflated: forward velocity, inverse velocity and the torque associated with a stated endpoint force. Prerequisites are planar kinematics and labeled frames.

## Learning objectives

1. Calculate planar endpoint velocity and check the Jacobian against position differences.
2. Diagnose lost instantaneous motion directions and constrained inverse-velocity demands.
3. Relate endpoint force to joint torque through power without inferring a hardware stall from geometry alone.

## Differentiate the position model

For link lengths L₁,L₂ and relative elbow angle q₂, x=L₁cosq₁+L₂cos(q₁+q₂) and y=L₁sinq₁+L₂sin(q₁+q₂). The linear velocity is v=J(q)q̇, with Jacobian rows [−L₁sinq₁−L₂sin(q₁+q₂),−L₂sin(q₁+q₂)] and [L₁cosq₁+L₂cos(q₁+q₂),L₂cos(q₁+q₂)]. Joint rates are radians per second; entries of this position Jacobian have units meters per radian.

Each column describes the endpoint velocity caused by one unit joint rate while the other joint is held fixed. The columns add linearly at the current configuration. This is a local instantaneous relation. Using one frozen Jacobian for a long motion ignores how its columns rotate and change length as the arm moves.

A finite-difference check changes one joint by a small angular increment and compares the position difference divided by that increment with the corresponding column. Several increment sizes help distinguish truncation error from floating-point subtraction error. The calculation uses radians internally; a degree-valued increment without conversion changes the derivative scale.

## Rank determines the available directions

The determinant is L₁L₂sin q₂. It vanishes at a straight or fully folded configuration. With positive link lengths and other elbow angles, the square position Jacobian is invertible. At q₁=q₂=0, both columns point in the y direction. No finite instantaneous joint rate produces an x velocity there, even though a finite bending motion can change x at second order.

The distinction between position reachability and instantaneous velocity is important. A target can lie in the geometric workspace while a selected motion direction at the current pose is poorly conditioned. At the exact boundary, an outward radial target may also be unreachable. Those statements arise from different checks and should not be substituted for one another.

Near a singularity, a desired velocity in a weak direction can require large joint rates. A tangential direction may remain easy. A determinant gives a quick planar indicator, but its magnitude depends on length scale; singular values describe directional gain more directly. A condition number becomes meaningful only after task coordinates and their units are defined, especially when angular and linear motion are combined.

## Damping trades motion error for smaller commands

An unconstrained inverse enforces Jq̇=v when J is invertible, regardless of actuator limits. Damped least squares instead minimizes ||Jq̇−v||²+λ²||q̇||² in a consistently scaled problem. Its solution is Jᵀ(JJᵀ+λ²I)⁻¹v. The extra term reduces amplification in weak directions but generally leaves a nonzero task-velocity residual. It does not create a motion direction absent from the Jacobian.

For a singular-direction scalar gain σ, damping changes the inverse gain from 1/σ to σ/(σ²+λ²). A chosen λ has a meaning only relative to the coordinate scale and performance objective. A speed-constrained optimization or uniform slowdown is another policy. Independently clipping each joint rate can change endpoint direction; uniformly scaling all rates preserves the requested direction under the frozen linear mapping but reduces speed.

## Force mapping follows virtual power

For an endpoint force F expressed in the same base coordinates as v, define τ=JᵀF. Then τᵀq̇=Fᵀv. This equality relates the chosen endpoint force contribution to generalized joint torque. If F is an external force acting on the robot, a static balancing actuator contribution has the opposite sign. State that sign convention before interpreting a motor command.

Crucially, JᵀF does not automatically diverge as the Jacobian becomes singular. At a straight horizontal arm, a purely radial x force has zero moment about these ideal joints, so its joint-torque contribution is zero. The structure can still carry internal loads. Large inverse rates for a prescribed velocity and torque requirements for a prescribed force are different questions. Dynamic torque for executing a trajectory can be large because of inertia and acceleration, but needs a dynamic model.

## Worked example

Take L₁=0.30 m,L₂=0.20 m,q₁=0,q₂=90°. The Jacobian is approximately [−0.2,−0.2;0.3,0], with determinant 0.06 m². Desired inward velocity (−0.01,0) m/s requires q̇₁=0 and q̇₂=0.05 rad/s. For F=(5,0) N, τ=(−1,−1) N·m. Those signed torques describe JᵀF, not a complete actuator command including gravity or friction.

For q̇=(0.1,0.2) rad/s, v=(−0.06,0.03) m/s. With F=(5,2) N, endpoint power is −0.24 W and joint power from JᵀF is also −0.24 W. Separately, a synthetic diagonal Jacobian with weak gain 0.01 and requested weak-axis velocity 0.1 gives inverse rate ten. Damping λ=0.05 gives rate about 0.384615 and achieved weak-axis velocity only 0.00384615. The lower command explicitly sacrifices tracking.

## Common mistakes

Using an inverse at rank loss, assuming all task directions become difficult equally, treating damping as exact tracking and claiming every singularity demands infinite force all mislead. Another mistake is comparing a force in one frame with velocity in another. Power equality is an effective check on frame, transpose and sign conventions.

## Limits of this lesson

The analysis is local, planar and rigid. It omits actuator dynamics, compliance, collisions and time-varying constraints. The preserved stall-case checklist broadly mentions amplified velocity/torque demands; this lesson limits that wording to inverse-velocity demands and separately modeled dynamics, not universal divergence of JᵀF. The [Modern Robotics singularity supplement](https://modernrobotics.northwestern.edu/nu-gm-book-resource/5-3-singularities/) is link-only. Original calculations are CC BY 4.0, with no imported assets or qualified review.
