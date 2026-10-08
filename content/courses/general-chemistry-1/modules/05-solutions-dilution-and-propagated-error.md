# Making solutions you can trust: mass, molarity, dilution and propagated error

Almost every wet-lab result rests on solutions someone made by weighing and diluting. A concentration error there passes silently into every downstream number, from enzyme rates to cell responses. This lesson treats solution preparation as a calculation with units and uncertainty: converting between mass and moles, diluting stocks with C₁V₁ = C₂V₂, planning serial dilutions, and estimating how small errors in each step combine.

## Learning objectives

By the end of this lesson, you should be able to:

1. Calculate the mass of solute needed for a target molar concentration and convert between mass and molar concentration units.
2. Plan single and serial dilutions with C₁V₁ = C₂V₂ and compute the resulting concentrations.
3. Check a preparation's dimensions, purity correction and propagated uncertainty, and identify the step that dominates the error.

## From moles to grams

Molarity is moles of solute per liter of solution: c = n / V. The mass needed is

**m = c × V × M,**

with M the molar mass. To make 500 mL of 150 mM sodium chloride (M = 58.44 g/mol): m = 0.15 mol/L × 0.5 L × 58.44 g/mol = 4.383 g. Writing the units at each step shows immediately whether the answer is a mass: (mol/L)(L)(g/mol) = g.

Two corrections are common. If the reagent is 98% pure by mass, weigh m / purity = 4.472 g. If the reagent is a hydrate, use the molar mass of the hydrate, not of the anhydrous salt, since the water is part of what you weigh.

## Mass concentration and molarity

Many biological reagents are specified in mg/mL. To convert to molar units divide by molar mass: 4.5 mg/mL of glucose (M = 180.16 g/mol) is 4.5 g/L ÷ 180.16 g/mol = 25.0 mM. The reverse conversion multiplies by M. For proteins the molar mass is large, so a modest mg/mL concentration is a small molar concentration, which matters when comparing with binding constants given in molar units.

## Dilution

Diluting conserves the moles of solute, so **C₁V₁ = C₂V₂**. To make 200 mL of 150 mM from a 5 M stock: V₁ = 0.15 × 0.2 / 5.0 = 6.0 mL of stock, made up to 200 mL total. "Made up to" matters: the solvent added is the total volume minus the stock volume, not the total volume itself.

## Serial dilution

When the final concentration is far below the stock, one-step dilution would require a volume too small to pipette accurately. A serial dilution repeats a fixed dilution factor. Four successive 1:10 dilutions from 2.0 mM give 2.0 / 10⁴ mM = 0.20 μM. Each step multiplies the dilution factor; the total factor is 10,000.

Serial dilutions also multiply errors. If each step has a relative error of 2%, independent errors add in quadrature, so four steps give about √4 × 2% = 4%. A systematic error, such as a pipette that always delivers 2% too much, compounds instead: (1.02)⁴ − 1 ≈ 8.2%.

## Propagating uncertainty

For a product or quotient of independently measured quantities, relative uncertainties add in quadrature:

**(δc/c)² ≈ (δm/m)² + (δV/V)² + (δM/M)².**

Weighing 0.010 g on a balance read to ±0.001 g is a 10% uncertainty, while weighing 1.000 g on the same balance is 0.1%. That is why it is often better to make a concentrated stock from a larger mass and dilute it than to weigh a tiny mass directly. Identify the largest relative error in the chain; improving any other step changes little.

## Common mistakes

- Using millimolar as if it were molar, which produces masses a thousand times too large. Writing the unit at every step catches this.
- Adding the full target volume of solvent to the stock instead of making the solution up to that volume, which dilutes it slightly more than intended.
- Weighing an anhydrous molar mass for a hydrated reagent, which gives a solution that is too dilute by the mass fraction of water.
- Reusing one diluted intermediate for many days without checking stability, so that degradation adds an error the calculation does not show.

## Worked example

**Problem.** You need 50 mL of 2.0 mM of a compound with M = 250.0 g/mol, and your balance reads to ±0.001 g. Should you weigh it directly?

**Step 1: mass needed.** 0.0020 mol/L × 0.050 L × 250.0 g/mol = 0.025 g.

**Step 2: weighing error.** ±0.001 g on 0.025 g is a 4% relative error before any other step.

**Step 3: alternative.** Make 50 mL of a 100 mM stock (1.250 g, a 0.08% weighing error) and dilute 1.0 mL of it to 50 mL. If the pipette is good to 1% and the flask to 0.2%, the combined error is about √(0.08² + 1² + 0.2²) ≈ 1.0%, four times better than direct weighing. The calculation shows where the error lives.

## Limits of this lesson

All numbers are synthetic teaching values. The lesson ignores temperature effects on volume, nonideal solutions and activity, and the specific tolerances of any instrument; it is not a laboratory procedure.
