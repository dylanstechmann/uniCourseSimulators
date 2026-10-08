# Functional groups at work in biomolecules: acyl reactivity, ionization and slow chemical damage

Organic chemistry is the chemistry of the body's molecules. The same functional-group rules that predict reactions in a flask explain why cells store energy in thioesters, build proteins from stable amides, keep certain amino acid side chains charged, and slowly accumulate chemical damage on proteins that are not replaced. This lesson connects acyl-transfer reactivity, side-chain ionization and nonenzymatic modification, and ends with a simple kinetic model of why long-lived proteins collect modifications.

## Learning objectives

By the end of this lesson, you should be able to:

1. Rank acyl derivatives by reactivity toward nucleophilic acyl substitution and relate the ranking to their biological roles.
2. Calculate the protonated fraction of an ionizable side chain at a given pH and predict its charge and nucleophilicity.
3. Model the steady-state level of a nonenzymatic modification as a balance of modification and turnover, and explain why long-lived proteins accumulate damage.

## Acyl derivatives: reactivity follows leaving-group ability and resonance

Carboxylic acid derivatives react with nucleophiles by addition to the carbonyl followed by loss of a leaving group. Reactivity falls in the order

**acyl phosphate ≈ acid anhydride > thioester > ester > amide > carboxylate.**

Two factors set the order. A better leaving group (a weaker base) departs more easily. And the more the substituent donates electrons into the carbonyl by resonance, the less electrophilic the carbon. Nitrogen donates strongly, so amides are stabilized; sulfur's larger 3p orbitals overlap poorly with carbon's 2p, so thioesters are less stabilized and more reactive than oxygen esters.

Biology uses this ladder. Acetyl-CoA and other thioesters are activated acyl carriers: reactive enough to transfer their acyl group in enzyme-catalyzed reactions, stable enough to persist in water. Peptide bonds are amides: thermodynamically favorable to hydrolyze but so slow without a catalyst that proteins last; proteases provide the catalysis. Esters, as in lipids, sit between.

## Ionization of side chains

Whether a side chain is charged at a given pH follows from its pKa. For a basic group, the protonated (charged) fraction is

**f(BH⁺) = 1 / (1 + 10^(pH − pKa)).**

At pH 7.4, a lysine side chain (typical pKa about 10.5) is 99.92% protonated, and a histidine imidazole (typical pKa about 6.0) is only 3.8% protonated. These are typical solution values; inside a protein, neighboring charges and burial can shift a pKa by several units. Charge controls reactivity: only the unprotonated amine has a lone pair to act as a nucleophile, which is why the small unprotonated fraction of lysine amino groups is the form that reacts with electrophiles such as sugars. Histidine's pKa near neutral pH lets it act as both acid and base in enzyme active sites.

## Nonenzymatic modification: glycation as an example

Reducing sugars such as glucose exist mostly as cyclic hemiacetals, with a small fraction in the open-chain form that carries a free aldehyde. That aldehyde reacts with an unprotonated amine to form an imine (a Schiff base), which can rearrange to a more stable ketoamine (the Amadori product). Over long times further oxidation and rearrangement give a heterogeneous set of advanced glycation end products, some of which crosslink proteins. These are ordinary organic reactions: carbonyl addition by an amine, loss of water, tautomerization. They happen without enzymes, slowly, wherever sugars and amines meet. Oxidation of side chains and deamidation of asparagine are other examples of slow, uncatalyzed protein chemistry.

## Why long-lived proteins accumulate modifications

Treat modification of a site as first order with rate constant k_m and replacement of the protein (removing modified copies and supplying new unmodified ones) as first order with rate constant k_d. At steady state the modified fraction is

**f_ss = k_m / (k_m + k_d).**

With a synthetic k_m = 0.01 per year:

- a protein with a half-life of 2 days (k_d = 126 per year) reaches f_ss = 7.9×10⁻⁵, essentially unmodified;
- a protein with a half-life of 10 years (k_d = 0.0693 per year) reaches f_ss = 0.126, about 13%.

The model makes a general point without any claim about specific tissues: when replacement is slow, even a slow chemical reaction can modify a substantial fraction of a protein pool. Proteins such as some extracellular matrix components and lens proteins turn over slowly, and are among the molecules in which accumulated modifications are studied in aging research. The model also says the approach to steady state is slow for such proteins: its half-time is ln 2 / (k_m + k_d) = 8.7 years here.

## Common mistakes

- Ranking acyl derivatives by the strength of the carbonyl instead of by leaving-group ability and resonance donation.
- Treating a typical pKa as fixed, when burial and neighboring charges inside a protein can shift it by several units.
- Computing the protonated fraction when the unprotonated fraction, the nucleophile, is what matters, or the reverse.
- Concluding that a group that is 99.9% protonated cannot react, when its small unprotonated fraction is the reactive form.
- Dismissing slow chemistry, when with slow replacement f_ss = k_m/(k_m + k_d) can be large.
- Reading the steady-state model as a statement about particular tissues.

## Worked example

**Problem.** Using the same k_m = 0.01 per year, how much would doubling the replacement rate of the 10-year protein lower the steady-state modified fraction?

**Step 1.** Doubling k_d gives 0.1386 per year.

**Step 2.** f_ss = 0.01 / (0.01 + 0.1386) = 0.067, down from 0.126.

**Step 3.** Interpretation: in this model, the modified fraction is controlled by the ratio of the two rates; faster renewal or slower chemistry both lower it. The model is a teaching abstraction. Real modifications have several steps, some are repaired, and modified proteins may be removed faster or slower than unmodified ones.

## Limits of this lesson

Rate constants and half-lives are synthetic; pKa values are typical textbook values. The lesson makes no claim about the rate of any modification in a person or about any intervention.
