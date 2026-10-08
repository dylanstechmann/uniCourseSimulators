# Continuous and perfused culture: chemostat steady states, washout and cell-specific perfusion

A batch culture ends when its nutrients run out. A continuous culture avoids that by feeding fresh medium and removing culture at the same rate, so that a steady state is reached in which growth exactly replaces what is removed. The two design questions are how fast a culture can be fed before the cells wash out of the vessel, and what feed rate gives the most output. The same arithmetic applies, with a twist, to the perfusion cultures that retain the cells and remove only spent medium, which is the setting of the package's case. This lesson derives the steady states of a chemostat from Monod kinetics, finds the washout rate and the rate of maximum productivity, and then states the corresponding rule for perfusion. All values are synthetic.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute the steady-state nutrient and cell concentrations of a chemostat and the washout dilution rate.
2. Find the dilution rate that maximizes cell output and compare operating points.
3. Compute cell-specific perfusion rates and evaluate what they require of a perfused culture.

## The chemostat

Fresh medium with nutrient concentration S₀ enters a well-mixed vessel at a flow F, and culture leaves at the same flow. The **dilution rate** is D = F/V per hour, and its inverse 1/D is the mean residence time. Cells are removed at rate D X and made at rate μ X, so at steady state μ = D. With Monod growth, μ = μ_max S/(K_s + S) = D gives the nutrient concentration

**S_ss = D K_s / (μ_max − D),**

and, with a constant yield, the cell concentration **X_ss = Y (S₀ − S_ss)**. **Synthetic values:** μ_max = 0.04 per hour, K_s = 0.5 mM, S₀ = 20 mM and Y = 1.5 × 10⁵ cells/mL per mM. At D = 0.02 per hour (a residence time of 50 h), S_ss = 0.02 × 0.5/(0.04 − 0.02) = **0.50 mM** and X_ss = 1.5 × 10⁵ × (20 − 0.50) = **2.925 × 10⁶ cells/mL**. At D = 0.03 per hour the nutrient left over rises to 1.50 mM and the cell density falls to 2.775 × 10⁶ cells/mL.

## Washout

The steady state exists only while D is smaller than the largest growth rate the feed can support. Setting S = S₀ in Monod gives the critical dilution rate

**D_crit = μ_max S₀ / (K_s + S₀) = 0.04 × 20/(0.5 + 20) = 0.0390 per hour.**

Above it, cells are removed faster than they can grow, even at the highest nutrient concentration the feed provides, and the culture **washes out**. D_crit is slightly below μ_max because the feed concentration is finite. A chemostat is therefore always operated below D_crit, with a margin, since a disturbance that lowers μ for a while can push the culture past it.

## Output and the best dilution rate

Cell output per volume per hour is D X_ss. Raising D increases the factor D but lowers X_ss, so the output has a maximum:

**D_opt = μ_max (1 − √(K_s/(K_s + S₀))) = 0.04 × (1 − √(0.5/20.5)) = 0.0338 per hour.**

Output is 5.85 × 10⁴ cells/(mL·h) at D = 0.02, 8.32 × 10⁴ at D = 0.03 and 8.76 × 10⁴ at D_opt, where X_ss = 2.595 × 10⁶ cells/mL and S_ss = 2.70 mM. Operating at the optimum is rarely wise in practice, because the culture is closer to washout, and what is wanted is often a product made per cell, not the cells themselves.

## Perfusion with cell retention

In a perfusion culture a membrane, filter or settling device returns the cells to the vessel while spent medium leaves, so cells do not wash out and densities far above a chemostat's can be maintained. The rule that replaces the washout limit is a **cell-specific perfusion rate** (CSPR): the volume of medium fed per cell per day. At a perfusion of 0.04 vessel volumes per hour and 5.0 × 10⁶ cells/mL, CSPR = 0.04 × 24/5.0 × 10⁶ mL per cell per day = **192 pL/(cell·day)**. The minimum CSPR is set by consumption: with a glucose uptake of 2.0 × 10⁻¹⁰ mmol/(cell·h) and a feed of 25 mM from which 20 mM may be consumed (leaving 5 mM), the cell needs at least 2.0 × 10⁻¹⁰/(20 × 10⁻³) × 24 mL per cell per day = **240 pL/(cell·day)**. A perfusion rate below that starves the culture of glucose; one far above it wastes medium. Retention devices can fail (a filter fouls, cells leak or die in the loop), so retention is never perfect, and a retention efficiency below one means some washout.

## Common mistakes

- Setting D above D_crit and expecting a steady state.
- Using μ_max instead of D_crit as the washout limit.
- Reading X_ss as increasing with D, when it falls.
- Optimizing the cell output D X_ss without a margin from washout.
- Confusing the dilution rate (per hour) with a flow in mL per hour.
- Assuming that a perfusion device retains every cell.

## Worked example

**Problem.** A synthetic chemostat has μ_max = 0.05 per hour, K_s = 1.0 mM, S₀ = 10 mM and Y = 1.0 × 10⁵ cells/mL per mM. Find D_crit and, at D = 0.03 per hour, S_ss, X_ss, the output and the residence time.

**Step 1: washout.** D_crit = 0.05 × 10/(1.0 + 10) = 0.0455 per hour, so D = 0.03 is below it.

**Step 2: nutrient.** S_ss = 0.03 × 1.0/(0.05 − 0.03) = 1.50 mM.

**Step 3: cells and output.** X_ss = 1.0 × 10⁵ × (10 − 1.50) = 0.850 × 10⁶ cells/mL, and D X_ss = 2.55 × 10⁴ cells/(mL·h).

**Step 4: residence time.** 1/D = 33.3 h.

## Limits of this lesson

All numbers are synthetic. The chemostat model assumes perfect mixing, one limiting nutrient, constant yield and no cell death or maintenance. Real continuous cultures of animal cells have by-product inhibition and slow transients, and a perfused culture's steady state depends on the retention device. Nothing here is a protocol or a statement about any real cell line.
