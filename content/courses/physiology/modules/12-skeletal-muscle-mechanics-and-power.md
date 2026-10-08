# Skeletal muscle mechanics: sarcomere length, force–velocity and power

A skeletal muscle is a force generator whose output depends on how large it is, how long its sarcomeres are and how fast it is shortening. These three dependencies come from the structure of the contractile filaments and the kinetics of the myosin cross-bridges, and they set what movements a muscle can produce and why loss of muscle mass lowers power more than it appears to. This lesson works through the maximum force of a muscle, the length–tension relation and Hill's force–velocity curve, and computes power, with synthetic numbers throughout.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute the maximum isometric force of a muscle from its physiological cross-sectional area and specific tension.
2. Use the length–tension relation and Hill's force–velocity equation to compute force, velocity and power.
3. Predict how a loss of cross-sectional area changes force and power, and state what the model leaves out.

## Maximum force from cross-sectional area

The muscle's maximal isometric (fixed-length) force scales with the number of sarcomeres in parallel, that is, with its **physiological cross-sectional area (PCSA)**:

**F₀ = σ₀ × PCSA,**

where σ₀ is the specific tension, force per unit area, which is roughly similar across mammalian muscles. With a synthetic σ₀ = 25 N/cm² and PCSA = 20 cm², F₀ = 500 N. Doubling the area doubles the force, which is why muscle size is a strong predictor of strength, while length affects the distance over which force can be produced.

## Sarcomere length and force

Force is produced by cross-bridges between thick and thin filaments, so the force a sarcomere can produce depends on how much the filaments overlap. A simplified length–tension curve has a plateau at about 2.2 μm and a descending limb in which force falls linearly to zero at about 3.6 μm, where the filaments no longer overlap:

**F/F₀ = (3.6 − L) / (3.6 − 2.2)** for 2.2 ≤ L ≤ 3.6 μm.

At a sarcomere length of 3.0 μm, F/F₀ = (3.6 − 3.0)/1.4 = 0.43; at 2.6 μm it is 0.71. At long lengths a passive tension from stretched connective tissue and titin also contributes, which this simple curve leaves out.

## Force and velocity

A muscle that is allowed to shorten produces less force the faster it shortens. Hill's characteristic equation describes this:

**(F + a)(v + b) = (F₀ + a) b,** or **v = b (F₀ − F) / (F + a),**

where a has units of force and b of velocity. Maximal shortening velocity occurs at F = 0: v_max = b F₀ / a. The shape is a hyperbola, which falls steeply at low loads and flattens as load approaches F₀.

**Synthetic muscle:** a = 0.25 F₀ = 125 N, optimal fiber length L₀ = 10 cm, and v_max = 4 L₀/s = 40 cm/s, so b = a v_max/F₀ = 1.0 L₀/s = 10 cm/s. At half load (F = 250 N) the shortening velocity is v = 10 × (500 − 250)/(250 + 125) = 6.67 cm/s (0.67 L₀/s).

## Power

**Mechanical power is force times velocity**, P = F v. It is zero when the muscle is held at a fixed length (v = 0) and zero when it shortens with no load (F = 0), so it has a maximum at an intermediate load. At half load the power is 250 N × 0.0667 m/s = 16.7 W. Setting dP/dF = 0 in Hill's equation gives the force at peak power,

**F* = F₀ [√(a/F₀ (a/F₀ + 1)) − a/F₀],**

which for a/F₀ = 0.25 is F* = 0.309 F₀ = 154.5 N. There v = 12.4 cm/s, so the peak power is 154.5 × 0.1236 = 19.1 W, more than at half load. This is why the best load for the highest power output (in a jump, a sprint or a cycling effort) is about a third of the maximum force, not the largest or smallest load.

## What a loss of muscle changes

If a muscle loses cross-sectional area with the same fiber properties, F₀ falls in proportion and so does the power at every load fraction. With 30% less PCSA, F₀ = 350 N and peak power falls to 13.4 W (70% of 19.1 W). Observational data show that muscle mass declines on average with age, and that power often declines faster than strength; the model explains part of this through lost area but says nothing about changes in fiber type, activation by the nervous system, or tendon stiffness, which also matter, and it does not describe any person.

## Common mistakes

- Treating the muscle's force as independent of its length, or using sarcomere length and muscle length interchangeably.
- Expecting maximum power at maximum force or at maximum velocity, when it occurs at an intermediate load.
- Computing power as F₀ × v_max, which no real contraction achieves.
- Using a length–tension curve for the whole muscle when only sarcomeres overlap in this way.
- Assuming that a loss of cross-sectional area changes force but not power.
- Ignoring the passive tension at long lengths.

## Worked example

**Problem.** A second synthetic muscle has PCSA = 12 cm², σ₀ = 25 N/cm², a = 0.25 F₀, L₀ = 8 cm and v_max = 6 L₀/s. Find its isometric force, its force at a sarcomere length of 2.8 μm, and its power at half load.

**Step 1: maximum force.** F₀ = 25 × 12 = 300 N.

**Step 2: length effect.** F = F₀ × (3.6 − 2.8)/1.4 = 300 × 0.571 = 171 N.

**Step 3: half-load velocity.** b = 0.25 × 6 L₀/s × 8 cm = 12 cm/s and a = 75 N, so v = 12 × (150)/(150 + 75) = 8.0 cm/s.

**Step 4: power.** P = 150 N × 0.080 m/s = 12.0 W.

## Limits of this lesson

All values are synthetic and round. The length–tension curve is a straight-line simplification of a plateau-and-limbs shape, Hill's equation describes concentric shortening of fully activated muscle, and real muscles have pennate architecture, tendons in series, fiber-type mixtures and submaximal activation. The lesson does not estimate any person's strength and gives no training or medical advice.
