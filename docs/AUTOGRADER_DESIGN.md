# Autograder design

## Current boundary

The static reader exposes practice answers and has no secure grade record. The backend milestone covers existing choice/numeric formative practice on the server. That foundation is not the complete requested modular grading system.

## Grade authority

Implemented immutable attempts record learner, course/question IDs, course version, grader-policy version, response, score, diagnosis, time and a SHA-256 digest of the exact authored question specification plus grader-policy version. Alembic migration 0002 leaves historical attempts unpinned (`question_spec_sha256=null`) while new attempts record a digest. The digest is server-side only and omitted from learner attempt DTOs because hashes of answer-bearing specifications could be guessed offline. A digest verifies equality; it cannot reconstruct a retired specification without an immutable package archive. Randomized variant seeds are not implemented. Deterministic grading or explicit analytic rubrics determine scores. A correct value/selection cannot alone establish sound reasoning. Self-assessment and provisional design feedback are separate from grades.

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

## Enabled implementation

The deterministic grader supports single-choice, multiple-select and Decimal-based finite numeric checks with authored absolute tolerance. Multiple-select answers define either all-or-nothing or the clamped equal-share rule: score = points × max(0, correct selected − incorrect selected) / number of keyed correct choices. Learners see the policy before submitting. Empty, repeated, non-integer, out-of-range and unsupported-policy responses fail closed. This rule is transparent but is not a validated universal grading policy.

For numeric items, SI symbol/prefix case is preserved (mV differs from MV; ms from mS), micro-symbol variants normalize, and conflicting value-field/unit-field text is rejected. Legacy optional unit-entry policy is retained in the authoring data; the frontend requests an explicit unit. This is not dimensional conversion. Unsupported type, restricted visibility, relative tolerance, randomization, dimensional and significant-figure specifications cannot silently receive scores.

The API records immutable attempts; tests verify owner isolation, malformed/injection input, near misses, alternate exponent forms, wrong units, no score mutation and no code-execution route. Learner gradebooks aggregate best formative checks and evidence counts for the current enrolled course version without mastery claims. Previous-version attempts remain in history but do not enter the new version's aggregate. Feedback remains deterministic and unreleased solutions/specifications remain withheld. The disabled runner/provider interfaces are extension points, not implemented isolated execution or LLM integrations.
