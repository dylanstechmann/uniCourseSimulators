# Mass matrix, gravity and energy ledgers

**Status:** original formative instruction with substantial AI assistance. Point masses, links and torques are synthetic. This lesson adds a small dynamic model to the geometric arm, so a feasible position is no longer confused with a feasible acceleration. It is not a hardware sizing specification.

## Learning objectives

1. Calculate kinetic energy and acceleration torque from a symmetric mass matrix.
2. Separate gravity, velocity-product and endpoint-force terms with explicit sign conventions.
3. Check a dynamic model through energy and distinguish joint inertia from singular task-space inertia.

## Declare a deliberately simple mechanical model

Consider an arm moving in a vertical plane. Angles q₁ and q₂ follow the existing convention: shoulder measured from horizontal and elbow relative to link one. Massless links have lengths L₁=0.30 m and L₂=0.20 m. A point mass m₁=1 kg lies at the elbow, and m₂=0.5 kg lies at the endpoint. There is no rotor inertia, friction or link-distributed mass in this construction. Gravity acts downward with g=9.81 m/s².

The elbow velocity has magnitude L₁|q̇₁|. Endpoint velocity comes from the position Jacobian. Kinetic energy is half m₁ times elbow speed squared plus half m₂ times endpoint speed squared. Expanding those terms gives K=½q̇ᵀM(q)q̇. This derivation makes the matrix's meaning inspectable rather than treating it as a fitted table without provenance.

Its entries are M₁₁=m₁L₁²+m₂(L₁²+L₂²+2L₁L₂cosq₂), M₁₂=M₂₁=m₂(L₂²+L₁L₂cosq₂), and M₂₂=m₂L₂². Off-diagonal entries couple the joints: accelerating one joint can require torque at the other. A diagonal-only approximation omits those effects and needs its own justification.

## Positive energy is a useful model check

M is symmetric because it comes from a quadratic kinetic-energy expression. For this model with positive masses and lengths, nonzero joint velocity has positive kinetic energy. At q₂=90°, M=[0.155,0.020;0.020,0.020] kg·m². Its determinant is 0.0027 and its leading diagonal entry is positive, so it is positive definite.

At q₂=0, the endpoint position Jacobian loses rank, but M becomes [0.215,0.050;0.050,0.020], with determinant 0.0018. It remains positive definite because the elbow mass also moves and constrains the kinetic energy. Singular endpoint kinematics does not require a singular joint mass matrix. Different mechanical assumptions, such as removing an independently moving mass, could change that conclusion.

## Gravity follows the potential-energy gradient

Choose potential U=(m₁+m₂)gL₁sinq₁+m₂gL₂sin(q₁+q₂), with zero at horizontal links. Gravity-compensation torque is G=∂U/∂q: G₁=(m₁+m₂)gL₁cosq₁+m₂gL₂cos(q₁+q₂), and G₂=m₂gL₂cos(q₁+q₂). These are the actuator contributions needed to balance gravity in the ideal static model. The gravitational generalized force itself has the opposite sign.

The dynamic equation can be written τ=Mq̈+h+G when τ represents actuator torque and no external endpoint load is present. The velocity-product vector is h₁=−m₂L₁L₂sinq₂(2q̇₁q̇₂+q̇₂²), h₂=m₂L₁L₂sinq₂ q̇₁². It vanishes at rest, but not generally during motion. Adding an external force requires a consistent sign: τ+JᵀF_external=Mq̈+h+G.

These equations do not permit combining every scalar torque estimate with an arbitrary plus sign. Signed terms can oppose or reinforce each other. A budget can use conservative magnitude bounds if that is its stated purpose, but a simulated trajectory needs the actual signed equation and configuration-dependent terms.

## Energy exposes missing dynamics

For an ideal no-friction model with no external force, actuator power τᵀq̇ equals the time derivative of K+U. A finite-difference energy check or a sufficiently accurate numerical trajectory can expose sign errors in gravity and missing velocity-product terms. Passing one configuration is insufficient; test multiple configurations and nonzero joint rates.

A task-space apparent inertia, when J is square and invertible, can be formed as J⁻ᵀMJ⁻¹. It can become large in a weak motion direction near singularity because the required joint velocities and accelerations are amplified. At rank loss this ordinary inverse expression is undefined. That behavior differs from the direct static force map JᵀF, which stays finite for finite J and F.

## Worked example

At q₁=0,q₂=90° and zero joint rates, gravity compensation is G₁=4.4145 N·m,G₂=0. Requesting q̈=(1,0) rad/s² adds inertial torque (0.155,0.020) N·m. Total actuator torque is therefore (4.5695,0.020) N·m under this point-mass model. A motor sized only for gravity would omit the acceleration term.

At the same posture with q̇=(1,2) rad/s, K=½(0.155+0.080+0.080)=0.1575 J. The cross term is included twice inside the symmetric quadratic form. Separately, raising only the endpoint link from q₂=0 to 90° while keeping q₁=0 changes potential by m₂gL₂=0.981 J. In a quasistatic ideal motion, actuator work against gravity equals that increase, although peak torque and power still depend on the path and timing.

## Common mistakes

Using endpoint mass alone for the entire arm, omitting cross terms, confusing compensation torque with gravity force and interpreting a kinematic singularity as zero joint inertia all mislead. A static torque margin does not establish dynamic tracking. Checking units and an energy ledger helps find errors that an endpoint-position plot cannot reveal.

## Limits of this lesson

The point-mass model omits real link inertia, gearing, thermal behavior, friction, compliance and contact. Formative questions assess selected energy and torque calculations, not an implementation or actual machine model. The [Modern Robotics mass-matrix supplement](https://modernrobotics.northwestern.edu/nu-gm-book-resource/8-1-3-understanding-the-mass-matrix/) is link-only. Original equations are derived for the stated synthetic construction; no source example, dataset or figure is imported. Instruction remains CC BY 4.0 and unreviewed.
