# Virtual lab 1: enzyme kinetics and inhibition from replicate rates

**Activity type:** synthetic-data analysis with public, ungraded formative checks
**Course package:** Biochemistry I: Proteins, Enzymes & Metabolism. **Estimated learner time:** 2–3 hours
**Data status:** all measurements are constructed for instruction. They describe no real enzyme, inhibitor or experiment, and nothing here is evidence about any compound or any cell.
**Dataset:** [synthetic initial rates (CSV)](https://raw.githubusercontent.com/dylanstechmann/uniStemCourseSimulators/main/content/courses/biochemistry/labs/enzyme-kinetics-rates.csv).

## Experimental question

An enzyme converts one substrate to a product. Its initial rate is measured at six substrate concentrations (1 to 50 μM) with three replicate reactions at each, once without inhibitor (**control**) and once with a fixed 4 μM of an inhibitor. The lab asks for the enzyme's Vmax and Km, how the inhibitor changes them, which mode of inhibition fits, how strongly the inhibitor binds, and which assumptions the answers rest on.

## Learning objectives

1. Summarize replicate initial rates by condition and substrate concentration.
2. Estimate Vmax and Km from a double-reciprocal fit and the apparent Km under an inhibitor, and compute the inhibition constant.
3. Evaluate the mode of inhibition, the limits of linearized fits and the assay conditions that make initial rates trustworthy.

## Data dictionary

| Column | Meaning |
|---|---|
| condition | control or inhibitor |
| substrate_um | substrate concentration in μM |
| replicate | 1 to 3, an independent reaction |
| rate_um_per_min | initial rate in μM of product per minute |

## The synthetic data

**Control**

| [S] (μM) | Rep. 1 | Rep. 2 | Rep. 3 | Mean |
|---:|---:|---:|---:|---:|
| 1 | 17.27 | 16.37 | 16.37 | 16.67 |
| 2.5 | 32.93 | 33.53 | 33.53 | 33.33 |
| 5 | 50.30 | 49.40 | 50.30 | 50.00 |
| 10 | 67.27 | 66.37 | 66.37 | 66.67 |
| 20 | 79.60 | 80.20 | 80.20 | 80.00 |
| 50 | 91.21 | 90.31 | 91.21 | 90.91 |

**Inhibitor**

| [S] (μM) | Rep. 1 | Rep. 2 | Rep. 3 | Mean |
|---:|---:|---:|---:|---:|
| 1 | 5.85 | 6.45 | 6.45 | 6.25 |
| 2.5 | 14.59 | 13.69 | 14.59 | 14.29 |
| 5 | 25.60 | 24.70 | 24.70 | 25.00 |
| 10 | 39.60 | 40.20 | 40.20 | 40.00 |
| 20 | 57.44 | 56.54 | 57.44 | 57.14 |
| 50 | 77.52 | 76.62 | 76.62 | 76.92 |

## Work sequence

To use the software checks, open **Practice gradebook** and select **Virtual lab 1: enzyme kinetics and inhibition (ungraded practice)**. The points are practice feedback only.

1. **Summarize.** Count the replicates and average the rates at each substrate concentration. Upload a table with columns `condition`, `replicates`, `mean_v_1um`, `mean_v_5um`, `mean_v_20um` and `mean_v_50um`.
2. **Fit the control.** Compute 1/[S] and 1/v for the six mean rates and fit a straight line by least squares. The intercept is 1/Vmax and the slope is Km/Vmax.
3. **Fit the inhibitor group** the same way and read the apparent Km. Compare Vmax and Km in the two groups and decide which mode of inhibition fits.
4. **Compute the inhibition constant** for a competitive inhibitor: α = Km(app)/Km and K_I = [I]/(α − 1).
5. **Reflect on the method.** Say why the double-reciprocal plot is good for showing a pattern and poor for estimating parameters, and what an assay must satisfy for its rates to be initial rates.

## Worked calculation

The control line has intercept 0.01000 and slope 0.0500, so Vmax = 100.0 μM/min and Km = 0.0500 × 100.0 = 5.00 μM. The inhibitor group gives Vmax 100.0 μM/min (unchanged within error) and an apparent Km of 15.0 μM, so α = 15.0/5.00 = 3.00 and, for a competitive inhibitor at 4 μM, K_I = 4/(3.00 − 1) = 2.00 μM. The two double-reciprocal lines meet at the same y-intercept, the signature of competitive inhibition. A fit of the untransformed data by nonlinear least squares is preferable for real work, because the reciprocal transformation gives the smallest rates the most weight.

## Analytic rubric for discussion

| Criterion | Evidence for full credit |
|---|---|
| Summary table | Averages replicates at each concentration and reports the number of replicates |
| Parameters | Obtains Vmax and Km from the intercept and slope, with correct units |
| Mode of inhibition | Recognizes unchanged Vmax and raised apparent Km as competitive and computes K_I |
| Method limits | States that reciprocals magnify error at low rates and prefers a nonlinear or weighted fit |
| Scope | Treats the result as a property of a purified enzyme in this assay, not of a cell or a person |

## Limits and provenance

This is an original exercise with constructed data and round parameters. Real kinetic data are noisier, need checks for substrate depletion, product inhibition and enzyme stability, and are usually fitted by nonlinear regression with confidence intervals. Original lab text and dataset: CC BY 4.0.
