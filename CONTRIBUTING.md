# Contributing to Lattice CourseLab

Start with the audit and roadmap. Keep commits focused on one milestone. Preserve identifiers and working content during migration. Every package must state its maturity and limitations honestly; lesson counts alone cannot substantiate completeness.

Teaching and assessments belong in `content/`. Follow [the authoring guide](docs/AUTHORING_GUIDE.md), attach provenance and run validation. Develop experimental interpretation, controls, uncertainty and justified mechanisms. Do not copy paid or unlicensed teaching. Public catalogs inform scope only.

Software changes require relevant tests. Grading changes require alternate correct answers, wrong units, near misses, malformed inputs and misleading keyword responses. Use fixed seeds. Keep solution specifications out of learner DTOs/frontend imports. Use synthetic learner data.

Record passed and failed commands. Human review requires an actual qualified person reviewing a specified version; never invent approval. Do not commit credentials, database passwords, `.env`, learner exports or production assessment secrets. Report vulnerabilities privately as described in SECURITY.md.
