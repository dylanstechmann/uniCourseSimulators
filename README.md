# uniStemCourseSimulators

This is a personal hobby and learning project. Code and educational drafts were developed with substantial assistance from AI coding tools.

Repository: [dylanstechmann/uniStemCourseSimulators](https://github.com/dylanstechmann/uniStemCourseSimulators). See the [progress review](docs/PROGRESS_REVIEW.md) for delivered features, material findings and prioritized remaining work. The software includes local study tools and a graded-assignment prototype; the requested semester-depth courses are still unfinished. Instructor access is granted to registered accounts by an operator after out-of-band identity verification. Practice score changes are blocked unless the saved question and variant digest still match.

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

**No current package meets the complete-course standard.** Current versions are in each package's `course.json` and syllabus, and [the gap report](docs/COURSE_GAP_REPORT.md) gives measured counts. The 257 lesson files, 1,116 formative questions, 768 cards and 25 self-assessed cases are useful practice material; they are not semester courses. Genetics, biochemistry, physiology and biomaterials, all still partial, add original lessons with synthetic data and computed keys: Hardy–Weinberg departures, heritability with polygenic scores, three-point mapping and the design of a controlled gene-perturbation experiment; enzyme kinetics and cellular free energy; oxygen delivery by the Fick principle and renal clearance; hydrogel degradation and release and scaffold porosity, stiffness and permeability. General chemistry 1 and 2, organic chemistry, calculus 1 and 2 and differential equations (still partial) add the supporting lessons: solution preparation and propagated error; buffers and ionization; rate laws and Arrhenius; functional groups in biomolecules and slow chemical damage; derivatives in growth models; integrals as accumulation; a well-mixed perfused chamber with Euler stability; and equilibria and stability. Cellular biomechanics, linear algebra, statics and materials, physics mechanics, physics EM, circuits and signals and control (still partial) add lessons on cell indentation and viscoelasticity, separating stiffness from ligand density, least-squares calibration, Markov chains for cell states, bending of a long bone, impact forces, the membrane as a capacitor, sensor loading and ADC resolution, and proportional control of an incubator. Calculus 3 (gradients in a concentration field) and robotics (planar arm kinematics for lab positioning) complete the set, so every package now has at least one lesson-length original reading alongside its compact prototype units. A further twelve lessons (cell-culture mass balances, perfusion tubing, limits and net change, Taylor error bounds, constrained optimization and polar integrals, RC frequency response, polarity and calorimetry, redox and metal centers, substitution and stereochemistry, induction and current limits, centrifuge rotation, and forearm equilibrium) link every course outcome to at least one lesson objective, and each assessment now lists the course outcomes its own items assess (the validator rejects any outcome an assessment's items do not assess). Ten research-skill lessons follow: multiple testing and FDR; effect sizes, intervals and regression to the mean; algorithmic cost; floating-point pitfalls; aging-biomarker reliability and surrogate endpoints; Mendelian randomization; binding equilibria; Starling forces; convolution and sensor lag; and robot-joint torque budgets. Biochemistry I (still partial) has a proposed 14-week schedule, six more lessons (amino-acid charge and isoelectric points; protein folding and stability; glycolysis, energy charge and the AMP signal; mitochondrial bioenergetics; flux control; reading a metabolic perturbation) and a synthetic enzyme-kinetics lab. Human Physiology for Engineers (still partial) has a proposed 14-week schedule, seven more lessons (balance and feedback gain; membrane potential; hemodynamics; respiratory mechanics; muscle mechanics; tissue repair; compensation and reserve) and a synthetic scratch-assay lab. Genetics & Genomics (still partial) has a proposed 14-week schedule, six more lessons (epistasis and complementation; X-linked inheritance and Bayesian carrier risk; nondisjunction and maternal age; mutation rates and the fluctuation test; expression measurement and false discoveries; designing the follow-up of an association locus) and a synthetic association lab with a population-structure confounder. Thermodynamics & Transport in Bioengineering (still partial) has a proposed 14-week schedule, seven more lessons (transient diffusion; advection, diffusion and the Péclet number; oxygen in a spheroid; saturable uptake; lumped heat transfer; residence time and tanks in series; a perfused construct with a hypoxic center) and a synthetic oxygen depth-profile lab. Bioreactors & Tissue Culture Engineering (still partial) has a proposed 14-week schedule, seven more lessons (Monod growth and yield; chemostat washout and perfusion; mixing and scale-up; shear, eddies and the Kolmogorov scale; dissolved-oxygen control and the capacity limit; factorial design of experiments; designing a scale-down experiment) and a synthetic kLa gassing-out lab. Biomaterials & Tissue Engineering (still partial) has a proposed 14-week schedule, seven more lessons (protein adsorption and surface coverage; hydrogel networks, modulus and mesh size; polymer chain scission and erosion; vascular scaffold wall stress, collapse and shear; biocompatibility evidence and the unit of analysis; cells for a scaffold; reading a failure in a degrading vascular scaffold) and a synthetic degradation time-course lab. Probability, Biostatistics & Experimental Design (still partial) has a proposed 14-week schedule, seven more lessons (sources of variability and pseudoreplication; comparing two groups; power and sample size; regression and calibration; permutation, bootstrap and rank-based methods; base rates and replication; planning a confirmatory study from a pilot) and a synthetic nested-design lab. Geroscience & Regenerative Biology (still partial, now with a proposed 14-week schedule, a synthetic lifespan-cohort lab and a study-design lesson) now pairs each of its four compact units with an original lesson—survival and healthspan endpoints, senescent-cell causality and senolytic safety, clonal hematopoiesis and circulating-factor claims, and epigenetic clocks with partial reprogramming—each with explicitly synthetic data, worked examples, three or four formative items and retrieval cards. Foundations of Cell and Molecular Biology remains partial: a proposed 14-week scope is mapped; weeks 1–7 have original lesson pairs (with compact prototype readings retained in weeks 4 and 7); week 5 includes an interactive fluorescence-count data lab; week 11 now includes a second virtual lab with 120 synthetic signaling observations, replicate-aware summary upload, time-course plotting, and inhibitor/rescue interpretation; week 9 has two original lessons and eight questions on RNA processing/protein regulation; weeks 10–14 each have two lessons and seven questions on their topics, including inheritance, signaling, matrix mechanics, cell fate, stem-cell potency, and integrative experimental design. Week 8 has a 12-question cumulative formative practice set; it is not a midterm or exam. Week 3 now includes one substantial open, ungraded homework companion with a synthetic trafficking dataset and five interactive practice items; its answer specifications are public, so it is not a grade-bearing or protected assessment. The course still lacks all eight full graded homework sets, one additional data/lab activity, summative exams, a cumulative project, workload evidence, and independent course review. No instructor review is fabricated.

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

