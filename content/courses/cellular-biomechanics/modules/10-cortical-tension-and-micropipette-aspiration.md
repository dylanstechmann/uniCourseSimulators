# Cortical tension and micropipette aspiration: a surface-tension model of a whole cell

When a cell is slowly sucked into a glass pipette, its resistance over the first part of the aspiration is dominated by a thin layer under the membrane, the actin cortex, which behaves as a surface under tension. The force balance is that of a liquid drop: the suction pressure must overcome the pressure that surface tension builds up across a curved interface. The method turns a pressure and two radii into a tension, and it is a good example of a mechanical model with a very small number of parameters whose assumptions can be listed. This lesson derives the pressure balance, computes the cortical tension from a measured threshold, shows how the pressure depends on the pipette and cell sizes, and states what the model leaves out. All values are synthetic.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute a cortical tension from the threshold aspiration pressure and the pipette and cell radii.
2. Predict how the threshold pressure changes with the tension, the pipette radius and the cell radius.
3. Evaluate the assumptions of the liquid-drop model and what it cannot distinguish.

## The pressure balance

Consider a spherical cell of radius R_c held by a micropipette of radius R_p. The cortex carries a tension T (force per length, N/m), constant over the cell surface. The pressure inside the cell exceeds the outside pressure by 2T/R_c (Laplace's law for a sphere). Inside the pipette the cell surface forms a hemispherical cap of radius R_p, where the pressure difference across the interface is 2T/R_p. The suction pressure ΔP applied in the pipette must make up the difference between the two,

**ΔP = 2T (1/R_p − 1/R_c).**

When ΔP exceeds this threshold the cell flows into the pipette; when it is below, the aspirated length stays short. Solving for the tension,

**T = ΔP / (2 (1/R_p − 1/R_c)).**

**Synthetic measurement:** R_p = 4 μm, R_c = 8 μm and a threshold ΔP = 100 Pa give T = 100/(2 × (1/(4 × 10⁻⁶) − 1/(8 × 10⁻⁶))) = **4.0 × 10⁻⁴ N/m**, which is 0.40 mN/m (a typical order of magnitude for the tension of a cell cortex). Over the pipette's circumference the tension supports a force of T × 2πR_p = 10.1 nN.

## How the threshold depends on the sizes

The threshold is proportional to the tension: a cell with twice the tension needs 200 Pa instead of 100 Pa. It depends on the pipette radius through 1/R_p, so a wider pipette (R_p = 6 μm) needs only 33.3 Pa for the same cell, and it depends on the cell radius through the difference: a smaller cell (R_c = 6 μm) with the same tension needs only 66.7 Pa. The method works best when the pipette is clearly smaller than the cell (R_p/R_c of 0.3 to 0.7), because the difference 1/R_p − 1/R_c vanishes as R_p approaches R_c.

## What the model assumes

The liquid-drop model treats the cell as a fluid with a uniform tension at its surface. That is a good description of a cell with a dominant cortex when the aspiration is slow and the cell is in suspension, but it ignores the elastic response of the interior (important in the nucleus and in adherent cells), the viscosity that sets the rate of flow into the pipette, the friction of the cell on the pipette wall, and the heterogeneity of the cortex. A tension is a property of a surface and a modulus is a property of a volume, and they are not interchangeable: a cortex of thickness h = 0.2 μm with tension 0.40 mN/m has an effective stress scale T/h = 2000 Pa, but this is a scale, not a measured modulus. The measured tension also depends on the time scale of the aspiration, the cell's state in the cycle, and the pipette's surface treatment.

## Common mistakes

- Using the diameter in place of the radius in the pressure balance.
- Forgetting that a negative or gauge pressure must be taken as a magnitude.
- Reading a cortical tension as a modulus.
- Using the model for a cell that is strongly adherent or has a stiff nucleus in the pipette.
- Comparing tensions measured at different aspiration rates without saying so.
- Ignoring that the threshold is approached slowly and is read from a change in the aspirated length.

## Worked example

**Problem.** A synthetic cell of radius 6 μm aspirated by a pipette of radius 3 μm has a threshold pressure of 60 Pa. Find the tension and the pressure that a cell of the same size would need with a tension of 0.15 mN/m.

**Step 1: tension.** T = 60/(2 × (1/(3 × 10⁻⁶) − 1/(6 × 10⁻⁶))) = 0.18 mN/m.

**Step 2: new pressure.** ΔP = 2 × 1.5 × 10⁻⁴ × (1/(3 × 10⁻⁶) − 1/(6 × 10⁻⁶)) = 50 Pa.

**Step 3: reading the result.** The tension of this cell is 0.18 mN/m, and a cell with a tension of 0.15 mN/m would need 50 Pa, which is 0.83 times the measured threshold.

## Limits of this lesson

All numbers are synthetic. The liquid-drop model is an idealization for cells in suspension with a dominant cortex; it does not describe adherent cells, the nucleus, or the viscous flow into the pipette, and the numbers are not measurements of any real cell.
