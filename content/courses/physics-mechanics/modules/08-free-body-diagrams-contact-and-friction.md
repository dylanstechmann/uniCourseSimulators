# Free-body diagrams, contact and friction

## Learning objectives

1. Identify forces on one selected body with explicit axes and interactions.
2. Test static contact feasibility before using a kinetic-friction model.
3. Distinguish contact forces, net forces and frame-dependent interpretations.

## Select one body before drawing arrows

A free-body diagram includes forces acting on the selected body, not every force in the surrounding scene. For a synthetic block on a horizontal support, choose x right and y up. Gravity acts downward, support normal upward, an applied horizontal force right and possible friction left when it opposes rightward relative sliding or its tendency. The following original text diagram summarizes that selected case.

```text
             N
             ^
             |
      f <-- [block] --> F
             |
             v
             mg
```

Description: four arrows act on the block. N points vertically upward, mg vertically downward, F horizontally right and f horizontally left. Their displayed lengths are schematic rather than a force scale. The direction assigned to friction follows the selected relative-motion tendency and must be reconsidered if the interactions change.

The support's force on the block and the block's force on the support are a third-law pair on different bodies. They do not cancel within this one-body diagram. Weight and normal also are not a third-law pair, even when their magnitudes are equal. That equality follows from the block's particular vertical force balance, not from an automatic rule that every normal equals mg.

## Contact conditions first

Take mass m=2.0 kg and g=9.81 m/s² with no vertical acceleration or other vertical forces. Normal magnitude is N=19.62 N. If the applied force has an upward or downward component, or the support accelerates vertically, N must be recalculated. An ordinary nonadhesive support can push but not pull the block; a proposed negative normal is a warning that the assumed contact may be lost.

The [OpenStax friction section](https://openstax.org/books/university-physics-volume-1/pages/6-2-friction) is a link-only reference for the simple static/kinetic distinction. We stipulate synthetic coefficients μ_s=0.40 and μ_k=0.20. They are model inputs rather than measured properties of a particular material pair. Static friction magnitude is bounded by μ_sN; it does not always equal that maximum.

## Static feasibility is an inequality

The bound here is 0.40×19.62=7.848 N. Under a rightward 6.0 N push from rest, a stationary solution needs leftward friction of 6.0 N, below the bound. Thus static equilibrium is feasible in the stipulated model. Assigning the full 7.848 N would produce a spurious leftward acceleration and violate the intended static constraint.

A rightward 8.0 N push exceeds the static bound. Once the block slides right and the kinetic model applies, friction magnitude is 0.20×19.62=3.924 N. Net horizontal force is 8.0−3.924=4.076 N, giving acceleration 2.038 m/s². The change of friction law is a declared idealization; it does not resolve every real transition or speed dependence.

At a force exactly equal to the static limit, the simple inequality permits a limiting static solution. It does not determine the effect of every perturbation or provide a unique transition history. A model with kinetic friction also needs the sliding direction so that its force sign is specified. Friction opposes relative slipping, not necessarily the center-of-mass velocity in every situation.

## Inclined axes reduce confusion

For a separate 2.0 kg block on a 30° incline, choose one axis down the slope and the other normal to it. With no normal acceleration, N=mg cos30°≈16.991418 N. The downhill weight component is mg sin30°=9.81 N. A static solution would need that much uphill friction, but the same μ_s model permits only about 6.796567 N, so it is not feasible.

Under downhill kinetic sliding, acceleration is g(sin30°−μ_k cos30°)≈3.205858 m/s². Replacing the normal with mg would overstate friction on this slope. The two components of weight are projections of one force, not extra forces added alongside the original weight vector. A diagram should show either the vector with its component interpretation or a consistent component accounting.

## Net force and one interaction differ

In a separate vertical example, a 2.0 kg suspended point mass accelerates upward at 1.0 m/s². T−mg=ma gives tension 21.62 N, while net upward force is only 2.0 N. The measured tension cannot be replaced by net force merely because both are associated with the same acceleration. Likewise, stopping an object by contact while gravity acts requires including both forces in the momentum balance.

Newton's inertial-frame relation concerns the vector sum. A zero acceleration can coexist with several nonzero forces that balance, and constant-speed motion does not imply no interactions. An accelerating camera or support can complicate a visually inferred acceleration; explicitly name the frame before concluding that a diagram contradicts motion.

## Worked example

For the level block, calculate N=19.62 and the static limit 7.848 N. Compare the required friction under a 6 N push with that limit before selecting a model. For 8 N and rightward sliding, use kinetic friction 3.924 and net force 4.076. In the inclined example, project weight, test the static inequality and then compute the downhill acceleration. Finally distinguish tension 21.62 N from the 2 N net force in the suspended example.

## Common mistakes

Do not put action/reaction partners on the same one-body diagram or set static friction to its maximum by default. Check contact feasibility, relative sliding direction and all normal components. Do not confuse a component of one force with another force or a contact reading with the net force.

## Limits of this lesson

Masses, coefficients and imposed motions are synthetic. Contact and Coulomb friction are restricted introductory models, with no actual material pairing, device setting or biological load recommendation. The text diagram is original and fully described but has no assistive-technology review. Original instruction has substantial AI assistance. The course remains partial, unreviewed and formative-only.
