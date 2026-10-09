# Homework 2 candidate: calibrated initial rates and inhibition evidence

**State:** inactive candidate for review, authored with substantial Codex assistance. It is not available as graded coursework and contributes no course grade. No scientific, assessment or accessibility reviewer has approved it. Course package: 0.21.0, partial, unreviewed and formative-only.

## Preparation and purpose

Read [enzyme catalysis and free energy](../modules/04a-enzyme-catalysis-and-free-energy.md) and [initial rates and reversible inhibition](../modules/04b-initial-rates-and-enzyme-inhibition.md). The existing open Homework 2 companion remains available for practice. This candidate uses a separate dataset and new questions; public practice keys are not being relabeled as confidential assessment material.

The task connects a detector response to product concentration, separates background drift from a reaction slope, retains an independent assay-day unit and compares an early rate with a later interval. A lower fluorescence slope can reflect catalytic change, optical interference, background or several effects together. A useful control addresses a specific alternative; it does not identify a binding site or establish that every other explanation is absent.

Eight proposed machine-scored items total 25 points. The point allocation is a review draft, not a course-grade policy. The written discussion at the end is unscored. There is no selected deadline, time limit or attempt policy for actual learners, and workload has not been measured. This candidate is not listed in the Practice gradebook and has no live submission route. Its preparation as a packet does not satisfy the independent-review or semester-course gates.

## Experimental construction

Download the [synthetic fluorescence table](homework-02-candidate-fluorescence.csv). Four independently prepared assay days, d01–d04, each contain vehicle, compound_a and compound_b conditions. Condition and substrate measurements are paired within a day. Each day uses one independent enzyme preparation/dilution for this construction. Time observations, standards and substrate concentrations are repeated or matched measurements within that day, not additional independently prepared assays. Four days do not estimate between-laboratory or between-enzyme-construct variation.

Every day/condition block contains product standards at 0, 500 and 1000 nM. Reaction and no-enzyme blank series are provided at substrate 5, 15, 45 and 135 µM, each at times 0, 2, 4 and 10 seconds. The file therefore has 420 rows: twelve day/condition blocks, each with three standard records, sixteen blank records and sixteen reaction records. Standard rows have substrate and time zero as their labeled convention; they are static concentration controls, not reaction time points.

All signals, concentration levels, day differences and curvature are deterministic teaching values, not physical observations or samples from an estimated noise distribution. Standards are constructed to follow an affine relation within each day/condition. Their calibration is stipulated to apply across the four tested substrate levels in that same block, with no substrate-dependent optical response in this construction. That transfer is an assumption: a real experiment would need suitable matrix controls or evidence that the transfer is valid. Three exact teaching standards do not establish a real detector's uncertainty, dynamic response or usable range.

## Data dictionary

| Column | Meaning and scale |
|---|---|
| day | Independently prepared assay-day block, d01 through d04 |
| condition | vehicle, compound_a or compound_b |
| series | standard for static product calibration, blank for no-enzyme time course, reaction for enzyme time course |
| substrate_um | Starting substrate concentration in micromolar; zero on standard records |
| product_standard_nm | Known product concentration in nanomolar on standard records; zero as a labeling convention on blank/reaction records |
| time_s | Seconds for blank/reaction records; zero on static standards |
| signal_au | Fluorescence detector response in arbitrary units, a.u.; neither product concentration nor an enzyme-rate unit |

All essential values are in plain-text CSV. Missing or mislabeled records should be flagged rather than filled with fabricated measurements. The matched blank is a no-enzyme reference at the same day, compound condition and substrate level. It describes measured background behavior under this stipulated reference construction, not a separate enzyme replicate or proof of catalytic specificity.

## Calibration and slope contract

For static standards, write y=a+bP, where P is product concentration in nM, y is signal in a.u., a is an offset and b has scale a.u. per nM. Estimate b by ordinary least squares: b=Σ(P−mean P)(y−mean y)/Σ(P−mean P)², and a=mean y−b mean P. Keep each day and condition separate. The denominator must be positive and the gain must be nonzero for the conversion. Use the static conversion P=(y−a)/b for the separate concentration question; do not apply a static offset alone to remove a drifting background.

