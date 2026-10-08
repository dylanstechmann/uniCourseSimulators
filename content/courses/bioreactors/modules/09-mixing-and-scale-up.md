# Mixing and scale-up: power, tip speed and what cannot be kept constant

A process that works in a 2 L vessel has to be run in 2,000 L, and the cells should feel the same environment. They will not, and the reason is geometry. When all linear dimensions are multiplied by 10, the volume grows by 1,000 but the surface, the impeller tip and the time it takes to circulate the liquid grow at different rates, so no single choice of stirrer speed keeps oxygen supply, shear and mixing the same. Scale-up is therefore a choice of what to keep constant, informed by what the cells are sensitive to. This lesson computes power input, Reynolds number, tip speed and mixing time for a stirred vessel, scales them under three common criteria and shows which quantity changes in each case. All values are synthetic and the correlations are textbook-level approximations.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute the power input, power per volume, Reynolds number and tip speed of a stirred vessel.
2. Apply the scaling laws for geometrically similar vessels under constant power per volume, constant tip speed and constant speed.
3. Evaluate the trade-offs between criteria and explain why scale-down models are used.

## Power, Reynolds number and tip speed

For a turbulent flow in a stirred vessel, the power input of an impeller of diameter D at speed N (revolutions per second) is

**P = N_p ρ N³ D⁵,**

where N_p is the power number (a constant, about 1.5 for the pitched-blade impeller assumed here) and ρ the density. The power per volume P/V is the usual measure of how vigorously the vessel is stirred; the Reynolds number Re = ρ N D²/μ shows whether the flow is turbulent (Re above about 10⁴), and the impeller tip speed π N D is a common proxy for the highest shear. **Synthetic lab vessel:** V = 2 L, D = 6 cm, N = 200 rpm = 3.33 rev/s, ρ = 1000 kg/m³ and μ = 0.70 mPa·s. Then P = 1.5 × 1000 × 3.33³ × 0.06⁵ = **0.0432 W**, P/V = **21.6 W/m³**, Re = **17,143** and the tip speed is 0.63 m/s. For turbulent flow in geometrically similar vessels the time to blend an additive is inversely proportional to the speed, t_mix = (N t_mix)/N with N t_mix of about 20 as an illustrative value, which gives 6.0 s here.

## Scaling by 10 in linear dimension

Keeping geometric similarity, D grows by 10 and V by 1,000. With N_p constant, P/V ∝ N³D², tip speed ∝ N D, Re ∝ N D² and mixing time ∝ 1/N. Choosing which quantity to hold fixed gives the factors in the table (relative to the lab vessel):

| Kept constant | Speed N | P/V | Tip speed | Reynolds number | Mixing time |
|---|---:|---:|---:|---:|---:|
| Constant P/V | 0.215 | 1 | 2.15 | 21.5 | 4.64 |
| Constant tip speed | 0.100 | 0.10 | 1 | 10 | 10 |
| Constant speed (mixing time) | 1 | 100 | 10 | 100 | 1 |

**Constant P/V** is the most common choice, since power per volume controls oxygen transfer and the turbulence that suspends cells and microcarriers. It lowers the speed to N = 43.1 rpm, but the tip speed rises to **1.35 m/s**, the Reynolds number rises 21.5 times and the mixing time grows from 6.0 s to **27.8 s**. **Constant tip speed** protects against shear but drops P/V to 2.16 W/m³, so the vessel is stirred ten times less per volume, and mixing takes 60 s. **Constant speed** keeps the mixing time but multiplies P/V by 100 to 2,160 W/m³ and the tip speed by 10 to 6.28 m/s, which is not feasible for most cells.

## What to hold constant

No answer is right in general. The quantity to keep is the one the cells are most sensitive to and the one the process can least afford to lose: oxygen transfer (the kLa of the lesson on oxygen supply, which rises with P/V and with gas flow), shear damage (tip speed and the eddy sizes of the lesson on shear), or mixing time (for feeds and for pH control). The usual compromise holds P/V or kLa constant, accepts a longer mixing time, and checks the tip speed. The consequence is that the large vessel has **concentration gradients** that the small vessel did not: where base is added the pH is locally high, and where cells consume oxygen far from the sparger the dissolved oxygen is locally low. Scale-down models, small vessels operated to reproduce the mixing time and gradients of the large one, are used to expose cells to the large-scale environment before committing to it.

## Common mistakes

- Choosing one criterion and assuming that all the others scale with it.
- Using the stirrer speed in rpm in P = N_p ρ N³ D⁵, which needs revolutions per second.
- Expecting constant P/V to keep the shear constant.
- Forgetting that the mixing time rises on scale-up at constant P/V.
- Using the turbulent power number at a low Reynolds number.
- Assuming the large vessel is well mixed because the small one was.

## Worked example

**Problem.** A synthetic vessel has D = 5 cm, V = 1 L and N = 240 rpm. It is scaled by 5 in linear dimension at constant P/V. Find the starting P/V, the new speed, and the change in tip speed and mixing time.

**Step 1: starting power per volume.** N = 4 rev/s, so P = 1.5 × 1000 × 4³ × 0.05⁵ = 0.030 W and P/V = 30.0 W/m³.

**Step 2: new speed.** N₂ = N₁ × 5^(−2/3) = 1.37 rev/s = 82.1 rpm.

**Step 3: tip speed.** 0.63 m/s becomes π × 1.37 × 0.25 = 1.07 m/s, a factor of 1.71.

**Step 4: mixing time.** 5.0 s becomes 14.6 s, a factor of 2.92.

## Limits of this lesson

All numbers are synthetic. The scaling laws assume geometric similarity, turbulent flow with a constant power number, and a constant dimensionless mixing time; real vessels have baffles, gas sparging (which lowers the power drawn), multiple impellers and non-ideal flow. Nothing here is a design for any real vessel.
