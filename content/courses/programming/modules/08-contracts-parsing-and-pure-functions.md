# Input contracts, parsing and pure scientific functions

**Status:** original formative instruction with substantial AI assistance. Every record and numerical parameter below is synthetic. This lesson extends the compact data-structures reading by turning an informal calculation into an explicit, testable interface. No learner code is executed by the course server.

## Learning objectives

1. Trace a small function through valid inputs, conversions and its return value.
2. Classify malformed, missing and nonfinite inputs using a stated contract.
3. Separate parsing, scientific calculation and report production without mutating raw records.

## The contract comes before the implementation

A scientific function needs more than a descriptive name. Its contract states what its arguments represent, which units they use, which values are allowed, what it returns and how failure is communicated. For a concentration derived from a synthetic mass measurement, define concentration_mg_per_ml(mass_mg, volume_ml). Both arguments must be finite real numbers; mass is nonnegative and volume is strictly positive. The result is mass divided by volume in mg/mL. A blank string is not a measured zero, and infinity is not a very large valid observation.

This domain reflects this exercise, rather than a universal rule about laboratory records. Some instruments report negative blank-corrected signals. Such a signal would need a different contract, with its meaning and conversion documented. Rejecting an observation and declaring a phenomenon physically impossible are different decisions. Good software makes the selected rule visible so that it can be evaluated and changed intentionally.

The following original implementation checks its domain before division. Python booleans are rejected even though they behave like integers in several numeric operations. This makes accidental flags harder to treat as measurements. The function accepts Python integers and floats only; supporting Decimal, array scalars or quantities would require another explicit interface.

```python
import math

def concentration_mg_per_ml(mass_mg, volume_ml):
    for value in (mass_mg, volume_ml):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("expected a Python real measurement")
        if not math.isfinite(value):
            raise ValueError("measurement must be finite")
    if mass_mg < 0 or volume_ml <= 0:
        raise ValueError("outside concentration domain")
    result = mass_mg / volume_ml
    if not math.isfinite(result):
        raise ValueError("result exceeds supported numeric range")
    return result
```

These checks do not establish measurement accuracy. They establish a predictable computational domain. A valid concentration can still be biased by a faulty balance, incorrect volume metadata or the wrong unit label. Testing division cannot validate the experimental system.

## Parsing is a separate boundary

A CSV reader normally supplies strings, so a parsing stage must distinguish an absent token from a number. It can strip surrounding whitespace, reject a blank field and then attempt numeric conversion. Tokens such as `nan` can convert successfully to floats, which is why conversion success is followed by a finite-value check. Catch the expected conversion error and attach the row identifier. Do not catch every exception and silently substitute zero: that would erase both missingness and programming failures.

Preserve the original token beside the parsed value in an audit record. For this example, a raw volume of `500` with unit `uL` becomes 0.500 mL by division by 1000. A volume of `0.500` with unit `mL` already has the desired scale. Unknown unit labels are quarantined rather than guessed. Unit conversion happens once at the boundary, and the computational function receives values in the units promised by its name.

Separate three stages: parse and validate a record; calculate using a pure function; serialize a report. A pure function returns a value based on its arguments without altering the original record, reading another file or choosing a global calibration invisibly. It can be called twice with the same inputs and checked against the same result. File access and timestamps belong in the surrounding pipeline, where they can be inspected independently.

## Worked example

A synthetic record reports mass 1.5 mg and volume 500 uL. Convert volume to 0.5 mL, then calculate 1.5/0.5=3 mg/mL. The equivalent record in mL must give the same answer. Scaling both mass and volume by two gives 3/1=3 mg/mL, another invariant. Scaling only mass by two doubles the result; these are useful tests because they check the meaning of the calculation rather than copying its internal statements.

Suppose a six-row file has two valid records, one blank mass, one zero volume, one `nan` mass and one unknown unit. The declared policy accepts two rows and quarantines four with distinct reasons. Computing a mean requires reporting both the accepted count and the exclusions. A report that says only “mean concentration 3” hides whether that value came from two observations or all six. Its denominator is part of the evidence.

For a separate synthetic calibration, convert a reading of 2.4 arbitrary units using baseline 0.4 and scale 2 arbitrary units per mg/mL. The corrected concentration is (2.4−0.4)/2=1 mg/mL. Applying this correction before parsing, or forgetting the baseline, changes the scientific meaning even if the code runs without exceptions.

## Common mistakes

Treating a missing token as zero changes the data. Mutating a raw dictionary in place makes later stages depend on call order. Dividing before checking volume can produce an exception without useful row context. Accepting every successful float conversion admits nonfinite values. Repeating unit conversion in two stages produces a thousand-fold error. Recording only a cleaned file without exclusion reasons prevents reconstruction of the selected observations.

## Limits of this lesson

This is a small Python contract, not a general type system or a validated laboratory pipeline. Huge integers, decimal rounding, arrays, file encodings and physical quantity libraries require additional design. Selected choice questions assess tracing and decisions; numeric answers assess stated calculations. They do not execute or grade a learner's implementation, error handling or written explanation. Qualified code and subject review remain absent. The official [Python CSV documentation](https://docs.python.org/3/library/csv.html) is a link-only reference for reader behavior; its examples are not imported. The original function and synthetic records are CC BY 4.0 instructional content.
