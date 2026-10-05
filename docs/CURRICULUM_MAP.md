# Curriculum map

`content/curriculum-map.json` is the curriculum planning layer. The FastAPI endpoint serves it at `/api/v1/curriculum`; the catalog UI renders expandable pathway sequences, prerequisite relations, source links, maturity labels, and links to related partial packages. The data contract is in `content/schemas/curriculum-map.schema.json`, and the repository validator checks references and cycles across both package manifests and planned catalog nodes.

## Maturity and limits

The repository currently has 25 course packages, all marked **partial**, plus 37 **catalog-only** topic nodes. A catalog-only node describes a planned subject, dependency hints, and sometimes a related combined prototype package. It has no lessons or assessments and cannot be enrolled in. The related partial package remains separately labeled and does not make the planned node a developed course.

Pathway order is an exploration sequence. `prerequisites.course_ids`, `recommended_course_ids`, and `concurrent_course_ids` form the explicit project planning graph. These edges do not establish a university's admission rules, course equivalency, transfer credit, or affiliation. Local programs may order or scope subjects differently.

## Pathways

The eight pathway IDs are:

1. `science-mathematics-foundation`
2. `electrical-computer-engineering`
3. `mechanical-engineering-robotics`
4. `biomedical-engineering`
5. `tissue-regenerative-medicine`
6. `geroscience-aging`
7. `drug-discovery-translational-science`
8. `jhu-regenerative-stem-cell-prerequisites`

The planning map separates the engineering subjects that were previously bundled into broad prototype packages. It includes numerical methods; statics; dynamics; mechanics of materials; thermodynamics; fluid mechanics; heat and mass transfer; materials science; Circuits I and II; analog electronics; digital logic; signals and systems; feedback control; instrumentation and sensors; embedded systems; mechanical design; robotics and mechatronics; and engineering design/experimental methods. Calculus I–III, linear algebra, differential equations, probability/statistics, classical mechanics, and electricity and magnetism link to their existing partial packages.

Catalog-only science topics add physical and analytical chemistry; molecular and developmental biology; microbiology and immunology; stem-cell biology; regenerative medicine; gene therapy; bioethics; engineered-tissue systems for drug discovery; biotherapeutic manufacturing; cell-culture/stem-cell laboratory concepts; medicinal chemistry; pharmacology; and drug-discovery/translational science. All retain catalog-only maturity until original teaching and assessment material is actually developed.

## Johns Hopkins topic alignment

The JHU regenerative/stem-cell map includes organic chemistry, biochemistry, molecular biology, and cell biology as foundational topics. Its advanced topic list includes developmental biology, gene therapy, regenerative medicine, bioethics, stem-cell biology, tissue-engineered systems for drug discovery, biotherapeutic manufacturing, and cell-culture/stem-cell laboratory concepts. The map cites public catalog pages in `content/sources/registry.json` and documents link-only use there. No Johns Hopkins instructional text or assessment has been copied; CourseLab makes no affiliation, admission, equivalency, or credit claim. See [curriculum reference notes](CURRICULUM_REFERENCE_NOTES.md).

## Validation

`tools/validate_content.py` checks the map schema, required pathway set, topic coverage, package/catalog ID collisions, unknown prerequisite or source references, duplicate catalog descriptions, placeholders, and dependency cycles spanning package and catalog nodes. Backend tests confirm public API maturity and dependency fields; frontend tests cover the explorer; Playwright verifies the JHU reference path and automated accessibility scan.