For a time-course slope over the predefined early window, use only t=0,2,4 s. Estimate β=Σ(t−mean t)(y−mean y)/Σ(t−mean t)² separately for the reaction and its matched blank. The calibrated net product rate is (β_reaction−β_blank)/b in nM/s. Subtract slopes in signal units before converting, or convert both slopes consistently. Retain one corrected rate per day, condition and substrate before calculating the requested four-day arithmetic mean. A pooled signal slope divided by a pooled gain can apply different weights and is not the specified calculation.

The later comparison deliberately uses the endpoint slope from 0 to 10 seconds, not an ordinary-least-squares fit to every time point. Calculate the reaction signal difference divided by ten seconds, subtract the matched blank endpoint slope and divide by the same block gain. Compare that value with the predefined early slope. Curvature changes the meaning of a window; the construction does not identify a physical cause such as depletion, inactivation, product inhibition or detector dynamics. These records do not simulate the governing differential equations of any such mechanism.

For the separately stipulated one-to-one accounting question, net product accumulated between t=0 and 4 s is the reaction signal increment minus the matched blank increment, divided by the block gain. Convert starting substrate from µM to nM before taking the ratio. This calculation does not measure substrate loss directly or guarantee that every condition satisfies initial-rate assumptions. Enzyme stability, reversibility, side reactions and product effects remain separate questions.

## Separate worked illustration

The following values are unrelated to the candidate dataset. Suppose standards at 0, 250 and 500 nM give signals 8, 33 and 58 a.u. Then the fitted offset is 8 a.u. and gain is 0.10 a.u. per nM. A reaction signal slope of 4.2 a.u./s with matched blank slope 0.2 a.u./s gives corrected rate (4.2−0.2)/0.10=40 nM/s. Subtracting only the blank's t=0 offset would leave its drift inside the rate. A separate static signal of 28 a.u. corresponds to (28−8)/0.10=200 nM. Static conversion and background-slope correction answer different questions.

## Response rules and limitations of scoring

The four numeric items require compatible units and their stated significant figures. Concentration, concentration per time and percent are different scales; arbitrary fluorescence units cannot substitute for a calibrated chemical amount. The window-comparison field asks for a bare dimensionless ratio with exactly two significant figures. An unanswered or malformed field earns no credit; incomplete valid composite responses receive only the points of fields they satisfy.

The upload has exact columns condition,days,mean_rate_15_nm_s,mean_rate_135_nm_s, one unique row per listed condition and nine scored numeric cells. Use small UTF-8 CSV, not formulas or executable code. Day counts are exact; rate means use tolerance 0.005 nM/s. The numeric rate cells contain plain values on the stated nM/s scale, without unit strings in the table. The grader does not enforce significant figures in the upload or assess your analysis code, residual plots, parameter fit or uncertainty discussion.

Each structured field is a one-point choice check. Multiple-select credit follows the explicitly stated correct-minus-incorrect rule. Selecting a scored categorical response does not demonstrate a written explanation or a molecular mechanism. No high-stakes assessment security, university credit or reviewed grading validity is claimed.

## Item stems and proposed allocation

### Item 1 — 2 proposed points

Using the compound_b product standards on day d01, convert a separate static signal of 35.0 arbitrary units to product concentration. Report a compatible concentration unit and exactly three significant figures.

### Item 2 — 2 proposed points

At substrate 45 µM for compound_b, calculate each day's ordinary least-squares slope over 0, 2 and 4 seconds for reaction and its matched blank. Subtract the blank slope, divide by that day/condition's calibration gain, then average the four day rates. Report concentration per time with exactly three significant figures.

### Item 3 — 2 proposed points

In a separately stipulated simple competitive model, Km is 15 µM, inhibitor concentration is 30 µM and Ki is 15 µM. Calculate Km,app=(1+[I]/Ki)Km. Report concentration with exactly two significant figures. These supplied model constants are not a fit to the displayed observations.

### Item 4 — 2 proposed points

For vehicle day d01 at starting substrate 5 µM, calculate blank-corrected product accumulated from 0 to 4 seconds using the matched gain. Under the separately stipulated one-to-one substrate-to-product accounting, express that amount as a percent of the starting substrate concentration. Report a percent unit and exactly four significant figures.

### Item 5 — 9 proposed points

