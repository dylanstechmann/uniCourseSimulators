# Virtual lab 1: calibration, loading and observed time constants

**Status:** public formative practice with public answers and unlimited retries. Points are study feedback, not course grades. This is a constructed data-analysis exercise with no equipment operation, electrode attachment or biological measurement procedure. Prerequisites: Thevenin loading, first-order RC transitions and reporting-versus-transfer distinctions.

## Learning objectives

1. Summarize grouped raw reports and determine independently supplied voltage-reference offset and gain.
2. Recover source resistance and input capacitance under a declared resistive-capacitive measurement model.
3. Distinguish physical loading, reporting calibration and unsupported source or biological inference.

## Construction and independent information

A hypothetical generator supplies an ideal open-circuit step from 0 to 1.0 V at t=0. Its series source resistance is 100 kΩ. The input contains a known resistor in parallel with an initially uncharged capacitance of 1.0 µF. Condition A uses input resistance 1.0 MΩ and condition B uses 100 kΩ. These declared construction values explain the public worked answers; the learner recovers the unknown source resistance and capacitance using the supplied reports and independent reference information.

The node equation is C dV/dt=(V_s−V)/R_s−V/R_in. Its final voltage is V_sR_in/(R_s+R_in), and its time constant is (R_s parallel R_in)C. Changing the input resistor therefore changes both the final amplitude and transition rate while the source generator and capacitor stay unchanged. This mathematical example is not a claim that every real recording behaves as one linear mode.

A separate reporting model maps actual node voltage to reported voltage y=b+gV. The construction uses offset b=0.020 V and gain g=2. Independent reference zero has known node voltage 0 V; independent reference cal has known node voltage 2.50 V. These reference voltages are supplied externally to the circuit observations. They identify the reporting map without proving the source/input model or removing its physical loading.

## Data dictionary

[Download the synthetic CSV](https://raw.githubusercontent.com/dylanstechmann/uniStemCourseSimulators/main/content/courses/physics-em/labs/loading-reports.csv). There are 36 rows in twelve groups. `sample` identifies the reference or condition/time group, `condition` is reference, a or b, `time_s` is elapsed seconds for timed circuit rows, `replicate` identifies one of three constructed reports, and `reported_voltage_v` is raw reported voltage in volts.

Reference rows and steady-state rows have an empty time field because they are not finite-time transient observations. Codes ending ss denote the exact model's steady-state limit, not a claim that a measured finite duration is infinite. Every central raw report is rounded to six decimal places. Three variants at −0.002,zero,+0.002 V relative to that rounded value deliberately balance to its mean. These are deterministic demonstration offsets, not independently sampled errors or evidence of a probability distribution.

| Sample | Condition | Time (s) | Mean raw reported voltage (V) |
|---|---|---|---:|
| zero | reference | not a timed row | 0.020000 |
| cal | reference | not a timed row | 5.020000 |
| a00 | a | 0 | 0.020000 |
| a05 | a | 0.05 | 0.789182 |
| a10 | a | 0.1 | 1.232962 |
| a20 | a | 0.2 | 1.636722 |
| ass | a | not a timed row | 1.838182 |
| b00 | b | 0 | 0.020000 |
| b05 | b | 0.05 | 0.652121 |
| b10 | b | 0.1 | 0.884665 |
| b20 | b | 0.2 | 1.001684 |
| bss | b | not a timed row | 1.020000 |

## Work sequence

Open Practice gradebook and select **Virtual lab 1: calibration, loading and observed time constants (ungraded practice)**. Upload exact columns `sample,replicates,mean_reported_v` with all twelve sample codes. The software checks twelve counts and twelve arithmetic means, with 0.005 V tolerance for each mean. It does not automatically grade a written uncertainty budget, a fitted curve, an electrode drawing or a causal explanation.

First summarize raw reports without removing offsets. Determine b from the independently known zero-voltage reference. Calculate g=(mean_cal−b)/2.50 V from the nonzero reference. Convert circuit-group means to actual loaded voltage using V=(mean_y−b)/g. This correction removes the stipulated reporting transformation; the result remains the physical loaded node voltage.

Next use condition A's steady voltage and independently known 1.0 MΩ input resistance to solve R_s=R_in(V_s/V_final−1). The known source step amplitude is part of the supplied information. Without it, one steady amplitude would not determine both source amplitude and resistance uniquely. Use condition B's steady result as a separate consistency check against the same inferred source resistance.

Then use a timed condition B voltage to determine the remaining transition fraction 1−V(t)/V_final. Its logarithm gives τ=−t/ln(remaining). Infer C from τ divided by the parallel resistance R_sR_in/(R_s+R_in). Finally compare the same capacitance against condition A's time-dependent reports. Multiple times provide model-consistency checks rather than a newly demonstrated real noise distribution.

## Worked example

Zero and cal means are 0.020 and 5.020 V. Their independently known voltages give b=0.020 V and g=2. Condition A steady raw mean 1.838182 V calibrates to approximately 0.909091 V, the rounded representation of 10/11. The DC divider gives source resistance approximately 100 kΩ. Condition B steady raw mean 1.020 V calibrates to 0.50 V, consistent with equal source and input resistances.

Condition B's 0.050 s raw mean is 0.652121 V, giving calibrated voltage approximately 0.3160605 V. Relative to final 0.50 V, the remaining fraction is approximately 0.367879. Thus τ≈0.050 s and C≈1.0 µF with effective resistance 50 kΩ. Rounding explains the tiny difference from the exact analytic values. Condition A instead has effective resistance 90.9091 kΩ and τ≈0.090909 s with the same capacitance.

## Interpretation criteria

| Criterion | Evidence to discuss |
|---|---|
| Summary | Twelve groups, three reports each and correct raw means |
| Reference | Independent zero/nonzero voltages used for reporting calibration |
| Loading | Calibrated node amplitude still distinguished from open-circuit source |
| Dynamics | Correct parallel resistance and stated initial state used for τ |
| Consistency | Both conditions agree with one source resistance and capacitance |
| Scope | Synthetic dummy-source result kept separate from actual biology |

The preserved high-impedance recording case asks for electrical explanations and discriminating measurement changes. This lab supplies a mathematical dummy-source control with known inputs. It demonstrates how loading can create a smaller and faster observed trace without a source change. A real source could also change, and reactive electrode behavior or multiple modes could invalidate the simple model. Reference calibration and a good fit are useful conditional evidence, not unique causal identification.

## Limits of this lesson

All reports, references and component values are synthetic. Exact source step, linear components, common reporting gain/offset and ideal steady-state limits are supplied assumptions. Balanced variants establish neither instrument precision nor a real noise law. The lab gives no device-safety certification or human-subject procedure. Original guide and CSV are CC BY 4.0 with substantial AI assistance; no third-party dataset or teaching asset was imported. One data lab is not a laboratory sequence. Workload, accessibility and qualified review remain absent; the package stays partial, unreviewed and formative-only.
