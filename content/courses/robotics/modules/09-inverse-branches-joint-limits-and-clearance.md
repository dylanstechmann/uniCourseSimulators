# Inverse branches, joint limits and clearance

**Status:** original formative instruction with substantial AI assistance. Every arm, target, obstacle and limit is synthetic. This lesson separates an algebraic inverse-kinematics solution from a feasible configuration and a feasible path. It describes a paper model, not a validated motion planner.

## Learning objectives

1. Recover both planar inverse branches and verify their forward positions.
2. Apply stated joint limits and branch-continuity criteria without inventing redundancy.
3. Distinguish endpoint reachability from whole-link and swept-path clearance.

## Begin with geometric reachability

For a two-link arm, let r=√(x²+y²). An ideal unrestricted arm can reach radii between |L₁−L₂| and L₁+L₂. The cosine relation is c₂=(r²−L₁²−L₂²)/(2L₁L₂). If c₂ lies strictly outside [−1,1], there is no real elbow angle under the stated geometry. A numerical roundoff policy may clamp a value only infinitesimally outside the interval, but must not turn a genuinely unreachable target into a reachable one.

When −1<c₂<1, choose q₂=atan2(±√(1−c₂²),c₂). The two signs produce the two elbow branches. Then q₁=atan2(y,x)−atan2(L₂sinq₂,L₁+L₂cosq₂). Angles need consistent wrapping and joint conventions. A physical joint with a finite travel range cannot be treated as freely rotating merely because trigonometric functions are periodic.

Substitute every candidate into the forward position equations. This catches sign, branch and degree/radian mistakes. The check should compare the endpoint with the intended target in the same frame and units. A correct endpoint does not yet establish acceptable joint angles, link clearance, dynamic demands or tool orientation.

## A two-joint position task is usually not redundant

For this two-joint arm controlling two independent position coordinates away from singularities, the two discrete inverse branches are not continuous kinematic redundancy. There is no free joint direction that preserves arbitrary endpoint position locally. A three-joint planar arm controlling only two position coordinates can have such a free direction under appropriate rank conditions. Adding an orientation requirement changes the dimension of the task again.

The preserved case suggests constrained redundancy as one possible general approach. That applies only if additional usable degrees of freedom or a relaxed task are available. It is not a capability automatically possessed by the modeled two-link position arm. A planner can instead change the selected branch, move the fixture, choose an intermediate target, slow the trajectory or revise its task constraints, with each option requiring its own feasibility check.

## Joint limits reduce the geometric workspace

Check each candidate against all stated intervals. A target inside the unrestricted annulus can still have no allowed branch. If a branch is allowed at one target, it may become invalid as the target moves. Selecting the closest branch independently at every sample can cause discontinuous jumps in commanded angles. Maintain branch identity or explicitly plan a transition rather than silently switching solutions.

Angle differences should respect the actual joint travel, not a shortest angular wrap that passes through a forbidden stop. A simple distance in joint coordinates can be a useful selection score, but its weights and collision conditions must be named. Minimizing angular distance does not by itself minimize energy, time or risk.

## The endpoint is only one part of the geometry

Represent each link as a segment between its two joint centers and, for a simple clearance model, give it a finite radius. For a circular obstacle centered at c and segment endpoints a,b, project c onto the line using u=((c−a)·(b−a))/||b−a||². Clamp u to [0,1] and calculate the nearest point a+u(b−a). Subtract obstacle radius and link radius from the center-to-segment distance.

A zero-length segment needs a separate point-distance rule because the denominator vanishes. A negative clearance means overlap in this geometry; a positive clearance is separation under the model, not a certified safety margin. Unknown obstacle location, calibration error and unmodeled tool shape can consume that clearance.

Checking only the tool point can miss a collision at the elbow or middle of a link. Checking only start and finish can miss a collision during motion. Joint interpolation and Cartesian interpolation trace different curves. Dense samples can help find a violation, but finite samples alone do not prove continuous clearance unless motion bounds or another continuous method support the claim.

## Worked example

Take equal links 0.25 m and target (0.25,0.25) m. Then c₂=0 and q₂=±90°. The corresponding shoulders are 0° and 90°. Both produce the same endpoint. If q₁ must remain between −30° and 60° and q₂ between −120° and 120°, only the branch q₁=0°,q₂=90° is allowed. There remains one allowed candidate, not two equivalent control choices.

For an independent clearance example, a line segment from (0,0) to (1,0) m lies below a circular obstacle centered at (0.5,0.1) m with radius 0.05 m. With zero link radius in this simplified example, the nearest distance is 0.1 m and clearance is 0.05 m. Adding link radius 0.02 m leaves clearance 0.03 m. These differences show why a line drawing is insufficient for a finite-size link.

Finally, move a straight equal-link arm from q₁=0° to 90° while q₂ stays zero. Joint interpolation places its midpoint at q₁=45°, giving tool coordinates approximately (0.353553,0.353553) m. A straight Cartesian segment between the endpoint positions (0.5,0) and (0,0.5) instead has midpoint (0.25,0.25). Both share endpoints, but their swept geometry differs substantially.

## Common mistakes

Clamping a truly invalid cosine, considering only one elbow branch, assuming endpoint reach implies joint-limit feasibility and checking only the tool all lose constraints. Calling two discrete branches redundancy is another error. A nearest-sample clearance is evidence at those samples, not a proof about the entire continuous motion.

## Limits of this lesson

The geometry omits three-dimensional shapes, contact mechanics, cable routing and real motion planning. Numeric and choice items assess selected inverse and clearance checks without grading a planner implementation. Existing robotics links and the [Modern Robotics singularity supplement](https://modernrobotics.northwestern.edu/nu-gm-book-resource/5-3-singularities/) remain link-only context; no problems or figures are copied. Original instruction is CC BY 4.0. Qualified review, workload measurement and any physical safety validation remain absent.
