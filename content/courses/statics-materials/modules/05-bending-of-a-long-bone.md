# Bending of a long bone: second moment of area, combined stresses and why bones are hollow

Long bones carry body weight and muscle forces, and much of that load is bending, not pure compression. The same beam theory used for building frames explains why limb bones are hollow tubes, how much stress a given moment produces, and why a stiff metal implant can leave the surrounding bone under-loaded. This lesson computes bending and axial stress in an idealized bone cross-section, combines them, compares a hollow tube with a solid rod of the same material, and states a safety factor with its failure criterion.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute the second moment of area of a hollow circular section and the maximum bending stress from a moment.
2. Combine axial and bending stresses at a point and calculate a safety factor against a stated failure criterion.
3. Explain, using I and section area, why a hollow section is more efficient in bending than a solid one of equal area, and evaluate the limits of applying beam theory to bone and implants.

## Bending stress

For a straight beam with a symmetric section under bending moment M, the normal stress varies linearly across the section:

**σ = M y / I,**

where y is the distance from the neutral axis and I is the second moment of area. The largest stress occurs at the outer surface, y = r_o. For a hollow circular section with outer radius r_o and inner radius r_i,

**I = (π/4)(r_o⁴ − r_i⁴).**

**Synthetic cross-section:** r_o = 13 mm and r_i = 7 mm, roughly the proportions of an adult long-bone shaft. Then I = (π/4)(13⁴ − 7⁴) = 20546 mm⁴. Under a bending moment of 100 N·m (10⁵ N·mm), the peak bending stress is

σ_b = 10⁵ × 13 / 20546 = 63.3 MPa,

tensile on one side and compressive on the other.

## Adding an axial load

The same bone also carries an axial compressive force. With P = 2000 N on the area A = π(r_o² − r_i²) = 377 mm², the axial stress is σ_a = P/A = 5.31 MPa, uniform across the section. Stresses that act in the same direction at a point add. On the compressive side of the bend, the total compressive stress is 63.3 + 5.31 = 68.6 MPa; on the tensile side it is 63.3 − 5.31 = 58.0 MPa in tension. Bending dominates: the axial load contributes less than a tenth of the peak stress.

## Safety factor with a stated criterion

A safety factor compares a strength with a stress, and it means nothing without saying which strength and which stress. Using a synthetic compressive strength of 150 MPa and the maximum-normal-stress criterion, SF = 150 / 68.6 = 2.19. Cortical bone is weaker in tension than in compression and weaker still under repeated loading, so the governing case may be the tensile side or a fatigue limit, not this static number.

## Why hollow?

Take the same amount of material (377 mm²) as a solid rod: radius √(A/π) = 10.95 mm and I = (π/4)r⁴ = 11310 mm⁴. Under the same moment its peak stress is 96.9 MPa, 1.53 times the hollow bone's. Material far from the neutral axis contributes to I in proportion to the fourth power of radius, so moving it outward buys bending stiffness and strength without adding mass. The marrow cavity has its own functions; the mechanical point is that a tube is an efficient way to resist bending for a given weight.

## Implants and stress shielding

A metal plate or stem much stiffer than bone carries a larger share of the load when attached to it, because load divides between parallel members in proportion to their stiffness (EI for bending). Bone adapts to its mechanical environment, and under-loaded bone can lose mass. This "stress shielding" is a reason implant design pays attention to stiffness, not only to strength.

## Common mistakes

- Using diameters in place of radii in I = (π/4)r⁴, which inflates I sixteenfold.
- Mixing N·m and N·mm, giving stresses off by a factor of 1,000.
- Quoting a safety factor without naming the failure criterion or the load case.
- Treating bone as isotropic and homogeneous; it is neither.

## Worked example

**Problem.** Ageing-related bone loss in this synthetic model enlarges the inner radius from 7 to 9 mm while the outer radius stays 13 mm. What happens to the peak bending stress under the same moment?

**Step 1.** I = (π/4)(13⁴ − 9⁴) = 17279 mm⁴.

**Step 2.** σ_b = 10⁵ × 13 / 17279 = 75.2 MPa, a 19% rise.

**Step 3.** Endosteal loss removes material near the axis, which matters less for I than outer material would, so the stress rises moderately; if the material itself also weakens, the safety factor falls on both counts. This is a geometric argument with synthetic numbers, not an estimate of fracture risk for any person.

## Limits of this lesson

All dimensions, loads and strengths are synthetic. Real bones are curved, tapered, anisotropic and viscoelastic, and fracture depends on fatigue, rate and local defects that beam theory does not capture.
