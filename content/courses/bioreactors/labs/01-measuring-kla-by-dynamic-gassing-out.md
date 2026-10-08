# Virtual lab 1: measuring kLa by dynamic gassing-out

**Activity type:** synthetic-data analysis with public, ungraded formative checks
**Course package:** Bioreactors & Tissue Culture Engineering. **Estimated learner time:** 2–3 hours
**Data status:** all measurements are constructed for instruction. They describe no real vessel, probe or experiment, and nothing here is evidence about any culture or process.
**Dataset:** [synthetic gassing-out curves (CSV)](https://raw.githubusercontent.com/dylanstechmann/uniStemCourseSimulators/main/content/courses/bioreactors/labs/gassing-out-do-curves.csv).

## Experimental question

The volumetric mass-transfer coefficient kLa limits the cell density a vessel can support. A common way to measure it in a cell-free vessel is the **dynamic gassing-out method**: the dissolved oxygen is first brought to zero, the gas is then switched to air at a fixed flow, and the dissolved oxygen is recorded as the vessel returns toward saturation. For a well-mixed liquid the approach is first order, C(t) = C* (1 − e^(−kLa t)) when the starting value is zero, so ln(1 − C/C*) is a straight line against time with slope −kLa. In the synthetic experiment the dissolved oxygen (percent of air saturation) is recorded at 7 times in each of three independent runs at each of three agitation speeds (200, 300 and 400 rpm). The lab asks for kLa at each speed, its dependence on speed, the cell density it supports and the limits of the measurement. It describes the logic of the method, not an operating procedure.

## Learning objectives

1. Summarize replicate gassing-out runs by agitation speed.
2. Estimate kLa from the dissolved-oxygen curve and its dependence on agitation speed.
3. Evaluate the cell density a measured kLa can support and the limits of the method, including probe response.

## Data dictionary

| Column | Meaning |
|---|---|
| rpm | agitation speed |
| run | 1 to 3, an independent gassing-out run |
| time_min | minutes after switching to air |
| do_pct | dissolved oxygen, percent of air saturation |

## The synthetic data

**200 rpm**

| Time (min) | Run 1 | Run 2 | Run 3 | Mean |
|---:|---:|---:|---:|---:|
| 0 | 0.0 | 0.0 | 0.0 | 0.0 |
| 5 | 14.8 | 16.2 | 15.0 | 15.3 |
| 10 | 28.0 | 27.8 | 29.2 | 28.3 |
| 15 | 40.2 | 39.0 | 38.8 | 39.3 |
| 20 | 48.1 | 49.6 | 48.4 | 48.7 |
| 30 | 62.9 | 62.6 | 64.1 | 63.2 |
| 45 | 78.6 | 77.4 | 77.1 | 77.7 |

**300 rpm**

| Time (min) | Run 1 | Run 2 | Run 3 | Mean |
|---:|---:|---:|---:|---:|
| 0 | 0.0 | 0.0 | 0.0 | 0.0 |
| 5 | 26.1 | 25.8 | 27.3 | 26.4 |
| 10 | 46.7 | 45.5 | 45.2 | 45.8 |
| 15 | 59.5 | 61.0 | 59.8 | 60.1 |
| 20 | 70.3 | 70.0 | 71.5 | 70.6 |
| 30 | 85.0 | 83.8 | 83.5 | 84.1 |
| 45 | 93.0 | 94.5 | 93.3 | 93.6 |

**400 rpm**

| Time (min) | Run 1 | Run 2 | Run 3 | Mean |
|---:|---:|---:|---:|---:|
| 0 | 0.0 | 0.0 | 0.0 | 0.0 |
| 5 | 38.5 | 37.3 | 37.0 | 37.6 |
| 10 | 60.4 | 62.0 | 60.8 | 61.1 |
| 15 | 75.4 | 75.1 | 76.6 | 75.7 |
| 20 | 85.7 | 84.5 | 84.2 | 84.8 |
| 30 | 93.5 | 95.0 | 93.8 | 94.1 |
| 45 | 98.3 | 98.0 | 99.5 | 98.6 |

## Work sequence

To use the software checks, open **Practice gradebook** and select **Virtual lab 1: measuring kLa by dynamic gassing-out (ungraded practice)**. The points are practice feedback only.

1. **Summarize.** Count the runs and average the dissolved oxygen at 10 and 30 min for each speed. Upload a table with columns `speed`, `runs`, `do_10` and `do_30`.
2. **Estimate kLa.** Convert the percentage to a fraction, compute −ln(1 − C/C*) and divide by the time in hours. Use the 30 min mean at 200 rpm and the 10 min mean at 400 rpm, and check the other times for consistency.
3. **Speed dependence.** Compute the exponent a in kLa ∝ N^a from the values at 200 and 400 rpm, and relate it to the power per volume.
4. **Supportable density.** For kLa = 5.66 per hour, C* = 0.2 mmol/L, a critical level of 0.05 mmol/L and a specific uptake of 2.0 × 10⁻¹⁰ mmol/(cell·h), compute the cell density the vessel supports.
5. **Check the method.** Compute the product of kLa and the probe response time, and state what a cell-free measurement does not show.

## Worked calculation

The mean readings at 30 min at 200 rpm and at 10 min at 400 rpm are 63.2% and 61.1%, so kLa(200) = −ln(1 − 0.6320)/0.5 = 2.00 per hour and kLa(400) = −ln(1 − 0.6107)/(10/60) = 5.66 per hour; at 300 rpm and 20 min the mean of 70.6% gives 3.67 per hour. The exponent is a = ln(5.66/2.00)/ln 2 = 1.50, and since P/V ∝ N³ this means kLa ∝ (P/V)^0.5. At kLa = 5.66 per hour the capacity is 5.66 × (0.2 − 0.05) = 0.849 mmol/(L·h), which at 2.0 × 10⁻¹⁰ mmol/(cell·h) supports 4.245 × 10⁶ cells/mL. With a probe response time of 20 s, kLa × τ_p = 0.031, small enough that the probe follows the curve. The result holds for a cell-free vessel in this medium and gas flow; cells, antifoam and medium components can change kLa.

## Analytic rubric for discussion

| Criterion | Evidence for full credit |
|---|---|
| Summary table | Reports the number of runs and the mean dissolved oxygen at each time for each speed |
| kLa | Uses the logarithmic form with consistent units to obtain kLa at each speed |
| Speed dependence | Obtains the exponent and relates it to power per volume |
| Capacity | Converts kLa to a supportable cell density with the correct unit conversions |
| Limits | States the probe-lag check and that a cell-free measurement does not carry over unchanged to a culture |

## Limits and provenance

This is an original exercise with constructed data and round parameters. Real gassing-out curves are noisier, depend on gas flow, probe position and temperature, and are often fitted by nonlinear regression with a correction for the probe response. Original lab text and dataset: CC BY 4.0.
