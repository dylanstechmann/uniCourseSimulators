# Rate laws and mechanism inference

## Learning objectives

1. Infer empirical orders from controlled synthetic initial-rate comparisons.
2. Derive limiting rate laws from a stated elementary-step model.
3. Distinguish agreement with a rate law from identification of a unique mechanism.

## Compare one change at a time

An empirical rate law relates a specified reaction rate to current concentrations under specified conditions. It is not obtained by copying the coefficients of an arbitrary overall equation. For a synthetic conversion, suppose r=k[A]^m[B]^n. Keep temperature, volume convention and the definition of r fixed while comparing initial mixtures. An initial-rate comparison aims to avoid later composition changes, but the experimental assumptions still need justification in a real application.

Construct three mixtures: A=0.10,B=0.20 mol/L gives r=0.002 mol/(L·s); doubling A while holding B fixed gives r=0.008; doubling B while holding A fixed gives r=0.004. The fourfold A response implies m=2, and the twofold B response implies n=1. Their total order is three. These are deliberately exact synthetic comparisons, not noisy measured rates or a unique mechanistic fingerprint.

The inferred k is 0.002/(0.10²×0.20)=1.0 L²/(mol²·s). At A=0.15 and B=0.30 mol/L, the same empirical model predicts 0.00675 mol/(L·s). Units follow from rate divided by the concentration powers. A first-order constant and this third-order constant cannot be compared numerically as though they had the same dimensions.

## Rate definition and coefficients

For 2A+B→C, a stoichiometrically normalized reaction rate can be written r=−(1/2)d[A]/dt=−d[B]/dt=d[C]/dt. If r=0.00675 mol/(L·s), A disappearance magnitude is 0.01350 mol/(L·s). The empirical powers need not be 2 and 1 merely because those coefficients appear. In this constructed case they coincide, but the coincidence is not a derivation.

A rate reported as reactant disappearance must identify the species. Otherwise a factor of two can appear to be a discrepancy between experiments or constants when it is only a convention difference. Conservation checks apply to the derivatives just as they apply to integrated amounts: consuming two A per B requires matching derivative ratios under the one-reaction model.

## Elementary steps and intermediates

An elementary step represents a proposed molecular event in a mechanism. Under elementary mass-action assumptions, its molecularity constrains the concentration powers in its rate. A multistep overall equation can instead contain intermediates and limiting approximations. The [OpenStax mechanisms section](https://openstax.org/books/chemistry-2e/pages/12-6-reaction-mechanisms) supplies a link-only reference for that distinction; no mechanism or teaching problem is copied here.

Consider the hypothetical sequence A+B⇌I, followed by I→P. In an ideal fast-pre-equilibrium limit, let K_c=[I]/([A][B]) and product formation r=k₂[I]. Substitution gives r=k₂K_c[A][B]. With stipulated K_c=5 L/mol, k₂=0.2 s⁻¹, A=0.1 and B=0.2 mol/L, the model intermediate is 0.1 mol/L and rate 0.02 mol/(L·s). These stipulated free concentrations are not the same as analytical totals if much material occupies I.

Pre-equilibrium requires reversible redistribution to be fast relative to the subsequent drain. A steady-state approximation instead requires intermediate production and removal to nearly balance. For this sequence it gives [I]≈k₁[A][B]/(k₋₁+k₂), producing a different effective coefficient unless k₂ is negligible beside k₋₁. Approximation names describe conditions, not interchangeable algebraic permissions.

## Pseudo-first-order behavior

If a bimolecular law r=k[A][B] has B held nearly constant by a large excess, the observed A disappearance can appear first-order with k_obs=k[B]. With stipulated k=0.5 L/(mol·s) and nearly constant B=0.20 mol/L, k_obs=0.10 s⁻¹. Changing the excess B changes the apparent first-order constant. That observation helps test the hidden dependence rather than establishing a unimolecular elementary mechanism.

The approximation fails if B is depleted enough to change appreciably, if competing chemistry matters or if the reported signal is not proportional to A. A straight line in a transformed plot cannot independently validate the concentration calibration, background subtraction or excess-reactant condition. The preserved integrated-rate lesson provides useful mathematical forms, while the new lab examines an additional plateau ambiguity.

## Identifiability and distinguishing evidence

Two mechanisms can predict the same empirical concentration powers over a restricted range. A valid proposed mechanism must conserve atoms and charge, sum to the overall equation and agree with observed behavior under its stated approximations. Meeting those requirements makes it compatible; it does not necessarily make it uniquely identified. Additional perturbations or intermediate-sensitive observations may separate alternatives.

For example, testing a wider B range can expose failure of pseudo-first-order behavior. Independently measuring an intermediate can test whether pre-equilibrium occupancy is plausible. Temperature dependence, isotope substitutions or catalyst concentration can also constrain a real mechanism, but those approaches need their own justified models. This lesson specifies no laboratory procedure or real reaction investigation.

## Worked example

Take initial-rate ratios 4 for a twofold A increase and 2 for a twofold B increase. Solve 2^m=4 and 2^n=2, giving m=2,n=1. Compute k from the reference mixture and predict the new rate 0.00675. For the separate hypothetical pre-equilibrium mechanism, calculate I from K_c[A][B], then form k₂[I]. Keep the empirical example and proposed mechanism separate: they describe different synthetic models and do not claim to explain the same reaction.

## Common mistakes

Do not infer overall rate powers solely from balanced coefficients. Distinguish normalized reaction rate from species disappearance. Do not confuse free concentrations with analytical totals or pre-equilibrium with steady state.

## Limits of this lesson

All rates and species here are synthetic, and no actual mechanism is uniquely identified. Original instruction has substantial AI assistance. The course remains partial, unreviewed and formative-only.
