# Time scaling, clearance and stopping bounds

**Status:** original formative instruction with substantial AI assistance. Paths, speeds, accelerations, latency and clearance values are synthetic. This lesson distinguishes a geometric path from its timing and gives conditional paper checks for motion limits. It provides no certified stopping distance or permission to operate a robot.

## Learning objectives

1. Calculate velocity and acceleration from a declared path and time scaling.
2. Choose a duration that satisfies stated scalar speed and acceleration limits.
3. Combine latency, braking and geometric allowances without treating a sampled path as continuously verified.

## A path does not specify its execution time

Let q(s) describe a joint path for s from zero to one. A time scaling s(t) turns it into a trajectory. The chain rule gives q̇=q_s ṡ and q̈=q_s s̈+q_ss ṡ². For a straight joint path, q_ss is zero. For a curved path, the second term remains even if the path parameter advances at constant speed. Ignoring it omits a component of acceleration and therefore dynamic torque.

A straight joint path need not be straight in Cartesian space. Its tool velocity is J(q)q̇, which varies with configuration even if joint rates are constant. A straight Cartesian path also needs inverse configurations along its interior, not merely reachable endpoints. Both representations require branch, limit and collision checks appropriate to their geometry.

Slowing the time scaling reduces velocity and acceleration demands but does not change the geometric path. It cannot remove a collision or make an unreachable Cartesian point reachable. Slower motion can help a conditional speed or torque limit; moving the fixture or changing the path addresses a different constraint.

## A cubic scaling makes endpoint velocity zero

For a scalar move Δq completed in T seconds, define s=t/T and q(t)=q_0+Δq(3s²−2s³). Velocity is (Δq/T)(6s−6s²), and acceleration is (Δq/T²)(6−12s). Endpoint velocities are zero. Endpoint accelerations are generally nonzero, so adjoining a stationary segment creates an acceleration jump.

The maximum speed magnitude occurs at s=0.5 and equals 1.5|Δq|/T. Maximum acceleration magnitude equals 6|Δq|/T² at the endpoints. Thus speed cap v_max requires T≥1.5|Δq|/v_max, while acceleration cap a_max requires T≥√(6|Δq|/a_max). Choose the larger duration if both constraints apply under this scalar model.

A quintic scaling 10s³−15s⁴+6s⁵ also makes endpoint acceleration zero. Its peak normalized velocity is 1.875, so it can require more duration than the cubic at the same speed cap. Smooth endpoints do not automatically minimize time or keep dynamic torque within limits. The path, time scaling and actuator envelope must still be checked together.

## Stopping begins after information and actuation delays

For a one-dimensional constructed motion at positive speed v, suppose a hazard is recognized after latency ℓ and a constant guaranteed deceleration a then starts immediately. During latency, traveled distance is vℓ. During braking, distance is v²/(2a). Add a separately stipulated position allowance δ to obtain d_allow=vℓ+v²/(2a)+δ.

Every term is conditional. The model assumes no acceleration during latency, known initial speed, immediate constant braking after latency and sufficient braking capability for the current load. Actual stop distance can depend on jerk limits, communications, controller state, power loss, gravity and drive behavior. If a bound on latency or deceleration is absent, the formula is not a measured guarantee.

An uncertainty allowance is also not the same thing as a standard uncertainty. If δ is intended as a deterministic clearance allowance, label it that way. Substituting one standard deviation as though it were a strict error bound changes the claim. Correlated location errors and moving obstacles can require a different construction entirely.

## Sampling needs a motion bound

Suppose a point's speed is bounded by V throughout an interval Δt. Its displacement from the interval start is at most VΔt. That can help bound what might occur between checked samples. It does not account for the full shape of rotating links unless a suitable bound covers each relevant point or swept geometry. Endpoint speed alone is insufficient for the elbow and link bodies.

Minimum clearance at sampled points can exceed zero while an intervening collision occurs. A motion bound can provide a conservative certificate for a simplified geometry if all assumptions are satisfied; otherwise report only sampled evidence. A planner's nominal clearance must also account for calibration and shape-model limitations rather than treating precise numerical coordinates as exact physical locations.

## Worked example

A synthetic joint move is Δq=0.4 rad over T=2 s using the cubic. At t=1 s, position has advanced 0.2 rad and speed is 0.3 rad/s. Peak acceleration magnitude is 0.6 rad/s². For speed cap 0.2 rad/s, duration must be at least three seconds. For acceleration cap 0.4 rad/s², duration must be at least √6≈2.44949 seconds. A three-second duration satisfies both scalar bounds, but says nothing about obstacles or torque from a different model.

For a separate Cartesian stopping example, speed is 0.2 m/s, latency 0.05 s, deceleration one m/s² and deterministic position allowance 0.003 m. Distance allowance is 0.010+0.020+0.003=0.033 m. A supplied static clearance of 0.040 m leaves nominal reserve 0.007 m under those assumptions. This is a synthetic arithmetic reserve, not evidence that a real stop or protective system is safe.

## Common mistakes

Treating a path as a timed trajectory, dropping curved-path acceleration, assuming zero endpoint velocity means zero acceleration and slowing down an already colliding path all miss constraints. Another mistake is reporting the stopping formula without its latency and braking assumptions or calling sampled clearance a continuous proof.

## Limits of this lesson

The scalar trajectory and one-dimensional stop are simplified paper models. They do not cover complete multi-joint constraints, hardware validation or standards compliance. Numeric and choice items assess selected calculations, not motion-planner code or a safety system. The [Modern Robotics trajectory supplement](https://modernrobotics.northwestern.edu/nu-gm-book-resource/9-1-and-9-2-point-to-point-trajectories-part-1-of-2/) is link-only. Original instruction and parameters are CC BY 4.0; no figure or trajectory example was copied. Qualified review and workload evidence remain absent.
