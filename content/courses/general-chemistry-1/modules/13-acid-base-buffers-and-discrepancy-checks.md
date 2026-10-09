# Acid–base buffers and discrepancy checks

## Learning objectives

1. Calculate idealized pH from activities or a stated concentration approximation.
2. Account for acid neutralization before evaluating a buffer ratio and its validity.
3. Distinguish calibration, composition and nonideal explanations for a discrepancy.

## pH and the reference scale

The [IUPAC pH entry](https://goldbook.iupac.org/terms/view/P04524) defines pH through hydrogen-ion activity rather than an unqualified dimensional concentration. Write pH=−log₁₀a_H. In a stipulated concentration-based teaching approximation, a_H=γ_H[H⁺]/c°, with c°=1 mol/L. At [H⁺]=10⁻⁵ mol/L and γ_H=0.7, the resulting pH is approximately 5.154902, compared with 5.0 when γ is taken as one. The numerical coefficient is synthetic and is not an experimentally determined activity correction.

The logarithm argument must be dimensionless and positive. A pH difference of one corresponds to a factor of ten in hydrogen activity, not a one-unit concentration difference. Real pH reporting also requires measurement conventions and calibration; the formula alone does not establish that an instrument is accurately reporting an unknown sample. This lesson uses a declared ideal scale for its model calculations.

## A weak-acid pair

For HA⇌H⁺+A⁻, the thermodynamic equilibrium relation is K_a=a_Ha_A/a_HA. Rearranging gives pH=pK_a+log₁₀(a_A/a_HA). If the acid/base activity ratio is approximated by their concentration ratio, this becomes the familiar Henderson–Hasselbalch form. The logarithm identity is not the main approximation; substituting nominal post-neutralization inventories for equilibrium concentrations is.

Use a synthetic acid with pK_a=4.8 in the ideal concentration model. The preserved course case begins with 0.050 mol HA and 0.030 mol A⁻ in 0.50 L. Their common volume cancels in the ratio, giving pH≈4.8+log₁₀(0.030/0.050)=4.578151. This does not identify a real acid or supply a preparation recipe. It is a paper accounting model with stipulated values.

## Neutralization before a logarithm

Adding a specified amount q of strong-acid equivalents first converts A⁻ to HA in the stoichiometric approximation: n_A=0.030−q and n_HA=0.050+q. Assume fixed final volume and no material loss for these calculations. At q=0.010 mol, the ratio is 0.020/0.060 and the predicted pH is 4.322879. At q=0.020 mol, it is 0.010/0.070 and the prediction is 3.954902. The pH response becomes more sensitive as the base inventory approaches exhaustion.

At q=0.030 mol, nominal base inventory is zero. Substituting zero into the logarithm does not provide a valid buffer prediction. Weak-acid dissociation creates some A⁻ and H⁺, so the real model concentration is not captured by the zero post-neutralization inventory. Beyond exhaustion, excess strong-acid charge must also be included. A negative formal base amount is a warning that the assumed buffer approximation has left its domain.

For the exhausted ideal model, total acid concentration is 0.080/0.50=0.16 mol/L. Define the concentration-form parameter K_a,c=c°10^(−4.8), numerically 1.584893 × 10⁻⁵ mol/L. Neglecting water contribution for this calculation, let h=[H⁺]=[A⁻]. Solve h²/(0.16−h)=K_a,c. The positive quadratic root gives a finite pH near 2.80, instead of the undefined inventory-ratio logarithm. Verify h is positive and below total concentration.

## Full balance and small terms

A more complete idealized calculation combines acid mass balance, equilibrium and electroneutrality. With fixed C_T=[HA]+[A⁻], define S as the excess spectator-cation concentration over strong-acid-anion concentration. Then [A⁻]=C_TK_a,c/(K_a,c+h), [OH⁻]=K_w,c/h and charge balance is h+S−[A⁻]−[OH⁻]=0. The virtual lab stipulates K_w,c=10⁻¹⁴ (mol/L)² as a teaching parameter and solves this equation numerically.

Water contribution can be negligible in an acidic example yet essential near neutral conditions. Retaining it in the lab avoids claiming a universal omission rule. The full balance remains an ideal model: it does not establish real activity coefficients, temperature dependence, ion pairing or electrode response. A more elaborate equation can be more internally consistent without being experimentally validated.

## Discrepancies need distinguishing evidence

A pH lower than a nominal buffer prediction could reflect less conjugate base, more acid equivalents, a different acid parameter, activity effects or measurement bias. These alternatives need discriminating information. A supplied reference sample can reveal a common offset; an independent composition measurement can test the assumed base inventory. Agreement with one fitted pH value is not enough to identify a unique cause.

The synthetic lab uses both a known reference and an independently supplied composition difference. Correcting its instrument offset does not remove the composition mismatch. The repeats deliberately balance around constructed readings, so they establish neither an independent noise distribution nor statistical evidence for a real acid parameter.

## Worked example

Compute nominal initial ratio 0.030/0.050 for pH 4.578151. After 0.010 mol acid, update both inventories before forming 0.020/0.060, yielding 4.322879. At 0.030 mol, reject the zero-base logarithm and solve the weak-acid balance for total concentration 0.16 mol/L instead. For a discrepancy, keep calibration and composition questions separate: a reference constrains reporting bias, while an independently supplied inventory checks the stoichiometric model. Neither step alone establishes every nonideal effect.

## Common mistakes and checks

Do not subtract acid from HA when it neutralizes A⁻. Do not use negative or zero inventory ratios in the buffer logarithm. Do not call every mismatch an electrode error or every corrected reading a validated chemical model. Specify temperature, concentration/activity convention and volume assumptions before comparing predictions.

## Limits of this lesson

Acid parameters, inventories, activities and observations are synthetic. This is a data and calculation exercise with no chemical handling procedure, real reagent choice or biological recommendation. Detailed acid–base speciation continues in General Chemistry II. Original instruction has substantial AI assistance; the package remains partial, unreviewed and formative-only.
