# Signals, Systems & Feedback Control

**Maturity: partial. Version: 0.4.0.**

Continuous and discrete signals, linear systems, frequency response, feedback, stability, and controller design for sensors, actuators, and biological regulation.

## Prerequisites

Differential Equations; Linear Algebra; Circuits recommended. Structured required, recommended, and concurrent relationships appear in the manifest and remain subject to author review. This package establishes no university prerequisite equivalency.

## Authored outcomes

- Model systems with transfer functions or state space.
- Interpret poles, zeros, and frequency response.
- Evaluate closed-loop stability and tracking.
- Tune feedback with attention to noise, saturation, and uncertainty.

## Proposed 14-week schedule

This is a proposed scope, not a measured or reviewed semester. Each week lists its readings; the four short prototype readings (about 65 to 75 words each) sit in weeks 1, 4, 8 and 12 beside the original lessons, and every lesson has public formative items and retrieval cards.

| Week | Theme | Readings |
|---|---|---|
| 1 | LTI systems, convolution and transfer functions | LTI systems, convolution, and transfer functions |
| 2 | Convolution and impulse response: why a sensor blurs and delays what it measures | Convolution and impulse response: why a sensor blurs and delays what it measures |
| 3 | From a transfer function to a time response: poles, zeros and the final value | From a transfer function to a time response: Laplace transforms, poles, zeros and the final value |
| 4 | Frequency response and filtering | Frequency response and filtering |
| 5 | Second-order systems: damping, overshoot and ringing | Second-order systems: damping, overshoot and ringing in a pressure transducer |
| 6 | Reading Bode plots: decibels, phase and the cost of a delay | Reading Bode plots: gain in decibels, phase, corner frequencies and the cost of a delay |
| 7 | Proportional control of an incubator: steady-state error and saturation | Holding a culture at 37 °C: first-order plants, proportional control, steady-state error and saturation |
| 8 | Feedback, stability and robustness | Feedback, stability, and robustness |
| 9 | Stability margins: gain, phase and delay margins | Stability margins: gain margin, phase margin and how much delay a loop can take |
| 10 | PI control, tuning and integrator windup | PI control, tuning and integrator windup: removing steady-state error without losing the margin |
| 11 | Virtual lab: identifying an incubator from step tests and checking a PI design | Virtual lab 1: identifying an incubator from step tests and checking a PI design |
| 12 | Controller design and sampled implementation | Controller design and sampled implementation |
| 13 | Sampling, aliasing and a discrete-time PI controller | Sampling, aliasing and a discrete-time PI controller |
| 14 | When a sensor filter makes a fast loop oscillate: phase lag, crossover and a safe retuning sequence | When a sensor filter makes a fast loop oscillate: phase lag, crossover and a safe retuning sequence |

## Assessment and study policy

Every lesson has public formative items (numeric, single-choice, multiple-select, data-interpretation, structured-response and CSV-upload) mapped to its objectives, plus retrieval cards for the review queue; each practice assessment also lists the course outcomes its items assess. Week 11 is a synthetic-data virtual lab and week 14 pairs a retuning lesson with the course case and its self-assessment checklist. These are practice activities with unlimited retries and no institutional grade, university credit or transferable credit. Workload has not been measured.

## Current limitations

The schedule above is proposed, not measured, and has not been reviewed by a qualified instructor. There are no graded homework sets, midterm, final or graded project. The four prototype readings remain short. The package cites no new papers: the lessons teach standard methods with synthetic data, and the typical values they quote (tuning rules, margin targets, damping ratios, sampling rules of thumb) are textbook-level and vary between sources. All plants, signals, controllers and numbers are synthetic; no lesson gives controller settings, a safety procedure or a test protocol for any real device, and nothing here says anything about any real incubator, instrument or process. Qualified human review is required before this course could meet the complete-course standard.

## Sources and licensing

Read source-map.json for module provenance and content/SOURCES_AND_LICENSES.md for the software/content license boundary. Listed source courses are public curriculum comparators; no affiliation or equivalency is implied.
