# Frames, calibration and position uncertainty

**Status:** original formative instruction with substantial AI assistance. Every dimension, reference and error below is synthetic. This lesson extends the compact frame reading with an explicit convention that can be checked through a chain of transformations. It supplies no procedure for operating a physical robot.

## Learning objectives

1. Transform a point between labeled planar frames and invert the transformation.
2. Separate geometric calibration errors from encoder resolution and repeatability.
3. Propagate small translation and orientation uncertainties under explicit assumptions.

## A coordinate pair needs a frame

A target at (0.04,0.02) m has no operational meaning until its frame is named. It might be measured from a plate corner, a camera origin or the robot base. Use p_P for coordinates in plate frame P and p_B for coordinates in base frame B. The transform T_BP maps coordinates from P into B. Define it by p_B=R_BP p_P+t_BP, where t_BP is the plate origin expressed in B and R_BP describes plate-axis directions expressed in B.

For a planar rotation φ, R has rows [cosφ,−sinφ] and [sinφ,cosφ]. Rotation preserves distances and orientation when detR=+1. A matrix with orthogonal columns and determinant −1 describes a reflection, not the rigid rotation assumed here. Checking determinant and orthogonality helps identify a mirrored calibration or mixed axis convention, although those checks alone cannot identify the correct physical frame.

In homogeneous coordinates, append one to the point and use a three-by-three matrix with R in its upper-left block, t in its final column and bottom row [0,0,1]. Direction vectors use homogeneous final entry zero, so translation does not apply to them. This distinction matters when transforming a velocity direction instead of a target position. Applying a point transform indiscriminately to both adds a false translational velocity.

## Compose by matching the frame labels

If a camera C reports a plate point and transforms T_BC and T_CP are known, then T_BP=T_BC T_CP. Apply the rightmost mapping first. Inverting the chain reverses its order: T_PB=T_PC T_CB. Multiplication is associative but generally not commutative. A program that stores unlabeled matrices can multiply valid arrays in the wrong order while producing plausible coordinates.

For a single mapping, p_P=R_BPᵀ(p_B−t_BP). The inverse translation is −R_BPᵀt_BP, rather than simply −t_BP. Rotation and translation must both change their expressed frame. A round-trip test maps a known plate point into B and back, checking that the original coordinates are recovered. It checks algebraic consistency, not whether the measured calibration corresponds to the actual plate placement.

An original text map makes the convention explicit:

```text
plate coordinates p_P --T_CP--> camera coordinates p_C --T_BC--> base coordinates p_B
```

Read the map from left to right for a point's journey. The corresponding matrix product acts right to left on the column vector. The arrows describe coordinate mappings, not a physical motion of the plate. This verbal description is intended to accompany the text map; assistive-technology review remains outstanding.

## Calibration and repetition answer different questions

Repeatedly reaching the same wrong point can show repeatability without accuracy. Encoder counts can be fine while a plate origin is displaced by several millimeters. A tool offset also changes the point whose position is being controlled. The wrist frame origin and the tip are distinct; rotating a fixed tool offset changes its base-frame contribution.

Calibration needs independently supplied references that constrain the intended unknowns. A single planar point cannot separately determine arbitrary rotation and translation. Two distinct point correspondences can constrain a proper planar rigid mapping in an ideal noiseless setting. Nearly coincident references give weak orientation information, because a small positional perturbation can greatly alter the short baseline's angle. Real fitting requires multiple checks and a suitable error model.

## Small orientation error grows with lever arm

For a point r meters from the plate origin, small orientation error δφ in radians causes a tangential position error approximately rδφ. An error near the origin can be small while an error near the far corner is much larger. The sign and direction depend on the point, so orientation error should not always be treated as a scalar translation added identically to every target.

If one translation component has standard uncertainty u_t and the corresponding orientation-induced component has standard uncertainty u_r, independence permits u=√(u_t²+u_r²). This is a standard uncertainty, not a worst-case bound. For bounded magnitudes, a conservative scalar sum can be appropriate instead. Correlated errors require covariance terms; more repeated measurements do not eliminate a shared calibration bias.

## Worked example

A synthetic plate is rotated 90° counterclockwise relative to B, with origin t_BP=(0.30,0.10) m. The point p_P=(0.04,0.02) m rotates to (−0.02,0.04), then translates to p_B=(0.28,0.14) m. Subtracting t and applying Rᵀ returns (0.04,0.02). Translating before rotating as though the translation were expressed in P would give a different answer and violate the stated convention.

At r=0.10 m, orientation standard uncertainty 0.002 rad contributes 0.0002 m, or 0.2 mm, in its tangential component. Combining that component with independent translation standard uncertainty 0.3 mm gives approximately 0.360555 mm. If the same numbers were instead declared strict error bounds, their sum would be 0.5 mm. Neither value measures actual accuracy; both are conditional calculations from supplied synthetic assumptions.

## Common mistakes

Omitting frame labels, negating translation without rotating it, treating directions as points and confusing repeatability with calibration accuracy all change the interpretation. Using degrees in rδφ exaggerates the result. A perfectly invertible matrix can still describe an incorrect real calibration, so round-trip algebra is necessary evidence with limited scope.

## Limits of this lesson

The construction is planar and locally linear for uncertainty propagation. Camera projection, three-dimensional hand-eye calibration, covariance estimation and actual reference metrology need further work. Choices and numbers assess selected calculations, not a calibration implementation or physical accuracy. The [Modern Robotics transformation supplement](https://modernrobotics.northwestern.edu/nu-gm-book-resource/3-3-1-homogeneous-transformation-matrices/) is link-only. Original explanation, map and parameters are CC BY 4.0; no diagram or teaching asset was imported. Qualified review and workload measurement remain absent.
