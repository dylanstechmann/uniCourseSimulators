# Initial-rate evidence and reversible enzyme inhibition

Kinetic data can distinguish useful model patterns, but a curve is not a photograph of a molecular mechanism. This lesson asks what an initial-rate experiment measures, how simple inhibitor models change apparent parameters, and which controls prevent an assay artifact from being mistaken for inhibition.

## Learning objectives

By the end of this lesson, you should be able to:

1. Use the Michaelis–Menten model to calculate an initial rate and describe its units.
2. Compare substrate-rate data with simple competitive, uncompetitive, and mixed-inhibition patterns.
3. Identify controls that address substrate depletion, detector interference, solvent effects, and enzyme stability.
4. State what an inhibition pattern supports and what requires independent evidence about binding or mechanism.

## Measure initial rates, not a convenient endpoint

An initial velocity is estimated from the early, approximately linear part of product accumulation or substrate disappearance. The window should be short enough that substrate concentration changes little, product has not accumulated enough to drive a substantial reverse reaction or product inhibition, and the signal remains in the detector's calibrated range. “The first five minutes” is not a transferable rule: the correct interval depends on the enzyme amount, substrate, temperature, readout, and reaction progress.

For each substrate concentration, collect multiple measurements over time and estimate the slope in a prespecified linear interval. Include independent replicates. Plot individual values and residuals, report the number of replicates and variability, and check whether variance grows with the mean. A single late endpoint can confuse lower enzyme activity with substrate depletion, product inhibition, protein instability, or detector saturation.

Vary `[S]` while holding active enzyme concentration, buffer, pH, temperature, solvent, and measurement method fixed. The simple one-substrate model predicts `v₀ = Vmax[S]/(Km + [S])`. Fit the rate data directly to this nonlinear equation and examine residuals and uncertainty in parameter estimates. Reciprocal plots such as Lineweaver–Burk can illustrate limiting behavior, but taking reciprocals magnifies errors at low substrate concentration; do not use a straight-line reciprocal plot as the sole basis for parameter estimates or inhibitor classification.

## Apparent parameter patterns in simple reversible models

For a reversible inhibitor that binds free enzyme or the ES complex, a useful mixed-inhibition form is:

`v₀ = Vmax[S] / (αKm + α′[S])`

`α = 1 + [I]/Ki` describes inhibitor association with free enzyme in this simplified model. `α′ = 1 + [I]/Ki′` describes association with ES. The apparent parameters are `Vmax,app = Vmax/α′` and `Km,app = αKm/α′`.

- **Competitive pattern:** inhibitor binds free enzyme in the simple model, so `α > 1` and `α′ = 1`. Apparent `Km` rises while `Vmax` is unchanged. Raising substrate can overcome the rate effect asymptotically, provided the mechanism and concentration range satisfy the model.
- **Uncompetitive pattern:** inhibitor binds ES, so `α = 1` and `α′ > 1`. Apparent `Km` and `Vmax` both decrease by the same factor in this model.
- **Mixed pattern:** inhibitor can bind free enzyme and ES with different affinities. Apparent `Vmax` decreases and apparent `Km` may rise or fall depending on the two interactions.
- **Pure noncompetitive pattern:** a special mixed case with equal association to free enzyme and ES (`α = α′`). Apparent `Vmax` decreases while `Km` is unchanged. Real datasets can deviate from this idealized pattern.

These are model descriptions of measured kinetics. A competitive-looking pattern does not prove that an inhibitor occupies the substrate-binding pocket. Slow binding, aggregation, substrate sequestration, covalent inactivation, mixed mechanisms, and optical interference can produce misleading observations. A time-dependent loss of activity after inhibitor preincubation is not captured by a simple equilibrium inhibition model; recovery after dilution or washout and direct binding or structural measurements address different questions.

## Worked analysis: a synthetic inhibitor dataset

The table below is **synthetic teaching data**. Each value is the mean of three constructed initial-rate replicates; the listed ±1 nM·s⁻¹ is the sample standard deviation used for the example. These numbers are not experimental observations. The control values were generated around a single-substrate curve with `Vmax ≈ 120 nM·s⁻¹` and `Km ≈ 20 μM`. The inhibitor values were generated around a competitive-looking curve with the same limiting `Vmax` and a larger apparent `Km`. Small rounding and replicate differences are intentional.

| `[S]` (μM) | Vehicle rate (nM·s⁻¹) | Inhibitor rate (nM·s⁻¹) |
|---:|---:|---:|
| 10 | 40 ± 1 | 17 ± 1 |
| 20 | 60 ± 1 | 30 ± 1 |
| 40 | 80 ± 1 | 48 ± 1 |
| 80 | 96 ± 1 | 68 ± 1 |
| 160 | 107 ± 1 | 87 ± 1 |
| 320 | 113 ± 1 | 101 ± 1 |
| 640 | 116 ± 1 | 110 ± 1 |

At `[S] = 40 μM`, the control model predicts `120 × 40/(20 + 40) = 80 nM·s⁻¹`, consistent with the table. If inhibitor concentration is 40 μM and the simple model's `Ki` is 20 μM, `α = 1 + 40/20 = 3`, so the apparent `Km` is 60 μM and the rate predicted at `[S] = 40 μM` is `120 × 40/(60 + 40) = 48 nM·s⁻¹`.

The observations are consistent with a competitive-like pattern: the inhibitor condition is lower at matched substrate concentrations, while the rates get closer at high substrate. The tested values do not establish that both reactions reach the same limiting `Vmax`; the high-substrate range, fit uncertainty, and activity of the enzyme at those conditions still matter. The pattern also does not prove a physical binding site or exclude mixed and time-dependent mechanisms. Report it as support for a simple model, not as direct proof of a unique molecular interaction.

## Controls that test alternative explanations

Use controls tied to the measurement and the claim:

- A **vehicle-matched control** keeps solvent concentration and handling the same in inhibitor and control wells.
- A **no-enzyme substrate blank** estimates nonenzymatic substrate conversion or background signal.
- An **inhibitor-plus-product standard without enzyme** tests whether the compound absorbs, quenches fluorescence, or otherwise distorts the product readout.
- A **product calibration series** checks signal linearity and verifies that the detector is not saturated.
- A **known active-enzyme control** checks that the assay can detect expected turnover; an enzyme-free or heat-inactivated condition checks background, not catalytic specificity by itself.
- A **time course at more than one enzyme concentration** tests whether initial rate scales with active enzyme amount and whether the chosen time window is linear.
- A **matched pH, temperature, substrate, and preincubation schedule** reduces the chance that an apparent inhibitor effect is caused by condition changes or slow enzyme decay.

For a stronger mechanism claim, collect a wide enough substrate range, test more than one inhibitor concentration, fit the data globally with parameter uncertainty, and compare alternatives. Add orthogonal readouts, a binding measurement, dilution or washout recovery, and a suitable active-site or resistance variant when those tests answer the specific hypothesis. No single control proves all these alternatives absent.

### Check your reasoning

If the inhibitor condition has a lower rate at every measured substrate concentration but the curves nearly converge at the highest dose, name the simplest model pattern that fits. Then state one reason that pattern does not prove where the inhibitor binds and one assay control that tests detector interference.

## Provenance

This is original explanatory text and an explicitly synthetic dataset under the course's CC BY 4.0 content license. MIT OpenCourseWare 5.07SC Biological Chemistry I is linked as a topic-scope comparator only. Briggs and Haldane's 1925 article and Johnson and Goody's historical analysis are link-only research references. No source text, figure, or empirical data was copied or adapted.
