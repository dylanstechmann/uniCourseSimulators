# Transient diffusion: penetration depth, the error function and equilibration times

The oxygen-limit lesson found steady profiles: a balance between diffusion and consumption that does not change in time. Many questions in tissue engineering are about time instead. How long after a medium change does a solute reach cells 500 μm inside a gel? How long must a construct soak in a solution before its interior is loaded? How long before the interior of a thick construct reaches its steady oxygen profile, and is that short or long compared with the experiment? This lesson uses the order-of-magnitude diffusion time L²/D, the exact solution for a semi-infinite medium (the error function), and a check of when that solution applies. All values are synthetic, and the diffusion coefficient is the one used in the oxygen-limit lesson.

## Learning objectives

By the end of this lesson, you should be able to:

1. Estimate diffusion times with L²/D and compare them with consumption times and experiment durations.
2. Use the error-function solution to compute the concentration at a depth and time, and the time to reach a given fraction of the surface value.
3. Evaluate when the semi-infinite and constant-surface-concentration assumptions hold.

## The characteristic time

Dimensional analysis already gives the scale: a distance L is crossed by diffusion in a time of order **τ = L²/D**. With D = 2.0 × 10⁻⁹ m²/s, a distance of 100 μm takes 5 s, 1 mm takes **500 s** (8.3 min) and 5 mm takes 12,500 s, or **3.47 h**. The time grows as the square of the distance: ten times the distance takes a hundred times as long, which is why diffusion supplies cells a few hundred micrometres away within seconds but cannot supply a centimetre-thick construct on the time scale of an experiment.

## The semi-infinite medium

Suppose a medium that is initially free of solute is exposed at x = 0 to a solute held at a constant concentration C₀, and that the medium extends far beyond the region of interest. The solution of the diffusion equation depends only on the combination η = x/(2√(Dt)):

**C(x, t) = C₀ erfc(η),**

where erfc is the complementary error function. Selected values:

| η = x / (2√(Dt)) | erfc(η) = C/C₀ |
|---:|---:|
| 0 | 1.0000 |
| 0.25 | 0.7237 |
| 0.5 | 0.4795 |
| 1 | 0.1573 |
| 1.5 | 0.0339 |
| 2 | 0.0047 |

**Synthetic example:** at x = 200 μm and t = 60 s, η = 200 × 10⁻⁶/(2√(2.0 × 10⁻⁹ × 60)) = **0.2887**, erfc(0.289) = 0.683, so C = 0.2 × 0.683 = **0.1366 mol/m³**, which is 68% of the surface value. The profile moves into the medium as √t, not as t, so doubling the exposure time deepens the front by only 41%.

## Time to reach a given fraction

Set erfc(η) = 0.5: η = 0.4769, so the concentration at depth x reaches half of the surface value when 2 × 0.4769 × √(Dt) = x, or

**t₅₀ = x² / (4 × 0.4769² × D) = 1.099 x²/D ≈ 1.1 x²/D.**

For x = 500 μm, t₅₀ = 1.099 × (500 × 10⁻⁶)²/(2.0 × 10⁻⁹) = **137 s**. Because t₅₀ ∝ x², a point twice as deep takes four times as long. Reaching 1% of the surface value needs η = 1.821, so after 600 s the front at the 1% level has penetrated 2 × 1.821 × √(2.0 × 10⁻⁹ × 600) = 4.0 mm. The time to half-loading of the interior is a useful design number; the time to near-complete loading is several times longer.

## When the semi-infinite solution applies

The solution assumes that nothing happens at the far side. For a slab of thickness L with a sealed back face, that holds only while the profile has not yet reached the back, which requires erfc(L/(2√(Dt))) to be negligible; taking L/(2√(Dt)) of at least 2 (erfc(2) = 0.005) gives t ≤ L²/(16 D). For L = 1 mm this is 31 s. After that the back face matters, and the approach to the new steady state has a time of order L²/D, here 500 s. The solution also assumes a surface held at a constant concentration (a well-stirred bath with no resistance in the medium), a uniform diffusion coefficient and no reaction. With consumption, the time to reach the steady profile is limited by the shorter of the diffusion time and the consumption time C₀/q = 0.2/0.02 = 10 s; across a 100 μm slab the diffusion time 5 s is 0.5 times the consumption time, which is the dimensionless ratio φ² of the oxygen-limit lesson.

## Common mistakes

- Using a time proportional to distance rather than to its square.
- Reading the order-of-magnitude time L²/D as the time to complete equilibration.
- Using the semi-infinite solution for a thin slab at times when the back face already matters.
- Forgetting that the surface concentration is held constant in the solution, which a depleting bath does not do.
- Taking the penetration depth to grow linearly with time.
- Using a diffusion coefficient measured in water for a gel or tissue.

## Worked example

**Problem.** A synthetic solute with D = 1.0 × 10⁻⁹ m²/s is applied at a constant surface concentration of 1.0 mol/m³ to a thick gel. Find the concentration at 300 μm after 120 s, the time to reach half the surface value there, and the characteristic time x²/D.

**Step 1: similarity variable.** η = 300 × 10⁻⁶/(2√(1.0 × 10⁻⁹ × 120)) = 0.4330.

**Step 2: concentration.** erfc(0.433) = 0.540, so C = 1.0 × 0.540 = 0.540 mol/m³.

**Step 3: half time.** t₅₀ = 1.099 × (300 × 10⁻⁶)²/(1.0 × 10⁻⁹) = 99 s.

**Step 4: characteristic time.** x²/D = 90 s, so the half time is about 1.1 times the characteristic time; at 120 s the point has just not reached half of the surface value.

## Limits of this lesson

All numbers are synthetic. The erfc solution assumes one dimension, constant D, a constant surface concentration and no reaction, binding or convection; real gels bind solutes, swell and have surface resistances. Nothing here is a protocol or a statement about any real solute.
