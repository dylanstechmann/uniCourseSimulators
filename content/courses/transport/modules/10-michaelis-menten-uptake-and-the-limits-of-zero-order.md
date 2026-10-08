# When zero order fails: Michaelis–Menten oxygen uptake and a softer edge to the limit

The oxygen-limit lessons assumed that cells consume oxygen at a constant rate wherever there is any oxygen, which gives a clean critical thickness and a sharp anoxic core. Real uptake is saturable. It is nearly independent of the oxygen level when oxygen is plentiful and falls toward zero as oxygen disappears, so the real limit is softer than the model's, and the oxygen in the deep region does not reach exactly zero. This lesson introduces the Michaelis–Menten form of uptake, compares it with zero order using hand calculations, and shows with a numerical solution how the slab's minimum concentration changes near the critical thickness. All parameters are synthetic.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute the uptake rate, and the fraction of the maximum rate, at a given oxygen concentration.
2. Judge where the zero-order approximation is accurate and by how much it overestimates consumption elsewhere.
3. Evaluate how saturable uptake changes the interpretation of a critical thickness.

## Michaelis–Menten uptake

The volumetric uptake rate is v(C) = V_max C/(K_m + C), where V_max is the maximum rate and K_m the concentration at which the rate is half of V_max. **Synthetic values:** V_max = 0.02 mol/(m³·s), the zero-order rate of the earlier lessons, and K_m = 0.005 mol/m³ (5 μM). Then v(K_m) = **0.5 V_max**, and to reach 90% of V_max the concentration must be 9 K_m = **0.045 mol/m³**. At C = 0.02 mol/m³ (a tenth of the surface value), v = 0.02 × 0.02/(0.005 + 0.02) = **0.016 mol/(m³·s)**, or 80% of V_max, so a zero-order model that uses V_max everywhere overestimates the uptake there by the factor V_max/v = **1.25**. At concentrations well below K_m the rate is proportional to C, v ≈ (V_max/K_m) C, a first-order law with the rate constant V_max/K_m = **4.0 per second**. The ratio K_m/C₀ = 0.025 says that this construct is in the zero-order regime for all but the last few percent of the oxygen range.

## What changes in a slab

The zero-order slab has a critical thickness L_c = √(2DC₀/V_max) = 200 μm. With saturable uptake the equation D C'' = v(C) has no closed-form solution, and the numerical results for the minimum concentration, at the sealed face, are:

| Slab thickness (μm) | Zero-order minimum (mol/m³) | Michaelis–Menten minimum (mol/m³) |
|---:|---:|---:|
| 150 | 0.088 | 0.0925 |
| 180 | 0.038 | 0.0493 |
| 200 | 0.000 | 0.0229 |
| 220 | no valid solution | 0.0077 |
| 250 | no valid solution | 0.0016 |

Up to about 180 μm the two models differ little: by 0.005 to 0.011 mol/m³, a few percent of C₀. At the zero-order critical thickness (200 μm) the zero-order model gives exactly zero but the Michaelis–Menten model gives **0.0229 mol/m³**, 11% of the surface value, because uptake slows as oxygen runs down. Above 200 μm the zero-order model has no valid solution (it predicts a negative concentration), while the Michaelis–Menten model keeps giving small positive values that approach zero rapidly: 0.0016 mol/m³ at 250 μm, which is effectively anoxic.

## Interpreting a critical thickness

Two consequences follow. First, the critical thickness of the zero-order model is a good first estimate, because the Michaelis–Menten solution drops to a negligible concentration within a few tens of micrometres of it; the sharp boundary of the zero-order model becomes a gradual transition. Second, a more useful definition of the limit is the thickness at which the minimum concentration falls below a functional threshold, which depends on how the cells respond to low oxygen. Cells change their behavior at oxygen levels well above K_m, so the thickness at which function is lost is smaller than the thickness at which uptake stops, and a design that targets only the second will lose function in the interior. The uptake parameters also need to be measured at the oxygen levels that the cells will experience: a V_max measured in air-saturated medium used in the zero-order model overstates consumption in the deep region, which makes the zero-order critical thickness conservative.

## Common mistakes

- Using V_max as the uptake rate at every oxygen concentration.
- Treating K_m as the oxygen level at which cells die.
- Expecting the Michaelis–Menten model to give exactly zero oxygen in the core.
- Applying a first-order law at concentrations above K_m.
- Reading the zero-order critical thickness as the thickness at which cells begin to lose function.
- Using uptake rates measured at one oxygen level for the whole construct.

## Worked example

**Problem.** A synthetic cell has V_max = 0.03 mol/(m³·s) and K_m = 0.01 mol/m³. Find v at C = 0.03 mol/m³, its fraction of V_max, the concentration for 95% of V_max, the low-concentration rate constant, and the overestimate of a zero-order model at 0.03 mol/m³.

**Step 1: uptake.** v = 0.03 × 0.03/(0.01 + 0.03) = 0.0225 mol/(m³·s).

**Step 2: fraction.** 0.0225/0.03 = 75%.

**Step 3: 95% of V_max.** C = 19 K_m = 0.19 mol/m³.

**Step 4: first-order constant and overestimate.** V_max/K_m = 3.0 per second, and the zero-order model overestimates the uptake at 0.03 mol/m³ by 0.03/0.0225 = 1.33.

## Limits of this lesson

All parameters are synthetic. The numerical results come from a one-dimensional steady model with a constant diffusion coefficient and a single saturable uptake; real cells have several oxygen-consuming pathways, change their uptake with oxygen over hours, and respond to low oxygen with changes in gene expression. Nothing here is a measurement or a statement about any real cell.
