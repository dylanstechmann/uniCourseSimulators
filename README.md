# Lattice CourseLab

Interactive, source-grounded courses across science, mathematics, engineering, computing, and biomedicine.

An independent open-source learning platform under development. It does **not confer academic credit**, accreditation, degrees, or university prerequisite equivalency. Pathway mappings do not establish admission eligibility or transfer credit. Institutional references identify scope comparators; they do not imply affiliation or endorsement.

## Current course maturity

| Status | Packages | Meaning |
| --- | ---: | --- |
| catalog-only | 0 | Catalog metadata only |
| outlined | 0 | Structured plan without developed teaching |
| partial | 25 | Prototype packages with short readings and formative checks; depth varies |
| beta | 0 | Developed course awaiting required review/gates |
| complete | 0 | All full-course gates satisfied |
| externally reviewed | 0 | Qualified named reviewer examined a specified version |

**No current package meets the complete-course standard.** The 101 short lesson seeds, 103 formative questions, 202 cards and 25 self-assessed cases are useful practice material. They are not semester courses. Foundations of Cell and Molecular Biology remains partial; its requested 14-week vertical slice is planned. No instructor review is fabricated.

The curriculum map adds **37 catalog-only subject nodes** and **8 pathway maps** beside the 25 partial course packages. Catalog-only entries describe planned study areas and dependencies; they contain no authored lessons and cannot be enrolled in. Mapped prerequisite order is planning guidance and does not establish university equivalency.

See [the audit](docs/CURRENT_STATE_AUDIT.md), [quality standard](docs/CONTENT_QUALITY_STANDARD.md), and [remaining work](docs/ROADMAP.md).

## Package inventory

| Course | Domain | Status |
| --- | --- | --- |
| [Biochemistry I: Proteins, Enzymes & Metabolism](content/courses/biochemistry/course.json) | Biochemistry | partial |
| [Biomaterials & Tissue Engineering](content/courses/biomaterials/course.json) | Bioengineering | partial |
| [Bioreactors & Tissue Culture Engineering](content/courses/bioreactors/course.json) | Bioengineering | partial |
| [Calculus I: Differential and Integral Calculus](content/courses/calculus-1/course.json) | Mathematics | partial |
| [Calculus II: Integration, Series & Applications](content/courses/calculus-2/course.json) | Mathematics | partial |
| [Calculus III: Multivariable & Vector Calculus](content/courses/calculus-3/course.json) | Mathematics | partial |
| [Foundations of Cell and Molecular Biology](content/courses/cell-biology/course.json) | Life sciences | partial |
| [Cellular Biomechanics & Mechanobiology](content/courses/cellular-biomechanics/course.json) | Bioengineering | partial |
| [Electrical Circuits & Instrumentation](content/courses/circuits/course.json) | Electrical engineering | partial |
| [Differential Equations for Living & Engineered Systems](content/courses/differential-equations/course.json) | Mathematics | partial |
| [General Chemistry I](content/courses/general-chemistry-1/course.json) | Chemistry | partial |
| [General Chemistry II](content/courses/general-chemistry-2/course.json) | Chemistry | partial |
| [Genetics & Genomics](content/courses/genetics/course.json) | Life sciences | partial |
| [Geroscience & Regenerative Biology](content/courses/geroscience/course.json) | Life sciences | partial |
| [Linear Algebra for Modeling & Robotics](content/courses/linear-algebra/course.json) | Mathematics | partial |
| [Organic Chemistry I for Life Sciences](content/courses/organic-chemistry/course.json) | Chemistry | partial |
| [Physics: Electricity & Magnetism](content/courses/physics-em/course.json) | Physics | partial |
| [Physics: Mechanics for Biomedical Engineers](content/courses/physics-mechanics/course.json) | Physics | partial |
| [Human Physiology for Engineers](content/courses/physiology/course.json) | Life sciences | partial |
| [Programming & Numerical Methods for Bioengineering](content/courses/programming/course.json) | Computing | partial |
| [Robotics & Mechatronics](content/courses/robotics/course.json) | Mechanical engineering | partial |
| [Signals, Systems & Feedback Control](content/courses/signals-control/course.json) | Electrical engineering | partial |
| [Statics & Mechanics of Materials](content/courses/statics-materials/course.json) | Mechanical engineering | partial |
| [Probability, Biostatistics & Experimental Design](content/courses/statistics/course.json) | Quantitative methods | partial |
| [Thermodynamics & Transport in Bioengineering](content/courses/transport/course.json) | Bioengineering | partial |

## Run locally

Install Docker with Compose, then from the repository root:

```sh
docker compose up --build
```

Open http://localhost:8080. Startup generates a database credential in a private Docker volume, starts PostgreSQL, applies Alembic migrations and serves the React reader through a same-origin API proxy. No API key, database password, cloud account or `.env` is required for development. `.env.example` documents optional settings. Ports bind to localhost; HTTP cookies are a development setting. Production needs HTTPS and operator-supplied secrets.

## Tested learning system

