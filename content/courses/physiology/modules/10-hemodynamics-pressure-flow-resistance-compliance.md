# Hemodynamics: pressure, flow, resistance and compliance

The circulation is a pump driving blood through a network of tubes, and the same relations that govern flow in pipes and electrical circuits describe it. A pressure difference drives flow against resistance; elastic vessels store blood during each beat and release it afterwards. These relations explain why arterial pressure is the product of cardiac output and resistance, why narrowing a small artery has such a large effect on flow, and why stiffer arteries raise pulse pressure. This lesson develops them with the numbers of one synthetic person at rest.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute cardiac output, total peripheral resistance and the flow through a parallel organ bed from pressures and resistances.
2. Apply Poiseuille's relation to predict how radius changes alter resistance and flow.
3. Use compliance to relate stroke volume to pulse pressure, and estimate mean arterial pressure from systolic and diastolic values.

## Pressure, flow and resistance

Flow Q through a vessel or bed equals the pressure difference across it divided by its resistance, **Q = ΔP / R**. For the whole systemic circulation, ΔP is mean arterial pressure (MAP) minus central venous pressure (CVP), Q is cardiac output (CO), and R is total peripheral resistance (TPR):

**MAP − CVP = CO × TPR.**

**Synthetic resting person:** heart rate 80 per minute, stroke volume 60 mL, so CO = 80 × 60 = 4800 mL/min = 4.8 L/min. With MAP = 100 mmHg and CVP = 4 mmHg, TPR = (100 − 4)/4.8 = 20 mmHg per L/min. The equation can be read in either direction: for a given flow, higher resistance means higher pressure, and for a given pressure, higher resistance means lower flow.

## Series and parallel networks

Resistances in series add. Organs are supplied in **parallel**, and for parallel beds the conductances (1/R) add:

**1/R_total = 1/R₁ + 1/R₂ + 1/R₃.**

Suppose three synthetic beds have resistances 40, 60, 120 in the same units. Then 1/R_total = 1/40 + 1/60 + 1/120 = 1/20, so R_total = 20, matching the TPR above. Each bed receives ΔP/R: 96/40 = 2.4, 96/60 = 1.6 and 96/120 = 0.8 L/min, which sum to 4.8. Two consequences follow. A parallel network always has a lower total resistance than its lowest branch, and opening one bed (dilating its vessels) lowers TPR and diverts flow toward it, so something must compensate if pressure is to be held.

## Poiseuille's relation

For steady laminar flow of a Newtonian fluid in a rigid cylinder,

**R = 8 μ L / (π r⁴),**

where μ is viscosity, L length and r radius. Viscosity and length enter linearly, but radius enters as the fourth power. Halving the radius multiplies resistance by 2⁴ = 16 and, at a fixed pressure difference, divides flow by 16. This is why the small arteries and arterioles, whose radii are controlled by smooth muscle, are the main regulators of resistance and of the distribution of flow. Blood is not a simple Newtonian fluid (its apparent viscosity depends on red-cell concentration and on vessel size), and vessels are neither rigid nor straight, so the fourth-power law is a guide to scaling, not an exact calculator.

## Compliance and pulse pressure

The large arteries are elastic. During ejection they stretch and store part of the stroke volume, and during diastole they recoil and keep blood flowing to the tissues. **Compliance** is the volume change per unit pressure change, C = ΔV/ΔP. For a simple model in which the stroke volume is stored in the arteries during a beat, the **pulse pressure** (systolic minus diastolic) is approximately

**PP ≈ SV / C.**

For the synthetic person with blood pressure 124/88 mmHg, PP = 36 mmHg, so C ≈ 60/36 = 1.67 mL/mmHg. If the arteries stiffen to C = 1.2 mL/mmHg with the same stroke volume and the same mean pressure, PP rises to 60/1.2 = 50 mmHg, and systolic and diastolic pressures spread to about 133 and 83 mmHg. The mean pressure did not change; its pulsatile swing did. Arterial stiffening is one of the changes observed with age on average, and pulse pressure is one of its simplest consequences.

**Estimating MAP.** Because diastole is longer than systole, mean pressure sits closer to diastolic than systolic: **MAP ≈ DBP + PP/3**. For 124/88 mmHg this gives 88 + 36/3 = 100 mmHg.

## The heart as pump

Cardiac output is HR × SV. Stroke volume depends on how much the ventricle fills (**preload**), on the resistance it ejects against (**afterload**) and on its contractility. The Frank–Starling relation says that within limits a more filled ventricle ejects more, which matches output to venous return from beat to beat. In a steady state, cardiac output equals venous return, so changes in the circulation's resistance and capacity change the output as well as the pressure.

## Common mistakes

- Adding parallel resistances as if they were in series.
- Forgetting that a parallel network has a lower resistance than any one of its branches.
- Using pressure instead of pressure difference in Q = ΔP/R.
- Expecting a twofold narrowing of a vessel to double its resistance, when halving the radius multiplies it sixteenfold.
- Reading a higher pulse pressure as a higher mean pressure.
- Averaging systolic and diastolic pressure to get MAP.

## Worked example

**Problem.** In the synthetic person, the muscle bed dilates so that its resistance halves to 30, and the other two beds are unchanged. What happens to total resistance, and what must happen for MAP to stay at 100 mmHg?

**Step 1: new conductance.** 1/40 + 1/30 + 1/120 = 0.0667, so R_total = 15.00, down from 20.

**Step 2: effect on pressure.** If CO stayed at 4.8 L/min, MAP would fall to 4.8 × 15.00 + 4 = 76 mmHg.

**Step 3: compensation.** To hold MAP at 100 mmHg the output must rise to (100 − 4)/15.00 = 6.4 L/min, or resistance in other beds must rise. This is the problem that feedback control of heart rate, stroke volume and vessel tone solves, and what the integrated-response lesson examines.

## Limits of this lesson

All values are synthetic and round. Steady flow in rigid tubes is a simplification of pulsatile flow in branching, elastic vessels; the pulse-pressure and MAP approximations vary with heart rate and waveform, and real organ resistances are not independent of each other or of pressure.