Open http://localhost:8080. Startup generates a database credential in a private Docker volume, starts PostgreSQL, applies Alembic migrations and serves the React reader through a same-origin API proxy. No API key, database password, cloud account or `.env` is required for a fresh development installation. Existing installations must preserve their Compose project identity before updating to the renamed defaults; see [rename migration](docs/DEPLOYMENT.md#product-rename-and-existing-data). `.env.example` documents optional settings. Ports bind to localhost; HTTP cookies are a development setting. Production needs HTTPS and operator-supplied secrets.

## Tested learning system

- React/TypeScript reader with public catalog, explicit maturity/limitations, syllabus, lesson objectives and prerequisite lists.
- FastAPI/Pydantic with PostgreSQL SQLAlchemy/Alembic, server guest sessions, account registration/login/logout and guest-to-account preservation.
- Enrollment, notes, bookmarks and learner-marked reading progress stored on the server; lesson pages include self-assessment retrieval cards with revealable answers.
- Immutable choice, numeric, symbolic, data-interpretation, structured-rubric, fixed-axis graph-coordinate and bounded CSV-table **formative practice** attempts with diagnosis, hints, next steps, lesson links, and independent criterion scores. The graph exercise plots learner coordinates against supplied replicate data and awards coordinate-level credit; it does not grade axis choice, uncertainty bars, interpolation or interpretation. A cell-biology upload scores replicate counts and means from UTF-8 CSV as inert data with cell-level credit. It does not run uploaded files or grade free-form reasoning; correct results do not establish sound reasoning or mastery.
- Course-level public formative practice sets delivered from version-pinned manifests through answer-free API DTOs. The week-8 cell-biology cumulative rehearsal reuses 12 existing public items and is labeled ungraded and not a midterm; week 9 has eight questions, and weeks 10–14 each have seven questions on their stated topics. Their authoring keys remain openly visible in the repository and are not secure exam materials.
- Separate formative practice gradebook and configured weighted-assignment gradebook, attempt/feedback history and an objective-level study indicator based on distinct items, published thresholds and best reviewed formative scores. Graded submissions are deterministic, version/source-pinned, and limited to a strict deadline. Learners can request one human review per formative or graded attempt; operator-provisioned instructors can record a separate score adjustment while the automatic result stays immutable. Graded adjustments affect the weighted calculation and appear in learner history. None of the 25 current packages contains graded work, so none displays a course grade.
- Spaced retrieval review: enrolled learners self-rate revealed retrieval cards, the server schedules each card with a documented deterministic interval rule, and a course Review queue lists due, new and upcoming cards. Ratings are self-assessments and never change practice scores or objective evidence.
- Learner JSON export and confirmed account deletion, keyboard focus/skip link, larger text/high-contrast controls and safe Markdown rendering.
- Docker development/production examples, reverse proxy, CI and automated content/security-boundary tests.

