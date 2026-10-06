# Assessment and study tools

The current application serves lesson and course-level formative practice from the FastAPI backend. Learners can use guest sessions or accounts; enrollment pins a package version; attempts and feedback persist in PostgreSQL. The practice gradebook reports formative evidence only. No current course offers a weighted grade, credit, or a summative exam.

## Formative practice

Lesson items and course-level practice sets use deterministic grading with answer specifications held server-side and learner responses checked against explicit rubric fields. The learner API returns a whitelisted question view; it does not return grader solutions. The authoring bank in the public repository is explicitly marked `public-practice-authoring`, so its keys are visible in source. These public practice keys are not protected exam materials and are never used to represent a summative assessment.

Week 8 of Foundations of Cell and Molecular Biology includes a 12-item cumulative practice rehearsal over weeks 1–7. The UI labels it ungraded and not a midterm. Items submit individually, show immediate practice feedback, and persist like other practice attempts. The endpoint checks the enrollment-pinned source digest and only serves IDs explicitly listed in a `mode: practice`, `type: practice` manifest activity backed by `question-banks/practice.json`. It refuses other sources and does not return `solution_spec` or answer feedback.

Numerical items can require units, tolerances, dimensions, and significant figures. Structured items are composed of separately scored fields; they do not grade unrestricted prose. File-upload checks parse small UTF-8 CSV data as data and never execute it. Authored variants use signed, short-lived tokens bound to course, version, and question. The production graded-assignment route is separate: it uses version-pinned private sources, deadlines and attempt policies, and answer-free learner views. No shipped course currently uses that graded route.

The course case studio remains a self-assessed design task rather than an automatically graded response. Experimental reasoning, causal claims, and design tradeoffs require more than string matching.

## Study support

- **Retrieval cards:** cards appear with developed lessons; learners can use them for self-assessment. The current reader does not yet persist a spaced-review queue.
- **Notes and bookmarks:** server-backed learner notes and course bookmarks can be exported or deleted with account data.
- **Progress:** marked reading state is stored separately from quiz scores and does not certify mastery.
- **Legacy calculators:** dilution, buffer, enzyme-kinetics, RC, diffusion-timescale, and Ohm's-law tools remain under `legacy/` and are not yet integrated into the React course reader.

## Authoring and validation checklist

When adding a course or changing a problem:

1. State a prerequisite and measurable outcome that the item practices.
2. Define the system boundary, sign convention, units, and approximations in numerical problems.
3. Recalculate the answer independently; include a tolerance suitable for rounding, not a tolerance that hides a modeling error.
4. Make the hint point to a method and the explanation show the reasoning, not only the answer.
5. For biology or engineering cases, ask learners to distinguish a measurable result from a causal, functional, or translational conclusion.
6. Cite public comparators and write original notes and questions rather than importing restricted course text or answer keys.

## Current limitations

The curriculum remains incomplete: all catalog packages are partial or planning-only, and no course passes the project's complete-course gate. There is no protected exam-key repository, timed exam mode, independent reviewer sign-off, full mastery model, general code-execution sandbox, collaborative annotation, or laboratory safety supervision. Practice indicators do not establish learning transfer, university equivalency, credit, or course completion. Specialized experimental activities require qualified review before formal instructional use.
