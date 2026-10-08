# Tissue repair: the phases of wound healing, scar versus regeneration and the kinetics of closure

When tissue is injured, the body does not simply refill the gap. It stops bleeding, clears debris and microbes, covers the surface, rebuilds support and reorganizes what it has made, in overlapping phases whose timing and cell types are well described. Adult mammals often finish with a scar that restores the barrier but not the original structure, while some animals and some tissues regenerate. For engineers working on tissue repair, healing is both a physiological process to understand and a measurable one: closure of a cell layer can be timed, and the results depend on a few quantities that can be estimated. This lesson summarizes the phases, contrasts repair with regeneration and shows how closure kinetics are quantified with synthetic numbers.

## Learning objectives

By the end of this lesson, you should be able to:

1. Order the phases of skin wound healing, name their main cell types and compare their time scales.
2. Compute closure time, percent closed and migration speed from a front-migration model, and a half-time from an exponential model.
3. Evaluate what a closure assay in culture can and cannot show about healing in a tissue.

## Phases of healing

In skin, the textbook sequence has four overlapping phases.

- **Hemostasis (minutes).** Platelets and a fibrin clot stop bleeding and form a temporary matrix that also releases signals.
- **Inflammation (hours to days).** Neutrophils and then macrophages clear microbes and debris. Macrophages shift over time from clearing to supporting repair; an inflammation that does not resolve delays everything that follows.
- **Proliferation (days to weeks).** Keratinocytes at the wound edge migrate and divide to cover the surface (re-epithelialization). Fibroblasts deposit new matrix, and endothelial cells form new vessels, giving a red, vascular granulation tissue. Some fibroblasts become contractile myofibroblasts that pull the wound edges together.
- **Remodeling (weeks to months or longer).** Collagen is reorganized and cross-linked, vessels regress and the scar matures, gaining strength but usually remaining different from the original tissue in organization and function.

The phases overlap, so a delay in one shows up in the next, and many studies of "slow healing" are really studies of an unresolved phase.

## What limits healing

Cells at the repair front need oxygen and nutrients delivered by blood, which is why the oxygen-limits lesson in the transport course matters for repair: a wound with poor perfusion is a thick, poorly supplied construct. Infection, ongoing mechanical stress, nutrition and some chronic diseases are associated with slower or incomplete healing, and healing is on average slower in older adults. This lesson makes no statement about any person's wound.

## Repair versus regeneration

**Regeneration** restores the original tissue structure and function. **Repair** restores continuity, often with a scar of disorganized collagen. Adult skin repairs by scarring, whereas other systems regenerate, such as the liver after partial loss and the neonatal mouse heart in a brief window (see the regeneration lesson in the geroscience course). Showing regeneration needs structure, function, lineage origin and controls, not only an increase in dividing cells.

## Closure as a front moving at a speed

To quantify re-epithelialization, a simplified model treats a straight wound of width W whose two edges each advance toward the other at speed v. The gap closes at 2v, so

**time to close t_c = W / (2v),** and the **fraction closed at time t** is 2vt/W until closure.

**Synthetic values:** W = 500 μm and v = 25 μm/h per edge. Then t_c = 500/(2 × 25) = 10 h, and after 6 h the fraction closed is 2 × 25 × 6/500 = 0.60, or 60%. If a treatment slows the edge speed by 40% to 15 μm/h, closure takes 500/(2 × 15) = 16.7 h.

For a straight scratch, the open area is proportional to the remaining width, so percent open area declines linearly with time at a constant rate. Conversely, if the closure rate is proportional to the area that remains, as in some round wounds, the area decays exponentially, A(t) = A₀ e^(−kt), with **half-time t½ = ln 2 / k**. With k = 0.1 per hour, t½ = 6.9 h. Which description fits is an empirical question that data across several time points can answer; two points cannot.

## From images to numbers

In a typical scratch assay a confluent cell layer is scraped to leave a cell-free gap, and the gap area is measured by imaging at several time points and expressed as a percent of the starting area. Good practice includes:

- the **same fields** imaged at each time, with the gap defined by a stated rule;
- a **control** for proliferation, because dividing cells also fill the gap: either a short assay, or an agent that blocks division in a separate group, so migration and proliferation can be separated;
- **independent replicates**, meaning separate wells from separate experiments (different days or plates), not several images of one well;
- the **rate** reported as percentage points of area per hour from a fit, not from two time points;
- an honest account of what was left out: the layer is flat, has no immune cells or blood supply and no mechanical tension.

## What culture closure shows

A faster or slower closure in a dish shows an effect on the combined migration and proliferation of that cell type under those conditions. It does not by itself show an effect on healing in tissue, where inflammation, vessels, matrix and mechanics all take part. Culture assays are well suited to screening and mechanism, and weak as predictors of outcome.

## Common mistakes

- Reporting the speed of the whole gap as the speed of one edge, which are different by a factor of 2.
- Treating the fraction closed as linear in time after the gap has closed.
- Computing a rate from only the start and end images.
- Counting several fields of one well as independent replicates.
- Ignoring proliferation when claiming that a treatment changes migration.
- Concluding from faster closure in a dish that healing in a person would be faster.

## Worked example

**Problem.** In a synthetic scratch of width 300 μm, 75% of the gap has closed after 12 h. Assuming constant edge speed, find the speed per edge and when closure would be complete.

**Step 1: closed width.** 75% of 300 μm = 225 μm, shared by two edges: 112.5 μm each.

**Step 2: speed.** v = 112.5 μm/12 h = 9.38 μm/h per edge.

**Step 3: closure time.** t_c = 300/(2 × 9.38) = 16 h, consistent with 75% at 12 h because 12/16 = 0.75.

**Step 4: check.** A straight-line extrapolation holds only if the speed stays constant and no proliferation or edge effects change it. Further time points would test it.

## Limits of this lesson

All values are synthetic. The front-migration model assumes straight edges, constant speed and equal advance on both sides; real fronts speed up and slow down, and cells at the edge behave differently from cells behind it. The phases are described at textbook level; real wounds vary by tissue, size, depth, age and health. The lesson gives no clinical advice and makes no claim about any person.
