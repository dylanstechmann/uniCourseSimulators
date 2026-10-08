# Dose–response to stiffness: the Hill function, the half-maximal stiffness and how to choose the levels

A claim that "stiffer gels increase a differentiation marker" is a statement about a relation between two numbers, and the shape of that relation matters as much as its sign. If the marker rises steeply over a narrow range of stiffness, two gels on either side of the range will show a large difference and two gels both below it will show none; if the response saturates, a still stiffer gel adds nothing. The standard summary of a graded response is the Hill function, which gives a maximal response, a half-maximal stiffness and a steepness, and it also suggests how to choose the stiffness values of an experiment. This lesson uses the Hill function to compute responses and to invert it, and to show why stiffness values should be spaced on a logarithmic scale. All values are synthetic.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute the response at a given stiffness, and the stiffness for a given response, with a Hill function.
2. Interpret the maximal response, the half-maximal stiffness and the steepness, and the slope at the midpoint.
3. Evaluate how the choice of stiffness levels determines what an experiment can show.

## The Hill function

A saturating response y to a stimulus E (here a gel's stiffness, in kPa) is described by

**y = y_max E^n / (EC₅₀^n + E^n),**

where y_max is the maximal response, EC₅₀ the stiffness at which the response is half of y_max, and n the Hill coefficient, which sets the steepness. **Synthetic values:** y_max = 80% marker-positive cells, EC₅₀ = 10 kPa and n = 2.

| Stiffness (kPa) | Marker-positive cells (%) |
|---:|---:|
| 1 | 0.8 |
| 3 | 6.6 |
| 10 | 40.0 |
| 30 | 72.0 |
| 100 | 79.2 |

At 5 kPa the response is 16% and at 20 kPa 64%, so a fourfold increase in stiffness raises the response by 48 points; at the EC₅₀ the response is **40%**, half of the maximum; at 40 kPa it is 75.3%, close to saturation. The function can be inverted: for a response y, E = EC₅₀ (y/(y_max − y))^(1/n), so the stiffness that gives 64% is E = 10 × (64/16)^(1/2) = **20 kPa**. The slope at the midpoint is n y_max/(4 EC₅₀) = 2 × 80/(4 × 10) = **4 percentage points per kPa**, the steepest part of the curve; where the response is saturating or has not begun, the slope is smaller.

## Choosing the stiffness levels

The response is a function of the logarithm of stiffness, and its natural scale is multiplicative: a doubling means the same at 2 kPa and at 20 kPa. Stiffness levels should therefore be spaced logarithmically, for example 1, 3, 10, 30 and 100 kPa, which spans the transition at 10 kPa with two points below and two above (responses 1, 7, 40, 72, 79%). Linearly spaced levels such as 20, 40, 60, 80, 100 kPa put every point in the saturated range (responses 64, 75, 78, 79, 79%), and the experiment would conclude that stiffness has little effect on this marker even though it has a large effect below 20 kPa. Three levels give a direction but not a shape; five or more, spread over the range of interest, are needed to estimate the midpoint and the steepness, and the fit should be made to gel-level values, not to individual cells, because the independent unit is the gel.

## What the curve does not show

A fitted EC₅₀ is a property of a particular material system, not of a cell type: it depends on the ligand, on the viscoelasticity of the gel (see the rheology lesson), on the time of the assay and on the marker. If stiffness was raised by increasing crosslinking, other properties changed along with it, and the curve is a function of all of them together. A dose–response curve describes the association between a set of conditions and a response; separating the cause requires changing one property at a time.

## Common mistakes

- Spacing stiffness values linearly over a range that spans a decade or more.
- Reading the midpoint as the stiffness at which cells switch fate.
- Fitting a curve to individual cells and reporting the precision as if cells were independent.
- Extrapolating beyond the tested range.
- Assuming that the curve describes stiffness alone when other properties varied with it.
- Using too few levels to estimate both the midpoint and the steepness.

## Worked example

**Problem.** A synthetic marker follows a Hill function with y_max = 60%, EC₅₀ = 4 kPa and n = 3. Find the response at 2 and 8 kPa, the stiffness for a response of 45%, and the half-maximal response.

**Step 1: responses.** y(2) = 60 × 2³/(4³ + 2³) = 6.7%; y(8) = 60 × 8³/(4³ + 8³) = 53.3%.

**Step 2: half-maximal response.** 30% occurs at the EC₅₀, 4 kPa.

**Step 3: stiffness for 45%.** E = 4 × (45/15)^(1/3) = 5.77 kPa.

**Step 4: reading the result.** A fourfold change in stiffness (2 to 8 kPa) moves the response from 7% to 53%; levels chosen only above 16 kPa would show almost no effect.

## Limits of this lesson

All numbers are synthetic. The Hill function is an empirical description with three parameters, not a mechanism; real responses can be biphasic, time dependent and different for each marker. Nothing here is a statement about any real cell, gel or marker.
