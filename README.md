# Lattice CourseLab

Interactive, source-grounded courses across science, mathematics, engineering, computing, and biomedicine.

An independent open-source learning platform under development. It does **not confer academic credit**, accreditation, degrees, or university prerequisite equivalency. Pathway mappings do not establish admission eligibility or transfer credit. Institutional references identify scope comparators; they do not imply affiliation or endorsement.

## Current course maturity

| Status | Packages | Meaning |
| --- | ---: | --- |
| catalog-only | 0 | Catalog metadata only |
| outlined | 0 | Structured plan without developed teaching |
| partial | 25 | Preserved prototype notes, four lessons and four checks each |
| beta | 0 | Developed course awaiting required review/gates |
| complete | 0 | All full-course gates satisfied |
| externally reviewed | 0 | Qualified named reviewer examined a specified version |

**No current package meets the complete-course standard.** The 100 short lesson seeds, 100 formative questions, 200 cards and 25 self-assessed cases are useful practice material. They are not semester courses. Foundations of Cell and Molecular Biology remains partial; its requested 14-week vertical slice is planned. No instructor review is fabricated.

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

## Run the preserved reader

Until the full-stack milestone is integrated, serve this repository over HTTP:

```sh
python -m http.server 4173
```

Open http://localhost:4173. Browser notes and checks are local guest data. Previous valid storage is copied to a CourseLab key; the previous data and backup remain. Browser checks are unverified, and a correct result does not establish reasoning or mastery.

## Content and application boundaries

- `content/courses/`: original Markdown, manifests, public authoring question specifications, cards, and rubrics. No third-party instructional assets imported.
- `content/schemas/`: documented JSON Schema contracts.
- `src/`: preserved prototype reader with public practice answers; unsuitable for secure exams.
- `tools/validate_content.py`: schema, reference, provenance, duplicate, depth and maturity validation.
- `docs/`: audit, architecture, authoring, grading, curriculum, deployment, and validation reports.

Target architecture: React/TypeScript, FastAPI, PostgreSQL, SQLAlchemy/Alembic, server grading, Docker Compose and CI. Documentation distinguishes implementation from plans. Migration retains teaching content and useful study behavior.

## Contributing and licensing

Read [CONTRIBUTING.md](CONTRIBUTING.md). Software retains MIT. Educational licensing is separate in [LICENSE-CONTENT](LICENSE-CONTENT) and [content/SOURCES_AND_LICENSES.md](content/SOURCES_AND_LICENSES.md). Historical MIT grants remain valid. Adapted OCW material requires applicable CC BY-NC-SA 4.0 attribution/ShareAlike conditions and asset-level checks; JHU catalogs are alignment references only.

Security: [SECURITY.md](SECURITY.md). Test evidence: [docs/VALIDATION_REPORT.md](docs/VALIDATION_REPORT.md).
