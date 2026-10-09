# Array shapes, broadcasting and memory-aware reductions

**Status:** original formative instruction with substantial AI assistance. Arrays and timings discussed here are synthetic. The aim is to explain how a compact numerical expression can run successfully while subtracting the wrong baseline. Prerequisites are input contracts, loop tracing and the preserved algorithmic-cost lesson.

## Learning objectives

1. Predict the shape and selected values of an elementwise array operation.
2. Distinguish sample and channel reductions, paired differences and outer differences.
3. Estimate array memory and identify aliasing or chunking decisions that preserve meaning.

## Shape is part of the scientific contract

Let a recording matrix have shape (samples, channels). Each row is one time sample and each column is one sensor channel. This interpretation belongs in the function contract and report metadata, rather than being inferred from a plot. A vector of channel baselines has shape (channels,). Subtracting it from the matrix applies each channel's baseline to every sample. A vector of sample corrections has a different meaning even if the number of samples happens to equal the number of channels.

NumPy aligns trailing dimensions when broadcasting. Dimensions are compatible if they match or one is one. For shapes (4,3) and (3,), the trailing three matches and the missing leading dimension behaves as one, giving result (4,3). For (4,3) and (4,), the trailing dimensions three and four conflict. Reshaping the sample vector to (4,1) makes its intended application explicit. These rules determine computational compatibility; they do not determine which correction is scientifically appropriate.

A square array is particularly dangerous. A (3,) vector can broadcast across a (3,3) matrix without an error regardless of whether it contains channel or sample values. The software cannot read the variable's meaning. A miniature nonsquare test with distinct values on both axes exposes many errors that symmetric or constant arrays conceal.

## Reductions discard an axis

For a matrix of samples by channels, `mean(axis=0)` averages samples and returns one value per channel. `mean(axis=1)` averages channels and returns one value per sample. The default scalar mean pools both axes. None of those operations is inherently correct. The intended comparison determines the unit of analysis and the axis to retain.

Missingness changes reductions too. This lesson assumes all selected entries are finite; an actual pipeline needs an explicit missing-value policy and counts for each output. Automatically ignoring missing entries can give different denominators to different channels. A result with the right shape can still compare means based on different observation sets.

The following original example makes the axes visible. It uses a small array so that each number can be checked by hand.

```python
import numpy as np

signal = np.array([[10., 100.], [14., 104.], [18., 108.]])
channel_baseline = np.array([10., 100.])
corrected = signal - channel_baseline
channel_means = corrected.mean(axis=0)
sample_means = corrected.mean(axis=1)
```

The corrected rows are [0,0], [4,4] and [8,8]. Channel means are [4,4], while sample means are [0,4,8]. Both outputs are reasonable summaries of this construction, but they answer different questions. A global mean of four would erase the time trend. Here the channels are intentionally parallel; another fixture with unequal channel increments checks that an implementation has not merely reproduced this special symmetry.

## Pairing is different from an outer operation

For paired baseline [1,2,3] and follow-up [2,4,8], elementwise follow-up minus baseline gives [1,2,5]. The mean paired change is 8/3. Reshaping follow-up to (3,1) and subtracting baseline instead produces a (3,3) grid of every follow-up against every baseline. Its nine entries are not nine independent paired observations. Broadcasting has created comparisons, not new samples.

An outer distance matrix can be intentional, but its storage grows quadratically. An array of 2000 by 3000 float64 entries contains six million numbers at eight bytes each: 48,000,000 bytes, or 48 MB using decimal megabytes. Temporaries, object overhead and inputs add to that cost. Decimal MB and binary MiB are different reporting scales; name the one used.

Chunking an outer calculation can limit peak memory when the final goal is a reduction. For example, retain a running sum and count rather than storing every distance if only the mean is needed. A scientifically equivalent chunked reduction must include each intended comparison once and preserve the denominator. Benchmarking then addresses implementation cost after correctness has been established.

## Worked example

Compare sample corrections [1,2,3] against the same 3-by-2 signal matrix. Convert them to a column and subtract to get [9,99], [12,102] and [15,105]. The overall mean becomes 57. Using channel baselines instead gave overall mean four. These are different operations with different metadata, not competing estimates of one quantity. A shape assertion plus a hand-check of the first and last row can distinguish them.

A slice may share storage with its parent array. If a preprocessing stage needs an independent buffer, an explicit copy avoids changing the raw matrix through a view. Checking that the original signal remains unchanged after transformation provides a behavioral test; merely checking a variable name such as `cleaned` does not prove independence. An advanced-index selection often copies, while basic slicing often returns a view, so the actual operation matters.

## Common mistakes

Treating successful broadcasting as scientific validation, swapping axes, inventing replicate counts from an outer grid, and reporting memory without its unit all mislead. Another mistake is vectorizing first and testing only with equal dimensions. Small rectangular fixtures and preserved raw inputs make silent errors easier to see.

## Limits of this lesson

Examples assume finite float64 arrays and known axis meanings. Distributed arrays, masked data, sparse matrices and hardware performance need further work. The formative items assess shapes, values and design decisions without executing learner code. No performance claim describes actual hardware. The [NumPy broadcasting reference](https://numpy.org/doc/stable/user/basics.broadcasting.html) is link-only; no examples or figures are imported. Original instruction and code are CC BY 4.0, unreviewed, and provide no evidence of a complete programming course.
