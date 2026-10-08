# Oxygen limits in thick constructs: zero-order uptake, critical thickness and time scales

Cultured tissue and engineered constructs have no blood supply. Oxygen reaches the cells by diffusion, and the cells use it up on the way. Past some thickness the center runs out. That single fact shapes how organoids are grown, why engineered tissues fail when scaled up, and why vascularization is a central goal of regenerative engineering. This lesson derives the simplest model of the effect, uses it to compute a critical thickness, and shows how to compare time scales to decide whether diffusion or consumption is the limit.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute the oxygen profile minimum and the critical thickness for a slab or sphere with zero-order consumption.
2. Use a dimensionless ratio of consumption to diffusion to decide which process limits oxygen delivery.
3. Evaluate design levers (a thinner construct, higher surface oxygen, perfusion, vascularization) against the assumptions of the model.

## The model

Take a slab of tissue of thickness *L* with oxygen supplied at one face, *x* = 0, held at concentration *C*₀, and a sealed face at *x* = *L*. Oxygen diffuses with coefficient *D* and is consumed uniformly at a constant volumetric rate *q* (**zero-order** consumption, meaning the rate does not depend on the local oxygen level as long as oxygen is present). At steady state diffusion supplies what consumption removes:

D d²C/dx² = q, with C(0) = C₀ and dC/dx(L) = 0.

The solution is C(x) = C₀ − (q/D)(L x − x²/2). The lowest concentration is at the sealed face:

**C_min = C₀ − q L² / (2D).**

C_min reaches zero when L equals the **critical thickness**

**L_c = √(2 D C₀ / q).**

For a thicker slab the zero-order solution predicts negative concentration, which is impossible; it means that part of the slab is oxygen-depleted and the model must change there. A construct supplied from both faces behaves like two slabs of half the thickness, so its critical *total* thickness is 2 *L*_c. For a sphere of radius *R* supplied at its surface, the same reasoning gives C_center = C₀ − q R² / (6D) and a critical radius R_c = √(6 D C₀ / q).

## A dimensionless ratio

Two time scales compete. Oxygen takes about t_d = L²/D to diffuse across the construct. The local supply of dissolved oxygen is used up in about t_r = C₀/q. Their ratio

**φ² = t_d / t_r = q L² / (D C₀)**

is a Thiele-type modulus. If φ² is much smaller than 1, diffusion is fast compared with consumption and the interior stays close to the surface concentration. If φ² is of order 1 or larger, the interior is depleted. For the slab, φ² = 2 is exactly the critical thickness. The ratio shows what changes the answer without solving anything: length enters squared, so halving the thickness cuts φ² to a quarter.

## Design levers and what limits them

- **Thinner constructs or smaller organoids.** Effective and limited by the goal.
- **Higher surface oxygen.** *L*_c grows only as the square root of C₀, so doubling the surface level raises the critical thickness by a factor √2, not 2. Very high oxygen can also damage cells, so more is not always better.
- **Lower consumption.** Fewer or less active cells, which is usually at odds with the goal of dense tissue.
- **Perfusion and channels.** Perfusing medium through channels brings oxygen closer to the cells, replacing one long diffusion distance with several short ones. Channel spacing then sets the effective length.
- **Vascularization.** Inducing blood vessels to grow into or within a construct is the physiological solution, with its own demands on time and cell types.

## Where the zero-order model fails

Real oxygen uptake falls when oxygen is low (it follows a saturating, Michaelis–Menten form), so the real core is not at exactly zero oxygen at L_c; cells also change behavior in low oxygen. Real consumption varies between cell types and conditions, tissue is not uniform, and medium layers add resistance at the surface. The critical thickness from the zero-order model is a first estimate for design, and measured oxygen profiles are the test.

## Synthetic parameters

These are **synthetic teaching values** in SI units: D = 2e-09 m²/s, C₀ = 0.2 mol/m³ (0.20 mM), and q = 0.02 mol/(m³·s).

## Worked example

L_c = √(2 × 2e-09 × 0.2 / 0.02) = √(4.0e-08) m = 200 µm. For a 150 µm slab supplied at one face, C_min = 0.2 − 0.02 × (150×10⁻⁶)² / (2 × 2e-09) = 0.0875 mol/m³, about 44% of the surface value. If surface oxygen doubles to 0.4 mol/m³, L_c becomes 283 µm (a factor √2 = 1.41 larger). For L = 100 µm, φ² = 0.02 × (100×10⁻⁶)² / (2e-09 × 0.2) = 0.50, well below the critical value of 2. The sphere's critical radius with the same numbers is 346 µm.

## Limits of this lesson

The parameters are synthetic and the model is a first approximation. The lesson gives no protocol for culturing any tissue and makes no claim about the oxygen needs of any specific cell type.
