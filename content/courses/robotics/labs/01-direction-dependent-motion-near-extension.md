# Virtual lab 1: direction-dependent motion near extension

**Status:** public formative practice with public answers and unlimited retries. Points are study feedback, not a course grade. All postures, limits, commands and reports are synthetic. This is a local kinematic data exercise, not a robot operating procedure or a validated commissioning test.

## Learning objectives

1. Summarize paired velocity components and calculate inverse joint-rate demands at known postures.
2. Evaluate a common joint-speed limiter and direction-dependent tracking under a frozen Jacobian.
3. Distinguish kinematic limitation, force mapping and conditional evidence for the preserved stall case.

## Construction and independent inputs

The arm has L₁=0.30 m,L₂=0.20 m and shoulder q₁=0. Four elbow postures are 90°,30°,10° and 2°. Each is nonsingular, although the 2° posture is close to straight extension. At each posture, one task requests inward base-frame velocity (−0.01,0) m/s and another requests tangential velocity (0,+0.01) m/s. Here inward and tangent name the fixed base-frame x/y directions at the modeled near-horizontal arm; they are not exact radial/tangent directions about the base for every bent posture.

The dataset [near-extension-reports.csv](near-extension-reports.csv) supplies sample,task,q2_deg,replicate,command_q1_rad_s,command_q2_rad_s,reported_vx_mm_s,reported_vy_mm_s. Shoulder angle, link lengths, desired velocities and limiter rule are independently stated construction inputs. Sample codes combine direction and posture, so they must not be pooled by elbow angle alone.

For each frozen posture, calculate J from the planar position derivative and solve Jq̇_desired=v_desired. Both joint-speed caps are 0.5 rad/s. Define common scale α=min(1,0.5/max(|q̇₁|,|q̇₂|)) and command q̇_command=αq̇_desired. The achieved ideal velocity is Jq̇_command=αv_desired. This uniform scaling is the entire stipulated limiter policy; there is no simulated motor, mass matrix, controller delay or friction in these reports.

The same posture is used throughout each group's instantaneous calculation. The data do not integrate a physical path from 90° to 2°. Consequently they demonstrate local directional rate demands, not successful travel between the listed configurations. Collision clearance, joint-angle limits, acceleration and actual current delivery remain outside this construction.

## Model table

The following unconstrained rates and scales are shown as public formative worked information. Command rates in the CSV are rounded to nine decimal places; velocity reports are rounded to six decimals.

| Sample | Task | Elbow degrees | Desired shoulder rad/s | Desired elbow rad/s | Common scale |
|---|---|---:|---:|---:|---:|
| in90 | inward | 90 | −0.000000 | 0.050000 | 1.000000 |
| in30 | inward | 30 | −0.057735 | 0.157735 | 1.000000 |
| in10 | inward | 10 | −0.189043 | 0.476981 | 1.000000 |
| in02 | inward | 2 | −0.954542 | 2.387227 | 0.209448 |
| ta90 | tangent | 90 | 0.033333 | −0.033333 | 1.000000 |
| ta30 | tangent | 30 | 0.033333 | −0.033333 | 1.000000 |
| ta10 | tangent | 10 | 0.033333 | −0.033333 | 1.000000 |
| ta02 | tangent | 2 | 0.033333 | −0.033333 | 1.000000 |

Each group has three deterministic report variants. Add x perturbations −0.02,zero,+0.02 mm/s to the ideal achieved x velocity, and y perturbations +0.01,zero,−0.01 mm/s to ideal achieved y velocity. Perturbations are applied to reports after the commanded motion is calculated. They do not change the limiter commands. These are deliberately balanced variants, not independent errors sampled from a sensor distribution.

## Work sequence and summary contract

Open Practice gradebook and select this virtual lab as open, ungraded practice. Summarize all 24 reports using exact headers sample,reports,mean_vx_mm_s,mean_vy_mm_s and rows in90,in30,in10,in02,ta90,ta30,ta10,ta02. Counts must be exact; mean checks use the declared absolute tolerance. The uploaded table has 24 numeric checks: three cells for each of eight groups.

Next calculate the desired elbow rate at in02, the active common scale and the achieved inward-speed magnitude. Keep signed velocity components in the CSV summary and positive magnitude in the explicitly magnitude-based numeric response. Mixing m/s with mm/s changes answers by a factor of 1000. The listed joint commands are in rad/s, not degrees/s.

Finally compare common scaling with independent clipping, and calculate the separate force-map example at exact straight extension. That exact singular posture is not one of the CSV's inverse-velocity groups. A finite radial force can have zero joint moment there even though no finite instantaneous joint rate produces radial velocity. The comparison identifies which mathematical question is being answered.

## Worked example

At in02, inverse shoulder rate is about −0.954542 rad/s and elbow rate 2.387227 rad/s. The elbow sets α≈0.209448, so the delivered elbow command is 0.5 rad/s and achieved inward speed is about 2.094480 mm/s. The mean reported y component is zero. All other supplied inward postures stay below the cap and retain mean x component −10 mm/s.

Every tangent group has desired shoulder rate +1/30 rad/s and elbow rate −1/30 rad/s, so α=1 and mean y velocity remains +10 mm/s. These results show directional differences in the declared kinematic mapping. They do not demonstrate that tangential motion is physically safe or dynamically feasible on hardware.

Independent clipping at in02 would give rates (−0.5,+0.5) rad/s. The two equal x Jacobian entries cancel their x contributions, while y velocity becomes −0.15 m/s. Bounded joint commands therefore do not automatically preserve task direction. This counterexample explains why the limiter policy is part of the model, not merely a hidden implementation detail.

## Common mistakes

Pooling both task directions, treating report perturbations as command noise, computing a magnitude where a signed component is requested and applying an inverse at exact rank loss all break the interpretation. Another mistake is treating this known limiter as unique evidence for the preserved hardware-stall case. The CSV contains no current, torque or independent output-position measurements.

## Limits of this lesson

The preserved stall case remains a zero-point self-assessment checklist. These synthetic reports support conditional rate-limit reasoning without identifying a physical fault. The case's amplified-torque wording needs a dynamic model; JᵀF does not universally diverge. Its redundancy option needs extra degrees of freedom or a relaxed task, absent in the nonsingular two-link position model. The original guide and CSV are CC BY 4.0 with substantial AI assistance; no third-party data or figure was imported. Written diagnoses and plans remain ungraded. Qualified review, accessibility review and workload measurement remain absent; one data lab is not a laboratory sequence.
