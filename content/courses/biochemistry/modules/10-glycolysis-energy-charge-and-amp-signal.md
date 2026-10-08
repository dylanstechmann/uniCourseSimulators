# Glycolysis and its control: stoichiometry, energy charge and why AMP is a sensitive signal

Glycolysis is the oldest and most universal energy-yielding pathway, and it is a good place to learn how a metabolic pathway is both a chemical bookkeeping problem and a control problem. It converts one glucose into two pyruvate, makes a small net amount of ATP and reduces NAD⁺ to NADH; what happens next to the pyruvate and the NADH decides whether the cell makes lactate or sends carbon and electrons to the mitochondria. The pathway is also tightly controlled by the energy state of the cell, and the arithmetic of how a small drop in ATP becomes a large rise in a signaling molecule explains how AMP-sensing kinases such as AMPK, which the geroscience lesson on nutrient sensing introduces, can respond to modest changes. All concentrations are synthetic.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute AMP from the adenylate kinase equilibrium and the adenylate energy charge, and show how a small fall in ATP amplifies AMP.
2. Balance carbon, ATP and NADH through glycolysis and lactate fermentation and compute the glucose uptake needed to meet an ATP demand.
3. Explain allosteric control of phosphofructokinase and distinguish a change in a metabolite pool from a change in flux.

## Stoichiometry: what glycolysis makes

The net reaction of glycolysis is

**glucose + 2 NAD⁺ + 2 ADP + 2 Pᵢ → 2 pyruvate + 2 NADH + 2 ATP + 2 H⁺ + 2 H₂O.**

Two ATP are spent in the early steps and four are made in the later steps, so the net is two. The six carbons of glucose appear as two three-carbon pyruvates, and two NAD⁺ are reduced. Because the cell holds only a small amount of NAD⁺, the NADH must be reoxidized for glycolysis to continue. With oxygen and working mitochondria, electrons from NADH are passed to the respiratory chain through shuttles. Without them, lactate dehydrogenase reduces pyruvate to lactate and regenerates NAD⁺:

**pyruvate + NADH + H⁺ → lactate + NAD⁺.**

In lactate fermentation the NADH made by glycolysis is exactly consumed, so per glucose the cell nets 2 ATP and 2 lactate, with no net NADH. The yield of ATP is small, so supplying a given demand from glycolysis alone requires a high glucose flux: an ATP demand of 6.0 mmol/(L·h) met entirely by glycolysis needs 6.0/2 = 3.0 mmol/(L·h) of glucose and releases 6.0 mmol/(L·h) of lactate. Lactate, in this view, is a redox outlet: the way a cell reoxidizes NADH when oxygen-dependent routes cannot.

## Adenylates, energy charge and amplification

ATP, ADP and AMP are interconverted by adenylate kinase, **2 ADP ⇌ ATP + AMP**, which is close to equilibrium with K ≈ 1, so [AMP] ≈ K [ADP]²/[ATP]. The **adenylate energy charge** summarizes the pool:

**EC = ([ATP] + ½[ADP]) / ([ATP] + [ADP] + [AMP]).**

**Synthetic resting cell (mM):** ATP 3.0, ADP 0.3. Then AMP = 1 × 0.3² / 3.0 = 0.03, total adenylate = 3.33, and EC = (3.0 + 0.15)/3.33 = 0.946. The ATP/ADP ratio is 10.

Now let ATP fall by 10% to 2.7 mM with the same total adenylate. Solving ATP + ADP + ADP²/ATP = 3.33 gives ADP = 0.527 and AMP = 0.103 mM. A 10% fall in ATP therefore raises ADP 1.76-fold and AMP **3.4-fold**, while the energy charge falls only from 0.946 to 0.890. Because AMP depends on the square of ADP, a small relative change in the major nucleotide becomes a large relative change in the minor one. That amplification is why AMP is a sensitive reporter of energy state, and why enzymes and kinases that bind AMP can respond to modest energy stress.

## Control of phosphofructokinase

The major control point of glycolysis is phosphofructokinase-1 (PFK-1), which phosphorylates fructose-6-phosphate. Its activity is inhibited by high ATP and citrate (signals of an adequate energy and carbon supply) and enhanced by AMP, ADP and fructose-2,6-bisphosphate. Its kinetics are sigmoidal with respect to fructose-6-phosphate, so an effector that shifts the half-saturating concentration has a steep effect. With a Hill coefficient of 2.5 and fructose-6-phosphate at 1.0 mM, v/V_max = 1/(1 + (K₀.₅/[S])ⁿ) is 0.15 when K₀.₅ = 2.0 mM and 0.85 when an activator lowers K₀.₅ to 0.5 mM, a 5.7-fold rise in rate from a fourfold shift in K₀.₅.

## Flux is not pool size

A rise in the concentration of a metabolite does not by itself say whether production increased or consumption fell. If an enzyme is blocked, upstream metabolites rise and downstream metabolites fall, a pattern called a crossover that localizes a block. Energy stress can accelerate flux through PFK-1 while ATP stays within a few percent of its resting value, because the pool is large and flux is regulated by the small changes in the effectors. Measuring flux requires rates, for example from labeled substrates or from measured glucose uptake and lactate output.

## Common mistakes

- Counting gross ATP (4) instead of net ATP (2) per glucose.
- Forgetting that NADH must be reoxidized for glycolysis to continue.
- Expecting lactate production to be zero when oxygen is present, or to require no NADH.
- Treating the energy charge as a measure of ATP alone.
- Assuming that a rise in a metabolite means faster production.
- Looking for a single rate-limiting enzyme and ignoring that PFK-1 control is shared with other steps.

## Worked example

**Problem.** In a second synthetic cell, ATP is 2.0 mM and ADP 0.5 mM. With K = 1, find AMP and the energy charge, and compare with the resting cell above.

**Step 1: AMP.** AMP = 0.5²/2.0 = 0.125 mM.

**Step 2: total.** 2.0 + 0.5 + 0.125 = 2.625 mM.

**Step 3: energy charge.** EC = (2.0 + 0.25)/2.625 = 0.857.

**Step 4: comparison.** The resting cell had EC 0.946; this one is at 0.857, with AMP 4.2 times higher (0.125 against 0.03 mM) and the ATP/ADP ratio down from 10 to 4.

## Limits of this lesson

All concentrations are synthetic and round. The adenylate kinase equilibrium constant is close to 1 under cellular conditions but varies with magnesium, ionic strength and temperature, free and total nucleotide concentrations differ, and the sigmoidal PFK-1 model is a simplification of its complex allosteric behavior. The lesson explains reasoning about metabolic control and gives no laboratory protocol.
