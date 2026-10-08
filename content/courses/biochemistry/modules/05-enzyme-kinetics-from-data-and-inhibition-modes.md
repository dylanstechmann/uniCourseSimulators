# Enzyme kinetics from data: estimating Vmax and Km, turnover, and diagnosing inhibition

Enzymes set the pace of metabolism, and most drugs, many toxins and many regulatory signals act by changing enzyme rates. Kinetic parameters are how those effects are compared. This lesson builds the Michaelis–Menten description from a synthetic rate table, extracts turnover and catalytic efficiency, and shows how competitive and noncompetitive inhibitors leave different fingerprints on the apparent parameters.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute initial rates, turnover number and catalytic efficiency from Michaelis–Menten parameters.
2. Predict apparent Km and Vmax for competitive and pure noncompetitive inhibition and use them to diagnose an inhibitor's mode.
3. Evaluate how linearized plots and assay conditions can distort parameter estimates.

## The rate law and its assumptions

For a single-substrate enzyme measured at initial rates, with substrate in large excess over enzyme and the enzyme–substrate complex at steady state, the rate is

**v = Vmax [S] / (Km + [S]).**

Vmax = kcat [E]₀ is the rate when every enzyme molecule is occupied, and Km is the substrate concentration that gives half of Vmax. Km is not, in general, a dissociation constant: it equals (k₋₁ + kcat)/k₁, which approaches the dissociation constant only when catalysis is slow compared with substrate release.

**Synthetic rate table** (Vmax = 100 μM/min, Km = 5 μM, enzyme 0.01 μM):

| [S] (μM) | v (μM/min) |
|---|---|
| 1 | 16.7 |
| 2.5 | 33.3 |
| 5 | 50.0 |
| 10 | 66.7 |
| 20 | 80.0 |
| 50 | 90.9 |

At [S] = Km the rate is exactly half of Vmax; at four times Km it is 80% of Vmax; even at ten times Km it is still only about 91%. Saturation is approached slowly, which is why Vmax is hard to estimate from data that stop at moderate concentrations.

## Turnover and efficiency

kcat = Vmax / [E]₀ is the number of substrate molecules converted per active site per unit time. Here kcat = 100 / 0.01 = 10000 per minute = 166.7 s⁻¹. The ratio **kcat / Km** (33.3 μM⁻¹ s⁻¹ = 3.3×10⁷ M⁻¹ s⁻¹) is the second-order rate constant at low substrate. It governs which of two competing substrates an enzyme prefers, and it has an upper limit near the diffusion rate of about 10⁸ to 10⁹ M⁻¹ s⁻¹. kcat requires knowing the concentration of active enzyme, not only total protein.

## Inhibition modes and their fingerprints

Define α = 1 + [I]/K_I, where K_I is the inhibitor's dissociation constant.

- **Competitive** inhibitors bind the free enzyme at the substrate site. Apparent Km rises to α Km; Vmax is unchanged because enough substrate outcompetes the inhibitor.
- **Pure noncompetitive** inhibitors bind free enzyme and enzyme–substrate complex equally at another site. Apparent Vmax falls to Vmax/α; Km is unchanged.
- **Uncompetitive** inhibitors bind only the enzyme–substrate complex; both apparent Vmax and apparent Km fall by α.
- Mixed inhibitors change both, by different factors.

With [I] = 4 μM and K_I = 2 μM, α = 3. At [S] = 20 μM, the uninhibited rate is 80 μM/min. A competitive inhibitor raises Km to 15 μM and lowers the rate to 57.1 μM/min; a noncompetitive inhibitor lowers Vmax to 33.3 μM/min and the rate to 26.7 μM/min. The same α causes different losses depending on mode and substrate level, which is why an IC₅₀ measured at one substrate concentration does not transfer to another for a competitive inhibitor.

## Estimating parameters honestly

The double-reciprocal (Lineweaver–Burk) plot of 1/v against 1/[S] is a straight line with slope Km/Vmax and intercept 1/Vmax. It is useful for showing inhibition patterns but poor for estimation: taking reciprocals magnifies the errors of the lowest-rate points, which then dominate the fit. Nonlinear least-squares fitting of the hyperbola to untransformed data, with substrate concentrations spread around Km (from roughly 0.2 Km to 5 Km or higher), gives better estimates. Initial rates must actually be initial: if more than about 10% of substrate is consumed, or product inhibits, the rates are underestimated.

## Common mistakes

- Treating Km as a plain dissociation constant, which holds only when catalysis is slow compared with substrate release.
- Reading Vmax from data that stop at moderate substrate concentrations, where the rate is still well below saturation.
- Trusting the intercepts of an unweighted Lineweaver–Burk line, because taking reciprocals magnifies the error of the lowest-rate points.
- Using rates measured after more than about 10% of the substrate is consumed, or with product inhibition, as if they were initial rates.
- Comparing inhibitors by IC₅₀ values measured at different substrate concentrations, which is not valid for a competitive inhibitor.
- Computing kcat from total protein instead of the concentration of active enzyme.

## Worked example

**Problem.** Two synthetic inhibitors each halve the rate at [S] = 5 μM (from 50 to 25 μM/min). Inhibitor P is competitive with α = 3; inhibitor Q is pure noncompetitive with α = 2. Which measurement would tell them apart?

**Step 1: check the low-substrate point.** Competitive: v = 100 × 5 / (15 + 5) = 25 μM/min. Noncompetitive: v = 50 × 5 / (5 + 5) = 25 μM/min. At this substrate level the two are indistinguishable.

**Step 2: go to high substrate.** At [S] = 50 μM the uninhibited rate is 90.9 μM/min. With P it is 76.9 μM/min, because substrate outcompetes the inhibitor; with Q it is 45.5 μM/min, because half the enzyme remains effectively unavailable however much substrate is added.

**Step 3: conclude.** A single-concentration potency measurement cannot reveal mechanism. Rates across a range of substrate concentrations, fitted to the hyperbola with and without inhibitor, show which parameter the inhibitor changes.

## Limits of this lesson

All rates are synthetic. Real enzymes may show cooperativity, substrate inhibition, multiple substrates or tight-binding inhibitors where the simple equations fail.
