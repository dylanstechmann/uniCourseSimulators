# Virtual lab 1: gain, clipping, common mode and baseline recovery

**Status:** public formative practice with public answers and unlimited retries. Points are study feedback, not a course grade. This is a constructed data-analysis exercise with no hardware operation, subject connection or electrode-procedure change. Prerequisites: finite feedback, differential/common-mode decomposition, filtering and calibration domains.

## Learning objectives

1. Summarize grouped outputs and recover gain/offset only from known unsaturated references.
2. Calculate nominal common-mode rejection and a separately stipulated baseline time scale.
3. Distinguish clipping, drift, model domain and conditional case evidence.

## Construction and independent information

The settled channel model is V_out=clip(0.10+Gv_d+0.010v_c,−1,+1) V, where differential and common-mode inputs are in volts. Low gain uses G=20 and high gain uses G=100. Independently supplied differential references are −15,−5,0,+5,+15 mV. The common-mode range is stipulated valid from −1.5 to +1.5 V. Known common-mode tests use −1 and +1 V at zero differential input and the high-gain condition.

These declared construction parameters explain the public worked examples; the learner uses known inputs and reported outputs to recover selected parameters. They do not identify a real amplifier or interface. The output clamp is a phenomenological static model. It supplies no output-current limit, dynamic saturation recovery, internal stage headroom or component recommendation.

For a separate drifting condition, differential and common-mode inputs are both zero, while the baseline is b(t)=0.10+0.30exp(−t/0.50) V. Its time points are 0,0.50,1.0 and 2.0 s. The final baseline 0.10 V is independently supplied. This condition is deliberately distinct from the settled calibration sweep, so its reports must not be pooled as though they shared an unchanged offset.

## Report construction and data dictionary

[Download the synthetic CSV](https://raw.githubusercontent.com/dylanstechmann/uniStemCourseSimulators/main/content/courses/circuits/labs/channel-reports.csv). There are 48 rows in sixteen groups. `sample` identifies a group; `condition` is low, high, common or drift; `input_diff_mv` is the supplied differential reference in millivolts; `input_common_v` is its common-mode reference in volts; `time_s` is elapsed time for drift rows; `replicate` labels one of three constructed outputs; and `reported_output_v` is the observed model output in volts.

Each internal prediction has deterministic perturbations −0.001,zero,+0.001 V added before clipping. The resulting outputs are rounded to six decimals. Unsaturated groups balance around their rounded central output. The two high-gain endpoint groups have all three outputs clamped at the same rail because their internal predictions remain beyond it even after the perturbations. These are not independently sampled errors or evidence of Gaussian noise or instrument precision.

Settled gain and common-mode rows have empty time fields because they are not part of the transient sequence. Their absence is a declared condition, not a missing elapsed-time observation. Drift rows use the same numeric zero-input references with a different baseline state. Maintaining this distinction is part of the interpretation task.

| Sample | Condition | Differential (mV) | Common mode (V) | Time (s) | Mean output (V) |
|---|---|---:|---:|---|---:|
| low_m15 | low | −15 | 0 | settled | −0.200000 |
| low_m5 | low | −5 | 0 | settled | 0.000000 |
| low_0 | low | 0 | 0 | settled | 0.100000 |
| low_p5 | low | 5 | 0 | settled | 0.200000 |
| low_p15 | low | 15 | 0 | settled | 0.400000 |
| high_m15 | high | −15 | 0 | settled | −1.000000 |
| high_m5 | high | −5 | 0 | settled | −0.400000 |
| high_0 | high | 0 | 0 | settled | 0.100000 |
| high_p5 | high | 5 | 0 | settled | 0.600000 |
| high_p15 | high | 15 | 0 | settled | 1.000000 |
| cm_m1 | common | 0 | −1 | settled | 0.090000 |
| cm_p1 | common | 0 | 1 | settled | 0.110000 |
| drift_0 | drift | 0 | 0 | 0 | 0.400000 |
| drift_05 | drift | 0 | 0 | 0.5 | 0.210364 |
| drift_1 | drift | 0 | 0 | 1 | 0.140601 |
| drift_2 | drift | 0 | 0 | 2 | 0.105495 |

## Work sequence

Open Practice gradebook and select **Virtual lab 1: gain, clipping, common mode and baseline recovery (ungraded practice)**. Upload exact columns `sample,replicates,mean_output_v` with all sixteen sample codes. The software checks sixteen counts and sixteen arithmetic means, with 0.005 V tolerance for each mean. It does not automatically assess a written diagnosis, waveform shape, fitted curve or uncertainty budget.

First summarize every raw output group, preserving rail plateaus. Calculate low gain from its −5 and +5 mV reference difference. For high gain, use the corresponding interior points and the zero input to recover slope and intercept. Check the ±15 mV predictions against the declared rails before deciding whether those points belong in a linear calibration fit.

Next calculate common-mode coefficient from the output difference between known −1 and +1 V inputs. Divide differential gain by that coefficient and use 20log₁₀ for amplitude CMRR. This nominal calculation relies on the stipulated input-range validity and settled offset. It establishes neither frequency-dependent rejection nor a real instrument's worst-case specification.

Finally subtract the independently supplied 0.10 V final baseline from each drifting report. Normalize excess by its initial 0.30 V and infer τ from the negative time divided by the remaining-excess logarithm. Use the other drift times as consistency checks. The finite report rounding causes small differences from the exact construction, rather than evidence of an additional physical mode.

## Worked example

Low-gain means 0.00 and 0.20 V across a 0.010 V differential span give gain 20. High-gain interior means −0.40 and +0.60 V give gain 100, with zero-input mean 0.10 V. At ±15 mV, high-gain internal values −1.40 and +1.60 V clamp to −1 and +1. Low gain remains unsaturated from −0.20 to +0.40 V over the whole supplied sweep.

The settled common-mode means are 0.09 and 0.11 V, giving coefficient 0.010 and nominal CMRR 80 dB. The drifting mean at 0.50 s is 0.210364 V; subtracting 0.10 and dividing by initial excess 0.30 gives approximately exp(−1), hence τ≈0.50 s. Applying a logarithm directly to the raw baseline would describe the wrong model.

## Fit domain and interpretation criteria

| Criterion | Evidence to discuss |
|---|---|
| Summary | Sixteen groups, three reports each and correct means |
| Calibration | Known unsaturated references selected for affine fitting |
| Range | Offset-dependent −11/+9 mV headroom distinguished from symmetric rails |
| Common mode | Separate reference difference and valid input-range assumption |
| Drift | Final baseline removed before normalized decay |
| Case scope | Electrical explanations compared without unique real mechanism claims |

An ordinary all-point high-gain line gives slope 70 and intercept 0.06 V, because clipped endpoints violate the affine domain. More calibration points are useful only when their model conditions are appropriate. The preserved movement-clipping/rest-drift case can use these synthetic controls to discuss separate gain/range, interface/bias-return and state/recovery hypotheses. It remains a self-assessment discussion, not a scored clinical diagnosis or a real bench protocol.

## Limits of this lesson

Every input, gain, clamp, baseline and report is synthetic. Known references and a valid input range are supplied assumptions. Deterministic variants establish no real noise law, uncertainty interval or recovery specification. A clipping plateau does not reveal the original larger amplitude, and an exponential does not uniquely identify an electrode mechanism. Original guide and CSV are CC BY 4.0 with substantial AI assistance; no third-party teaching asset or dataset was copied. One data lab is not a laboratory sequence. Qualified review, accessibility review and measured workload remain absent; the course stays partial, unreviewed and formative-only.
