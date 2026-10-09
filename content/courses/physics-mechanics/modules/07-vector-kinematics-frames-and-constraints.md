# Vector kinematics, frames and constraints

## Learning objectives

1. Differentiate a stated position vector and distinguish speed from velocity.
2. Calculate a constrained projectile event using a consistent reference frame.
3. Check domains, units and the information available from sampled position data.

## A position needs a reference

Position is a vector relative to a specified origin and axes. A coordinate without that reference cannot describe a displacement between two objects. Fix an inertial frame for the following teaching examples, with x horizontal and y upward. Let time be in seconds and distances in metres. The synthetic path x=1+2t+t² and y=3−t+0.5t² specifies both components rather than only the curve's shape.

Velocity is the time derivative of position. Here v_x=2+2t and v_y=−1+t. Acceleration is the derivative of velocity, giving a_x=2 and a_y=1 m/s². At t=2 s, position is (9,3) m and velocity (6,1) m/s. Speed is the magnitude √37≈6.082763 m/s, which is neither the x component nor the sum of component values.

Displacement from t=0 to t=2 is (8,0) m. Average velocity is therefore (4,0) m/s, different from the instantaneous velocity at the endpoint. Distance traveled along the path is at least the displacement magnitude and requires integrating speed. Dividing an endpoint coordinate by elapsed time confuses position with displacement when the initial coordinate is nonzero.

## Acceleration is a vector change

A positive x acceleration increases v_x algebraically, but it does not automatically increase speed if velocity initially points differently. The rate of change of speed involves the component of acceleration along the instantaneous velocity. Acceleration perpendicular to velocity can change direction without changing speed. Circular motion therefore needs acceleration even when the speed is constant.

The synthetic polynomial trajectory is a kinematic specification. It does not identify a unique set of forces, particle mass or actual mechanism producing it. Newton's laws can connect acceleration to net force once the system and mass are supplied. Inferring a particular contact force from acceleration alone would require more information than this path contains.

## A projectile event rather than any time

For a separate point-particle model, stipulate launch height y₀=1.0 m, horizontal velocity 2.0 m/s and upward velocity 3.0 m/s under constant downward g=9.81 m/s². Neglect drag and all other forces after the initial event. Then x=2t and y=1+3t−0.5gt², with the horizontal origin at launch. The positive root y=0 gives a model landing time approximately 0.851148 s and horizontal displacement approximately 1.702297 m.

The other algebraic root is negative and lies outside the declared post-launch interval. Reject it for this event instead of averaging the two roots. At the highest point v_y=0, so t_top=3/9.81≈0.305810 s. Horizontal velocity remains 2 m/s; the particle is not at rest merely because its vertical velocity vanishes.

The landing surface, frame and force assumptions are part of the model. A different final height changes the event equation. Drag, launch uncertainty or a moving surface can change the result. The example supplies no launch apparatus, projectile-use procedure or actual trajectory measurement. Its point-particle equations are mathematical scope rather than operational advice.

## Relative motion needs frame discipline

If an observer moves at constant horizontal velocity 1.0 m/s relative to the original inertial frame and shares the same axes, the particle's horizontal velocity in that observer's frame is 2−1=1 m/s during the projectile interval. Vertical velocity is unchanged. Acceleration is unchanged under this constant-velocity Galilean transformation, while positions and velocities depend on the frame.

An accelerating observer needs additional accounting before applying Newton's usual inertial-frame form. Describing a curve in a moving image does not establish that the reference is inertial. A coordinate offset changes position but not velocity; a time-dependent reference motion can change measured velocity or acceleration. Calibration and frame motion are separate issues, revisited in the measurement lesson.

## Samples and derivatives

An exact position function can be differentiated analytically. Sampled positions instead require estimates such as central differences, with error determined by sampling interval, rounding and the trajectory. Differentiation can amplify position-reporting errors, especially for acceleration. More displayed decimal places do not establish more accurate timing or a correct physical model.

For the supplied x quadratic, symmetric samples about a time give the exact central-difference velocity in exact arithmetic. That property is specific to its polynomial degree and stencil, not a universal guarantee. Irregular time spacing requires a corresponding calculation rather than treating adjacent sample indices as equal time intervals. Always carry the units through the differences.

## Worked example

Differentiate each polynomial component before inserting t=2, giving velocity (6,1) and acceleration (2,1). Compute speed by the vector norm and compare it with average displacement divided by two seconds. In the separate projectile model, impose the landing condition y=0, retain the positive-time root and multiply by horizontal speed for range. At the apex, set only v_y to zero. Finally subtract the supplied observer velocity for the constant-frame comparison.

## Common mistakes

Do not confuse position, displacement and traveled distance. Do not add velocity components to get speed or assume an apex means zero vector velocity. Reject event roots outside the declared interval and distinguish a constant coordinate offset from time-dependent frame motion.

## Limits of this lesson

All paths, initial conditions and observations are synthetic. Constant gravity, no drag and inertial axes are declared simplifications, not a validated model of a real device or organism. No experimental or apparatus procedure is supplied. Original instruction has substantial AI assistance. The package remains partial, unreviewed and formative-only.