Single-choice, multiple-select, numeric, bounded symbolic-expression, narrow data-interpretation, structured-rubric, fixed-axis graph-coordinate and constrained CSV numeric-table graders are deterministic. The same supported response formats can be used in versioned graded-assignment submissions; question DTOs omit answer keys, source files are SHA-256 checked, and the API enforces release, attempt and strict-deadline rules. A separate read-only private assessment mount now supports server-only `private://` answer packages; no current course references one, and no graded assignment is shipped. One separate, auditable human decision may adjust a saved score after the exact source and question digest are verified. Stale assignments can only be declined; the automatic result is never rewritten. The tested graded flow uses a synthetic fixture: current catalog packages contain no graded assignments. Numeric grading supports constrained unit conversions, dimensional checks, absolute and relative tolerances, and significant figures. Symbolic grading compares rational expressions through a restricted grammar; it does not execute Python or accept arbitrary SymPy syntax. Structured items map criteria to exact keyed responses; they do not score prose or keyword overlap. The graph grader scores coordinates on fixed axes and does not assess axis choice or scientific interpretation. CSV uploads are size-limited, parsed as UTF-8 and scored only against authored numeric output cells; file contents are never executed. Practice attempts and graded assignments pin question/source specifications. Numeric parameter generation, broader data rubrics, arbitrary CSV analysis, immutable historical content archives, protected exams and isolated code execution remain unfinished. Instructors receive access only through the operator CLI; appeals with unavailable or changed content can only be declined. This does not make public practice questions secure exams. Course-version changes preserve historical records. Unsupported specifications fail explicitly. Code execution and LLM providers are disabled. The eight pathway maps and broad catalog layer are planning aids; weeks 1–7 and 9–14 of the proposed fourteen-week biology schedule have authored lessons, weeks 8–14 offer public cumulative or topic practice, and the eight homework sets, full lab activities, summative exams, and integrative project remain unfinished. See [the roadmap](docs/ROADMAP.md).

## Preserved local study tools

The six calculators, cards, case self-assessment and previous browser notebook remain in `legacy/` while their React equivalents are developed. To use them separately:

```sh
python -m http.server 4173 --directory legacy
```

Open http://localhost:4173. Valid previous storage is copied to a uniStemCourseSimulators key with a retained backup. Browser scores stay unverified; they are not silently imported as server grades. The default web image does not serve the legacy reader or authoring answers. The separate local reader intentionally exposes its public practice solutions and is unsuitable for secure exams.

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

Start Compose before E2E. Run `python tools/check_security.py --bundle frontend/dist` from the root after building. `python tools/validate_content.py --check-links` performs network probes; two JHU pages currently deny the automated client with HTTP 403, so live-link validation is **not fully passed**. Offline schema/content validation passes with 98 explicit legacy-depth warnings for the short prototype readings. Detailed commands, test counts and boundaries are in [VALIDATION_REPORT.md](docs/VALIDATION_REPORT.md). Browser QA of the protected, graded mode, which runs outside Docker against a throwaway fixture, is described in [QA_PROTECTED_GRADED.md](docs/QA_PROTECTED_GRADED.md). Production guidance: [DEPLOYMENT.md](docs/DEPLOYMENT.md).

## Contributing and licensing

Read [CONTRIBUTING.md](CONTRIBUTING.md). To review a lesson, or to understand what reader feedback, AI-assisted checks and subject-matter review can each change, read the [reviewer guide](docs/REVIEWER_GUIDE.md); AI-assisted check records are in [docs/reviews/ai-assisted](docs/reviews/ai-assisted/README.md). Software retains MIT. Educational licensing is separate in [LICENSE-CONTENT](LICENSE-CONTENT) and [content/SOURCES_AND_LICENSES.md](content/SOURCES_AND_LICENSES.md). Historical MIT grants remain valid. Adapted OCW material requires applicable CC BY-NC-SA 4.0 attribution/ShareAlike conditions and asset-level checks; JHU catalogs are alignment references only.

Security: [SECURITY.md](SECURITY.md). Test evidence: [docs/VALIDATION_REPORT.md](docs/VALIDATION_REPORT.md).
