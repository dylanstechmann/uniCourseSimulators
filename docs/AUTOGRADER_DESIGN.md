# Autograder design

## Current boundary

The static reader exposes practice answers and has no secure grade record. The first backend milestone will cover existing choice/numeric practice. That foundation is not the complete requested modular grading system.

## Grade authority

Immutable attempts record learner, course/question version, seed, response, specification version, points, diagnosis and time. Deterministic grading or explicit analytic rubrics determine scores. A correct value/selection cannot alone establish sound reasoning. Self-assessment and provisional design feedback are separate from grades.

Layer feedback as diagnosis, targeted hint, misconception, next step, policy-controlled solution, exact lesson/source links. Planned diagnoses distinguish arithmetic, units/dimensions, misapplied equations, unsupported biology, correlation/causation, missing controls, overgeneralization, weak reasoning and promising incomplete approaches. Reasoning claims need response evidence.

## Planned plugins

| Plugin | Required behavior |
| --- | --- |
| Choice/multiple select | Explicit shape and partial-credit policy |
| Numeric | Unit conversion/dimensions, tolerance, significant figures, independent recalculation |
| Symbolic | Bounded SymPy parsing, equivalence/domain assumptions |
| Structured concepts | Evidence-linked rubric; reject keyword-only responses |
| Graph/table/data | Schema/numeric checks, uncertainty and interpretation |
| CSV upload | Size/column/type checks, safe parsing, no executable files |
| Code | Separate isolated worker using pytest; never API execution |
| Design | Transparent provisional rubric, manual review/appeal |

Seeded variants must recompute reproducible specifications. Overrides append actor/reason/time audit events and retain original attempts. Weights and release policies are explicit. Legacy packages offer practice evidence only, not semester grades.

## Feedback providers: planned

Deterministic no-LLM mode is default. Optional OpenAI-compatible, Anthropic, OpenRouter-compatible and Ollama providers may elaborate feedback without score changes. Require criteria, response evidence, missing/incorrect concepts, confidence, provisional AI label and manual-review request. Keys never reach browsers/logs. No provider production readiness is asserted without tests.

Adversarial tests cover alternate forms, wrong units, near misses, invalid concepts, malformed inputs, injection/solution requests, keyword repetition and malicious/infinite code. Mutation tests must fail broken rules. Code safety checks require the actual runner, not a mock claiming isolation.
