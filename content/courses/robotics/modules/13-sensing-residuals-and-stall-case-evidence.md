# Sensing residuals and stall-case evidence

**Status:** original formative instruction with substantial AI assistance. All measurements, residuals and thresholds below are synthetic. This lesson uses the preserved near-extension stall case to ask what a collection of observations can distinguish. It supplies no real commissioning or troubleshooting procedure.

## Learning objectives

1. Calculate following errors, sensor-rate checks and transmission discrepancies with explicit timestamps.
2. Compare calibration, saturation, transmission and sensing hypotheses using independent information.
3. Bound conclusions from a model-based diagnostic without claiming unique fault identification.

## A residual compares two declared quantities

A following error can be e=q_command−q_measured. Its meaning depends on which sensor is measured, how the commanded value is timed and whether the measurement is current. Comparing a new command with an old position value produces a residual that mixes motion and latency. Comparing motor-equivalent position with output position instead tests part of the transmission relationship.

Record coordinate frame, units, sample time and sensor identity beside each channel. An angle reported in degrees and another in radians can produce a large apparent discrepancy without a mechanical fault. A timestamp expressed in milliseconds must be converted before differentiating. A derived field is evidence only to the extent that its inputs and transformation are understood.

For this paper example, a current output-position sample q=0.12 rad compared with a same-time command 0.20 rad gives following error 0.08 rad. That describes lag under the declared convention. It does not alone identify friction, a collision, an invalid trajectory, a torque cap, a bad sensor or a wrong command frame.

## Plausibility needs an independent bound

Suppose a trusted conditional mechanical bound limits joint speed magnitude to two rad/s during a 0.01 s interval. Position change should then be at most 0.02 rad, apart from stated sensor error allowances. An observed jump 0.10 rad implies differenced speed ten rad/s and violates that noiseless bound. It is a discrepancy requiring explanation, not proof that one named encoder failed.

The assumed speed bound must itself be justified. A commanded speed cap is not necessarily a measured physical cap during back-driving, impact or a control failure. Encoder wrapping, missed counts, reset events and time synchronization can also produce jumps. Adding a position-error allowance changes the permissible change; specify it rather than hiding it inside a threshold.

Two sensors can provide independent information, but they can also share calibration or clock errors. Averaging them reduces an independent random component under a suitable model; it does not remove a common bias. The preserved sensor-uncertainty item assumes independence explicitly. A covariance term is needed when that assumption is absent.

## Build hypotheses that make different predictions

Frame mislocalization can produce consistent Cartesian residuals across repeated targets while joint encoders track their commands. A translation bias can appear approximately constant, whereas a rotation bias grows with lever arm and changes direction across the workspace. Tool-offset error also depends on orientation. Repeating one target may be insufficient to separate these effects.

A transmission discrepancy can depend on direction reversal and load. Motor-side tracking accompanied by output lag is compatible with backlash or compliance, but is not unique evidence for either. An output-side measurement, a declared load model and repeat observations at several configurations help constrain the explanation. A motor encoder alone does not establish the tool position after the gearbox.

A velocity limit can become active when inverse kinematics requires large joint rates near extension. Inward motion and tangential motion at the same pose can have very different rate demands. Observing this directional difference is useful evidence for a kinematic limitation under known geometry. It does not by itself rule out additional drive or friction effects.

Torque saturation needs another kind of evidence. A delivered-current measurement with known motor constants can support a conditional torque estimate. Commanded current is not proof of delivery, and a motor estimate is not automatically an output-joint torque after unknown transmission losses. A static force map JᵀF also does not establish the dynamic torque needed to accelerate along a requested task-space trajectory.

## Detection is not a validated response

A paper rule can flag stale data, an excessive following error or a computed limit violation. Deciding what the physical machine does after a flag requires a separately validated response for its mechanics and hazards. Removing power can have different consequences for a gravity-loaded joint than for a horizontal table. This lesson identifies that design dependency without specifying an operating intervention.

A successful threshold on synthetic records is evidence that the rule implements its stated arithmetic. It is not an estimate of sensitivity or false-alarm rate on real faults. Those properties need representative observations and a defined fault population. A self-assessment checklist cannot substitute for a reviewed failure analysis.

## Worked example

Motor-equivalent angle is 0.20 rad and independently reported output angle is 0.19 rad at the same time. The discrepancy is 0.01 rad. At a 0.30 m lever arm, its small-angle endpoint contribution is approximately 0.003 m, or three mm. That exceeds a much finer nominal encoder count spacing, illustrating why count resolution does not settle transmission accuracy.

For a separate uncertainty calculation, joint standard uncertainty 0.001 rad at radius 0.50 m contributes 0.5 mm tangentially. Combine that component with independent frame standard uncertainty 0.8 mm to obtain approximately 0.943398 mm. This is a conditional standard uncertainty, not a deterministic bound or an actual measured error. Two synthetic fiducial x residuals of two mm have mean two mm; identical residuals provide no estimate that their shared bias is absent.

Revisit the preserved case: an arm reaches a target in simulation but stalls near full extension. First separate geometric reachability, required joint rates and the assumed actuator/dynamic model. Then compare synchronized joint motion, delivered-current information, output position and frame/load checks. The case wording's reference to amplified torque is conditional on dynamic requirements; finite endpoint force mapping alone does not universally diverge. A two-link position arm also lacks continuous redundancy away from singularity, so that proposed option requires a different mechanism or relaxed task.

## Common mistakes

Comparing asynchronous channels, treating commands as delivered measurements, averaging away shared bias and labeling one large residual a unique fault all overstate evidence. Another mistake is interpreting a toy threshold as a tested protective function. Keep the observed discrepancy, its possible explanations and the permitted conclusion separate.

## Limits of this lesson

The constructions omit real sensor specifications, fault populations, drive dynamics and validated machine responses. Written diagnoses remain self-assessed; the software scores only selected numbers and choices. Existing robotics/control links and the [Modern Robotics torque-control supplement](https://modernrobotics.northwestern.edu/nu-gm-book-resource/11-4-motion-control-with-torque-or-force-inputs-part-1-of-3/) are link-only. Original examples are CC BY 4.0 with substantial AI assistance. No measurements or third-party assets were imported; qualified subject and accessibility review remain outstanding.