Summarize the four independently prepared assay days after matched blank subtraction and day/condition calibration. Use only the 0, 2 and 4 second slope window. Upload exact columns condition,days,mean_rate_15_nm_s,mean_rate_135_nm_s with rows vehicle,compound_a,compound_b. Counts are exact; rate-cell tolerance is 0.005 nM/s. Time observations, substrate levels and calibration standards do not add independent assay days.

### Item 6 — 2 proposed points

For vehicle d01 at 135 µM, compare the blank-corrected calibrated endpoint slope from 0 to 10 seconds with the ordinary least-squares slope over 0, 2 and 4 seconds.

**ratio (1 point):** Report late endpoint slope divided by early slope as a bare dimensionless ratio. Report exactly 2 significant figures.

**inference (1 point):** Which conclusion follows from this window comparison?

1. The later window proves irreversible inhibition at a named active-site residue.

2. The rate estimate depends on the window; curvature alone does not identify depletion, inactivation or another cause.

3. Every late endpoint is an initial rate when its time axis starts at zero.

### Item 7 — 4 proposed points

Select one response for each independent calibration, blank, replication and inference criterion.

**matrix (1 point):** Which calibration should convert compound_b day d02 signal?

1. Vehicle standards pooled across days.

2. Compound_b product standards from day d02, subject to the stated linearity/matrix assumptions.

3. The compound_a curve at the highest substrate.

**blank (1 point):** How should background drift be handled before rate conversion?

1. Subtract the blank's initial offset only and ignore its slope.

2. Use the blank as extra independent enzyme replicates.

3. Subtract the same-day, same-condition, same-substrate no-enzyme slope in the selected window.

**unit (1 point):** What is the independent replicate unit in this construction?

1. Each separately prepared assay day, with conditions/substrates/time points paired within the day.

2. Every detector time point and standard is a separate biological replicate.

3. Each column in the input file.

**scope (1 point):** What does overlap with vehicle after calibrated blank correction support?

1. Proof that the compound has no molecular interaction under any condition.

2. Consistency with no resolved catalytic-rate difference in this synthetic assay; other effects need separate tests.

3. Proof of the compound's therapeutic safety.

### Item 8 — 2 proposed points

Select all statements justified by the stated single-substrate model and measurement limits. Scoring is two points times (correct options selected minus incorrect options selected) divided by the total number of correct options, clamped from zero to two.

1. A competitive-looking rate curve proves occupancy of the substrate-binding pocket.

2. An enzyme can speed approach to equilibrium without changing the reaction equilibrium constant.

3. A fluorescent product standard by itself measures the amount of active enzyme.

4. Km is always the substrate-binding dissociation constant.

5. With kcat and other model conditions fixed, doubling active enzyme concentration doubles Vmax.

## Written discussion for a future human reviewer

Describe how the inferred rate changes when the detector gain, matched blank and time window are handled correctly. Retain the independent assay-day unit and distinguish an amount per time from a raw detector slope. Explain why a finite substrate series and a competitive-looking pattern do not settle molecular binding, and propose an orthogonal readout or interaction measurement tied to a stated competing explanation. Discuss what uncertainty or matrix-transfer evidence is missing from the exact teaching standards. State how you would investigate late curvature without assuming its physical cause in advance.

A draft discussion rubric distinguishes absent or incompatible reasoning, partly correct reasoning with a material omission, and coherent reasoning with explicit controls, units, assumptions and bounded conclusions. Criteria are matched calibration and blank use, replication and pairing, time-window meaning, model-versus-mechanism distinctions, and a follow-up whose outcomes distinguish alternatives. These are discussion descriptors, not autograded prose or released grade weights. No written response has been assessed by a human or AI grader.

## Provenance, accessibility and readiness

This is an original exercise based on the existing enzyme lessons. No new outside source, paper identifier, third-party data, prose, question or figure was introduced. Original instructions and synthetic observations are CC BY 4.0 with substantial AI assistance. Public instructions and data remain independently solvable; a private key is not proof of assessment security.

All essential labels, units and values are textual. The task requires no color discrimination, image inspection or timed interaction. Screen-reader/manual workflow, accessibility and fairness review remain required; their absence is not repaired by these design choices. Independent numerical, scientific and assessment review, measured workload and operator provisioning/release decisions remain outstanding. No physical experiment, fitted real inhibition constant, unique binding site, therapeutic benefit or clinical safety was established. The candidate remains inactive.
