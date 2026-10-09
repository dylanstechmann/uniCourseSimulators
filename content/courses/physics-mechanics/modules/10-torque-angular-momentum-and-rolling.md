# Torque, angular momentum and rolling

## Learning objectives

1. Calculate a signed torque and fixed-axis response with the stated moment of inertia.
2. Relate rotational energy and angular momentum while distinguishing their conservation conditions.
3. Apply a rolling constraint and check when static friction can support it.

## The axis belongs in the question

Torque about a stated origin is r×F. Its z component in a planar example is r_xF_y−r_yF_x. With synthetic position r=(0.20,0.10,0) m and force F=(10,30,0) N, torque is +5.0 N·m in z. The sign follows the selected right-handed axes. Multiplying force magnitude by distance magnitude without the angle would give a different quantity.

Moving the reference origin can change torque because the lever arm changes. A force passing through the chosen origin gives zero torque there even if its magnitude is large. Torque and work share dimensional units, but torque is a rotational moment and work an energy transfer. Do not substitute one for the other merely because both can be written as N·m.

## Inertia describes mass distribution

For a stipulated uniform solid disk of mass 2.0 kg and radius 0.10 m, moment of inertia about its central symmetry axis is I=0.5mR²=0.0100 kg·m². The same mass at a different radius or with a different shape can have a different I. A point-mass formula mR² is not automatically the disk formula. The selected distribution is part of the mechanical model.

Under a net fixed-axis torque 5.0 N·m and constant I, angular acceleration is τ/I=500 rad/s². This is an instantaneous synthetic calculation, not a device spin-up setting. Bearing torques, flexibility and angular-speed limits are not supplied. An actual system can require more complete vector or variable-inertia dynamics than this introductory fixed-axis equation.

## Energy and angular momentum are different

At angular speed 20 rad/s, the same disk has rotational kinetic energy 0.5Iω²=2.0 J and fixed-axis angular momentum Iω=0.20 kg·m²/s. Doubling speed doubles angular momentum but quadruples kinetic energy. A statement about one cannot be converted into a statement about the other without the accompanying mass distribution and speed.

Net angular impulse over a time interval changes angular momentum about the selected axis. Zero external torque can conserve that component even if kinetic energy changes during internal redistribution. Conversely, energy conservation alone does not require angular momentum conservation when an external constraint exerts torque. Identify the relevant interactions and reference before applying either balance.

The familiar relation L=Iω in the same direction is limited to an appropriate fixed symmetry-axis case. General rigid-body angular momentum can involve an inertia tensor and need not align with angular velocity. The new examples remain deliberately within the simpler regime; the symbol I is not a universal scalar replacement for every three-dimensional mass distribution.

## Rolling adds a constraint

For a rigid body rolling without slip on a fixed surface, center speed and rotation magnitude satisfy v=Rω. The instantaneously contacting point has zero velocity relative to that surface. The [OpenStax rolling section](https://openstax.org/books/university-physics-volume-1/pages/11-1-rolling-motion) is a link-only conceptual reference; the following parameters are constructed teaching values.

Take a uniform solid cylinder starting from rest and descending through vertical height h=0.50 m, with adequate static friction and no rolling resistance. Include both translation and rotation: mgh=0.5mv²+0.5I(v/R)². With I=0.5mR², this gives v=√(4gh/3)≈2.557342 m/s for g=9.81. Assigning all potential energy to translation would overstate the speed.

At that endpoint, translational kinetic energy is two thirds of the initial gravitational potential reduction and rotational energy one third. Mass and radius cancel from this speed expression only because of the stipulated inertia ratio and no-slip constraint. A hoop, a slipping cylinder or a deforming rolling body gives a different model and need not have that cancellation.

## Static friction can provide torque

For the freely descending cylinder on a fixed incline, static friction can supply the torque that creates rotation even though the contact point is instantaneously at rest. In the ideal rigid no-slip model on a fixed surface, that contact force does no total instantaneous work on the body. This does not mean friction is zero or that it never affects the dynamical equations.

Resolve translation and rotation together to find the required friction, then compare it with μ_sN. For a solid cylinder on an incline, the required condition is μ_s≥tanθ/3 under these assumptions. If it fails, the no-slip solution is not feasible, and kinetic sliding requires a different calculation. A rolling drawing does not prove that the surface can sustain its constraint.

A moving support or a deformable contact changes the work analysis. A force at a point moving in the selected frame can transfer power, and real rolling resistance can dissipate energy. The ideal zero-work statement is therefore attached to a specific rigid-body/fixed-surface model rather than every real wheel or soft tissue contact.

## Worked example

Use the cross product component 0.20×30−0.10×10 for torque +5.0. Calculate I from the supplied disk geometry, then obtain α, rotational energy and angular momentum with their distinct units and speed dependence. For the separate cylinder, impose v=Rω and include both energy terms before solving for center speed. Finally check whether the required static friction fits the bound instead of assuming rolling without slip automatically.

## Common mistakes

Do not use lever-arm magnitude without its perpendicular relation, a point-mass inertia for every shape or L=Iω as an unrestricted vector law. Do not omit rotational energy in rolling or confuse zero ideal contact work with zero friction force. Check the axis, support frame and no-slip feasibility.

## Limits of this lesson

All geometries, forces and speeds are synthetic. Rigid-body, fixed-axis, no-slip and lossless assumptions are restricted teaching models, not a validated rotor or device specification. No apparatus operation or biological recommendation is supplied. Original instruction has substantial AI assistance. The course remains partial, unreviewed and formative-only.
