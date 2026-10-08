# Buckling of slender struts: Euler's critical load, effective length and slenderness

A short, thick block of material loaded in compression fails when the stress reaches the strength of the material. A long, thin strut can fail much earlier, by bowing sideways at a load that its material could carry many times over. The strut has not been crushed; it has become unstable, and the sideways deflection grows suddenly once a critical load is reached. Slender members are common in the systems this course models: the struts of a lattice scaffold, the columns of a printed frame, an array of thin pillars, and the trabecular struts of bone. This lesson gives Euler's formula for the critical load, shows how the end conditions and the slenderness ratio change it, and states when the formula applies at all. All values are synthetic.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute the second moment of area, radius of gyration and slenderness ratio of a solid circular strut.
2. Use Euler's formula with an effective-length factor to find the critical load and critical stress, and see how they scale with length and diameter.
3. Decide whether elastic buckling or yielding governs a given strut, and size a strut for a design load.

## Buckling is a stability limit

Consider an ideal straight strut, loaded exactly along its axis. Below a critical load, if you push it sideways a little it springs back. Above the critical load, the straight shape is no longer stable and a small disturbance grows into a large bow. The critical load depends on the **stiffness** of the strut, through the elastic modulus E and the second moment of area I, and on its length. It does not depend on the yield strength. Two steel struts of the same dimensions buckle at the same load even if one is made of a much stronger steel, because their modulus is the same. This is the main difference between buckling and the strength limits of earlier lessons, and it explains why making a strut stronger without making it stiffer does not help.

## Euler's critical load

For an ideal, elastic strut with pinned ends (free to rotate, held in position), the critical load is

**P_cr = π² E I / L².**

For other end conditions, replace L with the effective length K L, where K = 1 for pinned–pinned, 0.5 for fixed–fixed, about 0.7 for fixed–pinned and 2 for fixed at one end and free at the other. The more the ends are restrained, the higher the load. For a solid circular strut of diameter d, I = π d⁴/64, the area is A = π d²/4 and the radius of gyration is r = √(I/A) = d/4.

**Synthetic strut:** diameter d = 0.5 mm, length L = 5 mm, E = 2 GPa and pinned ends. Then I = π × 0.5⁴/64 = **3.068 × 10⁻¹⁵ m⁴** (0.003068 mm⁴), A = 0.19635 mm² and r = 0.125 mm. The critical load is P_cr = π² × 2000 N/mm² × 0.003068 mm⁴ / (5 mm)² = **2.422 N**. Doubling the length to 10 mm gives 0.6056 N, one quarter, because the length is squared. Fixing both ends (K = 0.5) gives 9.689 N, four times the pinned value. Because I contains d⁴, doubling the diameter at the same length multiplies the critical load by 16.

## Slenderness ratio and critical stress

Dividing the critical load by the area gives the critical stress σ_cr = π² E / λ², where **λ = K L / r** is the slenderness ratio. For the strut above, λ = 5/0.125 = **40** and σ_cr = π² × 2000 MPa/40² = **12.34 MPa**. The critical stress depends only on the material modulus and on the slenderness; it falls with the square of λ. A strut made more slender by lengthening it or thinning it has a rapidly falling buckling stress, while the material's yield stress is unchanged.

## When Euler's formula applies

Euler's formula assumes that the strut stays elastic. If the critical stress computed from it exceeds the yield stress, the strut will yield or crush before it can buckle, and the formula overestimates the load. The two limits meet at the **transition slenderness** λ* = π √(E/σ_y). With σ_y = 40 MPa and E = 2000 MPa, λ* = **22.21**. Struts with λ well above λ* fail by elastic buckling (the strut above, with λ = 40, is one); struts with λ well below it fail by yielding, with a load of σ_y A; between them there is an inelastic transition in which neither simple formula is accurate.

## From analysis to design

To size a strut for a design load P_design, invert Euler's formula. For a solid circular strut with pinned ends, d = (64 P_design (K L)² / (π³ E))^(1/4). For P_design = 5 N, L = 5 mm and E = 2000 MPa this gives **d = 0.599 mm**, with a slenderness of 33.4, which is above λ*, so the elastic formula is the right one to use. The fourth-power dependence means a small error in diameter is a large error in capacity, and the real design load is set below the critical load by a safety factor applied to the load, because the critical load is an upper bound for real members.

## Imperfections

Real struts are not perfectly straight, not perfectly centred and not perfectly uniform. An initial bow or an off-axis load turns the sudden buckling of the ideal strut into a gradual increase of deflection and a maximum load that is below the Euler value, and the shortfall is largest for struts near the transition slenderness. Residual stresses, creep of polymers under sustained load, and temperature also reduce capacity. A lattice with many struts has a further complication: buckling of a single strut may be followed by redistribution of load to its neighbours.

## Common mistakes

- Using the crushing load σ_y A for a slender strut, or Euler's formula for a stocky one.
- Using the wrong effective-length factor for the actual end conditions.
- Forgetting that I contains d⁴, so that the critical load is very sensitive to diameter.
- Expecting a stronger material with the same modulus to raise the elastic critical load.
- Treating the Euler load as a safe working load without a factor of safety.
- Mixing units: E in MPa with I in mm⁴ and L in mm gives a load in N, but E in Pa with I in mm⁴ does not.

## Worked example

**Problem.** A synthetic strut has d = 0.8 mm, L = 6 mm, E = 1500 MPa, σ_y = 30 MPa, and one end fixed and the other pinned (K = 0.7). Find the Euler critical load, the slenderness ratio, the transition slenderness, and decide which mode governs.

**Step 1: section properties.** I = π × 0.8⁴/64 = 0.02011 mm⁴, A = 0.5027 mm² and r = d/4 = 0.20 mm.

**Step 2: Euler load.** P_cr = π² × 1500 × 0.02011/(0.7 × 6)² = 16.87 N, which corresponds to σ_cr = 33.57 MPa.

**Step 3: slenderness.** λ = 0.7 × 6/0.20 = 21. The transition slenderness is λ* = π √(1500/30) = 22.21.

**Step 4: which governs.** Since λ = 21 is below λ* = 22.21, the Euler stress (33.57 MPa) exceeds the yield stress (30 MPa) and the strut yields first. The yield load is σ_y A = 30 × 0.5027 = 15.08 N, below the Euler value of 16.87 N, so the Euler formula would have overestimated the capacity by 12%. Because λ is close to λ*, the strut is in the transition range, and its real capacity would be a little below both numbers.

## Limits of this lesson

All numbers are synthetic. The lesson treats ideal, straight, solid circular struts of linear elastic material, with the textbook effective-length factors and no allowance for imperfections, creep or load redistribution. Real lattices and bones are not made of ideal pinned struts, and the inelastic range between the Euler and yield limits needs more than the two simple formulas given here. Nothing in this lesson is a design check for any device or structure.
