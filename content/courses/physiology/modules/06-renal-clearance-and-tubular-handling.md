# Renal clearance: measuring filtration, plasma flow and tubular handling

The kidneys filter roughly the whole plasma volume many times a day and then reclaim almost all of it, adjusting what remains to keep the body's water, salt and acid balance. Clearance is the single idea that turns urine and plasma measurements into rates of filtration, secretion and reabsorption. This lesson defines clearance, uses it to measure glomerular filtration rate and renal plasma flow with synthetic data, and shows how comparing a substance's clearance with filtration reveals what the tubules do to it.

## Learning objectives

By the end of this lesson, you should be able to:

1. Calculate clearance from urine concentration, urine flow and plasma concentration, and use suitable markers to estimate GFR and renal plasma flow.
2. Compute filtered load and predict urinary excretion of a reabsorbed solute with a transport maximum.
3. Infer net tubular secretion or reabsorption by comparing a substance's clearance with GFR, and evaluate the limits of creatinine-based estimates.

## Clearance

Clearance is the volume of plasma from which a substance is completely removed per unit time:

**C_x = (U_x × V̇) / P_x,**

with U_x the urine concentration, V̇ the urine flow and P_x the plasma concentration. It is a rate of volume, not of mass, and it is a virtual quantity: no particular milliliter of plasma is fully cleaned.

## Measuring GFR

A substance that is freely filtered, neither reabsorbed nor secreted, not metabolized by the kidney and not toxic has a clearance equal to GFR, because everything filtered is excreted. Inulin, a plant polysaccharide, meets these conditions. **Synthetic infusion data:** U = 30 mg/mL, V̇ = 1.0 mL/min, P = 0.25 mg/mL, so GFR = 30 × 1.0 / 0.25 = 120 mL/min.

## Measuring renal plasma flow

Para-aminohippurate (PAH) at low plasma levels is filtered and also secreted so efficiently that almost none leaves the kidney in renal venous plasma. Its clearance therefore approximates renal plasma flow. With U = 12 mg/mL and P = 0.02 mg/mL, C_PAH = 600 mL/min. The **filtration fraction** is GFR / RPF = 120/600 = 0.20: about a fifth of the plasma entering the glomeruli is filtered.

## Filtered load and a transport maximum

The **filtered load** of a freely filtered solute is GFR × P. Glucose is filtered and then reabsorbed by carriers in the proximal tubule that saturate. In an idealized model with a transport maximum T_m = 375 mg/min:

- at P = 1.0 mg/mL, load = 120 mg/min, below T_m, so all is reabsorbed and none appears in urine;
- at P = 4.0 mg/mL, load = 480 mg/min, so excretion = 480 − 375 = 105 mg/min.

Real kidneys show "splay": glucose appears in urine before the whole-kidney T_m is reached, because nephrons differ in their filtration and reabsorption capacity.

## Reading clearance against GFR

For a freely filtered substance:

- **C_x = GFR** → net filtration only (or reabsorption and secretion balance).
- **C_x < GFR** → net reabsorption.
- **C_x > GFR** → net secretion.

A synthetic drug X with U = 2.4 mg/mL, P = 0.04 mg/mL and V̇ = 1.0 mL/min has C_x = 60 mL/min, below GFR, so it is net reabsorbed. A substance bound to plasma protein is filtered only in its free fraction, so the comparison must use the free plasma concentration.

## Creatinine as a practical marker

Infusing inulin is impractical in routine care, so creatinine, produced continuously by muscle, is used instead. Its clearance slightly overestimates GFR because a small amount is secreted. Equations that estimate GFR from plasma creatinine alone assume a stable state and typical creatinine production for the person's characteristics. Lower muscle mass, which is common in older adults, lowers creatinine production, so a "normal" plasma creatinine can coexist with a reduced GFR. GFR on average declines with age, and this is one reason measured values and alternative markers are used when precision matters.

## Common mistakes

- Treating clearance as a mass rate or as plasma that is physically cleaned, when it is a virtual volume per unit time.
- Using the total plasma concentration for a protein-bound substance, when only the free fraction is filtered.
- Comparing a substance's clearance with GFR when it is not freely filtered or is metabolized by the kidney.
- Assuming a sharp transport maximum, when splay makes glucose appear in urine earlier.
- Reading a normal plasma creatinine as a normal GFR in a person with low muscle mass.
- Applying clearance equations while plasma levels are changing rather than steady.

## Worked example

**Problem.** In a synthetic steady state, muscle produces creatinine at 1.2 mg/min and GFR is 120 mL/min. Treat creatinine as filtered only. What is plasma creatinine, and what happens if GFR halves, with and without a parallel fall in production?

**Step 1: baseline.** At steady state, excretion equals production, and excretion ≈ GFR × P. So P = 1.2 / 120 = 0.010 mg/mL (1.0 mg/dL).

**Step 2: GFR halves.** With production unchanged, P rises until excretion matches production again: P = 1.2 / 60 = 0.020 mg/mL, double the baseline.

**Step 3: production also halves.** If lower muscle mass halves production to 0.6 mg/min, P = 0.6 / 60 = 0.010 mg/mL, the same as at baseline. Half the filtration is invisible in plasma creatinine alone. This is the arithmetic behind the caution in the previous section, and the reason estimating equations include terms for factors that affect production.

## Limits of this lesson

All numbers are synthetic. The idealized T_m model ignores splay, and the lesson does not cover the clinical equations used to estimate GFR or their calibration.
