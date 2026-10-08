# Combined stress: principal stresses, Mohr's circle and yield criteria

Earlier lessons found the axial stress from a force and the bending stress from a moment. At most points of a real part these act together with shear, and the question that matters is no longer how large each component is but how large the stress is in the worst direction and whether the combination makes a ductile material yield. A point in a plane stress state has a normal stress on each of two perpendicular faces and a shear stress between them; rotate the faces and all three numbers change, even though the physical state does not. Mohr's circle is a geometric way to follow that change, and yield criteria compress the whole state into one number that can be compared with a test result. This lesson works through plane stress with synthetic values.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute the principal stresses, their orientation and the maximum in-plane shear stress for a plane stress state.
2. Use the stress-transformation equations to find the stress on an inclined plane.
3. Compare the von Mises and Tresca criteria for a ductile material and state what they do not cover.

## Stress on an inclined plane

A plane stress state is given by σx, σy and τxy. For a plane whose normal is rotated by an angle θ counter-clockwise from the x axis, the normal and shear stresses on it are

**σθ = (σx + σy)/2 + (σx − σy)/2 cos 2θ + τxy sin 2θ,**
**τθ = −(σx − σy)/2 sin 2θ + τxy cos 2θ.**

Sign conventions for shear differ between textbooks; the principal values below do not depend on the convention. **Synthetic state:** σx = 80 MPa, σy = 20 MPa and τxy = 30 MPa. On the plane at θ = 30°, σθ = 50 + 30 cos 60° + 30 sin 60° = **90.98 MPa** and τθ = −10.98 MPa. The sum of the normal stresses on perpendicular planes is the same for every θ: σx + σy = 100 MPa is an invariant of the state.

## Principal stresses and Mohr's circle

The faces on which the shear stress is zero are the **principal planes**, and the normal stresses on them are the principal stresses. They are the largest and smallest normal stresses that occur at the point:

**σ1,2 = (σx + σy)/2 ± √[((σx − σy)/2)² + τxy²],  tan 2θp = 2τxy/(σx − σy).**

In Mohr's circle these are the ends of the horizontal diameter. The centre of the circle lies at σ = (σx + σy)/2 on the normal-stress axis, and the radius is R = √[((σx − σy)/2)² + τxy²]. The two faces of the original element plot as the ends of another diameter, and a rotation of the physical plane by θ moves the point around the circle by **2θ**. For the synthetic state, the centre is 50 MPa, R = √(30² + 30²) = **42.43 MPa**, so σ1 = **92.43 MPa** and σ2 = **7.57 MPa**, on planes at θp = ½ atan(2 × 30/60) = **22.5°** from the x axis. The largest in-plane shear stress is the radius, 42.43 MPa, on planes 45° away from the principal planes (90° on the circle), where the normal stress is the centre value of 50 MPa. In plane stress the third principal stress is zero, so the largest shear stress in three dimensions is the largest of half the differences between the three principal stresses, here σ1/2 = 46.21 MPa, which exceeds the in-plane value; this is why the Tresca criterion below uses all three differences.

## Yield criteria for ductile materials

A uniaxial tensile test gives one number, the yield stress σ_y. To use it for a combined state a criterion is needed.

- **Tresca (maximum shear):** yielding begins when the largest shear stress reaches σ_y/2. With the third principal stress included, this is max(|σ1|, |σ2|, |σ1 − σ2|) = σ_y for plane stress.
- **von Mises (distortion energy):** yielding begins when σ_vm = √(σ1² − σ1σ2 + σ2²) = σ_y, which can also be written √(σx² − σxσy + σy² + 3τxy²).

For the synthetic state, σ_vm = **88.88 MPa** by either expression and the Tresca value is 92.43 MPa. With σ_y = 120 MPa the factor of safety against first yield is **1.350** by von Mises and 1.298 by Tresca. Tresca is the more conservative of the two and the difference reaches 15% at most. In pure shear, the two criteria disagree about the shear yield stress: Tresca gives σ_y/2 = 60 MPa and von Mises gives σ_y/√3 = **69.28 MPa**; for ductile metals tested in torsion, the von Mises prediction is usually the closer.

## What the criteria do not cover

These criteria describe the onset of plastic yielding in isotropic, ductile materials whose yield stress is the same in tension and compression. Brittle materials such as ceramics and many glassy polymers fail by fracture, usually governed by the largest tensile principal stress, and their compressive strength is much higher than their tensile strength. Bone and other biological tissues are anisotropic and have different tensile and compressive strengths; fibre composites have strengths that depend on direction. A von Mises number for such a material is not a failure prediction. The criteria also say nothing about fatigue, stress concentrations or buckling, which have their own lessons.

## Common mistakes

- Using θ where 2θ is needed on Mohr's circle, or the reverse.
- Reporting the largest of σx and σy as the largest normal stress, when the principal stress is larger whenever τxy is not zero.
- Treating the von Mises stress as a stress that acts on a particular plane.
- Using von Mises for a brittle material.
- Dropping the third principal stress (zero in plane stress) when applying the Tresca criterion to a state in which both principal stresses have the same sign.
- Mixing sign conventions for shear within one problem.

## Worked example

**Problem.** A synthetic point has σx = 60 MPa, σy = −20 MPa and τxy = 35 MPa, in a ductile material with σ_y = 150 MPa. Find the principal stresses and angle, and the factors of safety by von Mises and Tresca.

**Step 1: circle.** Centre = (60 + (−20))/2 = 20 MPa, half-difference = 40 MPa and R = √(40² + 35²) = 53.15 MPa.

**Step 2: principal values.** σ1 = 20 + 53.15 = 73.15 MPa and σ2 = 20 − 53.15 = −33.15 MPa, at θp = ½ atan(2 × 35/80) = 20.59°.

**Step 3: von Mises.** σ_vm = √(73.15² − (73.15)(−33.15) + (−33.15)²) = 94.21 MPa, so n = 150/94.21 = 1.592.

**Step 4: Tresca.** The principal stresses have opposite signs, so σ1 − σ2 = 106.30 MPa is the largest of the three differences and n = 150/106.30 = 1.411, lower than the von Mises value as expected.

## Limits of this lesson

All numbers are synthetic. The lesson treats plane stress in a linear elastic, isotropic material and the onset of yielding only; it does not cover three-dimensional stress, anisotropic tissue, fracture, fatigue or stress concentrations, and a factor of safety against first yield is not a statement about the safety of any device or person.
