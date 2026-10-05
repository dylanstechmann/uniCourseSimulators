# Autograder design

## Current boundary

The static reader exposes practice answers and has no secure grade record. The backend milestone covers existing choice/numeric formative practice on the server. That foundation is not the complete requested modular grading system.

## Grade authority

Implemented immutable attempts record learner, course/question IDs, course version, grader-policy version, response, score, diagnosis, time and a SHA-256 digest of the resolved authored question specification plus grader-policy version and selected variant ID. Alembic migration 0002 leaves historical attempts unpinned (`question_spec_sha256=null`) while new attempts record a digest. The digest is server-side only and omitted from learner attempt DTOs because hashes of answer-bearing specifications could be guessed offline. A digest verifies equality; it cannot reconstruct a retired specification without an immutable package archive. Authored formative variants use a server-signed, seven-day token containing a random seed; a keyed HMAC selects the same authored form on replay. Tokens bind course, package version and question ID. Current implementation selects among finite, explicitly written forms; it does not generate numeric parameter variants. Deterministic grading or explicit analytic rubrics determine scores. A correct value/selection cannot alone establish sound reasoning. Self-assessment and provisional design feedback are separate from grades.

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

Future generated parameter variants must recompute reproducible specifications and pass independent recalculation tests. Current authored alternatives must have unique IDs, validate as complete standalone questions after overrides, and have distinct non-placeholder prompts. Overrides append actor/reason/time audit events and retain original attempts. Weights and release policies are explicit. Legacy packages offer practice evidence only, not semester grades.

## Feedback providers: planned

Deterministic no-LLM mode is default. Optional OpenAI-compatible, Anthropic, OpenRouter-compatible and Ollama providers may elaborate feedback without score changes. Require criteria, response evidence, missing/incorrect concepts, confidence, provisional AI label and manual-review request. Keys never reach browsers/logs. No provider production readiness is asserted without tests.

Adversarial tests cover alternate forms, wrong units, near misses, invalid concepts, malformed inputs, injection/solution requests, keyword repetition and malicious/infinite code. Mutation tests must fail broken rules. Code safety checks require the actual runner, not a mock claiming isolation.

## Enabled implementation

The deterministic grader supports single-choice, multiple-select and Decimal-based finite numeric checks with authored absolute tolerance. Multiple-select answers define either all-or-nothing or the clamped equal-share rule: score = points × max(0, correct selected − incorrect selected) / number of keyed correct choices. Learners see the policy before submitting. Empty, repeated, non-integer, out-of-range and unsupported-policy responses fail closed. This rule is transparent but is not a validated universal grading policy.

For numeric items, deterministic conversion uses an intentionally constrained parser and explicit unit table. It supports common SI and biology units, liter and molar concentration units, selected derived SI units, products, quotients, parentheses, and bounded integer powers. For example, `μmol/min`, `mmol/(L·h)`, `m/s²`, `N`, and `kJ/mol` are parsed into SI scale and seven base dimensions. Micro-symbol variants normalize; SI symbol/prefix case remains significant (`mV` differs from `MV`, `ms` from `mS`). An answer is converted into the authored unit before applying that unit's absolute tolerance. Optional dimension exponents can be authored using the seven documented bases and are checked against the unit expression. A conflicting inline and unit-field answer is rejected unless the expressions are equivalent. When unit entry is optional and absent, the learner's number is interpreted in the authored unit, retaining the prototype's explicitly disclosed legacy policy.

This is not a general-purpose unit library. Contextual labels (`pH`, assay `units`, and `mol ATP`) are retained as exact-label-only quantities: they cannot be combined with other units or converted to another label. Unknown symbols and affine temperature units fail closed; an unsupported authored unit disables grading with an explicit error, and an unsupported learner unit gets no credit. The question schema bounds authored dimensions. Relative tolerance combines with absolute tolerance by `allowed_error = absolute_tolerance + relative_tolerance × |authored_answer|` after converting into the authored unit; relative tolerance is bounded from 0 through 1 and remains well-defined for a zero answer. Optional significant-figure requirements are bounded to 1–12 and are checked only after the numeric value is within tolerance. The count follows lexical decimal notation: leading zeros do not count, trailing decimal zeros do, exponent digits do not, and trailing zeros in an integer without a decimal point are ambiguous and therefore do not count (`80` = 1; `80.` = 2; `8.0e1` = 2). The UI states the requirement and explains how to express precision. Grader v5 pins this policy; historical attempts retain their recorded grader version.

The API records immutable attempts; tests verify owner isolation, malformed/injection input, near misses, alternate exponent forms, wrong units, no score mutation and no code-execution route. Learner gradebooks aggregate best formative checks and objective evidence for the current enrolled course version. Repeated attempts increase the attempt count but not distinct-item coverage; objective points use the best score once per tagged question. A provisional practice-mastery indicator requires at least three distinct tagged items, at least 80% of the objective's tagged items attempted, and at least 80% of possible points on attempted items. The API returns these thresholds and the policy version so the learner can interpret the result. This is explicitly a study signal: short formative checks do not establish reasoning, transfer, course mastery, credit, or course completion. Objectives with fewer than three authored questions cannot reach the provisional state. Previous-version attempts remain in history but do not enter the new version's aggregate. Feedback remains deterministic and unreleased solutions/specifications remain withheld. The disabled runner/provider interfaces are extension points, not implemented isolated execution or LLM integrations.
