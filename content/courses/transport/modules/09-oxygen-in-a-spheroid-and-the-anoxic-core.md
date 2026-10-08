# Oxygen in a spheroid: the critical radius, the anoxic core and why the rim is not a constant thickness

Cell aggregates, spheroids and organoids are three-dimensional cultures without a blood supply, and they are the first place where oxygen limitation shows. Their cores die when they grow beyond a certain size, and the dying core is a standard feature of their histology. The slab model of the oxygen-limit lesson gave a critical thickness, but a sphere is supplied from every direction, and the geometry changes the answer. This lesson reviews the sphere's critical radius, extends the model to a sphere larger than that radius, which has an anoxic core, and computes how the core grows and how thick the living rim is. All values are synthetic and use the same diffusion coefficient, surface concentration and zero-order consumption as the slab lesson.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute the central oxygen concentration and the critical radius of a sphere with zero-order consumption.
2. Describe the anoxic core of a larger sphere, its radius and its share of the volume, and the thickness of the living rim.
3. Estimate the time a growing spheroid takes to reach its critical size and evaluate the limits of the model.

## The critical radius

For a sphere of radius R supplied at its surface (concentration C₀) with zero-order consumption q and diffusion coefficient D, the steady profile is C(r) = C₀ − (q/(6D))(R² − r²), so the centre has

**C_centre = C₀ − q R²/(6D),**

and the centre just reaches zero at the **critical radius** R_c = √(6 D C₀/q). With D = 2.0 × 10⁻⁹ m²/s, C₀ = 0.2 mol/m³ and q = 0.02 mol/(m³·s), R_c = √(6 × 2.0 × 10⁻⁹ × 0.2/0.02) = **346.4 μm**. A sphere of R = 300 μm has C_centre = 0.2 − 0.02 × (300 × 10⁻⁶)²/(6 × 2.0 × 10⁻⁹) = **0.050 mol/m³**, a quarter of the surface value. The sphere's critical radius (346 μm) is larger than the slab's critical thickness (200 μm), because a sphere has a larger surface for the volume it must supply.

## Beyond the critical radius: an anoxic core

For R above R_c, the model has to change. Oxygen is zero inside a core of radius r_n, where consumption cannot take place, and the living rim between r_n and R obeys the same equation with two conditions at r_n: the concentration is zero and the gradient is zero (no oxygen crosses into the core). The solution is

**C(r) = (q/(6D)) (r² − 3 r_n² + 2 r_n³/r) for r_n ≤ r ≤ R,**

and the condition at the surface, C₀ = (q/(6D)) (R² − 3 r_n² + 2 r_n³/R), fixes r_n. It is a cubic that is solved numerically; results for the synthetic parameters are:

| Radius (μm) | Centre concentration (mol/m³) | Anoxic core radius (μm) | Core share of volume |
|---:|---:|---:|---:|
| 200 | 0.133 | — | 0% |
| 300 | 0.050 | — | 0% |
| 346.41 | 0.000 | — | 0% |
| 400 | 0 (anoxic core) | 130.5 | 3.5% |
| 500 | 0 (anoxic core) | 256.7 | 13.5% |
| 600 | 0 (anoxic core) | 367.8 | 23.0% |

A sphere of 400 μm has a core of radius 130.5 μm, only **3.5%** of its volume, yet the cells inside it are dead or dying. At 500 μm the core is 256.7 μm in radius and **13.5%** of the volume, and the rim of living cells is 243.3 μm thick. The rim is not a constant thickness. It is thicker than the slab's 200 μm because the oxygen enters through an outer surface that is larger than the inner boundary of the rim, and it thins toward 200 μm as the sphere grows (232.2 μm at a radius of 600 μm), while the living fraction of the cells keeps falling. A fall in cell viability measured by a bulk assay is therefore an indirect and late sign of a growing core.

## How fast a spheroid reaches its limit

If the spheroid grows exponentially in volume with a doubling time t_d, the radius grows by a factor of 2^(t/(3 t_d)). Starting at R₀ = 100 μm with t_d = 24 h, the time to reach the critical radius is t = 3 t_d log₂(R_c/R₀) = 3 × 24 × log₂(346.4/100) = **129 h**, or 5.4 days. After that the core develops while the outer rim keeps growing, so growth slows. A spheroid kept in a stationary medium also depletes the surface concentration C₀, which the model holds fixed.

## Design levers

Raising the surface concentration helps only slowly, since R_c grows as √C₀: doubling C₀ raises R_c by a factor of **1.414**, to 490 μm. Lower consumption (fewer or less active cells) raises R_c as 1/√q. Stirring or perfusing the medium keeps C₀ at its set value but does not change the diffusion inside the sphere. For larger aggregates the options are to accept a core, to culture them in a medium with higher oxygen (with its own risk to cells), or to supply oxygen internally with channels.

## Common mistakes

- Using the slab's critical thickness for a sphere.
- Quoting a spheroid's diameter limit as 2 R_c when the surface concentration is not held fixed.
- Treating the anoxic core as the only sign of limitation, when the rim also has a gradient.
- Expecting a doubling of the surface oxygen to double the critical radius.
- Using the zero-order solution below zero concentration inside a sphere larger than R_c.
- Assuming that viability measured on the whole spheroid reflects the rim.

## Worked example

**Problem.** A synthetic spheroid has D = 1.5 × 10⁻⁹ m²/s, C₀ = 0.15 mol/m³ and q = 0.03 mol/(m³·s). Find R_c, the central concentration at R = 180 μm, and the time for a spheroid growing from R = 80 μm with t_d = 30 h to reach R_c.

**Step 1: critical radius.** R_c = √(6 × 1.5 × 10⁻⁹ × 0.15/0.03) = 212.1 μm.

**Step 2: central concentration.** C_centre = 0.15 − 0.03 × (180 × 10⁻⁶)²/(6 × 1.5 × 10⁻⁹) = 0.042 mol/m³.

**Step 3: time.** t = 3 × 30 × log₂(212.1/80) = 127 h.

**Step 4: reading the result.** 180 μm is 85% of the critical radius, and the centre keeps 28% of the surface concentration, so no core is expected there.

## Limits of this lesson

All numbers are synthetic. Zero-order consumption, a fixed surface concentration, uniform cells and a sharp edge to the core are idealizations; real uptake falls at low oxygen (see the next lesson), real cores are partly necrotic and partly quiescent, and the cells at the rim consume oxygen at different rates from the cells deeper in. Nothing here is a protocol or a statement about any real aggregate.
