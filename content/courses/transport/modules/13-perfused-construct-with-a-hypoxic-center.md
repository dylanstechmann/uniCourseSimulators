# A perfused construct with a hypoxic center: advection supplies the channel, diffusion supplies the tissue

The package's case describes a perfused construct whose inlet oxygen is adequate but whose center is hypoxic. The statement sounds contradictory and is not: oxygen reaches the tissue in two steps, and either step can fail. The medium carries oxygen along a channel (advection), and the oxygen then diffuses from the channel wall into the tissue (diffusion) while cells consume it throughout. Flow sets how much oxygen is left in the channel as it goes, geometry sets how far diffusion must reach, and consumption sets how much is used. This lesson combines the earlier lessons into a model of one channel and its surrounding tissue, computes where the oxygen is lowest, compares design changes with numbers, and says which measurement would falsify the model. All values are synthetic.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute the radial oxygen drop from a channel to the edge of the tissue it supplies, and the axial drop along the channel.
2. Locate the lowest oxygen concentration and compare design changes (flow, channel spacing) by their effects on it.
3. State what each step of the model assumes and design a measurement that could show it to be wrong.

## One channel and its tissue cylinder

**Synthetic geometry:** a channel of radius r_c = 100 μm and length 10 mm supplies a cylinder of tissue that extends to a radius R_t = 200 μm. Medium enters at C_in = 0.2 mol/m³ and flows at 10 μL/min through each channel. The tissue consumes oxygen at a zero-order rate q = 0.02 mol/(m³·s) and has D = 2.0 × 10⁻⁹ m²/s; no oxygen crosses the outer edge of the cylinder, which is the symmetry boundary between neighboring channels (a Krogh cylinder). A functional threshold of 0.03 mol/m³ is used for illustration.

## Step 1: radial diffusion into the tissue

At a given position along the channel, the channel concentration C_c sets the boundary value. In the tissue cylinder, steady zero-order consumption with no flux at R_t gives the lowest concentration at the outer edge,

**C_min = C_c − (q/(4D)) [2 R_t² ln(R_t/r_c) − (R_t² − r_c²)].**

With the numbers above the bracket is 2.545 × 10⁻⁸ m² and q/(4D) = 2.500 × 10⁶ s/m², so the radial drop is **0.0636 mol/m³**, 32% of the inlet value. At the inlet end, where the channel holds 0.2 mol/m³, the tissue minimum is 0.1364 mol/m³: the tissue farthest from the channel is well supplied there.

## Step 2: axial depletion along the channel

The tissue around the channel consumes π (R_t² − r_c²) ℓ q = π × (3.00 × 10⁻⁸) × 0.01 × 0.02 = 1.885 × 10⁻¹¹ mol/s, supplied by the flow. The flow per channel is 10 μL/min = 1.667 × 10⁻¹⁰ m³/s, so the concentration in the channel falls by

**ΔC_axial = (π (R_t² − r_c²) ℓ q)/Q = 1.885 × 10⁻¹¹/(1.667 × 10⁻¹⁰) = 0.1131 mol/m³**

along its length, and the outlet concentration is 0.2 − 0.1131 = **0.0869 mol/m³**. The axial Péclet number is 26,526, so axial diffusion is negligible and the radial model can be applied at each position along the channel with the local channel concentration.

## Step 3: where the oxygen is lowest

At the outlet end the tissue edge is at C_min = 0.0869 − 0.0636 = **0.0233 mol/m³**, 12% of the inlet value and below the functional threshold of 0.03 mol/m³. The inlet oxygen is adequate (0.2 mol/m³), the channel is well perfused at the inlet end, and the tissue farthest from the channel at the downstream end is hypoxic. The two losses add: 0.113 from the flow and 0.064 from the diffusion distance. The wall shear stress at this flow is 4μQ/(π r_c³) = **0.166 Pa**, and the pressure drop along the channel is 33 Pa, so the design is not limited by the pumping.

## Design changes

- **More flow.** To keep the lowest concentration at or above 0.05 mol/m³ the axial drop must not exceed 0.2 − 0.0636 − 0.05 = 0.0864 mol/m³, which needs Q = 1.885 × 10⁻¹¹/0.0864 = 2.182 × 10⁻¹⁰ m³/s = **13.1 μL/min**. The wall shear rises in proportion, to 0.217 Pa. Flow cannot reduce the radial drop at all.
- **Closer channels.** Reducing R_t to 150 μm reduces the radial drop to 0.0144 mol/m³ (a factor of 4.4) and the tissue each channel feeds, so the axial drop falls to 0.0471 and the lowest concentration at the outlet end rises to **0.1385 mol/m³**. Closer channels fix both limits, at the cost of more channels and less tissue volume.
- **Lower consumption or higher inlet oxygen.** Fewer cells lower both drops in proportion; raising the inlet oxygen shifts the whole profile, with the limits on high oxygen noted earlier.

## What would show the model wrong

The model predicts the oxygen at the tissue edge as a function of position along the channel: 0.14 mol/m³ near the inlet falling to 0.023 near the outlet. A measurement that could falsify it is the oxygen concentration (by microsensors or phosphorescent probes) at the edge of the cylinder at several positions along the channel. If the edge is already low near the inlet, radial diffusion is worse than assumed, perhaps because the consumption is higher or the diffusion coefficient lower. If the edge stays high at the outlet end, the flow bypasses the tissue or the consumption is lower. Measuring only the outlet concentration of the medium would not separate the two limits. The unit of replication is the construct, and the measurements should be repeated on independent constructs.

## Common mistakes

- Concluding from an adequate inlet concentration that the whole construct is supplied.
- Raising the flow to fix a limit that comes from the diffusion distance.
- Ignoring the oxygen used along the channel when the radial drop is computed.
- Treating the outlet concentration as the concentration in the tissue.
- Applying the radial formula without the symmetry boundary at the outer edge.
- Choosing a design change without computing which limit is larger.

## Worked example

**Problem.** A synthetic channel with r_c = 75 μm and ℓ = 8 mm supplies tissue to R_t = 150 μm; q = 0.015 mol/(m³·s), D = 2.0 × 10⁻⁹ m²/s, C_in = 0.2 mol/m³ and Q = 4 μL/min. Find the radial drop, the axial drop, the outlet concentration and the lowest tissue concentration.

**Step 1: radial drop.** (q/(4D)) × [2 R_t² ln(R_t/r_c) − (R_t² − r_c²)] = 0.0268 mol/m³.

**Step 2: axial drop.** π (R_t² − r_c²) ℓ q = 6.362 × 10⁻¹² mol/s; divided by Q = 6.667 × 10⁻¹¹ m³/s this is 0.0954 mol/m³.

**Step 3: outlet and minimum.** The outlet channel concentration is 0.2 − 0.0954 = 0.1046 mol/m³ and the lowest tissue concentration is 0.1046 − 0.0268 = 0.0777 mol/m³.

**Step 4: reading the result.** This design stays above the threshold of 0.03 mol/m³ everywhere, and the axial drop is the larger of the two losses.

## Limits of this lesson

All numbers are synthetic. The model treats the tissue as a Krogh cylinder with zero-order consumption, a uniform channel concentration at each position, no consumption in the lumen and no axial diffusion; real constructs have irregular channels, saturable uptake (see the lesson on Michaelis–Menten uptake), varying cell density and cross-flow between channels. The design list is an outline of how to reason, not a protocol, and nothing here is a statement about any real device.
