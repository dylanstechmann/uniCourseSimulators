# Lattice — Bioengineering Academy

An interactive, self-paced course studio for the science and engineering foundations that lead into biomedical engineering, robotics, tissue engineering, and geroscience.

Lattice combines original teaching notes and worked examples with immediate formative feedback, case studies, spaced retrieval, a private notebook, and small equation-driven lab tools. Its course map is compared with public MIT OpenCourseWare syllabi and resources; it is an independent learning project and is not affiliated with MIT.

## Start locally

The course app is a static site. It has no package install or account setup.

```powershell
python -m http.server 4173
```

Open `http://localhost:4173`. If you prefer another local static server, serve this directory as-is; ES modules should be loaded over HTTP rather than opened as a `file://` URL.

## What is in this release

- 25 courses across biology, chemistry, biochemistry, mathematics, statistics, physics, computing, electrical engineering, mechanical engineering, bioengineering, tissue engineering, and geroscience.
- Four developed core units per course (100 total), with measurable objectives, original notes, a worked example, an automatically graded problem, targeted feedback, and two retrieval cards.
- A course-level open-response case studio with a transparent rubric for integrative reasoning.
- Four suggested prerequisite-aware study paths: pre-biomedical engineering, robotics and mechatronics, tissue engineering, and geroscience.
- Six interactive calculators covering solution preparation, buffer pH, Michaelis–Menten kinetics, RC response, a diffusion timescale, and Ohm's law.
- Local progress tracking, course bookmarks, private notes, and a simple spaced-review schedule. Nothing is sent to a server.

## Courses

| Area | Courses |
| --- | --- |
| Biology and biochemistry | Foundations of Cell & Molecular Biology; Genetics & Genomics; Human Physiology for Engineers; Biochemistry I |
| Chemistry | General Chemistry I; General Chemistry II; Organic Chemistry I for Life Sciences |
| Mathematics and methods | Calculus I; Calculus II; Calculus III; Linear Algebra; Differential Equations; Probability, Biostatistics & Experimental Design |
| Physics and computing | Physics: Mechanics; Physics: Electricity & Magnetism; Programming & Numerical Methods |
| Electrical and mechanical engineering | Statics & Mechanics of Materials; Electrical Circuits & Instrumentation; Thermodynamics & Transport; Signals & Feedback Control; Robotics & Mechatronics |
| Specialized bioengineering | Cellular Biomechanics & Mechanobiology; Biomaterials & Tissue Engineering; Geroscience & Regenerative Biology; Bioreactors & Tissue Culture Engineering |

The catalog uses local course labels and planning-level credit-hour estimates to help communicate prerequisites and scope. They do not represent university credit or transfer equivalency.

## Curriculum comparison and scope

Read [the curriculum alignment and quality guide](docs/CURRICULUM_ALIGNMENT.md) for the OCW comparator map and review criteria. Read [the assessment and study-tool guide](docs/ASSESSMENT_AND_STUDY_TOOLS.md) for grading behavior, persistence, and answer conventions.

This first release is a compact, interactive core for each mapped course: four broad units, four short formative checks, and one integrative case. That is useful for guided self-study and identifying gaps, but it is not yet equivalent to a full 12–14 week university course with a complete lecture sequence, weekly problem sets, laboratories, exams, instructor feedback, or credit-bearing assessment. The next content expansion should deepen each course with additional sessions, problem sets, laboratory/data cases, and instructor review. The official OCW links provide additional primary materials for independent study.

## Data and implementation

- `src/data/courses.js` — original course notes, objectives, problems, answer keys, cards, case prompts, and source links.
- `src/data/pathways.js` — suggested curricular sequences.
- `src/app.js` and `styles.css` — accessible, responsive single-page learning interface.
- `docs/` — curriculum mapping and assessment behavior.

No build step, package dependency, API key, or backend is required. Browser local storage holds learner state. Clearing site data removes saved progress and notes.

## License

The original software and educational text in this repository are provided under the MIT License. External course materials remain the property of their respective authors and are linked for comparison only; consult each source's terms before reusing it.

