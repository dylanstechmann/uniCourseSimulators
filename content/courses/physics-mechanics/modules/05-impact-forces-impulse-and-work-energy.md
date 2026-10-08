# Impact forces: impulse, work–energy and why stopping more slowly protects tissue

Whether a fall, a collision or a dropped instrument causes damage depends less on the speed than on how quickly that speed is removed. Two ideas from mechanics make this quantitative: impulse, which links force to the time over which momentum changes, and the work–energy theorem, which links force to the distance over which kinetic energy is absorbed. This lesson applies both to an idealized fall, compares hard and padded stops, and uses limiting cases and units to check the answers. It is a physics exercise with synthetic numbers, not an injury model.

## Learning objectives

By the end of this lesson, you should be able to:

1. Calculate impact speed and momentum from a drop height using energy conservation.
2. Compute the average stopping force from impulse (momentum change over time) and from work–energy (kinetic energy over stopping distance).
3. Check predictions against units and limiting cases, and evaluate what an average force does and does not tell you about peak loads.

## Speed at impact

A body dropped from rest through height h, with air resistance neglected, converts potential to kinetic energy: mgh = ½mv², so **v = √(2gh)**. For a synthetic h = 0.5 m, v = √(2 × 9.81 × 0.5) = 3.13 m/s. The speed does not depend on mass, which is a useful check: if your formula for v contains m, something is wrong.

For a 70 kg body the momentum at impact is p = mv = 219.2 kg·m/s, and the kinetic energy is ½mv² = 343.4 J (equal to mgh = 343.4 J, as it must be).

## Impulse: force times time

Newton's second law in momentum form says the average net force times the stopping time equals the change in momentum: **F̄ Δt = Δp**. Stopping from 3.13 m/s to rest:

- on a hard surface in Δt = 10 ms: F̄ = 219.2 / 0.01 = 21925 N, about 32 times body weight;
- on a compliant surface in Δt = 50 ms: F̄ = 219.2 / 0.05 = 4385 N, about 6.4 times body weight.

The momentum change is the same; spreading it over five times longer cuts the average force fivefold. (Strictly, the floor must also support the body's weight during the stop, adding mg ≈ 687 N; for short stops this is small compared with the impact force.)

## Work–energy: force times distance

Alternatively, the average force over a stopping distance d does work equal to the kinetic energy removed: **F̄ d = ½mv²**. If padding compresses by 2 cm, F̄ = 343.4 / 0.02 = 17168 N; at 5 cm, F̄ = 6867 N. Both views say the same thing: stopping over a longer time necessarily means stopping over a longer distance, and vice versa.

## Average versus peak

These are average forces. Real stopping forces rise and fall; for a spring-like surface the peak is about twice the average, and for a surface that "bottoms out" the force can spike when the padding is fully compressed. Tissue damage often depends on the peak force, on the stress (force per area) and on the rate of loading, none of which an average captures. Spreading force over a larger contact area lowers stress even when the force is unchanged.

## Checking with units and limits

- **Units:** kg·m/s divided by s is kg·m/s², a newton. J/m = N·m/m = N.
- **Limit Δt → 0:** force → ∞, consistent with the idea that a perfectly rigid stop is impossible.
- **Limit h → 0:** v → 0, so the impact force vanishes and only the static weight remains.
- **Scaling:** doubling the height multiplies v by √2 and the impact force at fixed Δt by √2, but the energy (and thus force at fixed stopping distance) by 2. Which scaling applies depends on whether the surface sets the time or the distance.

## Common mistakes

- Using v = gh or forgetting the square root in v = √(2gh).
- Mixing milliseconds and seconds, which gives forces wrong by a factor of 1,000.
- Treating average force as peak force.
- Including mass in the impact-speed formula.

## Worked example

**Problem.** The same body falls from 1.0 m instead of 0.5 m onto the compliant surface (50 ms stop). What are the new speed and average force?

**Step 1.** v = √(2 × 9.81 × 1.0) = 4.43 m/s.

**Step 2.** p = 70 × 4.43 = 310.1 kg·m/s; F̄ = 310.1 / 0.05 = 6201 N.

**Step 3.** Doubling height raised the force by √2 ≈ 1.41 at fixed stopping time. If the padding instead set a fixed stopping distance, the force would double. Knowing which the surface controls is part of the model.

## Limits of this lesson

All numbers are synthetic, the body is treated as a rigid point mass, and air resistance and rotation are ignored. The lesson does not estimate injury risk for any person or situation.
