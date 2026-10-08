# Degradation and release from hydrogels: half-lives, diffusion times and matching a repair timeline

A scaffold meant to help tissue regenerate should support cells while new tissue forms and then get out of the way, and if it carries a signal it should release it over a useful period. Both behaviors are set by rates: how fast the material loses mass and how fast a cargo diffuses out. This lesson estimates both from simple models, compares their time scales, and frames design as matching them to the biological process the scaffold serves.

## Learning objectives

By the end of this lesson, you should be able to:

1. Calculate degradation half-life and remaining mass for a first-order degradation model.
2. Estimate a diffusion release time from gel dimension and diffusion coefficient and predict how size and cargo change it.
3. Compare degradation and release time scales with a tissue repair timeline and distinguish bulk from surface erosion.

## First-order degradation

Many hydrolytically degrading hydrogels lose mass approximately in proportion to how much remains, M(t) = M₀ e^(−kt). The half-life is **t½ = ln 2 / k**, independent of starting mass. With a synthetic rate constant k = 0.05 per day, t½ = 13.9 days and after 30 days 22.3% of the mass remains. Reaching 10% remaining takes ln 10 / k = 46 days.

Mass loss and mechanical loss are not the same curve. A crosslinked network can lose much of its stiffness through scission of a small fraction of crosslinks before much mass has dissolved, and in some polyesters acidic degradation products accelerate degradation from the inside, so a single exponential describes some systems poorly. The rate constant also depends on the environment: pH, enzymes, temperature and the local cell population can all change it, so a rate measured in buffer on a bench is a starting estimate for an implant, not a prediction.

## Bulk and surface erosion

If water penetrates the material faster than bonds break, degradation happens throughout the volume (**bulk erosion**): the device keeps its shape while its mass and strength fall, and then it can fragment late. If bonds break faster than water penetrates, degradation is confined to the surface (**surface erosion**): the device shrinks steadily from outside in and its release can be closer to constant. Hydrophilic hydrogels and many polyesters erode in bulk; some hydrophobic polyanhydrides erode at the surface.

## Diffusion-controlled release

A cargo that does not bind the gel leaves by diffusion. The characteristic time to diffuse a distance L is **τ ≈ L² / D**. For a slab of half-thickness L = 1 mm and a protein with D = 10⁻¹⁰ m²/s inside the gel, τ ≈ (10⁻³)² / 10⁻¹⁰ = 10⁴ s ≈ 2.8 h. Two consequences follow from the square:

- halving the dimension to 0.5 mm cuts the time fourfold, to 0.7 h;
- a smaller molecule with D = 5×10⁻¹⁰ m²/s leaves in 0.56 h from the 1 mm slab.

Diffusion within the gel is slower than in water because the polymer network obstructs it, especially when the network's **mesh size** approaches the size of the cargo. Tightening the network (more crosslinks, more polymer) slows release, but it also stiffens the gel and can slow cell infiltration.

## Matching time scales

The design question is which process is rate limiting and whether it fits the biology:

- If τ_diffusion ≪ t½, release is diffusion-controlled and finishes long before the gel degrades. A protein released within hours cannot support a process that takes weeks.
- To slow release to the degradation time scale, the cargo can be tethered to the network or bound by affinity, so that it is freed as the gel degrades.
- The scaffold's own life should match the time new tissue needs to take load; too fast leaves a gap in support, too slow can impede remodeling or prolong a foreign-body response.

Regenerating tissues proceed through phases (inflammation, proliferation, remodeling) over days to months, so a single release profile is rarely ideal, and the right target depends on the tissue and the model. Numbers from a bench model are hypotheses for that matching, not evidence that it has been achieved in an animal or a person.

## Common mistakes

- Assuming that mass loss and loss of stiffness follow the same curve.
- Taking a degradation rate measured in buffer as a prediction for an implant.
- Using the whole thickness for L in τ ≈ L²/D when the cargo only has to travel half of it.
- Using the diffusion coefficient in water for cargo inside a gel, whose network slows it, especially when the mesh size approaches the cargo size.
- Expecting release to follow degradation, when untethered cargo that diffuses quickly leaves long before the gel breaks down.
- Treating a bench release profile as evidence that the timing fits tissue repair in an animal or a person.

## Worked example

**Problem.** A synthetic design must keep at least half its mass for 21 days and release a protein (D = 10⁻¹⁰ m²/s) over at least one day. What constraints follow?

**Step 1: degradation.** t½ ≥ 21 days requires k ≤ ln 2 / 21 = 0.033 per day. The gel described above (k = 0.05) degrades too fast and would need slower-hydrolyzing crosslinks.

**Step 2: diffusion.** τ = L²/D ≥ 1 day needs L ≥ √(D × τ) = √(10⁻¹⁰ × 86400) = 2.94 mm of half-thickness.

**Step 3: judge.** A gel nearly 6 mm thick may itself starve embedded cells of oxygen, which is the subject of the transport course. Thickening the gel to slow release therefore conflicts with keeping cells alive, and binding the protein to the network is the more coherent option. The arithmetic does not decide the design; it shows which constraints collide.

## Limits of this lesson

All rate constants and diffusion coefficients are synthetic and illustrative. τ = L²/D gives an order of magnitude; exact release profiles depend on geometry, partitioning, swelling and binding.
