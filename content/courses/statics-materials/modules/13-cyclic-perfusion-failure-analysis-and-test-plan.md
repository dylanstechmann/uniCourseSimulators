# Why a scaffold that meets its strength target can still collapse: a failure analysis and an accelerated test plan

This lesson brings the earlier ones together on the problem posed in the course case. A porous scaffold meets a yield-strength target in a one-time compression test and collapses under cyclic perfusion. A single compression test applies one load once, to a dry or briefly wetted specimen at room temperature. Service applies a small load millions of times, to a wet specimen at body temperature, whose material may be degrading or creeping throughout. The question is which mechanisms the one-time test cannot see, how large they might be, and how to test for them in weeks instead of months without changing what is being tested. The course case has a three-criterion self-assessment checklist; try it first, then compare your answer with the analysis below. All values are synthetic.

## Learning objectives

By the end of this lesson, you should be able to:

1. Explain why a scaffold that meets a static strength target can fail under cyclic perfusion, using stress amplification, fatigue life and stiffness loss.
2. Estimate the number of cycles in a service period, the strut stress amplitude, the fatigue life and the effect of a loss of strength.
3. Design an accelerated test with controls and stopping criteria, and bound the heating that acceleration introduces.

## The synthetic case

A porous polymer scaffold has a yield strength of 1.9 MPa in a one-time compression test, above the target of 1.5 MPa. In the perfusion system it is loaded by a pulsatile compression with a nominal stress that swings from 0 to 0.4 MPa (mean 0.2 MPa, amplitude 0.2 MPa, R = 0) at 1 Hz for 30 days, in a fluid at 37 °C. The static factor of safety on the peak load is 1.9/0.4 = **4.75**, so the static test suggests a comfortable margin. The scaffold nevertheless collapses within weeks.

## What the one-time test cannot see

- **Fatigue of the struts.** The nominal stress is the force over the whole cross-section, but the load is carried by thin struts. A synthetic lattice model gives a strut stress 40 times the nominal stress at this porosity, so the strut stress amplitude is 40 × 0.2 = **8.0 MPa**. Thirty days at 1 Hz is 30 × 86,400 = **2,592,000 cycles**. With a Basquin law for the strut material, σ_f′ = 30 MPa and b = −0.08, the life is N_f = ½ (8.0/30)^(1/−0.08) = **7.49 million cycles**, about 2.9 times the required number. That is a thin margin for a quantity whose scatter is a factor of ten or more. The strut mean stress would shorten the life further, and this estimate ignores it, as well as the stress concentrations at the junctions.
- **Degradation and creep in the wet, warm environment.** Hydrolysis lowers the strength and the modulus with time, and a sustained mean load makes a viscoelastic polymer creep. Suppose the strength coefficient falls by 15%, to 25.5 MPa. The life becomes 0.98 million cycles, shorter by the factor 0.85^(−12.5) = **7.63**, which is 11.4 days at 1 Hz. The steep exponent of the S–N curve turns a modest loss of strength into a large loss of life.
- **Buckling of slender struts as the stiffness falls.** The Euler load of a strut is proportional to E. A strut with a critical load of 2.0 N when new, carrying 0.86 N at peak load, buckles when the modulus falls to 0.86/2.0 = **0.43** of its initial value, which no one-time test of a new specimen could show.

## Accelerating without changing the mechanism

Thirty days is long for a test, and the same 2,592,000 cycles take 3.0 days at 10 Hz. However, a viscoelastic polymer dissipates energy in each cycle, and faster cycling heats it. With a nominal amplitude of 0.2 MPa, a storage modulus of E′ = 5 MPa and sin δ = 0.1, the strain amplitude is 0.040 and the energy dissipated per volume per cycle is W = π σ_a ε_a sin δ = **2.513 kJ/m³**. At 10 Hz this is 25,133 W/m³. With a volumetric heat capacity of 4.0 MJ/(m³·K), the adiabatic upper bound on the heating rate is **6.28 mK/s**, so a 2 K rise takes at least **318 s** if no heat escapes. At 1 Hz the rate is 0.628 mK/s and the same rise takes 3,183 s. The fluid bath removes heat, so the real rise is smaller, but a test that accelerates by frequency must measure the specimen temperature, keep it at 37 °C, and show that results at 1 Hz and 10 Hz agree. Raising the stress amplitude is another way to accelerate; 25% more amplitude divides the life by 16.3, but only a series of levels that follows the same failure mode back to the service level supports an extrapolation.

