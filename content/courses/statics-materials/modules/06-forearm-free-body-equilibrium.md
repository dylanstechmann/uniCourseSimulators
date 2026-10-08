# Force and moment equilibrium in the body: free-body diagrams of a forearm holding a load

Muscles attach close to joints and act through short lever arms, so holding even a modest weight requires a muscle force many times larger, and the joint carries a large reaction force. Statics makes this precise. This lesson draws a free-body diagram of a forearm holding a load, uses moment equilibrium to find the muscle force and force equilibrium to find the joint reaction, then examines how the muscle's angle and the lever arms change the answer.

## Learning objectives

By the end of this lesson, you should be able to:

1. Draw a free-body diagram for a body segment and apply force and moment equilibrium to find unknown muscle and joint forces.
2. Resolve an angled muscle force into components and compute the resulting joint compression.
3. Interpret mechanical advantage and evaluate how changes in geometry and load affect muscle and joint forces.

## The free-body diagram

Isolate the forearm and hand as one rigid body, held horizontal with the elbow as the pivot. **Synthetic geometry and loads:**

- muscle (biceps-like) pulls upward at 4 cm from the elbow;
- the forearm's weight, 15 N, acts at its center of mass 15 cm from the elbow;
- a load of 50 N is held in the hand 35 cm from the elbow;
- the elbow joint exerts an unknown reaction force R on the forearm.

At rest, the sum of forces and the sum of moments about any point are zero: **ΣF = 0, ΣM = 0.** Choosing the elbow as the moment center removes R from the moment equation, because its lever arm is zero. That is the trick that makes these problems tractable: take moments about the point where the most unknowns act.

## Moment equilibrium: the muscle force

Counterclockwise moments from the muscle balance clockwise moments from the weights:

F_m × 0.04 = 15 × 0.15 + 50 × 0.35 = 2.25 + 17.50 = 19.75 N·m,

so **F_m = 493.8 N**, nearly ten times the load in the hand. The **mechanical advantage** of this lever is d_muscle/d_load = 0.04/0.35 = 0.114: the arrangement trades force for speed and range, since a small muscle shortening moves the hand a large distance.

## Force equilibrium: the joint reaction

Summing vertical forces: F_m − 15 − 50 + R_y = 0, so R_y = -428.8 N; the minus sign means the joint pushes **down** on the forearm with 428.8 N. The joint surface carries a force larger than the load and the arm's weight combined, because it must also resist the muscle's pull.

## An angled muscle

Muscles rarely pull exactly perpendicular to the bone. If the muscle's line of action makes 80° with the forearm, only its perpendicular component F sin θ produces a moment. To supply the same moment, F_m = 493.8 / sin 80° = 501.4 N. The parallel component F cos θ = 87.1 N presses the forearm into the elbow along its length, adding compression that a perpendicular-only analysis misses. As the elbow angle changes, so do both the lever arm and the muscle's angle, which is one reason strength varies through a joint's range of motion.

## How large is that muscle stress?

Dividing the muscle force by a synthetic cross-sectional area of 20 cm² gives a tensile stress of 247 kPa. Skeletal muscle can generate stresses of a few hundred kilopascals at full activation, so this static hold uses a substantial fraction of the capacity of a muscle that size; the comparison shows how quickly lever geometry consumes muscle capacity.

## Common mistakes

- Taking moments about a point other than the joint without including the joint reaction's moment.
- Using full muscle force in the moment equation when only its perpendicular component creates a moment.
- Forgetting the segment's own weight.
- Assigning the joint reaction a direction in advance and then misreading a negative result; a negative value simply means the opposite direction.

## Worked example

**Problem.** The load moves closer to the elbow, to 25 cm. What are the new muscle force and joint reaction (perpendicular muscle)?

**Step 1.** F_m × 0.04 = 15 × 0.15 + 50 × 0.25 = 14.75 N·m, so F_m = 368.8 N.

**Step 2.** R = F_m − 15 − 50 = 303.8 N, again directed down on the forearm.

**Step 3.** Bringing the load 10 cm closer cuts the muscle force by 25%. Load position, not just load weight, sets the internal forces, a point that applies equally to the design of handheld instruments.

## Limits of this lesson

All dimensions and forces are synthetic. The model is a single rigid segment with one muscle; real joints have several muscles sharing load, antagonist co-contraction and changing geometry, so it is not an estimate of loading in any person.
