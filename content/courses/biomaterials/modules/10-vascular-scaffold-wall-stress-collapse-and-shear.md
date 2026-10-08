# Vascular scaffolds: wall stress, collapse, compliance and wall shear stress

A scaffold for a blood vessel is a tube that must carry pressure and flow for weeks to months while it degrades and the host builds a new wall. Three questions are mechanical. How much stress does the pressure put in the wall? When the wall weakens, will it collapse under the loads that surround it? And how much do flow and shear stress on the lumen change if the lumen narrows? Each has a short first-order answer that shows which numbers matter most, and the answers give the framework for the package's case: a degradable vascular scaffold that is open at first and later narrows. All values are synthetic and the formulas are textbook-level estimates; they are not a design method for any device.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute hoop stress, strain and pulsatile distension of a thin-walled tube from pressure, radius, thickness and modulus.
2. Estimate the external pressure at which a tube buckles, and when a degrading wall falls below a given load.
3. Compute how narrowing changes flow and wall shear stress, and evaluate what these numbers do and do not show.

## Wall stress: Laplace's law for a thin tube

For a thin-walled cylinder of mean radius R and wall thickness h under internal pressure P, the circumferential (hoop) stress is

**σ = P R / h.**

Pressure must be in pascals (1 mmHg = 133.3 Pa). **Synthetic values:** P = 120 mmHg = 15,999 Pa, R = 2.0 mm and h = 0.40 mm give σ = 15,999 × 2.0/0.40 = **80.0 kPa**. With a wall modulus E = 2.0 MPa the strain is σ/E = 0.040. The stress grows in proportion to the radius and falls in proportion to the thickness: a thinner wall, or one that dilates, carries more stress.

## Compliance and pulsatile distension

Pressure changes with each heartbeat. For a pulse pressure of 40 mmHg (5,333 Pa), the radial strain of the same wall is ΔP R/(h E) = 5,333 Pa × (2.0 mm / 0.40 mm) / (2,000,000 Pa) = 0.0133, or **1.33%**, which corresponds to a distension of 3.3% per 100 mmHg. A native artery of this size is typically more distensible than a synthetic tube, and a mismatch in compliance at the junction between graft and artery has been proposed as one contributor to local disturbances of flow and stress; the strength of that evidence varies, and the number above is one input to a comparison, not a verdict.

## Collapse under external load: buckling

A long thin tube loaded by external pressure (from surrounding tissue, for example) can buckle, collapsing its cross-section, at

**P_cr = E / (4 (1 − ν²)) × (h/R)³.**

With E = 2.0 MPa, ν = 0.3, h/R = 0.2, P_cr = 4,396 Pa = **33.0 mmHg**. The cube makes thickness the strongest lever: halving h to 0.20 mm lowers P_cr by a factor of eight to 4.1 mmHg. During degradation the modulus falls. If E(t) = E₀ e^(−kt) with k = 0.02 per day, the wall can resist an external load of 10 mmHg only while E ≥ 0.607 MPa, which fails at t = ln(E₀/E)/k = ln(2.0/0.607)/0.02 = **59.7 days**. A design that supports a vessel for ten weeks must keep its modulus, and its thickness, above the level that the surrounding load requires until the host wall can take over.

## Flow and wall shear stress

For steady laminar flow in a tube of radius r, the flow driven by a pressure drop ΔP over a length ℓ is Q = π r⁴ ΔP/(8 μ ℓ), and the shear stress the flow exerts on the wall is

**τ = 4 μ Q / (π r³).**

With a synthetic blood-like viscosity μ = 3.5 mPa·s and Q = 4 mL/s, a lumen of radius 2.0 mm has τ = **2.23 Pa**. If tissue growth narrows the radius by 20% to 1.6 mm, then at the same pressure drop the flow falls to (0.8)⁴ = **0.41** of its value, a loss of 59%; if instead the flow is held constant, the shear stress rises by (1/0.8)³ = 1.95 to 4.35 Pa. Both effects are steep because of the high powers of the radius. Low and oscillatory wall shear has been associated with intimal thickening in many studies, and high shear has its own effects, but shear stress is one input among several (injury, inflammation, compliance, the material itself), so a computed value cannot by itself explain why a scaffold narrowed.

## Common mistakes

- Using pressure in mmHg in a formula that needs pascals.
- Using the thin-wall formula for a thick wall without checking h/R.
- Treating a wall modulus measured dry as the modulus in a wet, degrading, cell-filled wall.
- Forgetting that the buckling pressure depends on the cube of the thickness.
- Assuming that a 20% narrowing of the radius costs 20% of the flow.
- Reading a computed wall shear stress as the cause of narrowing.

## Worked example

**Problem.** A synthetic tube has R = 1.5 mm, h = 0.30 mm, E = 1.5 MPa and carries 100 mmHg. Find the hoop stress and strain, the buckling pressure, and the effect of narrowing the radius from 1.5 to 1.2 mm at 3 mL/s.

**Step 1: stress and strain.** σ = 13,332 × 1.5/0.30 = 66.7 kPa, so the strain is 66.7 kPa / 1.5 MPa = 0.044.

**Step 2: buckling.** P_cr = 1.5 MPa/(4 × (1 − 0.3²)) × (0.30/1.5)³ = 3,297 Pa = 24.7 mmHg.

**Step 3: flow and shear.** At the same pressure drop, flow falls to (1.2/1.5)⁴ = 0.41; at 3 mL/s the shear stress rises from 3.96 Pa to 7.74 Pa, a factor of 1.95.

**Step 4: reading the result.** A modest loss of radius removes more than half the flow capacity at fixed pressure and nearly doubles the shear stress at fixed flow, so small geometric changes are large functional ones.

## Limits of this lesson

All numbers are synthetic. The thin-wall formula, the buckling formula for a long tube and Poiseuille flow assume a homogeneous, isotropic, linear-elastic wall, steady flow and a Newtonian fluid. Real vessels are pulsatile, anisotropic and viscoelastic, blood is shear-thinning, and degrading scaffolds change thickness and modulus together. Nothing here is a design or safety calculation for any device or evidence about any patient.
