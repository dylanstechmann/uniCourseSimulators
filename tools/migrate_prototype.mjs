/** One-time, reproducible preservation of the compact prototype; this adds no semester claims. */
import { readFile, writeFile, mkdir, access } from "node:fs/promises";
import { createHash } from "node:crypto";
import { resolve, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const outputIndex = process.argv.indexOf("--output");
if (outputIndex >= 0 && !process.argv[outputIndex + 1]) throw new Error("--output requires a fresh directory path");
const outputRoot = resolve(root, outputIndex >= 0 ? process.argv[outputIndex + 1] : "content/courses");
try {
  await access(outputRoot);
  throw new Error("Refusing to overwrite migrated packages. Use --output with a fresh directory for a preservation rehearsal.");
} catch (error) {
  if (error.code !== "ENOENT") throw error;
}
const sourcePath = resolve(root, "legacy/src/data/courses.js");
const sourceText = await readFile(sourcePath, "utf8");
const sourceHash = createHash("sha256").update(sourceText).digest("hex");
const { courses } = await import(`data:text/javascript;base64,${Buffer.from(sourceText).toString("base64")}`);
const date = "2026-10-05";
const license = "MIT OR CC-BY-4.0";
const prerequisites = {
  "cell-biology": [[], [], [], ["High-school biology and chemistry"]],
  genetics: [["cell-biology"], [], [], []],
  physiology: [["cell-biology", "physics-mechanics"], ["calculus-1"], [], []],
  "general-chemistry-1": [[], [], [], ["Algebra", "High-school chemistry recommended"]],
  "general-chemistry-2": [["general-chemistry-1"], [], [], []],
  "organic-chemistry": [["general-chemistry-1", "general-chemistry-2"], [], [], []],
  biochemistry: [["general-chemistry-2"], ["organic-chemistry"], [], []],
  "calculus-1": [[], [], [], ["Algebra, functions, and trigonometry"]],
  "calculus-2": [["calculus-1"], [], [], []],
  "calculus-3": [["calculus-2"], ["linear-algebra"], [], []],
  "linear-algebra": [["calculus-1"], [], [], ["Matrix arithmetic"]],
  "differential-equations": [["calculus-1"], ["linear-algebra"], [], []],
  statistics: [[], ["calculus-1"], [], ["Algebra"]],
  "physics-mechanics": [[], [], ["calculus-1"], ["Algebra and trigonometry"]],
  "physics-em": [["calculus-1"], ["physics-mechanics"], [], []],
  programming: [[], [], [], ["Algebra", "One programming language helpful"]],
  "statics-materials": [["physics-mechanics", "calculus-1"], [], [], []],
  circuits: [["physics-em"], ["calculus-1"], [], []],
  transport: [["differential-equations", "physics-mechanics", "general-chemistry-2"], [], [], []],
  "signals-control": [["differential-equations", "linear-algebra"], ["circuits"], [], []],
  robotics: [["linear-algebra", "differential-equations"], ["circuits"], [], []],
  "cellular-biomechanics": [["cell-biology", "physics-mechanics"], ["differential-equations"], [], []],
  biomaterials: [["cell-biology", "organic-chemistry", "statics-materials"], ["transport"], [], []],
  geroscience: [["cell-biology", "genetics", "biochemistry"], ["statistics"], [], []],
  bioreactors: [["cell-biology", "statistics"], ["transport"], [], []],
};
const bloom = (description) => {
  if (/^(design|write|build|make|propose|derive)/i.test(description)) return "create";
  if (/^(evaluate|choose|check|justify|assess|select)/i.test(description)) return "evaluate";
  if (/^(interpret|distinguish|compare|diagnose|separate|trace|track|analyze|relate|connect)/i.test(description)) return "analyze";
  if (/^(calculate|quantify|compute|use|apply|solve|fit|transform|predict|differentiate|estimate|balance|draw|represent|set up)/i.test(description)) return "apply";
  return "understand";
};
const slug = (title) => title.toLowerCase().normalize("NFKD").replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
const json = async (path, value) => { await mkdir(dirname(path), { recursive: true }); await writeFile(path, `${JSON.stringify(value, null, 2)}\n`, "utf8"); };
const legacyReadings = [];

for (const original of courses) {
  const courseRoot = resolve(outputRoot, original.id);
  try {
    await access(resolve(courseRoot, "course.json"));
    const previous = JSON.parse(await readFile(resolve(courseRoot, "course.json"), "utf8"));
    if (previous.content_origin?.kind !== "legacy-prototype" || previous.maturity !== "partial") throw new Error(`Refusing to overwrite developed course ${original.id}`);
  } catch (error) { if (error.code !== "ENOENT") throw error; }
  const outcomes = original.outcomes.map((description, i) => ({ id: `${original.id}-outcome-${i + 1}`, description, bloom: bloom(description) }));
  const lessonObjectives = [];
  const questions = [];
  const cards = [];
  const assessments = [];
  const modifications = [];
  const courseTitle = original.id === "cell-biology" ? "Foundations of Cell and Molecular Biology" : original.title;
  if (courseTitle !== original.title) modifications.push("Normalized the course title to Foundations of Cell and Molecular Biology; the stable ID is unchanged.");
  const modules = [];
  const sourceModules = [];
  for (const [i, unit] of original.modules.entries()) {
    const objectiveIds = unit.objectives.map((description, j) => {
      const id = `${unit.id}-objective-${j + 1}`;
      lessonObjectives.push({ id, description, bloom: bloom(description), course_outcome_ids: [] });
      return id;
    });
    const reading = `modules/${String(i + 1).padStart(2, "0")}-${slug(unit.title)}.md`;
    let workedExample = unit.workedExample;
    let prompt = unit.check.prompt;
    let hint = unit.check.hint;
    let options = unit.check.choices ? [...unit.check.choices] : undefined;
    const changes = [];
    if (original.id === "calculus-2" && i === 1) {
      workedExample = workedExample.replace("the tail is 0.01/(1−0.2)=0.0125", "the tail is 0.2³/(1−0.2)=0.008/0.8=0.01");
      changes.push("Corrected the geometric-series tail arithmetic; the original approximation and exact sum are preserved.");
    }
    if (original.id === "organic-chemistry" && i === 2) {
      options[0] = "Anti-periplanar C–H and C–leaving-group bonds";
      changes.push("Clarified the typical E2 answer option as anti-periplanar; atypical syn elimination is not presented as equally typical.");
    }
    if (original.id === "biomaterials" && i === 1) {
      prompt = prompt.replace("15% of its initial mass each week", "15% of its remaining mass each week");
      changes.push("Replaced 'initial mass' with 'remaining mass' to make constant fractional loss agree with the stated first-order model.");
    }
    if (original.id === "robotics" && i === 2) {
      hint = "Multiply torque by angular velocity using P=τω; N·m × rad/s gives watts.";
      changes.push("Expanded the power hint to state the calculation method and units without changing the question or answer.");
    }
    const questionId = `${unit.id}:check`;
    const solutionSpec = unit.check.type === "numeric" ? {
      answer: unit.check.answer, unit: unit.check.unit, tolerance: unit.check.tolerance,
      unit_required: false, significant_figures: null, dimensions: null,
    } : { answer: unit.check.answer };
    questions.push({
      id: questionId, type: unit.check.type === "choice" ? "single_choice" : "numeric", prompt,
      ...(options ? { options } : {}), points: 1,
      // Association preserves the first authored lesson objective; comprehensive coverage needs review.
      objective_ids: [objectiveIds[0]], solution_spec: solutionSpec,
      feedback: { hint, solution: unit.check.solution, lesson_ids: [unit.id], misconception_ids: [] },
      visibility: "public-practice-authoring",
      provenance: { kind: "legacy-prototype", legacy_id: questionId, modifications: changes },
    });
    const cardIds = unit.cards.map(([front, back], j) => {
      const id = `${original.id}-${i}-${j}`;
      cards.push({ id, lesson_id: unit.id, front, back, objective_ids: [], license });
      return id;
    });
    const moduleId = `${original.id}-module-${i + 1}`;
    modules.push({ id: moduleId, title: unit.title, source_ids: original.sources, lessons: [{ id: unit.id, title: unit.title, reading, objectives: objectiveIds, worked_example: workedExample, question_ids: [questionId], card_ids: cardIds }] });
    assessments.push({ id: `${unit.id}-practice`, type: "practice", mode: "practice", path: "question-banks/practice.json", objective_ids: [objectiveIds[0]], question_ids: [questionId], points: 1 });
    sourceModules.push({ module_id: moduleId, lesson_id: unit.id, reading, source_ids: original.sources, relationship: "curriculum-comparator", original_content: true, license, modifications: changes });
    modifications.push(...changes);
    await mkdir(dirname(resolve(courseRoot, reading)), { recursive: true });
    const readingText = `# ${unit.title}\n\n${unit.notes}\n`;
    await writeFile(resolve(courseRoot, reading), readingText, "utf8");
    legacyReadings.push({ course_id: original.id, lesson_id: unit.id, reading, sha256: createHash("sha256").update(readingText).digest("hex") });
  }
  const caseId = `${original.id}:case`;
  const caseRecord = { id: caseId, prompt: original.capstone.prompt, mode: "self-assessment", objective_ids: [], rubric: original.capstone.rubric.map((criterion, i) => ({ id: `${original.id}-case-criterion-${i + 1}`, criterion, points: 0, levels: [] })), limitations: ["This preserved three-criterion checklist is self-assessment, not an analytic grading rubric or an institutional grade."] };
  assessments.push({ id: `${original.id}-case`, type: "case", mode: "self-assessment", path: "rubrics/case-studio.json", objective_ids: [], question_ids: [], points: 0 });
  const [required, recommended, concurrent, knowledge] = prerequisites[original.id];
  const limitations = [
    "Four compact legacy units are preserved; this package is not equivalent to a full university semester.",
    "There is no authored 12–15 week schedule, substantive homework sequence, laboratory sequence, midterm, cumulative final, or graded integrative project.",
    "The single formative check per lesson does not demonstrate comprehensive outcome coverage or mastery; association with the first lesson objective is provisional.",
    "Bloom labels and structured prerequisite edges are initial authoring classifications awaiting subject-matter review.",
    "Question answers and solution feedback are intentionally public practice authoring specifications, not restricted exam keys.",
    "Numerical specifications preserve the prototype's tolerance and optional unit entry; significant-figure and dimensional checks have not been authored.",
    "Total workload and weekly duration are unknown; former nominal credit values and hardcoded reading times do not establish workload.",
  ];
  const manifest = {
    schema_version: "1.0", id: original.id, legacy_code: original.code, title: courseTitle, description: original.summary,
    domain: original.domain, level: original.level, maturity: "partial", version: "0.1.0", license,
    content_origin: { kind: "legacy-prototype", source_path: "src/data/courses.js", source_sha256: sourceHash, migration_version: "1.0", modifications },
    prerequisites: { course_ids: required, recommended_course_ids: recommended, concurrent_course_ids: concurrent, knowledge, statement: original.prerequisites },
    outcomes, lesson_objectives: lessonObjectives,
    duration: { instructional_weeks: null, equivalent_structure: null, weeks: [] },
    workload: { estimated_total_hours: null, estimated_hours_per_week: null, basis: "Not measured. Legacy nominal credit and display-time labels are not retained as workload estimates." },
    modules, assessments,
    grading_policy: { mode: "formative-only", categories: [], attempt_policy: "Unlimited formative retries; no summative grade is awarded.", solution_release: "Public practice solutions may be shown after an attempt. They are not production exam keys.", late_policy: "No deadlines or late penalties exist in this partial package.", appeals: "No instructor review workflow is implemented; report ambiguous practice items to repository maintainers." },
    retrieval_cards: "question-banks/retrieval-cards.json", case_rubrics: "rubrics/case-studio.json", source_map: "source-map.json", syllabus: "syllabus.md",
    review: { status: "unreviewed", reviewed_version: null, reviewers: [] },
    accessibility: { language: "en", reading_format: "markdown", math_format: "unicode-text", diagram_policy: "The seed package contains no imported diagrams; newly authored diagrams require descriptions and individual license tracking.", known_issues: ["Unicode equations require structured mathematical alternatives and assistive-technology review."], review_status: "unreviewed" },
    history: [{ version: "0.1.0", date, summary: "Preserved original compact prototype content in separate manifests and readings; labeled partial without semester or credit equivalency.", }, ...(modifications.length ? [{ version: "0.1.0", date, summary: modifications.join(" ") }] : [])],
    limitations, intentionally_omitted: ["Full instructional sequence and summative assessments are not authored yet; this is a preserved seed inventory."]
  };
  await json(resolve(courseRoot, "course.json"), manifest);
  await json(resolve(courseRoot, "question-banks/practice.json"), { schema_version: "1.0", course_id: original.id, license, questions });
  await json(resolve(courseRoot, "question-banks/retrieval-cards.json"), { schema_version: "1.0", course_id: original.id, cards });
  await json(resolve(courseRoot, "rubrics/case-studio.json"), { schema_version: "1.0", course_id: original.id, cases: [caseRecord] });
  await json(resolve(courseRoot, "source-map.json"), { schema_version: "1.0", course_id: original.id, license, modules: sourceModules });
  await writeFile(resolve(courseRoot, "syllabus.md"), `# ${courseTitle}\n\n**Maturity: partial. Version: 0.1.0.**\n\n${original.summary}\n\n## Prerequisites\n\n${original.prerequisites}. Structured required, recommended, and concurrent relationships appear in the manifest and remain subject to author review. This package establishes no university prerequisite equivalency.\n\n## Authored outcomes\n\n${original.outcomes.map((o) => `- ${o}`).join("\n")}\n\n## Existing units\n\n${original.modules.map((m, i) => `${i + 1}. ${m.title}`).join("\n")}\n\n## Assessment and study policy\n\nEach unit includes one public formative check and two retrieval cards. A course case includes a self-assessment checklist. These are practice activities, with unlimited retries and no institutional grade, university credit, or transferable credit. Workload has not been measured.\n\n## Schedule and current limitations\n\nNo full-semester calendar or 14-week structure has been authored. No substantive homework sets, laboratories, midterm, final, or graded cumulative project are included. The four short readings preserve useful prototype explanations. They require substantial expansion and qualified human review before this course can meet the complete-course quality standard.\n\n## Sources and licensing\n\nRead source-map.json for module provenance and content/SOURCES_AND_LICENSES.md for the software/content license boundary. Listed source courses are public curriculum comparators; no affiliation or equivalency is implied.\n`, "utf8");
}
await json(resolve(outputRoot, "legacy-inventory.json"), { schema_version: "1.0", migration_version: "1.0", source_path: "src/data/courses.js", source_sha256: sourceHash, course_ids: courses.map((course) => course.id), readings: legacyReadings });
console.log(`Preserved ${courses.length} partial course packages, ${courses.reduce((n, c) => n + c.modules.length, 0)} lessons and questions, ${courses.reduce((n, c) => n + c.modules.reduce((a, m) => a + m.cards.length, 0), 0)} cards, and ${courses.length} self-assessed cases.`);
