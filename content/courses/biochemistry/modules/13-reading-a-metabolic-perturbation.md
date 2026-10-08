# Reading a metabolic perturbation: ATP, lactate, redox and oxygen consumption

A cell's energy metabolism can be disturbed in several ways that look alike from the outside. A drug that blocks the respiratory chain, a defect in glycolysis and a shortage of oxygen can each lower ATP, and each changes lactate, oxygen use and redox state in its own way. The previous lessons gave the tools to tell them apart: stoichiometry of glycolysis and oxidative phosphorylation, the redox role of lactate, the proton-motive force and the idea that a pool size does not give a flux. This lesson uses them on one question, the one the course case poses: a mitochondrial inhibitor lowers ATP and raises lactate. What carbon and electron flows explain it, and what single measurement would distinguish impaired oxidative phosphorylation from a primary glycolytic defect? All values are synthetic.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute the glucose uptake and lactate output a cell needs to maintain ATP when oxidative phosphorylation is blocked.
2. Interpret changes in the lactate/pyruvate ratio and in tracer labeling as signals of redox state and carbon source.
3. Design a measurement that separates impaired oxidative phosphorylation from a primary glycolytic defect, and state what each result would show.

## Setting the baseline

**Synthetic culture:** the ATP demand is 6.4 mmol/(L·h). In the baseline state 90% of the ATP comes from complete oxidation of glucose (32 ATP per glucose) and 10% from glycolysis ending in lactate (2 ATP per glucose). The glucose uptake needed is

U₀ = 0.9 × 6.4/32 + 0.1 × 6.4/2 = 0.18 + 0.32 = **0.50 mmol/(L·h)**.

The glycolytic fraction releases 0.64 mmol/(L·h) of lactate (two per glucose), and the oxidative part consumes 1.08 mmol/(L·h) of oxygen (six per glucose). Although 90% of the ATP is oxidative, only 36% of the glucose taken up is oxidized, because glycolysis yields so little ATP per glucose; the other 64% becomes lactate. A baseline lactate output above the glucose uptake (1.28 lactate per glucose here) is therefore normal in this synthetic culture and is not by itself a sign of a mitochondrial problem.

## What an inhibitor of the respiratory chain does

An inhibitor of electron transport stops electrons from leaving NADH at the chain. Four consequences follow, in order.

1. **Oxygen consumption falls**, close to zero for the mitochondrial component, because oxygen is the final acceptor for the chain.
2. **NADH is no longer reoxidized in the mitochondria** and the NADH/NAD⁺ ratio rises. NAD⁺ is needed by glycolysis (at the glyceraldehyde-3-phosphate dehydrogenase step), so glycolysis would stall unless NAD⁺ is regenerated elsewhere.
3. **Lactate dehydrogenase takes up the load**: pyruvate is reduced to lactate and NAD⁺ is regenerated. Lactate rises because it is the outlet for NADH's electrons.
4. **ATP falls, then glycolysis accelerates** to compensate. The fall in ATP raises AMP, which activates phosphofructokinase (see the glycolysis lesson).

If glycolysis must supply the whole demand, the glucose uptake becomes U₁ = 6.4/2 = **3.2 mmol/(L·h)**, a 6.4-fold increase, and the lactate output rises to 6.4 mmol/(L·h), 10 times the baseline. The lactate released per glucose rises from 1.28 to 2.0. Whether the cell can in fact raise glucose uptake that far depends on transporter capacity; if it cannot, ATP stays low.

## Signals of redox state and carbon flow

**The lactate/pyruvate ratio.** Lactate dehydrogenase is close to equilibrium, so at a fixed pH the ratio of lactate to pyruvate tracks the cytosolic NADH/NAD⁺ ratio. In the synthetic culture, lactate is 1.0 mM and pyruvate 0.10 mM at baseline (ratio 10). After the inhibitor, lactate is 4.0 mM and pyruvate unchanged (ratio 40), a 4-fold rise in NADH/NAD⁺. A rise in the ratio therefore signals a more reduced cytosol.

**Isotope tracing.** If the medium contains 50% glucose labeled on all six carbons, each labeled glucose gives two lactate molecules with three labeled carbons (M+3), and each unlabeled glucose gives unlabeled lactate. The M+3 fraction of lactate then equals the medium's labeled fraction (50%) times the fraction of lactate that came from medium glucose. A measured M+3 fraction of 0.35 at baseline means 0.35/0.5 = 70% of lactate came from medium glucose, and 0.48 after the inhibitor means 96%. The tracer shows where carbon goes, not how fast it flows.

## Two explanations for low ATP and different lactate

| Observation | Respiratory chain inhibited | Primary glycolytic defect |
|---|---|---|
| Oxygen consumption | falls sharply | stays near normal or falls only a little, if other fuels supply the mitochondria |
| Lactate | rises | falls |
| Lactate/pyruvate ratio | rises | stays the same or falls |
| Glucose uptake | rises (a compensation) | falls or limited by the defect |
| Effect of an extra electron acceptor | partly relieves the redox block | little effect |

The case states that lactate rises, which already favors the first explanation. A decisive measurement is the **oxygen consumption rate**, because a respiratory-chain inhibitor must reduce it, and a defect upstream of the mitochondria need not. Other discriminating tests are the lactate/pyruvate ratio, a glucose tracer, and a **rescue**: supplying an electron acceptor that lets NADH be reoxidized outside the chain (for example pyruvate in the medium) partly restores the redox balance if the chain is the problem, whereas it would be expected to do little for a glycolytic defect. Use at least two independent measurements, because each is indirect: lactate can also rise from hypoxia, from a fuel switch or from changes in lactate export.

## Common mistakes

- Assuming that low ATP with high lactate proves the respiratory chain is the primary defect, without measuring oxygen consumption.
- Reading a rise in lactate as faster glycolysis alone, when part of it can be a redox outlet.
- Counting lactate as a waste product with no role as an NADH outlet.
- Forgetting that glycolysis needs NAD⁺, so a respiratory-chain block threatens glycolysis too.
- Treating a tracer fraction as a rate.
- Using one measurement to separate two hypotheses that predict the same value for it.

## Worked example

**Problem.** A second synthetic culture has an ATP demand of 10 mmol/(L·h), with 80% supplied by complete oxidation of glucose and the rest by glycolysis to lactate. A complete block of oxidative phosphorylation forces all ATP to come from glycolysis. By how much must glucose uptake rise?

**Step 1: baseline uptake.** U₀ = 0.8 × 10/32 + 0.2 × 10/2 = 0.250 + 1.000 = 1.250 mmol/(L·h).

**Step 2: uptake after the block.** U₁ = 10/2 = 5.0 mmol/(L·h).

**Step 3: fold change.** 5.0/1.250 = 4.0-fold. A culture that depends less on glycolysis at baseline needs a larger rise.

**Step 4: check.** Whether the culture can reach 5.0 mmol/(L·h) depends on glucose transport; a smaller increase would leave ATP below demand.

## Limits of this lesson

All values are synthetic and idealized: complete inhibition, fixed ATP yields, no other fuels, and equilibrium of lactate dehydrogenase. Real cells use glutamine and fatty acids, differ in transporter capacity, and show partial inhibition. The lesson explains how to reason from measurements to a mechanism and gives no laboratory protocol.