- React/TypeScript reader with public catalog, explicit maturity/limitations, syllabus, lesson objectives and prerequisite lists.
- FastAPI/Pydantic with PostgreSQL SQLAlchemy/Alembic, server guest sessions, account registration/login/logout and guest-to-account preservation.
- Enrollment, notes, bookmarks and learner-marked reading progress stored on the server; lesson pages include self-assessment retrieval cards with revealable answers.
- Immutable choice, numeric, symbolic, and one composite data-interpretation **formative practice** attempt with diagnosis, hints, next steps, lesson links, and independent field scores. The data item gives separate points for a unit-aware calculation and an evidence-bounded choice; it does not grade free-form reasoning. Correct results do not establish sound reasoning or mastery.
- Practice gradebook, attempt/feedback history and an objective-level study indicator based on distinct items, published thresholds and best reviewed formative scores. Learners can request one human review per attempt; allowlisted instructors can adjust practice scores while the automatic result stays immutable. It does not certify mastery or calculate weighted semester grades.
- Learner JSON export and confirmed account deletion, keyboard focus/skip link, larger text/high-contrast controls and safe Markdown rendering.
- Docker development/production examples, reverse proxy, CI and automated content/security-boundary tests.

Single-choice, multiple-select, numeric, bounded symbolic-expression, and one narrow data-interpretation formative grader are enabled. Numeric grading supports a constrained set of exact unit conversions, dimensional checks, absolute and relative tolerances, and optional significant-figure requirements. Symbolic grading compares algebraically equivalent rational expressions through a restricted arithmetic grammar; it does not execute Python or accept arbitrary SymPy syntax. Multiple-select policies are explicit and show learners their partial-credit formula; the composite data item displays per-field credit and never grades prose or keyword overlap. New attempts pin a SHA-256 question-specification digest. Numeric parameter generation, general graph/table/data rubrics, upload assignments, protected exams, weighted course grading and full human grading remain unfinished milestone 3 work. Human appeal review is available for current-version formative attempts when an operator configures the instructor email allowlist; it does not make public practice questions secure. Course-version changes prompt learners to update enrollment while preserving historical attempts. Unsupported specifications fail explicitly. Code execution and LLM providers are disabled. The eight pathway maps and broad catalog layer are implemented as planning aids; the deep 14-week biology course remains milestone 5 work. See [the roadmap](docs/ROADMAP.md).

## Preserved local study tools

The six calculators, cards, case self-assessment and previous browser notebook remain in `legacy/` while their React equivalents are developed. To use them separately:

```sh
python -m http.server 4173 --directory legacy
```

Open http://localhost:4173. Valid previous storage is copied to a CourseLab key with a retained backup. Browser scores stay unverified; they are not silently imported as server grades. The default web image does not serve the legacy reader or authoring answers. The separate local reader intentionally exposes its public practice solutions and is unsuitable for secure exams.

## Repository boundaries and checks

| Directory | Purpose |
| --- | --- |
| `frontend/` | React/TypeScript application, Vitest and Playwright |
| `backend/` | FastAPI, SQLAlchemy, Alembic and Pytest |
| `content/` | Original Markdown, schemas, manifests, public authoring specifications and provenance |
| `legacy/` | Preserved static teaching/study reader |
| `tools/` | Content validation and credential/bundle checks |
| `docs/` | Audit, design, quality, deployment and validation evidence |

No third-party instructional assets have been imported. Public repository authoring solutions remain discoverable; a production operator must store restricted exam keys privately. Learner DTOs and default frontend bundles exclude assessment answer specifications and unreleased solution feedback. Educational worked examples remain public readings.

```sh
pip install -r requirements-dev.txt -r backend/requirements.txt
python tools/validate_content.py
python -m pytest tests -q
npm run test:legacy
cd backend
python -m pytest -q
ruff check .
cd ../frontend
npm ci
npm run lint
npm test
npm run build
npx playwright install --with-deps chromium
npm run test:e2e
```

Start Compose before E2E. Run `python tools/check_security.py --bundle frontend/dist` from the root after building. `python tools/validate_content.py --check-links` performs network probes; two JHU pages currently deny the automated client with HTTP 403, so live-link validation is **not fully passed**. Offline schema/content validation passes with explicit depth/coverage warnings. Detailed commands, test counts and boundaries are in [VALIDATION_REPORT.md](docs/VALIDATION_REPORT.md). Production guidance: [DEPLOYMENT.md](docs/DEPLOYMENT.md).

## Contributing and licensing

Read [CONTRIBUTING.md](CONTRIBUTING.md). Software retains MIT. Educational licensing is separate in [LICENSE-CONTENT](LICENSE-CONTENT) and [content/SOURCES_AND_LICENSES.md](content/SOURCES_AND_LICENSES.md). Historical MIT grants remain valid. Adapted OCW material requires applicable CC BY-NC-SA 4.0 attribution/ShareAlike conditions and asset-level checks; JHU catalogs are alignment references only.

Security: [SECURITY.md](SECURITY.md). Test evidence: [docs/VALIDATION_REPORT.md](docs/VALIDATION_REPORT.md).
