# Mitochondrial bioenergetics: the proton-motive force, ATP yield and the cost of leak

Almost all the ATP that a resting person makes comes from one process: electrons from NADH and FADH₂ flow to oxygen along the respiratory chain, protons are pumped out of the mitochondrial matrix, and ATP synthase lets them return and builds ATP. The coupling is chemiosmotic. The energy of electron flow is stored first as a gradient of protons across the inner membrane, and the gradient then pays for ATP synthesis. This lesson computes the size of that gradient, the number of protons each ATP needs, the ATP yield of a glucose molecule and what a leak of protons costs. It prepares the question of what happens to ATP and lactate when the respiratory chain is blocked. All values are typical and round.

## Learning objectives

By the end of this lesson, you should be able to:

1. Calculate the proton-motive force from its electrical and pH components and the free energy per mole of protons.
2. Estimate the minimum and actual protons per ATP and the ATP yield per NADH, FADH₂ and glucose.
3. Predict how proton leak or an uncoupler changes ATP made per oxygen and the whole-body ATP turnover implied by oxygen uptake.

## The proton-motive force

The inner membrane's electrical potential and its pH difference both store energy. The **proton-motive force** (Δp), expressed in volts or millivolts, is

**Δp = Δψ + (2.303 RT/F) ΔpH,**

with Δψ the electrical potential (matrix negative, taken as positive here), ΔpH the matrix pH minus the intermembrane-space pH and 2.303 RT/F = 61.5 mV per pH unit at 37 °C. **Synthetic values:** Δψ = 150 mV and ΔpH = 0.75. Then Δp = 150 + 61.5 × 0.75 = 196 mV. The electrical part supplies about three quarters of it.

Each mole of protons returning down this gradient releases F × Δp = 96.485 × 0.196 = **18.9 kJ per mole of protons**.

## How many protons does an ATP cost?

Making ATP in the cell requires a free-energy input of about 51.4 kJ/mol (the actual ΔG of the free-energy lesson, not the standard value). If every proton delivered 18.9 kJ/mol with perfect efficiency, the minimum would be 51.4/18.9 = **2.72 protons per ATP**. The measured stoichiometry is higher: the rotating ring of ATP synthase needs a whole number of protons per turn, and moving ADP and phosphate into the matrix costs about one more. A commonly used value is about 4 protons per ATP, giving an efficiency of 51.4/(4 × 18.9) = 68%. The rest is dissipated as heat. Papers differ in the exact stoichiometry, so ATP yields are best reported with the assumption used.

## From electrons to ATP

Electrons from NADH enter at the first complex and pass three proton-pumping steps, moving about 10 protons per NADH. Electrons from FADH₂ enter later and move about 6. At 4 protons per ATP:

- NADH yields 10/4 = 2.5 ATP;
- FADH₂ yields 6/4 = 1.5 ATP.

Complete oxidation of one glucose gives 4 ATP by substrate-level phosphorylation (2 in glycolysis, 2 in the citric acid cycle), 10 NADH and 2 FADH₂. The total is 4 + 10 × 2.5 + 2 × 1.5 = **32 ATP per glucose**. Shuttles that move cytosolic NADH electrons into the matrix can deliver them at the lower-yield entry point and reduce the total to about 30, so values from 30 to 32 appear in the literature depending on shuttles, stoichiometry and accounting. Six molecules of O₂ are reduced per glucose, so the yield is 32/6 = 5.3 ATP per O₂, a P/O ratio of 2.67 per oxygen atom.

## Leak, uncoupling and respiratory control

Protons also return through the membrane without making ATP (**leak**), and chemical uncouplers carry protons across directly. If a fraction of the gradient is dissipated this way, the oxidative ATP falls in proportion while electron flow and oxygen use are unchanged or rise. With 25% of the proton flux leaking, the oxidative ATP is 28 × (1 − 0.25) = 21 and the total is 25 ATP per glucose. Respiration is also limited by ADP availability: when ATP demand is low the gradient builds up and slows electron flow (respiratory control), and when demand rises, ADP stimulates ATP synthase and oxygen use rises. Oxygen consumption measured in cells and isolated mitochondria with and without an ATP-synthase inhibitor or an uncoupler therefore separates ATP-linked respiration from leak and shows the maximal capacity.

## What oxygen uptake implies for ATP turnover

Oxygen consumption can be converted to an ATP production rate if the yield per oxygen is known. At rest, V̇O₂ = 0.25 L/min at standard conditions is 0.25/22.4 × 1000 = 11.2 mmol O₂/min. With 5.3 ATP per O₂ the estimate is 11.2 × 5.3 = 60 mmol ATP/min, or about 86 mol per day. At 507 g/mol that is about 43 kg of ATP per day, far more than the body contains at one time (on the order of tens of grams; estimates vary). The same small pool is therefore remade every minute or two. The calculation assumes glucose as the only fuel and full coupling; fat and protein oxidation and leak change the yield per oxygen.

## Common mistakes

- Treating the standard ATP hydrolysis energy as the cell's cost of making ATP.
- Adding the electrical and pH terms in different units, or using the wrong sign for ΔpH.
- Quoting one ATP-per-glucose number without the stoichiometry and shuttle assumptions behind it.
- Assuming that more oxygen consumption always means more ATP: leak and uncouplers raise oxygen use while lowering ATP per oxygen.
- Forgetting that ATP made from glycolysis and from the citric acid cycle by substrate-level phosphorylation does not depend on the gradient.
- Reading an ATP turnover of tens of kilograms per day as a mass of ATP in the body.

## Worked example

**Problem.** A synthetic uncoupler causes 40% of the proton flux to leak. Assuming the same electron flow, how many ATP per glucose and per O₂ result?

**Step 1: oxidative ATP.** 28 × (1 − 0.4) = 16.8 ATP from the gradient.

**Step 2: total.** 4 + 16.8 = 20.8 ATP per glucose.

**Step 3: per oxygen.** 20.8/6 = 3.5 ATP per O₂, against 5.3 without the uncoupler.

**Step 4: reading the result.** The cell uses the same oxygen but makes about 35% less ATP from each glucose. To meet an unchanged ATP demand it would have to burn more glucose and oxygen, with the lost energy released as heat.

## Limits of this lesson

All values are typical and rounded. Protons per ATP, protons pumped per electron pair and the ATP-per-glucose range vary between sources and cell types. Δψ and ΔpH are not measured simply in living cells, and the whole-body estimate ignores fuel mixture and leak. The lesson explains reasoning about bioenergetics and gives no laboratory protocol.
