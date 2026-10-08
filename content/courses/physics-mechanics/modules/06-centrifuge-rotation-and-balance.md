# Rotation in the lab: the centrifuge, relative centrifugal force, moment of inertia and why balance matters

The centrifuge is the most common rotating machine in a biology lab, and almost every quantity in rotational mechanics shows up in it. Protocols specify relative centrifugal force (×g), not speed, because what sediments a cell or a protein is the acceleration it feels, which depends on both rotation rate and radius. The rotor stores kinetic energy, needs torque to spin up, and turns a small mass imbalance into a large rotating force. This lesson computes each with synthetic values.

## Learning objectives

By the end of this lesson, you should be able to:

1. Convert rotation rate to angular velocity and compute centripetal acceleration and relative centrifugal force, and find the speed for a target force.
2. Calculate a rotor's moment of inertia, rotational kinetic energy, angular momentum and the torque needed for a given spin-up.
3. Quantify the rotating force from a mass imbalance and check results with units and limiting cases.

## From rpm to ×g

A rotation rate in revolutions per minute converts to angular velocity by **ω = rpm × 2π/60** rad/s. A sample at radius r moves in a circle and needs centripetal acceleration **a = ω²r**. The **relative centrifugal force** is that acceleration divided by g:

**RCF = ω²r/g.**

**Synthetic run:** 3000 rpm gives ω = 314.2 rad/s. At r = 10 cm, a = 314.2² × 0.1 = 9870 m/s², so RCF = 1006 ×g. To reach 500 ×g at the same radius instead, solve for ω: ω = √(RCF × g/r), which gives 2115 rpm. Because RCF depends on ω², halving the speed quarters the force; because it depends on r, a protocol written for one rotor's radius is wrong in rpm on another. That is why protocols should state ×g.

## The rotor as a rotating body

A rotor's resistance to changes in rotation is its **moment of inertia** I = Σ m r². For a uniform solid disk of mass M and radius R, I = ½MR². A synthetic rotor of 2 kg and 12 cm radius has I = ½ × 2 × 0.12² = 0.0144 kg·m².

- **Rotational kinetic energy:** KE = ½Iω² = ½ × 0.0144 × 314.2² = 711 J at 3000 rpm. That energy must go somewhere if the rotor fails, which is why centrifuges have armored chambers and lid locks.
- **Angular momentum:** L = Iω = 4.52 kg·m²/s. Without external torque it is conserved; a spinning rotor resists being tilted.
- **Torque for spin-up:** reaching ω in 20 s at constant angular acceleration needs α = ω/t = 15.71 rad/s² and torque τ = Iα = 0.226 N·m. Doubling the target speed doubles the torque (at the same spin-up time) but quadruples the stored energy.

## Why balance matters

If one tube holds an extra mass Δm at radius r, the rotor carries an unbalanced force of magnitude Δm ω²r that rotates with it. An extra 1 g at 10 cm and 3000 rpm produces 9.9 N, roughly the weight of a 1.0 kg object, oscillating in direction 50 times per second. That shakes the drive shaft and bearings; larger imbalances at higher speeds can damage the instrument. Balancing tubes by mass, not by volume, and placing them symmetrically removes this force.

## Checking with units and limits

- ω²r has units (1/s)²·m = m/s², an acceleration, as required.
- RCF → 0 as r → 0: a sample at the axis feels no centrifugal effect.
- KE scales with ω², so a rotor at twice the speed stores four times the energy: a reason high-speed rotors have strict speed ratings and inspection schedules.

## Sedimentation time

How long a spin takes to pellet a particle also follows from RCF. A small particle reaches a terminal velocity where drag balances the centrifugal force, and that velocity is proportional to RCF. Doubling the ×g roughly halves the time for the same pelleting, which is why a protocol's time and force should be read together; changing one without the other changes the result. Temperature matters too, because viscosity of water falls as it warms, so the same spin pellets faster at room temperature than at 4 °C.

## Common mistakes

- Using rpm directly in ω²r without converting to rad/s.
- Converting ×g between rotors by keeping rpm the same.
- Using the full rotor radius when the sample sits at a smaller radius (protocols may specify r_min, r_avg or r_max).
- Balancing by volume when solutions of different density are spun.

## Worked example

**Problem.** A protocol written for a rotor at r = 8 cm says 4,000 rpm. What speed reproduces the same RCF at r = 10 cm?

**Step 1.** RCF ∝ ω²r, so ω₂ = ω₁ √(r₁/r₂).

**Step 2.** rpm₂ = 4000 × √(8/10) = 3578 rpm.

**Step 3.** The protocol's force is 1431 ×g; at 10 cm the lower speed gives the same value. Running the original 4,000 rpm on the larger rotor would apply 1789 ×g, 25% more than intended.

## Limits of this lesson

All values are synthetic. Real rotors are not uniform disks, and their speed limits come from the manufacturer's ratings, not from these formulas.
