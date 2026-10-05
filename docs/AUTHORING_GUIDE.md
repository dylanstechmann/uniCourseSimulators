# Course authoring

Use `content/courses/<id>/course.json`, `syllabus.md`, `modules/`, `question-banks/`, cards and rubrics. JSON Schemas are the normative field contracts; the validator adds cross-file and maturity gates.

Use stable IDs and acyclic dependencies. Separate assumed knowledge from required CourseLab packages. Objectives describe observable performance with Bloom levels: interpret perturbations, compare controls, calculate transport or justify a mechanism with uncertainty.

Manifest fields support workload/duration, prerequisites, outcomes, lessons, assignments/labs/exams/projects, grading, accessibility, sources, history, review and omissions. Map each assessed objective to questions/rubrics. Specifications are authoring data and must not be imported by frontend code.

Symbolic formative items use `type: symbolic` with a plain-string `expression`, a unique list of declared `variables`, and an `assumptions` map from declared names to boolean flags. The supported evaluator accepts rational arithmetic only: use `2*x`, parentheses, and integer powers such as `x^2`; do not author function calls or arbitrary SymPy syntax. Keep each item inside the documented expression limits in [AUTOGRADER_DESIGN.md](AUTOGRADER_DESIGN.md), link its objective and lesson, and test equivalent forms and near misses. The calculus seed item demonstrates this narrow plugin; it does not imply symbolic grading coverage for arbitrary courses.

Develop explanation, assumptions, worked reasoning, misconceptions, limitations and practice. Provide text equivalents for diagrams, meaningful headings, accessible tables, plain-text units and evidence-explaining captions. Register assets before reuse. Linking is not redistribution permission.

For a formative question with authored alternatives, add `randomization` with `seeded: true`, `generator_id: authored-variants-v1`, and at least one `variants` entry. The unmodified question is the `base` form. Each alternative needs a stable unique `id`, a distinct substantive `prompt`, a complete `solution_spec`, and targeted `feedback`; it may override `options` when the response type uses them. Keep course objectives, points, and other shared metadata on the parent question. The validator merges each alternative with those shared fields and validates every resolved specification against the question schema. Do not include protected exam keys in public content. The learner DTO receives only the selected prompt/options and a signed seven-day token; the token is tied to the course version and question, not an answer key. The attempt records the selected variant ID and digest so later review can identify what was graded.

Audited preserved seeds have an explicit brevity exception while partial. Newly authored placeholders, duplicated readings/questions and trivial teaching are rejected. Do not add filler to pass counts.

Complete promotion requires all quality gates, independent numerical checks, accessibility, current source links and actual human review. External review requires a named qualified person and specified version. Workload estimates must not imply credit equivalence.
