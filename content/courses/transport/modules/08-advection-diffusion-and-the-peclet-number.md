# Advection and diffusion together: the Péclet number and mass-transfer coefficients

A perfused culture moves solutes in two ways at once. The flow carries them along (advection), and concentration differences spread them (diffusion). Which one controls a given step depends on the scale and on the speed, and the ratio that tells them apart, the Péclet number, is one of the most useful single numbers in the design of a perfused device. This lesson defines it from the two time scales, shows how it decides whether delivery is limited by flow or by diffusion, and introduces the mass-transfer coefficient that describes how fast a solute moves from a flowing stream to the wall. All values are synthetic, and the diffusion coefficient is the one used in the other transport lessons.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute the Péclet number from the advection and diffusion time scales and say which process controls transport.
2. Compute a mass-transfer coefficient for laminar tube flow and the concentration difference needed to supply a wall flux.
3. Evaluate what raising the flow rate does, and does not do, for delivery to a surface.

## Two time scales and their ratio

Over a distance L the flow carries a solute in a time **t_adv = L/U**, where U is the velocity, while diffusion takes **t_diff = L²/D**. Their ratio is the **Péclet number**

**Pe = t_diff / t_adv = U L / D.**

**Synthetic example:** U = 0.2 mm/s (the velocity through a perfused scaffold in the porosity lesson), L = 1 mm and D = 2.0 × 10⁻⁹ m²/s give t_adv = 5 s and t_diff = 500 s, so **Pe = 100**. When Pe is much larger than 1, solute moves along the flow far faster than it spreads sideways, and the flow carries it downstream before diffusion can smooth it. When Pe is about 1 or less, the two are comparable or diffusion dominates: at a velocity of 2 μm/s, Pe = 1. The Péclet number depends on the length chosen. A flow can be advection dominated along a channel of 10 mm and diffusion dominated across a gap of 20 μm, which is the usual situation in a perfused construct.

## From stream to wall: the mass-transfer coefficient

The solute that cells on a wall consume must cross the stream by diffusion toward the wall, even in a fast flow. The flux to the wall is written as a coefficient times a concentration difference,

**N = k_c (C_bulk − C_wall),**

and the coefficient is expressed through the Sherwood number Sh = k_c d/D. For fully developed laminar flow in a tube of diameter d with a uniform wall concentration, Sh = 3.66, a constant. With d = 1 mm and D = 2.0 × 10⁻⁹ m²/s, k_c = 3.66 × (2.0 × 10⁻⁹)/(1 × 10⁻³) = **7.32 μm/s**. The constant Sherwood number has a consequence: **in fully developed laminar flow, k_c does not depend on the flow rate**. A faster flow does not change the transfer across a fully developed stream. It helps by replenishing the bulk concentration along the tube (a mass balance, not a transfer coefficient), and, near the entrance where the concentration profile is still developing, by raising k_c somewhat.

## What the cells need

A confluent monolayer of 2.0 × 10⁵ cells/cm² (2.0 × 10⁹ cells/m²) consuming 2.0 × 10⁻¹⁰ mmol/(cell·h) takes up oxygen at N = 2.0 × 10⁹ × 5.56 × 10⁻¹⁷ mol/(cell·s) = **1.11 × 10⁻⁷ mol/(m²·s)**. The concentration difference needed across the stream is ΔC = N/k_c = 1.11 × 10⁻⁷/(7.32 × 10⁻⁶) = **0.0152 mol/m³**, about 7.6% of an air-saturated bulk value of 0.2 mol/m³. The cells at the wall are therefore not starved by the transfer across the stream in this example. The limits are elsewhere: the bulk concentration falling along the tube, and the supply to cells that are not on the wall.

## Schmidt number and boundary layers

The Schmidt number Sc = ν/D compares the diffusion of momentum with that of the solute: for ν = 0.70 × 10⁻⁶ m²/s, Sc = **350**. Solutes in liquids diffuse very slowly compared with momentum, so a concentration boundary layer near a wall is much thinner than the velocity boundary layer, by a factor of about Sc^(−1/3) = 0.14 in the classical boundary-layer analysis of a flat plate. Thin concentration layers are why transfer coefficients in liquid flows are large for their size, and why they are sensitive to the details of the flow near the surface.

## Common mistakes

- Expecting the mass-transfer coefficient of fully developed laminar flow to rise with the flow rate.
- Using the Péclet number of the channel length to decide what happens across a gap.
- Comparing the velocity with the diffusion coefficient without a length.
- Forgetting that the flux needs a concentration difference between the bulk and the wall.
- Treating advection and diffusion as exclusive alternatives.
- Applying the fully developed value near an entrance or an obstruction.

## Worked example

**Problem.** A synthetic tube of diameter 0.5 mm carries a flow with U = 1.0 mm/s, and a solute has D = 3.0 × 10⁻⁹ m²/s. Cells on the wall take up 2.0 × 10⁻⁷ mol/(m²·s). Find the Péclet number for L = 0.5 mm, the two time scales, k_c (Sh = 3.66) and the concentration difference.

**Step 1: time scales.** t_adv = 0.5 × 10⁻³/(1.0 × 10⁻³) = 0.5 s; t_diff = (0.5 × 10⁻³)²/(3.0 × 10⁻⁹) = 83 s.

**Step 2: Péclet number.** Pe = 83/0.5 = 167: advection dominates along this length.

**Step 3: transfer coefficient.** k_c = 3.66 × (3.0 × 10⁻⁹)/(0.5 × 10⁻³) = 21.96 μm/s.

**Step 4: concentration difference.** ΔC = 2.0 × 10⁻⁷/(2.20 × 10⁻⁵) = 0.0091 mol/m³.

## Limits of this lesson

All numbers are synthetic. The Sherwood number quoted is for fully developed laminar flow in a circular tube with a uniform wall concentration; other geometries, developing flow, a consuming wall with finite kinetics and a porous wall have different values. Nothing here is a design for any device.
