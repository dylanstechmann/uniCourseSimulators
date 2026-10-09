# Virtual lab 1: buffer discrepancy, reference calibration and composition

**Status:** public formative practice with public answers and unlimited retries. Points are study feedback, not a course grade. This is a synthetic data exercise, with no chemical handling or preparation procedure. Prerequisite: the acid–base buffer and equilibrium-convention lessons.

## Learning objectives

1. Summarize pH reports and calculate a supplied reference offset.
2. Compare nominal buffer predictions with an independently specified composition and full ideal balance.
3. Explain what calibration does and does not establish about a chemical-model discrepancy.

## Construction and independent information

The preserved case nominally has 0.050 mol HA and 0.030 mol A⁻ in a fixed 0.50 L. For this lab, independent synthetic composition information instead supplies 0.056 mol HA and 0.024 mol A⁻. Both totals are 0.080 mol, so total acid-family concentration C_T is 0.16 mol/L in either description. The acid has a stipulated concentration-model pK_a=4.8. These numbers do not identify a real reagent or describe an actual measurement.

Six constructed conditions add q=0,0.005,0.010,0.020,0.025,0.030 mol strong-acid equivalents in an abstract fixed-volume calculation. Volume change is deliberately omitted. The independently supplied base inventory reaches stoichiometric exhaustion at 0.024 mol, earlier than the nominal 0.030 mol. The ideal full model retains weak-acid dissociation and water throughout; it does not attempt to infer the initial composition from these pH reports.

Let h be hydrogen concentration in mol/L, K_a,c=10^(−4.8) mol/L and the stipulated K_w,c=10⁻¹⁴ (mol/L)². The spectator charge difference is S=(0.024−q)/0.50 mol/L. Acid mass balance and equilibrium give [A⁻]=C_TK_a,c/(K_a,c+h), and water gives [OH⁻]=K_w,c/h. Electroneutrality requires h+S−[A⁻]−[OH⁻]=0. The positive solution defines ideal pH=−log₁₀(h/(1 mol/L)). Concentration activities are deliberately assumed ideal; no real activity coefficients are determined.

A synthetic reporting system adds +0.0800 pH units to every model value. The central report is rounded to four decimals, and three values are placed at central minus 0.0100, central and central plus 0.0100. A separate reference has stipulated target pH 4.0000 and the same reporting offset. This construction makes the arithmetic pH mean equal to each rounded central report. Repeats do not establish independent sampling or a real noise distribution.

## Data dictionary

[Download the synthetic CSV](https://raw.githubusercontent.com/dylanstechmann/uniStemCourseSimulators/main/content/courses/general-chemistry-1/labs/buffer-reports.csv). `sample` is the stable group code; `acid_equivalents_mol` is the abstract acid load, blank for the separate reference; `replicate` identifies one of three constructed reports; `reported_pH` is the value including offset. A blank reference load means not applicable, not zero acid added to the same buffer.

| Sample | Acid equivalents (mol) | Mean reported pH | Mean after reference correction |
|---|---:|---:|---:|
| q00 | 0 | 4.5125 | 4.4325 |
| q05 | 0.005 | 4.3742 | 4.2942 |
| q10 | 0.01 | 4.2080 | 4.1280 |
| q20 | 0.02 | 3.6175 | 3.5375 |
| q25 | 0.025 | 2.6211 | 2.5411 |
| q30 | 0.03 | 1.9934 | 1.9134 |
| reference | not applicable | 4.0800 | 4.0000 |

## Work sequence

Open Practice gradebook and select **Virtual lab 1: buffer discrepancy, reference calibration and composition (ungraded practice)**. Upload a summary with exact columns `sample,replicates,mean_ph` and seven row codes q00,q05,q10,q20,q25,q30,reference. The checks evaluate seven counts and seven arithmetic reported-pH means, using a mean tolerance of 0.005 pH units. They do not evaluate a written uncertainty argument.

Use the reference mean minus its target to estimate the common offset. Subtract that value from q10's reported mean. Separately update the nominal inventories after 0.010 mol acid: A⁻=0.020 mol and HA=0.060 mol. The nominal ratio predicts pH 4.322879. Compare it with the corrected q10 report and with the independently supplied composition. Retain the distinction between correcting measurement reporting and revising chemical amounts.

At q30, the actual base inventory would be negative under a naive subtraction. Reject that buffer logarithm and solve the stated full balance with S=−0.012 mol/L. The concentration root is positive even though that spectator difference is negative. The full balance includes excess strong acid; setting the formal negative base amount equal to a real species concentration would violate the model.

## Worked calculation

The reference arithmetic mean is 4.0800, so the supplied reporting offset is +0.0800. The q10 corrected mean is 4.1280, below nominal prediction 4.322879 by 0.1949. The independent composition has less base and more acid while preserving total amount, so its ratio and neutralization range differ. The full balance at q30 gives pH 1.913375; the corrected rounded CSV mean is 1.9134, agreeing to the data's rounding scale.

Calibration alone therefore does not remove the composition discrepancy. The current construction establishes this cause by supplying the composition independently. In a real case, acid-load error, temperature-dependent acid behavior, activities and additional instrument response could also matter. A single corrected pH value would not distinguish every explanation.

## Discussion criteria

| Criterion | Evidence to discuss |
|---|---|
| Summary | Correct grouping, counts and arithmetic mean pH |
| Calibration | Reference target, common offset and its limited scope |
| Chemical accounting | Nominal versus independent base/acid amounts and preserved total |
| Model domain | Positive species concentrations and charge balance beyond exhaustion |
| Interpretation | Separate observation correction, model assumptions and causal identification |

These criteria guide discussion rather than automatically graded prose. The logarithm means that averaging pH is not generally equivalent to averaging hydrogen concentrations and then taking minus log. A common offset can affect all reports together; repeating values does not automatically remove it. The reference's target is exact only within this construction, not a claim about real standard uncertainty.

## Limits and provenance

All parameters, reference values and readings are synthetic. No experimental procedure, real buffer choice, biological suitability or independently validated acid parameter is supplied. The [IUPAC pH definition](https://goldbook.iupac.org/terms/view/P04524) is a link-only activity reference; its official indexed definition was verified, while direct page retrieval was blocked. This lab's concentration calculations explicitly assume an ideal model. Original guide and CSV are CC BY 4.0 with substantial AI assistance; no third-party dataset or teaching text was copied. One data lab is not a laboratory sequence. The package remains partial, unreviewed and formative-only.
