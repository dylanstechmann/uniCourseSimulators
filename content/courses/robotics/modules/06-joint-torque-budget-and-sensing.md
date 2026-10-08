# Actuators, gearing and sensing for a lab robot joint: torque budgets, resolution and failure limits

A robot joint that moves a pipette or a camera over a plate is a motor, a gearbox, a sensor and a controller. Whether it works depends on simple budgets: can the motor, through its gears, hold the load with margin; how finely can the sensor tell where the joint is; and what happens when something goes wrong? This lesson works through those budgets for a synthetic single joint and connects them to the design of a safe closed loop.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute output torque and speed through a gearbox with a stated efficiency, and the gravity torque a load imposes.
2. Calculate a torque margin and evaluate whether a joint can hold and move its load.
3. Calculate encoder resolution at the joint and at the tool, compare it with mechanical backlash, and design failure limits for the control loop.

## Gearing trades speed for torque

A gearbox with reduction ratio N multiplies torque and divides speed:

**τ_out = η N τ_motor,** **ω_out = ω_motor / N,**

where η is efficiency (friction losses). **Synthetic joint:** a motor giving 0.05 N·m continuous torque at 3000 rpm, through a 50:1 gearbox with η = 0.8, delivers τ_out = 0.8 × 50 × 0.05 = 2.0 N·m at 60 rpm. Power is conserved apart from losses: the gearbox cannot increase both torque and speed.

## Torque budget

A horizontal arm holding a 0.2 kg tool at 30 cm needs a holding torque of m g r = 0.2 × 9.81 × 0.3 = 0.589 N·m against gravity. The torque margin is 2.0/0.589 = 3.4. The margin must also cover accelerating the load (τ = Iα), friction that rises with temperature and wear, and the arm's own weight. A common practice is to require a margin of at least about 2 under the worst static case and then check dynamic cases; the exact figure is a design decision.

## Sensing position

An incremental encoder on the motor shaft with 1024 counts per revolution, behind a 50:1 reduction, gives 51,200 counts per output revolution, an angular resolution of 360°/51,200 = 0.00703°. At the tool, 30 cm out, that is an arc of r × Δθ = 0.0368 mm.

But a motor-side encoder does not see what happens after the gears. **Backlash**, the play between gear teeth, lets the output move without the motor moving. A synthetic backlash of 0.1° at the output corresponds to 0.52 mm at the tool, about 14 times the encoder resolution. The encoder's fine resolution is therefore not the joint's accuracy. Remedies include an output-side encoder, preloaded or low-backlash gearing, and always approaching a target from the same direction so the gear teeth contact on the same side.

## Closing the loop safely

A position controller compares the commanded and measured angles and drives the motor to reduce the error (see the control lessons). Failure limits make the loop safe for people, samples and the machine:

- **Current (torque) limit:** caps force if the arm hits something.
- **Following-error limit:** if the measured position lags the command by more than a set amount, stop; this detects collisions, stalls and sensor faults.
- **Soft position limits:** prevent commands outside the reachable or allowed range (see the kinematics lesson).
- **Sensor plausibility checks:** a jump in encoder count larger than physically possible in one sample indicates a fault.
- **Safe stop:** what the joint does on power loss (brake, or a gearbox that cannot be back-driven) so a raised tool does not fall.

## Choosing the ratio

A higher reduction ratio gives more torque and finer resolution at the output, but lower top speed and more reflected inertia: the motor's rotor inertia appears at the output multiplied by N², which slows response and stores more energy in a collision. A lower ratio is faster and more back-drivable, which some collaborative robots use deliberately so that a person can push the arm away. The right ratio comes from the task's speed, load and safety requirements together.

## Common mistakes

- Forgetting gearbox efficiency, which overstates output torque.
- Sizing the motor for the static load only, ignoring acceleration.
- Treating motor-side encoder resolution as tool accuracy despite backlash.
- Omitting a following-error limit, so a collision is not detected until damage is done.

## Worked example

**Problem.** The tool is replaced with a 0.6 kg gripper at the same radius. Does the joint still have a margin of at least 2?

**Step 1.** Gravity torque = 0.6 × 9.81 × 0.3 = 1.766 N·m.

**Step 2.** Margin = 2.0/1.766 = 1.13, just above 1: the joint can barely hold the load and has almost nothing left for acceleration.

**Step 3.** Options: a higher reduction (more torque, less speed), a stronger motor, moving the load closer to the axis, or counterbalancing the arm. Each changes speed, cost or reach, which is the engineering trade-off.

## Limits of this lesson

All values are synthetic. Real joints need thermal limits, dynamic models and compliance with the safety requirements for the specific machine; this lesson covers first-pass budgets only.
