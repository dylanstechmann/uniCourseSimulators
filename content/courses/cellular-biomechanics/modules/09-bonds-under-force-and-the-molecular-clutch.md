# Bonds under force and rigidity sensing: lifetimes, loading rates and the molecular clutch

A cell cannot feel stiffness directly. It feels it through bonds: integrins attached to the substrate and to the actin network that is being pulled backward by myosin. If the substrate is soft it gives way as the cell pulls, the force on the bond rises slowly and the bond may break first. If it is stiff the force rises fast. So the question "how does a cell sense stiffness?" reduces in part to a race between two time scales, the time to load a bond to a given force and the lifetime of the bond under that force. This lesson writes both in a simple model (the Bell relation for lifetime and a constant loading rate), computes the critical stiffness at which the two are equal, and states what the model leaves out. All values are synthetic.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute a bond's lifetime under force from the Bell relation and the force at which it halves.
2. Compute the loading time on a substrate of given stiffness and compare it with the bond lifetime.
3. Evaluate a critical stiffness from the comparison and the limits of this simple clutch picture.

## Bond lifetime under force

Thermal energy at body temperature, k_B T, is 4.28 pN·nm. A force F applied along a bond lowers the energy barrier to breaking by F x_b, where x_b is a distance to the barrier, and the Bell relation gives the mean lifetime

**τ(F) = τ₀ exp(−F x_b/(k_B T)),**

where τ₀ is the lifetime without force. **Synthetic values:** τ₀ = 1 s and x_b = 0.5 nm. At F = 10 pN, F x_b/(k_B T) = 10 × 0.5/4.28 = 1.168, so the lifetime is multiplied by e^(−1.168) = **0.311**, to **0.311 s**. The lifetime halves at F = k_B T ln 2/x_b = 4.28 × 0.693/0.5 = **5.93 pN**. Forces of a few piconewtons already shorten a bond's life considerably. (Some bonds are "catch bonds" whose lifetime first increases with force; the Bell relation describes the more common "slip bonds".)

## Loading the bond: the substrate as a spring

Myosin drags actin backward at a retrograde flow speed v, which here is 100 nm/s. If the bond is anchored to a substrate that behaves as a spring of stiffness k_s, the substrate stretches as the bond is pulled, and the force rises at the rate k_s v. The time to reach a force F is therefore

**t_load = F/(k_s v).**

On a stiff substrate with k_s = 1.0 pN/nm, t_load = 10/(1.0 × 100) = **0.10 s** to reach 10 pN. On a soft substrate with k_s = 0.1 pN/nm it takes **1.0 s**. The loading time on the stiff substrate (0.10 s) is shorter than the bond lifetime at that force (0.311 s), so the bond usually survives to carry the force; on the soft substrate (1.0 s) it is longer, so the bond usually breaks before the force builds up, and the adhesion does not reinforce.

## A critical stiffness

Equating the loading time to the lifetime at the target force, F/(k_s v) = τ(F), gives

**k_s* = F/(v τ(F)) = 10/(100 × 0.311) = 0.322 pN/nm.**

Substrates stiffer than k_s* load bonds to 10 pN before they fail, and softer substrates do not. This is the core of a molecular-clutch explanation of why cells spread and build adhesions on stiff substrates and not on soft ones, and why the transition occurs over a limited range of stiffness. The number depends on the chosen target force, on the retrograde flow speed (which itself falls when the load rises) and on the bond parameters, so it is an illustration of the logic and not a prediction for any real cell.

## What the model leaves out

Real adhesions contain many bonds sharing the load and rebinding, the actin flow slows as force builds, catch bonds and adhesion-protein unfolding change the force dependence, and the cell responds to force by recruiting more bonds on a time scale of minutes. Viscoelastic substrates give way over time, so a gel with a given stiffness but a fast relaxation can behave as a soft one, which connects this lesson to the rheology lesson. A critical stiffness should be read as a hypothesis about what matters, to be tested by changing the stiffness, the ligand density and the relaxation independently.

## Common mistakes

- Using the bond lifetime without force as the lifetime under load.
- Confusing the stiffness of a single bond's anchor (pN/nm) with a modulus (Pa).
- Taking the critical stiffness as a universal property of cells.
- Forgetting that the loading time depends on the retrograde flow speed as well as the stiffness.
- Treating the Bell relation as valid for catch bonds.
- Ignoring that a viscoelastic substrate relaxes during loading.

## Worked example

**Problem.** A synthetic bond has τ₀ = 2 s and x_b = 0.8 nm. Find the lifetime at 8 pN, the force at which it halves, and the critical stiffness at a retrograde flow of 80 nm/s for a target force of 8 pN.

**Step 1: lifetime.** F x_b/(k_B T) = 8 × 0.8/4.28 = 1.495, so τ = 2 × 0.224 = 0.449 s.

**Step 2: half-life force.** F = 4.28 × 0.693/0.8 = 3.71 pN.

**Step 3: critical stiffness.** k_s* = 8/(80 × 0.449) = 0.223 pN/nm.

**Step 4: reading the result.** Substrates stiffer than 0.22 pN/nm load the bond before it breaks in this model; the value changes with each assumed parameter.

## Limits of this lesson

All numbers are synthetic. The model has one bond, a constant retrograde flow, a linear spring and a fixed target force; it illustrates a mechanism and is not a quantitative model of any real adhesion or cell.
