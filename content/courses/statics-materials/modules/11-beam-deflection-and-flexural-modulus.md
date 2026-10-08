# Beam deflection and stiffness: three-point bending, superposition and what the span and thickness control

The bending stress formula of the earlier lessons answers whether a beam is strong enough. A second question is how much it moves. A bone plate that is strong but too flexible lets a fracture move, a cantilever probe has to be soft enough to be bent by a small force and stiff enough to read it, and a thin polymer strip in a bench test is converted into a modulus only through its deflection. This lesson gives the beam equation, the standard deflection formulas for the cases that come up most often, the three-point bend test as a way to measure a flexural modulus, and the limits of the small-deflection theory. All values are synthetic.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute the second moment of area of a rectangular section and use the standard formulas to find the deflection and stiffness of cantilever and simply supported beams.
2. Obtain a flexural modulus and the maximum stress from three-point bending data.
3. Evaluate how thickness and span control stiffness, and when the simple beam formulas are not valid.

## The beam equation and standard cases

For a beam of linear elastic material, the curvature is proportional to the bending moment: 1/ρ = M/(EI), and for small slopes the deflection y(x) satisfies EI y″ = M(x). Integrating twice and using the boundary conditions (a clamped end has zero deflection and zero slope, a pinned support has zero deflection and free rotation) gives the standard results. The product **EI**, the flexural rigidity, is the only way the material and section enter.

| Case | Maximum deflection |
|---|---|
| Cantilever, load P at the tip | PL³/(3EI) |
| Cantilever, uniform load w per length | wL⁴/(8EI) |
| Simply supported, load P at the centre | PL³/(48EI) |
| Simply supported, uniform load w per length | 5wL⁴/(384EI) |

For a rectangular section of width b and depth h, the second moment of area about the bending axis is **I = b h³/12**, with h the dimension in the direction of the load. A bar that is 5 mm wide and 1 mm thick is 25 times stiffer when the load acts along its 5 mm dimension (on edge) than when it acts along its 1 mm dimension (flat), because I grows with the cube of the dimension along the load: 5³/(5 × 1³) = 25.

## A synthetic three-point bend

**Synthetic strip:** span L = 20 mm, width b = 5 mm, thickness h = 1 mm and E = 3 GPa, loaded at its centre by P = 2 N. Then I = 5 × 1³/12 = **0.4167 mm⁴**, EI = 1250 N·mm², and the central deflection is δ = PL³/(48EI) = 2 × 20³/(48 × 1250) = **0.2667 mm**. The stiffness, the force per unit deflection, is k = P/δ = 48EI/L³ = **7.5 N/mm**. The largest stress occurs at the centre on the outer surfaces: σ = Mc/I with M = PL/4 and c = h/2, so σ = 3PL/(2bh²) = **12.0 MPa**. The deflection is 1.3% of the span, so the small-slope theory is adequate.

## What controls the stiffness

The stiffness of the strip is k = 48EI/L³ = 4Ebh³/L³. It is proportional to the width, to the **cube of the thickness** and to the inverse **cube of the span**. Halving the thickness multiplies the stiffness by 0.125, one eighth, and doubling the span has the same effect, while the strength does not follow the same laws (the maximum stress at a given load rises with the inverse square of the thickness). Therefore a thin beam can be limited by deflection long before it is limited by stress. The same relations explain why the stiffness of a clamped cylindrical pillar of length L and diameter d, k = 3EI/L³ with I = πd⁴/64, is so strongly dependent on the aspect ratio.

**Cantilever and distributed loads.** For the same strip clamped at one end with length 20 mm and loaded with 0.05 N at the tip, δ = PL³/(3EI) = 0.05 × 20³/(3 × 1250) = **0.10667 mm**. For the simply supported strip under a uniform load of w = 0.02 N/mm (a total of 0.4 N), δ = 5wL⁴/(384EI) = **0.03333 mm**.

## Measuring the flexural modulus

A three-point bend test measures the force and the central deflection and fits a slope m = P/δ in the linear region. Solving k = 4Ebh³/L³ for the modulus gives **E = L³ m/(4 b h³)**. For a strip with b = 6 mm, h = 1.2 mm and span L = 24 mm, and a slope of m = 11.2 N/mm, E = 24³ × 11.2/(4 × 6 × 1.2³) = **3733 MPa**. The thickness enters as a cube, so a 5% error in the measured thickness gives an error of about 15% in the modulus, which is why thickness is measured at several points. Soft or hydrated samples need low forces, a check that the supports do not indent the sample, and a statement of the conditions in which the modulus applies.

## Superposition and the limits of the theory

For linear elastic material and small deflections, the deflection from several loads is the sum of the deflections from each. A complex loading is therefore built from the standard cases. The small-deflection theory breaks down when the deflection is no longer small compared with the span (about 10% is a common limit for the simple formulas), when the material is not linear, and when the beam is short and thick, so that shear deformation adds a significant fraction to the deflection. A common rule of thumb is that the span should be at least 16 times the thickness for a flexural modulus test of an isotropic material; anisotropic materials, such as fibre composites, need a larger ratio because their shear stiffness is low compared with their bending stiffness.

## Common mistakes

- Using h where b belongs in I = bh³/12, or the reverse.
- Applying the cantilever formula to a simply supported beam.
- Mixing units: newtons, millimetres and MPa are consistent; metres with MPa are not.
- Expecting a stronger material to give a stiffer beam.
- Forgetting that the thickness enters as a cube in the modulus calculation.
- Using beam theory for a short, thick specimen or a deflection that is not small.

## Worked example

**Problem.** A synthetic strip has b = 4 mm, h = 0.8 mm, span L = 16 mm and E = 2400 MPa, with a central load of 1.3 N. Find the deflection, stiffness and maximum stress, and the thickness needed for a stiffness of 10 N/mm with the same width and span.

**Step 1: section.** I = 4 × 0.8³/12 = 0.17067 mm⁴.

**Step 2: deflection.** δ = 1.3 × 16³/(48 × 2400 × 0.17067) = 0.2708 mm, which is 1.7% of the span.

**Step 3: stiffness and stress.** k = 48EI/L³ = 4.80 N/mm and σ = 3PL/(2bh²) = 12.19 MPa.

**Step 4: required thickness.** From k = 4Ebh³/L³, h³ = kL³/(4Eb) = 10 × 16³/(4 × 2400 × 4) = 1.0667 mm³, so h = 1.022 mm. A change in thickness of 28% raises the stiffness by a factor of 2.08. The span-to-thickness ratio of the original strip is 20, so beam theory is adequate for it; the thicker strip has a ratio of 15.7, slightly below the usual 16, so a check for shear deformation would be wanted.

## Limits of this lesson

All numbers are synthetic. The lesson covers straight beams of linear elastic, isotropic material in small deflection, with the textbook support conditions. It does not cover shear deformation in short beams, large deflection, plasticity, composites or viscoelastic creep, and the three-point bend arithmetic is not a test method for any real material.
