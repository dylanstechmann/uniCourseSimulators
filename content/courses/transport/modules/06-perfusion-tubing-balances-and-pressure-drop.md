# Perfusing a culture through tubing: control-volume balances, Reynolds number and pressure drop

A perfusion system pumps medium from a reservoir, through tubing and a heater, into a culture chamber. Designing it means answering a few concrete questions: is the flow laminar, how much pressure does the pump need, how much power warms the medium to 37 °C, and how much shear do cells or walls feel? Each is a control-volume balance or a standard correlation. This lesson works through them for a synthetic perfusion line.

## Learning objectives

By the end of this lesson, you should be able to:

1. Write steady control-volume balances for mass and energy across a heated flow line and compute the heating power required.
2. Calculate mean velocity and Reynolds number to determine the flow regime in a tube.
3. Estimate pressure drop and wall shear stress for laminar flow with the Hagen–Poiseuille relation, and evaluate how they scale with diameter.

## Control volumes

Draw a boundary around the part of the system you care about. At steady state, for each conserved quantity, **rate in = rate out** (plus any generation or consumption inside). For mass in a rigid line of incompressible fluid, mass flow in equals mass flow out: ṁ = ρQ is the same at every cross-section. That is why velocity rises where the tube narrows.

For energy in a heater with negligible changes in kinetic and potential energy and no work other than the heating, the steady balance is

**Q̇_heat = ṁ c_p (T_out − T_in).**

**Synthetic line:** medium (ρ = 1000 kg/m³, c_p = 4180 J/(kg·K), viscosity μ = 7.80×10⁻⁴ Pa·s) flows at 2.0 mL/min = 3.333×10⁻⁸ m³/s. Mass flow is ṁ = 3.333×10⁻⁵ kg/s, and heating from 22 to 37 °C needs Q̇ = 3.333×10⁻⁵ × 4180 × 15 = 2.09 W, plus whatever the tubing loses to the room downstream. If the heater is placed far from the chamber, those losses can cool the medium before it arrives; the energy balance drawn around the tubing segment shows how much.

## Flow regime: Reynolds number

The **Reynolds number** compares inertial to viscous forces: **Re = ρ v D / μ**, with v the mean velocity Q/A. In a 1.0 mm tube, A = 7.854×10⁻⁷ m² and v = 42.4 mm/s, so Re = 54.4. Flow in straight tubes stays laminar below roughly 2,000; perfusion systems, microfluidic chips and most small blood vessels are deep in the laminar regime. Laminar flow is predictable and smooth, but it also mixes poorly: two streams flowing side by side in a channel mix only by diffusion.

## Pressure drop: Hagen–Poiseuille

For fully developed laminar flow in a circular tube of length L,

**ΔP = 128 μ L Q / (π D⁴).**

For a 0.5 m length: ΔP = 128 × 7.80×10⁻⁴ × 0.5 × 3.333×10⁻⁸ / (π × (10⁻³)⁴) = 529.7 Pa. The fourth-power dependence on diameter dominates design: halving the diameter to 0.5 mm raises the pressure drop sixteenfold, to 8475 Pa, at the same flow. Long, narrow tubing can demand more pressure than a small pump or a chip's bonding can tolerate, and pressure also drives gas out of solution as bubbles at low-pressure points.

## Wall shear stress

For the same flow, the shear stress at the wall is **τ_w = 32 μ Q / (π D³)** = 0.2648 Pa. Cells cultured on channel walls respond to shear: endothelial cells, for example, align and change gene expression under sustained flow. In a perfused construct, shear on cells depends on local channel or pore size, not just tube size, so the tube calculation is a bound on the delivery path, not on the cells.

## Common mistakes

- Using radius in place of diameter (or vice versa) in Re or Hagen–Poiseuille; the D⁴ term makes this a sixteenfold error.
- Forgetting to convert mL/min to m³/s.
- Assuming the medium arrives at the heater's outlet temperature regardless of tubing length.
- Applying Hagen–Poiseuille in short tubes where the flow is still developing, or in non-circular channels without the appropriate shape factor.

## Worked example

**Problem.** The same flow (2.0 mL/min) is sent through a microfluidic channel modeled as a 0.2 mm diameter tube, 20 mm long. Find Re and ΔP.

**Step 1.** v = Q/A = 1.061 m/s; Re = 1000 × 1.061 × 0.0002 / 7.80×10⁻⁴ = 272, still laminar.

**Step 2.** ΔP = 128 × 7.80×10⁻⁴ × 0.020 × 3.333×10⁻⁸ / (π × (2×10⁻⁴)⁴) = 13242 Pa.

**Step 3.** A channel 25 times shorter than the tubing still needs about 25 times its pressure drop, because diameter enters to the fourth power. Flow rates suitable for tubing can be impractical in microchannels.

## Limits of this lesson

All properties and dimensions are synthetic; culture medium viscosity depends on temperature and serum content. The formulas assume steady, fully developed, Newtonian, laminar flow in rigid circular tubes.
