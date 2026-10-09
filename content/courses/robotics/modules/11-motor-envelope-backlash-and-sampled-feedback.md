# Motor envelope, backlash and sampled feedback

**Status:** original formative instruction with substantial AI assistance. Motor constants, limits and gains are synthetic. This lesson combines the preserved gearbox budget with speed-dependent actuation and a deliberately simple control model. No gain or threshold below is a recommendation for a real robot.

## Learning objectives

1. Calculate a conditional motor current/torque envelope and transmission output.
2. Distinguish reflected inertia, backlash and encoder quantization in a joint budget.
3. Relate an ideal PD response to saturation and sampled sensing limits.

## A torque rating needs operating conditions

For a simplified DC motor in steady electrical operation, V=RI+k_eω and τ_motor=k_t I. The back-emf term k_eω grows with speed, leaving less voltage for current through winding resistance. Use SI-compatible constants and state whether torque is continuous, peak or merely the ideal value under the algebraic model. Real inductance, drive behavior and temperature add dynamics that this model omits.

A constructed motor has maximum voltage 12 V, resistance 2 ohms, k_e=0.1 V·s/rad and k_t=0.1 N·m/A. A separate drive current cap is 2 A. At motor speed 100 rad/s, the steady positive-motoring voltage-limited current is (12−10)/2=1 A. Its torque is 0.1 N·m, below the 0.2 N·m current-cap torque. At 20 rad/s, the voltage-only expression gives 5 A, so the separate current cap controls this operating point.

This envelope is restricted to the stated positive-motoring quadrant. It does not describe regenerative braking, signed negative speeds or a thermal duty cycle. A zero-speed algebraic voltage current of six amperes is not a permitted continuous stall current in this exercise, because the drive cap is two. A quoted maximum voltage does not remove a current or temperature limit.

## Gearing changes torque, speed and inertia

With reduction N defined as motor speed divided by output speed, ω_out=ω_motor/N. Under a stated motoring efficiency η, output torque is ηNτ_motor. For N=50 and η=0.8, a motor torque of 0.2 N·m gives eight N·m output. At motor speed 20 rad/s, output speed is 0.4 rad/s. Those two values belong to the same declared operating point; combining a high-speed value from another point with this torque would invent performance.

Rotor inertia J_m reflected to the output is N²J_m in an ideal rigid kinematic transmission. With J_m=0.0001 kg·m² and N=50, the reflected value is 0.25 kg·m². It contributes to acceleration torque and stored kinetic energy. Efficiency in this simplified torque-transfer relation is not a general instruction to multiply or divide every inertial term by η; a more detailed loss model is needed for that bookkeeping.

The same reduction that improves nominal motor-side encoder resolution may hide output backlash. Encoder count spacing is quantization. A gap between motor-equivalent position and actual output position after a direction reversal may instead indicate backlash, compliance or another transmission state. An output-side measurement is independent information that helps discriminate those possibilities.

## Feedback describes a model and its limits

For an ideal single joint with inertia M, viscous coefficient b and no uncompensated gravity, Mq̈+bq̇=τ. For a constant target q_ref, apply τ=K_p(q_ref−q)−K_d q̇. The error follows M ë+(b+K_d)ė+K_p e=0. Its natural frequency is √(K_p/M), and damping ratio is (b+K_d)/(2√(MK_p)).

With M=0.02 kg·m²,b=0.01 N·m·s/rad,K_p=2 N·m/rad and K_d=0.39 N·m·s/rad, natural frequency is ten rad/s and damping ratio is one. For an initial error with zero velocity, this ideal critically damped model has a monotone approach. A sampled, delayed or saturated implementation need not follow that continuous-time response.

Increasing gains can demand torque beyond the available envelope. A 0.5 rad position error with zero speed requests one N·m from the proportional term alone. If the modeled actuator cap is 0.3 N·m, that command cannot be delivered. The unsaturated analytic solution then does not describe the actual closed-loop equation. A stored integral term, if added, would also require an explicit saturation-management policy rather than assuming that more integral action repairs missing torque.

## Differencing position can amplify measurement changes

A speed estimate (q_k−q_{k−1})/Δt depends on sample timing and position quantization. A small count change at short Δt produces a large estimated speed. Filtering changes noise and delay; it does not preserve the ideal derivative action automatically. Missing or stale timestamps can make a plausible count difference produce the wrong rate.

Record actual measured position, commanded position, delivered-current information and timing separately. A command is not a measurement of delivered torque. Motor current supports a torque estimate only under known motor constants and an appropriate drive model, while gear friction and efficiency complicate output torque. These distinctions matter when investigating a stall.

## Worked example

At 100 rad/s motor speed, the synthetic motor has voltage-limited torque 0.1 N·m. A 50:1 gearbox at efficiency 0.8 gives output torque four N·m at output speed two rad/s. At 20 rad/s, current cap gives eight N·m at 0.4 rad/s. The operating points cannot be combined into eight N·m at two rad/s under the same supplied envelope.

A synthetic output backlash magnitude 0.1° corresponds to approximately 0.523599 mm at a tool radius of 0.30 m. A motor-side encoder can report finely spaced counts during part of a reversal while the output takes up the gap. The preserved resolution reading therefore remains a quantization budget, not an accuracy specification or evidence that a tip actually follows every count.

## Common mistakes

Combining torque and speed from different operating points, applying the motoring envelope to regeneration without a model, forgetting N² inertia and treating commanded current as measured torque all mislead. Another mistake is using ideal PD poles as proof of stability after adding delay, saturation or discrete sampling.

## Limits of this lesson

The construction omits inductance, temperature, gear compliance and validated drive limits. It supplies no real tuning procedure or machine safety claim. The [Modern Robotics torque-control supplement](https://modernrobotics.northwestern.edu/nu-gm-book-resource/11-4-motion-control-with-torque-or-force-inputs-part-1-of-3/) is link-only context. All examples and calculations are original CC BY 4.0 content with substantial AI assistance. No diagram or code was imported; qualified review remains absent.
