# Positioning a lab robot arm: forward and inverse kinematics of a planar two-link arm and the cost of joint error

Liquid-handling and imaging robots move a tool, such as a pipette tip, to precise positions above wells and dishes. Many arms are built from rotating joints, so the controller must convert between joint angles and tool position. Forward kinematics computes the position from the angles; inverse kinematics finds angles that reach a given position, and it can have two answers or none. This lesson works through both for a planar two-link arm and estimates how a small joint error turns into a positioning error at the tool.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute the tool position of a planar two-link arm from its joint angles (forward kinematics).
2. Solve the inverse kinematics for a reachable target, identify the two solutions and test reachability.
3. Estimate tool position error from joint angle error and evaluate what limits positioning accuracy.

## Forward kinematics

Link 1 of length L₁ rotates about the base by θ₁ from the x-axis; link 2 of length L₂ rotates by θ₂ relative to link 1. Adding the two link vectors gives the tool position:

**x = L₁ cos θ₁ + L₂ cos(θ₁ + θ₂), y = L₁ sin θ₁ + L₂ sin(θ₁ + θ₂).**

**Synthetic arm:** L₁ = 0.30 m, L₂ = 0.20 m. At θ₁ = 30°, θ₂ = 45°:

x = 0.3 cos 30° + 0.2 cos 75° = 0.3116 m, y = 0.3 sin 30° + 0.2 sin 75° = 0.3432 m.

The same result is the product of homogeneous transforms for each joint; for two links in a plane, the vector sum is enough.

## Inverse kinematics

Given a target (x, y), the distance from the base, r = √(x² + y²), and the law of cosines give the elbow angle:

**cos θ₂ = (x² + y² − L₁² − L₂²) / (2 L₁ L₂).**

For a target at (0.35, 0.15) m: cos θ₂ = (0.1225 + 0.0225 − 0.09 − 0.04) / 0.12 = 0.1250, so θ₂ = ±82.82°. Then

**θ₁ = atan2(y, x) − atan2(L₂ sin θ₂, L₁ + L₂ cos θ₂).**

With θ₂ = +82.82°, θ₁ = 23.20° − 31.41° = -8.21°. With θ₂ = −82.82°, θ₁ = 54.61°. Both reach the same point with the elbow on opposite sides of the line from base to target ("elbow up" and "elbow down"). A controller chooses one by rule: to avoid an obstacle, stay within joint limits, or minimize motion from the current pose. Substituting either solution back into the forward equations is the check that the algebra is right.

## Reachability

cos θ₂ must lie in [−1, 1], which is equivalent to |L₁ − L₂| ≤ r ≤ L₁ + L₂. This arm reaches an annulus from 0.10 m to 0.50 m from the base. A target at the edge (r = L₁ + L₂) has one solution with the arm straight; there the arm is at a **singularity**: small changes in joint angles produce almost no radial motion, and the arm cannot move outward at all. Workcells are laid out so that frequently used positions sit well inside the reachable region.

## From joint error to tool error

A small rotation δθ₁ at the base moves the tool along a circle of radius r, so the tool error is approximately **r δθ₁** (with δθ in radians). For the pose above, r = 0.4635 m, and a 1° (0.01745 rad) base error moves the tool 8.1 mm. A typical 96-well plate has wells about 9 mm apart and around 6–7 mm across, so an error of that size could put a tip on a well's edge. Errors from both joints, link-length errors, backlash in gears and deflection under load all add, which is why lab robots calibrate positions against physical references (teaching points) rather than relying on nominal geometry alone.

## Common mistakes

- Mixing degrees and radians, especially in r δθ.
- Using θ₂ as an absolute angle rather than relative to link 1.
- Taking only one inverse solution and missing a collision-free alternative.
- Forgetting to check reachability before solving.

## Worked example

**Problem.** Is the target (0.55, 0.05) m reachable, and what about (0.05, 0.05) m?

**Step 1.** r = √(0.55² + 0.05²) = 0.552 m > 0.50 m: out of reach (cos θ₂ would exceed 1).

**Step 2.** r = √(0.05² + 0.05²) = 0.071 m < 0.10 m: also unreachable, inside the hole of the annulus where the arm cannot fold tightly enough.

**Step 3.** A plate must be placed within 0.10–0.50 m of the base, and preferably away from both edges, where accuracy and dexterity degrade.

## Limits of this lesson

Dimensions and angles are synthetic. Real arms have more joints, joint limits, dynamics and compliance; the lesson covers geometry only.
