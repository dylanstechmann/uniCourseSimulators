# Stress concentrations: holes, notches and why the nominal stress is not the stress that fails a part

The stress formulas of the basic lessons give the nominal stress in a member: the force over the area, or the moment times the distance over the second moment of area. Real parts have holes for pins, grooves, sharp internal corners and lattice joints, and near each of them the stress is higher than the nominal value, sometimes several times higher. A part can be adequate by the nominal calculation and fail at a hole. This lesson defines the stress concentration factor, gives the classical results for a circular hole and for an elliptical hole or notch, shows the difference between the static and the fatigue consequences, and states what the formulas assume. All values are synthetic.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute the local stress at a hole or notch from a stress concentration factor and the nominal stress.
2. Use the elliptical-hole and notch relations to see how the geometry of the root controls the concentration.
3. Evaluate when a stress concentration matters for static and for fatigue loading, and how to reduce it.

## The stress concentration factor

For a part loaded within its elastic range, the **theoretical stress concentration factor** is

**K_t = σ_max / σ_nom,**

the ratio of the largest local stress to the nominal stress, which is the force over the net area or the bending stress at the section. K_t depends only on the geometry and the type of loading, not on the material or the load. For a small circular hole in a wide plate under uniaxial tension, K_t = **3** at the edge of the hole on the line perpendicular to the load. **Synthetic example:** with a far-field stress of 50 MPa the peak stress at the hole is 3 × 50 = **150 MPa**, above a yield strength of 120 MPa: the edge of the hole yields when the far-field stress reaches only 120/3 = **40 MPa**.

## Elliptical holes and notches

For an elliptical hole with semi-axis a perpendicular to the load and b parallel to it, the classical result is

**K_t = 1 + 2a/b.**

A narrow slit across the load has a large K_t. With a = 2 mm and b = 0.5 mm, K_t = 1 + 2 × 2/0.5 = **9**, and the same 50 MPa far-field stress gives a local stress of **450 MPa**. The radius of curvature at the end of the ellipse is ρ = b²/a, so the result can be written K_t = 1 + 2√(a/ρ), which is the basis of the rule for a notch of depth a and root radius ρ: for a = 1 mm and ρ = 0.1 mm, K_t ≈ 1 + 2√(1/0.1) = **7.32**. Halving the root radius to 0.05 mm raises it to 9.94. A sharp internal corner is the extreme: the concentration grows as the radius shrinks, which is why designers round corners, enlarge fillet radii and add relief features, and why the sharp joints of a lattice or the corners of a printed scaffold strut are the first places to look for a crack.

## Static loading and fatigue

Under a single static load, a ductile material yields locally at the concentration and the stress redistributes, so the net-section stress (force over the area remaining after the hole) is often an adequate basis for the strength of a ductile part, and K_t matters little for the load at final failure. A brittle material cannot redistribute, and fracture starts at the peak stress, so K_t applies in full. Under cyclic loading the local peak stress controls crack initiation even in a ductile material, but real materials are less sensitive than K_t predicts, and the **fatigue notch factor**

**K_f = 1 + q (K_t − 1)**

uses a notch sensitivity q between 0 (no sensitivity) and 1 (full). With q = 0.8 and K_t = 3, K_f = 1 + 0.8 × 2 = **2.6**. Stronger materials and larger notch radii have values of q closer to 1, and a very sharp notch in a ductile metal has a lower q, which is why K_f is smaller than K_t there.

## Nominal stress must use the net section

A plate 30 mm wide and 2 mm thick with a 6 mm hole carries 12 kN. The gross-section stress is 12000/(30 × 2) = 200 MPa, but the stress on the section through the hole, where the area is (30 − 6) × 2 mm², is 12000/(24 × 2) = **250 MPa**, and the local peak stress is K_t times the net-section value for a hole in a plate of finite width, with a K_t that depends on the ratio of hole diameter to width and is read from handbook charts or computed numerically. Using the gross area underestimates the stress.

## Common mistakes

- Applying the nominal stress of the gross section to a part with a hole.
- Using K_t to predict the final load of a ductile part under a single static load.
- Using K_t instead of K_f for fatigue, or ignoring the notch altogether.
- Forgetting that a smaller root radius raises K_t.
- Applying the infinite-plate value of 3 to a hole that is large compared with the width.
- Assuming that a stress concentration can be offset by a stronger material alone.

## Worked example

**Problem.** A synthetic plate with a far-field stress of 90 MPa and yield strength 200 MPa has a hole with K_t = 2.5. It also has an elliptical slot with semi-axes a = 1.5 mm and b = 0.75 mm, and a notch of depth 0.8 mm and root radius 0.2 mm with notch sensitivity q = 0.6. Find the peak stress at the hole, the far-field stress at first yield there, K_t for the slot and the notch, and K_f for the notch.

**Step 1: hole.** σ_max = 2.5 × 90 = 225 MPa; first yield at 200/2.5 = 80 MPa.

**Step 2: slot.** K_t = 1 + 2 × 1.5/0.75 = 5.

**Step 3: notch.** K_t = 1 + 2√(0.8/0.2) = 5.00; K_f = 1 + 0.6 × (5.00 − 1) = 3.40.

**Step 4: reading the result.** The edge of the hole is already above yield at 90 MPa far-field stress (225 against 200 MPa), and the notch concentrates fatigue stress by a factor of about 3.4.

## Limits of this lesson

All numbers are synthetic. The formulas assume linear elastic behavior, an infinite or wide plate, and a smooth ellipse or notch; real parts have finite width, three-dimensional geometry and residual stresses, and the factors are taken from handbooks or computed by finite elements. Nothing here is a design check for any part.