## A test plan

| Element | Choice | Reason |
|---|---|---|
| Specimens and environment | 20 specimens (4 amplitude levels × 5) in culture-type fluid at 37 °C with the service flow | degradation and creep act in the wet, warm environment |
| Loading | sinusoidal compression, R = 0, nominal amplitudes 0.15, 0.2, 0.25 and 0.3 MPa, 1 Hz reference | brackets the service level, so the S–N slope is measured |
| Acceleration check | 5 specimens at 0.2 MPa and 10 Hz, specimen temperature measured | tests whether frequency changes the result |
| Controls | unloaded specimens in the same fluid (15 in all, at days 0, 15 and 30), 5 held at the mean stress without cycling, and 5 cycled dry at room temperature at 0.2 MPa | separate degradation and creep from cyclic damage, and show what the environment adds |
| Measurements | secant stiffness every 10⁴ cycles, height, porosity by imaging, pressure drop at fixed flow, mass and molar mass of controls | stiffness, porosity and flow are the quantities the case names |
| Stopping criteria | stiffness down 20%, or height down 10%, or flow resistance up 30%, whichever is first; run-out at 5 × 10⁶ cycles, recorded as censored | decided before the test, so that stopping cannot be adjusted to the data |
| Analysis | log life against log amplitude by level, with censoring, then the 1 Hz and 10 Hz groups compared | follows the statistics and fatigue lessons |

This plan uses 50 specimens (20 + 5 + 15 + 5 + 5). One change at a time is what makes the results interpretable.

## Reading the outcomes

If the lives in the wet fluid are much shorter than in a dry control, degradation or creep is acting; if the stiffness drifts down before any strut fails, damage or creep is accumulating; if the 10 Hz group fails sooner than the 1 Hz group at the same number of cycles, heating or rate effects have changed the mechanism and acceleration is not valid at that level. A rise in flow resistance with little loss of stiffness can indicate collapse of pores. None of these readings is conclusive without a look at the failed specimens.

## Common mistakes

- Treating the static yield strength as the service limit for a cyclic load.
- Using the nominal stress as the strut stress.
- Testing in a dry, room-temperature environment and extrapolating.
- Accelerating by a large increase in frequency or stress without checking temperature or the failure mode.
- Treating specimens that survive to the cutoff as failures.
- Choosing the stopping criteria after seeing the data.

## Worked example

**Problem.** A synthetic scaffold has a nominal amplitude of 0.15 MPa, a strut amplification of 35, and a strut material with σ_f′ = 28 MPa and b = −0.09. The requirement is 2,592,000 cycles. Find the margin on life, the margin after a 15% loss of σ_f′, and the adiabatic heating rate at 10 Hz for E′ = 4 MPa, sin δ = 0.08 and 4.0 MJ/(m³·K).

**Step 1: strut stress.** 35 × 0.15 = 5.25 MPa.

**Step 2: life.** N_f = ½ (5.25/28)^(1/−0.09) = 59.8 million cycles, a margin of 23.1 over 2,592,000.

**Step 3: after degradation.** With σ_f′ = 23.8 MPa, N_f = 9.83 million cycles, a margin of 3.8.

**Step 4: heating.** ε_a = 0.15/4 = 0.0375, W = π × 0.15 × 10⁶ × 0.0375 × 0.08 = 1,414 J/m³ per cycle, so at 10 Hz the rate is 14,137/4,000,000 = 3.53 mK/s and a 2 K rise takes at least 566 s.

**Step 5: conclusion.** A margin of 3.8 after degradation is smaller than the factor of ten that fatigue scatter can span, so the design is not yet shown to be adequate, and the plan above would be the way to find out.

## Limits of this lesson

All numbers are synthetic. The strut amplification, the Basquin constants, the loss of strength and the dissipation are illustrative inputs, not properties of any real scaffold; the estimates ignore the mean stress, stress concentrations, load redistribution among struts and conduction of heat. This is a teaching plan for a synthetic case and not a laboratory protocol or a design basis for any device.
