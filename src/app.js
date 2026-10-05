import { allCards, courseById, courses, references } from "./data/courses.js";
import { pathways } from "./data/pathways.js";

const STORAGE_KEY = "lattice-academy:v1";
const totalUnits = courses.reduce((total, item) => total + item.modules.length, 0);
const domains = ["All courses", ...new Set(courses.map((item) => item.domain))];
const appRoot = document.querySelector("#app");

const freshState = () => ({
  completed: {},
  visited: {},
  answers: {},
  notes: {},
  capstoneDrafts: {},
  rubricChecks: {},
  cardSchedule: {},
  bookmarks: [],
  lastCourseId: "cell-biology",
});

function loadState() {
  try {
    const stored = JSON.parse(localStorage.getItem(STORAGE_KEY) || "null");
    return stored && typeof stored === "object" ? { ...freshState(), ...stored } : freshState();
  } catch {
    return freshState();
  }
}

let state = loadState();
let route = parseRoute();
let domainFilter = "All courses";
let query = "";
let studySearch = "";
let selectedCardId = null;
let cardFlipped = false;

function saveState() {
  try { localStorage.setItem(STORAGE_KEY, JSON.stringify(state)); } catch { /* private browsing may disable storage */ }
}

function parseRoute() {
  const parts = (location.hash || "#home").replace(/^#/, "").split("/");
  if (parts[0] === "course" && courseById[parts[1]]) {
    return { page: "course", courseId: parts[1], moduleIndex: Math.max(0, Number(parts[2]) || 0), tab: ["learn", "map", "exam"].includes(parts[3]) ? parts[3] : "learn" };
  }
  return { page: ["home", "catalog", "pathways", "study", "tools"].includes(parts[0]) ? parts[0] : "home" };
}

function navigate(hash) {
  const nextHash = `#${hash}`;
  if (location.hash === nextHash) {
    route = parseRoute();
    render();
    return;
  }
  location.hash = nextHash;
}

function openCourse(courseId, moduleIndex = 0, tab = "learn") {
  const item = courseById[courseId];
  if (!item) return;
  state.lastCourseId = courseId;
  state.visited[item.modules[moduleIndex]?.id] = true;
  saveState();
  navigate(`course/${courseId}/${moduleIndex}/${tab}`);
}

function esc(value = "") {
  return String(value).replace(/[&<>"']/g, (char) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[char]);
}

function prose(value = "") {
  return String(value).split(/\n\s*\n/).map((part) => `<p>${esc(part)}</p>`).join("");
}

function percentForCourse(item) {
  const count = item.modules.filter((unit) => state.completed[unit.id]).length;
  return Math.round((count / item.modules.length) * 100);
}

function dueCards() {
  const now = Date.now();
  const scheduled = allCards.filter((card) => state.cardSchedule[card.id]?.dueAt <= now)
    .sort((a, b) => state.cardSchedule[a.id].dueAt - state.cardSchedule[b.id].dueAt);
  const fresh = allCards.filter((card) => !state.cardSchedule[card.id]).slice(0, Math.max(0, 10 - scheduled.length));
  return [...scheduled, ...fresh];
}

function answerStats() {
  const attempts = Object.values(state.answers);
  const answered = attempts.filter((entry) => Number.isFinite(entry.attempts));
  const correct = answered.filter((entry) => entry.correct).length;
  return { attempts: answered.length, correct, accuracy: answered.length ? Math.round((correct / answered.length) * 100) : 0 };
}

function activePageName() {
  return ({ home: "Overview", catalog: "Course catalog", pathways: "Learning paths", study: "Study room", tools: "Lab tools", course: courseById[route.courseId]?.code || "Course" })[route.page];
}

function render() {
  route = parseRoute();
  appRoot.innerHTML = `
    <div class="app-shell">
      ${renderSidebar()}
      <div class="main-shell">
        <header class="topbar">
          <div class="crumbs">LATTICE <span aria-hidden="true">/</span> <strong>${esc(activePageName())}</strong></div>
          <div class="topbar-actions">
            <label class="search-shell"><input class="search-input" id="global-search" value="${esc(query)}" aria-label="Search courses" placeholder="Search courses · press Enter" /></label>
            <div class="topbar-meta"><span class="online-dot" aria-hidden="true"></span> LOCAL WORKSPACE</div>
          </div>
        </header>
        <main class="page-content" id="main-content">
          ${renderPage()}
          ${renderFooter()}
        </main>
      </div>
    </div>`;
  if (route.page === "tools") ["dilution", "buffer", "enzyme", "rc", "diffusion", "ohm"].forEach(renderToolResult);
}

function renderSidebar() {
  const nav = [
    ["home", "⌂", "Overview"], ["catalog", "▦", "All courses"], ["pathways", "⌁", "Learning paths"],
    ["study", "✳", "Study room"], ["tools", "⌘", "Lab tools"],
  ];
  return `<aside class="sidebar" aria-label="Main navigation">
    <a class="brand" href="#home" aria-label="Lattice Academy home">
      <span class="brand-mark" aria-hidden="true"><svg viewBox="0 0 32 32" fill="none"><path d="M5 7h4v14h7v4H5zm13 0h4v6h6v4h-6v8h-4z" fill="currentColor"/><circle cx="27" cy="7" r="2.5" fill="#b6d978"/></svg></span>
      <span class="brand-wordmark"><span class="brand-name">Lattice</span><span class="brand-sub">Bioengineering academy</span></span>
    </a>
    <div class="nav-label">Workspace</div>
    <nav class="primary-nav">
      ${nav.map(([page, icon, label]) => `<button class="nav-button ${route.page === page ? "active" : ""}" data-page="${page}" ${route.page === page ? 'aria-current="page"' : ""}><span class="nav-icon" aria-hidden="true">${icon}</span><span>${label}</span>${page === "study" && dueCards().length ? `<span class="nav-count">${dueCards().length}</span>` : ""}</button>`).join("")}
    </nav>
    <div class="sidebar-divider"></div>
    <div class="nav-label">Study tracks</div>
    <div class="path-nav">${pathways.map((path) => `<button class="path-shortcut" data-page="pathways"><span class="path-glyph" aria-hidden="true">${path.icon}</span>${esc(path.short)}</button>`).join("")}</div>
    <div class="sidebar-spacer"></div>
    <div class="offline-note"><div class="offline-note-title"><span aria-hidden="true">●</span> Progress stays here</div><p>Notes, scores, and review cards save in this browser. No account required.</p></div>
    <div class="sidebar-foot"><span>OPEN LEARNING STUDIO</span><span>v1.0</span></div>
  </aside>`;
}

function renderFooter() {
  return `<footer class="site-footer">Course notes and exercises are original teaching material. MIT OpenCourseWare links are included as public curriculum comparators; no OCW problem text or solutions are reproduced. Practice scores and notes are stored locally in this browser.</footer>`;
}

function renderPage() {
  if (route.page === "home") return renderHome();
  if (route.page === "catalog") return renderCatalog();
  if (route.page === "pathways") return renderPathways();
  if (route.page === "study") return renderStudyRoom();
  if (route.page === "tools") return renderTools();
  if (route.page === "course") return renderCourse(route.courseId, route.moduleIndex, route.tab);
  return renderHome();
}

function renderHeroArt() {
  return `<svg viewBox="0 0 360 230" role="img" aria-label="An abstract cell, scaffold, and engineering signal">
    <defs><linearGradient id="cellFill" x1=".1" y1=".1" x2=".9" y2=".9"><stop stop-color="#d4e5b6" stop-opacity=".96"/><stop offset="1" stop-color="#99c190" stop-opacity=".7"/></linearGradient></defs>
    <circle cx="191" cy="112" r="75" fill="url(#cellFill)" fill-opacity=".18" stroke="#d2e6c4" stroke-opacity=".75" stroke-width="1.2"/>
    <circle cx="191" cy="112" r="59" fill="none" stroke="#cae0c0" stroke-opacity=".24" stroke-dasharray="3 5"/>
    <circle cx="181" cy="108" r="28" fill="#bed997" fill-opacity=".42" stroke="#e2f0d0" stroke-opacity=".82"/>
    <circle cx="185" cy="105" r="12" fill="#d8ebb8" fill-opacity=".76"/><circle cx="211" cy="132" r="5" fill="#d2e7be"/>
    <circle cx="156" cy="82" r="4" fill="#d7e9ca"/><circle cx="227" cy="88" r="3.5" fill="#d7e9ca"/><circle cx="151" cy="135" r="3" fill="#d7e9ca"/>
    <path d="M39 167h37l13-26 18 45 22-66 20 38h43" fill="none" stroke="#b6d978" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" opacity=".92"/>
    <path d="M237 153h23v-40h18v40h18v-64h18v64h18" fill="none" stroke="#c6e2cf" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" opacity=".6"/>
    <circle cx="278" cy="113" r="3" fill="#b6d978"/><circle cx="314" cy="89" r="3" fill="#b6d978"/>
    <path d="M59 71l10 10m-10 0 10-10" stroke="#bed9a8" stroke-linecap="round" opacity=".65"/><path d="M287 43l9 0m-4.5-4.5v9" stroke="#bed9a8" stroke-linecap="round" opacity=".65"/>
  </svg>`;
}

function renderHome() {
  const stats = answerStats();
  const started = courses.filter((item) => item.modules.some((unit) => state.visited[unit.id] || state.completed[unit.id]));
  const suggestions = (started.length ? started : courses.filter((item) => ["cell-biology", "general-chemistry-1", "calculus-1"].includes(item.id))).slice(0, 3);
  const cards = dueCards().length;
  return `<section class="welcome-line"><div class="welcome-copy"><div class="eyebrow">A connected course studio</div><h1>Learn the systems behind better health.</h1><p>Build a rigorous foundation in biology, chemistry, mathematics, and engineering—then connect it to robotics, tissue design, and the science of aging.</p></div><div class="date-chip"><span aria-hidden="true">◷</span> SELF-PACED · UNIVERSITY LEVEL</div></section>
    <section class="hero-card"><div class="hero-copy"><div class="hero-kicker">A better way to connect the disciplines</div><h2>Start with the fundamentals.<br/>Follow the question further.</h2><p>Short lectures, worked examples, auto-graded checks, and study tools help you move from core science to real engineering decisions.</p><div class="hero-actions"><button class="button button-primary" data-page="catalog">Explore all ${courses.length} courses <span aria-hidden="true">→</span></button><button class="hero-link" data-page="pathways">View learning paths</button></div></div><div class="hero-art">${renderHeroArt()}</div></section>
    <section class="metric-row" aria-label="Learning progress">
      <div class="metric-card"><div class="metric-label">Lessons mastered</div><div class="metric-number">${Object.keys(state.completed).length}<span>/ ${totalUnits}</span></div></div>
      <div class="metric-card"><div class="metric-label">Checks answered</div><div class="metric-number">${stats.attempts}<span>graded</span></div></div>
      <div class="metric-card"><div class="metric-label">Recent accuracy</div><div class="metric-number">${stats.attempts ? `${stats.accuracy}%` : "—"}<span>${stats.attempts ? `${stats.correct} correct` : "start a check"}</span></div></div>
      <div class="metric-card"><div class="metric-label">Cards ready</div><div class="metric-number">${cards}<span>for review</span></div></div>
    </section>
    <section><div class="section-heading"><div><h2>${started.length ? "Pick up where you left off" : "A good place to begin"}</h2><p>Build momentum one focused lesson at a time.</p></div><button class="text-link" data-page="catalog">Browse the catalog →</button></div>
      <div class="continue-grid">${suggestions.map((item) => renderContinueCard(item)).join("")}</div>
    </section>
    <section><div class="section-heading"><div><h2>Choose a direction</h2><p>Four connected routes through the same course library.</p></div><button class="text-link" data-page="pathways">All learning paths →</button></div>
      <div class="path-feature-grid">${pathways.map((path) => `<button class="path-feature" data-page="pathways"><span class="path-symbol" aria-hidden="true">${path.icon}</span><h3>${esc(path.title)}</h3><p>${esc(path.description)}</p></button>`).join("")}</div>
    </section>`;
}

function renderContinueCard(item) {
  const nextIndex = Math.max(0, item.modules.findIndex((unit) => !state.completed[unit.id]));
  const percent = percentForCourse(item);
  const nextTitle = item.modules[nextIndex]?.title || item.modules[0].title;
  return `<article class="continue-card" tabindex="0" role="button" data-open-course="${item.id}" data-open-module="${nextIndex}" aria-label="Continue ${esc(item.title)} at ${esc(nextTitle)}">
    <div class="continue-top"><span class="course-code">${esc(item.code)}</span><span class="pill">${esc(item.domain)}</span></div>
    <h3>${esc(item.title)}</h3><p>Next · ${esc(nextTitle)}</p>
    <div class="continue-progress"><div class="progress-track"><div class="progress-fill" style="width:${percent}%"></div></div><span>${percent}%</span></div>
  </article>`;
}

function renderCatalog() {
  const filtered = filteredCourses();
  return `<section class="page-intro"><div><div class="eyebrow">Build your course plan</div><h1>Course catalog</h1><p>${courses.length} structured, original courses move from foundational science through quantitative engineering to tissue design, robotics, and geroscience.</p></div><span class="pill pill-lime">${totalUnits} interactive lessons</span></section>
    <div class="catalog-toolbar" role="group" aria-label="Filter courses by subject">${domains.map((domain) => `<button class="filter-chip ${domainFilter === domain ? "active" : ""}" data-domain="${esc(domain)}" aria-pressed="${domainFilter === domain}">${esc(domain)}</button>`).join("")}<span class="catalog-count">${filtered.length} courses</span></div>
    <div class="course-grid-wrap">${renderCourseGrid(filtered)}</div>`;
}

function filteredCourses() {
  const term = query.toLowerCase().trim();
  return courses.filter((item) => {
    const matchesDomain = domainFilter === "All courses" || item.domain === domainFilter;
    const searchable = [item.title, item.code, item.domain, item.summary, ...item.outcomes, ...item.modules.map((unit) => `${unit.title} ${unit.notes}`)].join(" ").toLowerCase();
    return matchesDomain && (!term || searchable.includes(term));
  });
}

function renderCourseGrid(items) {
  if (!items.length) return `<div class="empty-state">No courses match that search. Try a broader subject or term.</div>`;
  return items.map((item) => `<article class="course-card" tabindex="0" role="button" data-open-course="${item.id}" aria-label="Open ${esc(item.code)} ${esc(item.title)}">
    <div class="course-card-top"><span class="course-code">${esc(item.code)}</span><span class="pill ${domainPill(item.domain)}">${esc(item.domain)}</span></div>
    <h3>${esc(item.title)}</h3><p class="course-card-summary">${esc(item.summary)}</p>
    <div class="course-meta"><span>${esc(item.level)}</span><span>${item.credits} credits</span><span>${item.modules.length} units</span></div>
    <div class="course-card-progress"><div class="progress-track"><div class="progress-fill" style="width:${percentForCourse(item)}%"></div></div><span class="course-code">${percentForCourse(item)}%</span></div>
  </article>`).join("");
}

function domainPill(domain) {
  return ({ "Life sciences": "pill-lime", Chemistry: "pill-peach", Biochemistry: "pill-lime", Mathematics: "pill-blue", "Quantitative methods": "pill-purple", Physics: "pill-blue", Computing: "pill-blue", "Mechanical engineering": "pill-peach", "Electrical engineering": "pill-blue", Bioengineering: "pill-lime" })[domain] || "";
}

function renderPathways() {
  return `<section class="page-intro"><div><div class="eyebrow">Sequence the foundations</div><h1>Learning paths</h1><p>Each path is a suggested three-year sequence, not an institutional degree audit. Prerequisites inside each course describe the knowledge assumed for its material.</p></div><span class="pill pill-purple">4 study tracks</span></section>
    <div class="pathway-list">${pathways.map((path) => renderPathway(path)).join("")}</div>
    <div class="tool-callout"><strong>How to use a path.</strong> Start with the first available course, use the course prerequisites to adjust for prior study, and move forward when you can explain the objectives and solve the checks without relying on hints. This sequence is a learning guide, not a transfer-credit or accreditation claim.</div>`;
}

function renderPathway(path) {
  const ids = [...new Set(path.terms.flatMap((term) => term.courses))];
  const done = ids.filter((id) => courseById[id] && percentForCourse(courseById[id]) === 100).length;
  const pct = ids.length ? Math.round(done / ids.length * 100) : 0;
  return `<article class="pathway-card"><div class="pathway-card-header"><div class="pathway-title-line"><span class="path-symbol" aria-hidden="true">${path.icon}</span><h2>${esc(path.title)}</h2></div><p>${esc(path.description)}</p></div>
    <div class="pathway-terms">${path.terms.map((term) => `<div class="pathway-term"><div class="pathway-term-label">${esc(term.label)}</div><div class="pathway-course-list">${term.courses.map((id) => {
      const item = courseById[id];
      return item ? `<button class="pathway-course-chip" data-open-course="${item.id}" title="${esc(item.code)}">${esc(item.code)} · ${esc(item.title)}</button>` : "";
    }).join("")}</div></div>`).join("")}</div>
    <div class="pathway-progress"><span>${done} of ${ids.length} courses complete</span><div class="progress-track"><div class="progress-fill" style="width:${pct}%"></div></div><span>${pct}%</span></div></article>`;
}

function renderCourse(courseId, moduleIndex, tab) {
  const item = courseById[courseId];
  if (!item) return `<div class="empty-layout"><span class="path-symbol">?</span><h2>Course not found</h2><p>This course may have moved in the catalog.</p><button class="button button-primary" data-page="catalog">Return to catalog</button></div>`;
  const safeIndex = Math.min(Math.max(0, moduleIndex), item.modules.length - 1);
  const unit = item.modules[safeIndex];
  const completed = item.modules.filter((part) => state.completed[part.id]).length;
  return `<section class="course-heading">
      <div class="course-heading-top"><button data-page="catalog">Course catalog</button><span>›</span><span>${esc(item.code)}</span><span>·</span><span>${esc(item.domain)}</span></div>
      <div class="course-title-row"><div><span class="pill ${domainPill(item.domain)}">${esc(item.level)} · ${item.credits} credits</span><h1>${esc(item.title)}</h1><p>${esc(item.summary)}</p></div><div class="course-stat-box"><strong>${completed}/${item.modules.length}</strong><span>units completed</span></div></div>
    </section>
    <div class="course-toolbar"><div class="tabs" role="tablist" aria-label="Course sections">${[["learn", "Learn"], ["map", "Syllabus"], ["exam", "Case studio"]].map(([key, label]) => `<button class="tab-button ${tab === key ? "active" : ""}" role="tab" aria-selected="${tab === key}" data-course-tab="${key}">${label}</button>`).join("")}</div>
      <button class="button button-secondary button-small" data-bookmark="${item.id}" aria-pressed="${state.bookmarks.includes(item.id)}">${state.bookmarks.includes(item.id) ? "★ Saved" : "☆ Save course"}</button></div>
    ${tab === "learn" ? renderLessonWorkspace(item, safeIndex, unit) : tab === "map" ? renderCourseMap(item) : renderCourseExam(item)}
  `;
}

function renderLessonWorkspace(item, index, unit) {
  return `<div class="course-workspace"><aside class="module-rail" aria-label="Course units"><div class="module-rail-heading">Course units · ${item.modules.length}</div><div class="module-rail-inner">${item.modules.map((part, partIndex) => `<button class="module-button ${partIndex === index ? "active" : ""} ${state.completed[part.id] ? "done" : ""}" data-module-index="${partIndex}" aria-current="${partIndex === index ? "step" : "false"}"><span class="module-index">${state.completed[part.id] ? "✓" : String(partIndex + 1).padStart(2, "0")}</span><span class="module-text"><strong>${esc(part.title)}</strong><small>LESSON · ${String(20 + partIndex * 5)} MIN</small></span></button>`).join("")}</div></aside>
    <div class="lesson-panel">
      <article class="lesson-card"><div class="lesson-topline"><span class="pill pill-lime">Unit ${String(index + 1).padStart(2, "0")}</span><span class="pill">Foundational lecture</span>${state.completed[unit.id] ? '<span class="pill pill-lime">Mastered</span>' : ""}</div>
        <h2>${esc(unit.title)}</h2><div class="objectives"><div class="objectives-title">Learning objectives</div><ul class="objective-list">${unit.objectives.map((objective) => `<li>${esc(objective)}</li>`).join("")}</ul></div>
        <div class="lesson-copy">${prose(unit.notes)}</div><div class="worked-example"><div class="worked-label">Worked example</div><p>${esc(unit.workedExample)}</p></div>
        <div class="lesson-footer"><span>ORIGINAL COURSE NOTES · CHECK THE MODEL'S ASSUMPTIONS</span><div class="footer-actions"><button class="button button-quiet button-small" data-page="study">Open study room ↗</button><button class="button button-quiet button-small" data-page="tools">Lab tools ↗</button></div></div>
      </article>
      ${renderQuestion(unit, unit.check, `${unit.id}:check`, "Concept check", "Apply the principle before moving on.")}
      ${renderNotes(item, unit)}
      <div class="footer-actions" style="justify-content:space-between;margin-top:14px"><button class="button button-secondary" data-module-index="${Math.max(0, index - 1)}" ${index === 0 ? "disabled" : ""}>← Previous lesson</button><button class="button button-primary" data-module-index="${Math.min(item.modules.length - 1, index + 1)}" ${index === item.modules.length - 1 ? 'data-course-tab="map"' : ""}>${index === item.modules.length - 1 ? "View course syllabus" : "Next lesson →"}</button></div>
    </div></div>`;
}

function renderQuestion(unit, q, key, heading, subtitle) {
  const result = state.answers[key];
  const submitted = Boolean(result);
  const selection = result?.value ?? "";
  const choices = q.type === "choice" ? `<fieldset class="choice-list" ${submitted ? "disabled" : ""}><legend class="visually-hidden">${esc(q.prompt)}</legend>${q.choices.map((answer, index) => `<label class="choice-option ${String(selection) === String(index) ? "selected" : ""}"><input type="radio" name="${esc(key)}" value="${index}" ${String(selection) === String(index) ? "checked" : ""} ${submitted ? "disabled" : ""}/><span class="choice-letter">${String.fromCharCode(65 + index)}</span><span>${esc(answer)}</span></label>`).join("")}</fieldset>` : `<div class="numeric-row"><input class="answer-input" type="text" inputmode="decimal" autocomplete="off" id="answer-${esc(key)}" aria-label="Your numerical answer" placeholder="Type a number" value="${submitted ? esc(selection) : ""}" ${submitted ? "disabled" : ""}/><span class="unit-label">${esc(q.unit || "numeric answer")}</span></div>`;
  let feedback = "";
  if (result) {
    feedback = `<div class="feedback ${result.correct ? "correct" : "incorrect"}" role="status"><strong>${result.correct ? "Correct — principle applied." : "Not quite — use the worked clue."}</strong><p>${esc(result.correct ? q.solution : q.hint)}</p>${!result.correct ? `<p><b>Reasoning:</b> ${esc(q.solution)}</p>` : ""}</div>`;
  }
  const actionButton = submitted ? result.correct ? "Completed" : "Try again" : "Check answer";
  return `<article class="learning-card"><div class="learning-card-header"><div><div class="eyebrow">Practice · auto-graded</div><h3>${esc(heading)}</h3><p>${esc(subtitle)}</p></div><span class="question-points">1 POINT</span></div>
    <div class="question-prompt">${esc(q.prompt)}</div>${choices}
    ${feedback}<div class="question-actions"><button class="button ${result?.correct ? "button-secondary" : "button-primary"} button-small" data-grade="${esc(key)}" data-unit="${unit.id}" ${result?.correct ? "disabled" : ""}>${actionButton}</button>${!submitted ? '<span class="hint-text">A hint appears after your first attempt.</span>' : result.correct ? '<span class="hint-text">This unit is marked complete.</span>' : `<button class="button button-quiet button-small" data-reset-answer="${esc(key)}">Clear and retry</button>`}</div>
  </article>`;
}

function renderNotes(item, unit) {
  const key = unit.id;
  const note = state.notes[key] || "";
  return `<section class="notes-card"><div class="notes-card-header"><h3>Lesson notes</h3><span class="saved-label" id="note-status-${key}">${note ? "Saved locally" : "Private to this browser"}</span></div><textarea class="notes-textarea" data-note="${key}" aria-label="Personal notes for ${esc(unit.title)}" placeholder="Capture a question, a connection to another course, or the assumption you want to revisit…">${esc(note)}</textarea></section>`;
}

function renderCourseMap(item) {
  return `<div class="course-map-panel"><article class="lesson-card"><div class="eyebrow">Course syllabus</div><h2>What you will be able to do</h2><ul class="exam-rubric">${item.outcomes.map((outcome) => `<li>${esc(outcome)}</li>`).join("")}</ul><div class="divider"></div><div class="eyebrow">Prerequisites</div><p class="muted small" style="line-height:1.6;margin:7px 0">${esc(item.prerequisites)}</p></article>
    ${item.modules.map((unit, index) => `<article class="map-unit"><div class="map-unit-head"><span class="module-index">${String(index + 1).padStart(2, "0")}</span><strong>${esc(unit.title)}</strong>${state.completed[unit.id] ? '<span class="pill pill-lime" style="margin-left:auto">Complete</span>' : ""}</div><p>${esc(unit.notes.split(".")[0])}.</p><div class="map-objectives">${unit.objectives.map((objective) => `<span>${esc(objective)}</span>`).join("")}</div><div style="margin:12px 0 0 36px"><button class="button button-secondary button-small" data-open-course="${item.id}" data-open-module="${index}">Open lesson →</button></div></article>`).join("")}</div>`;
}

function renderCourseExam(item) {
  const checkKey = `${item.id}:case`;
  const checks = state.rubricChecks[checkKey] || [];
  const draft = state.capstoneDrafts[item.id] || "";
  return `<section class="exam-panel"><div class="eyebrow">Integrative case · short written response</div><h2>Case studio</h2><p>This open-ended case asks you to transfer ideas across the course. The response is saved in your browser; use the rubric to assess whether your argument includes the required evidence. Lesson checks are automatically graded and tracked separately.</p><div class="question-prompt">${esc(item.capstone.prompt)}</div><textarea class="capstone-text" data-capstone="${item.id}" aria-label="Case studio response for ${esc(item.title)}" placeholder="Write a concise argument. State assumptions, calculations, and what evidence would change your conclusion…">${esc(draft)}</textarea><div class="self-rubric">${item.capstone.rubric.map((criterion, index) => `<label class="rubric-check"><input type="checkbox" data-rubric="${item.id}" data-rubric-index="${index}" ${checks[index] ? "checked" : ""}/><span>${esc(criterion)}</span></label>`).join("")}</div><div class="lesson-footer"><span id="case-status">${checks.filter(Boolean).length}/${item.capstone.rubric.length} criteria self-checked · draft saved locally</span><span>Practice case · not an institutional grade</span></div><div class="source-list">${item.sources.map((id) => references[id] ? `<a class="source-link" href="${esc(references[id].url)}" target="_blank" rel="noreferrer">OCW comparator · ${esc(references[id].title)}</a>` : "").join("")}</div></section>`;
}

function renderStudyRoom() {
  const due = dueCards();
  const selected = selectedCardId ? allCards.find((card) => card.id === selectedCardId) : null;
  const current = selected || due[0];
  const filtered = allCards.filter((card) => !studySearch || `${card.front} ${card.back} ${card.courseCode} ${card.lessonTitle}`.toLowerCase().includes(studySearch.toLowerCase())).slice(0, 80);
  const stats = answerStats();
  return `<section class="page-intro"><div><div class="eyebrow">Retrieve · space · connect</div><h1>Study room</h1><p>Review cards from every course, keep private notes, and return to the concepts that need another pass.</p></div><span class="pill pill-lime">${allCards.length} course cards</span></section>
    <div class="study-layout"><div class="study-main"><div class="study-banner"><div><div class="eyebrow">Spaced retrieval</div><h2>${due.length ? `${due.length} cards ready to review` : "Your review queue is clear"}</h2><p>Rate how well you recalled each idea. New cards return on the next visit until you schedule them.</p></div><button class="button button-primary" data-reset-queue>Review due cards →</button></div>
      ${current ? renderFlashcard(current, selected ? "Library card" : "Due for review", due.length) : `<div class="study-empty">You have no due cards. Browse a course card in the library or come back when a review is scheduled.</div>`}
      <div class="notes-card"><div class="notes-card-header"><h3>Cross-course notebook</h3><span class="saved-label">Private to this browser</span></div><textarea class="notes-textarea" data-global-note aria-label="Cross-course notebook" placeholder="Capture a connection between courses, a question for your next session, or a problem to revisit…">${esc(state.notes.global || "")}</textarea></div>
    </div><aside class="study-side"><div class="study-mini-card"><h3>Study snapshot</h3><div class="study-mini-stats"><div class="study-stat"><strong>${stats.attempts}</strong><span>graded checks</span></div><div class="study-stat"><strong>${stats.attempts ? `${stats.accuracy}%` : "—"}</strong><span>recent accuracy</span></div></div><p style="margin-top:10px">Revisit explanations after a miss; use the note area to record assumptions and follow-up questions.</p></div>
      <div class="study-mini-card"><h3>Card library</h3><input class="search-box" id="card-search" value="${esc(studySearch)}" placeholder="Search cards, terms, courses" aria-label="Search flashcards"/><div class="card-library-list">${filtered.slice(0, 35).map((card) => `<div class="library-card-row"><span class="library-card-code">${esc(card.courseCode)}</span><button data-select-card="${card.id}">${esc(card.front)}</button></div>`).join("") || '<p>No cards match that search.</p>'}</div></div>
      <div class="study-mini-card"><h3>Study loop</h3><p>Try retrieval before revealing the back. Mark “Again” when recall was fragile; the scheduler brings it back soon. This lightweight local schedule supports practice, not validated clinical or institutional assessment.</p></div></aside></div>`;
}

function renderFlashcard(card, label, dueCount) {
  return `<article class="study-card"><span class="flash-meta">${esc(card.courseCode)} · ${esc(card.lessonTitle)}</span><span class="flash-progress">${dueCount} DUE</span><div class="flash-label">${cardFlipped ? "Answer" : "Recall the idea"}</div><div class="flash-content ${cardFlipped ? "back" : ""}">${esc(cardFlipped ? card.back : card.front)}</div>
    <div class="flash-controls">${!cardFlipped ? `<button class="button button-primary button-small" data-flip-card>Show answer</button>` : `<button class="rating-button again" data-rate-card="again">Again · 1 min</button><button class="rating-button" data-rate-card="hard">Hard · 1 day</button><button class="rating-button" data-rate-card="good">Good · 3 days</button><button class="rating-button easy" data-rate-card="easy">Easy · 7 days</button>`}</div>
  </article>`;
}

function renderTools() {
  return `<section class="page-intro"><div><div class="eyebrow">Interactive calculators</div><h1>Lab tools</h1><p>Explore the equations behind course examples. Change an input and observe the output; each tool displays its assumptions and units.</p></div><span class="pill pill-blue">6 quick tools</span></section>
    <div class="tool-grid">
      ${renderToolCard("dilution", "Solution prep", "Set a target concentration and final volume.", "⚗", [["stock", "Stock concentration C₁ (mM)", 100], ["target", "Target concentration C₂ (mM)", 2], ["volume", "Final volume V₂ (mL)", 25]], "—", "V₁ = C₂V₂ / C₁")}
      ${renderToolCard("buffer", "Buffer pH", "Estimate pH for a conjugate acid/base pair.", "◉", [["pka", "pKa", 7.2], ["ratio", "Base / acid ratio", 1]], "—", "pH ≈ pKa + log₁₀([A⁻]/[HA])")}
      ${renderToolCard("enzyme", "Enzyme kinetics", "Explore substrate saturation in the Michaelis–Menten model.", "⌁", [["vmax", "Vmax (μmol/min)", 120], ["km", "Km (mM)", 3], ["substrate", "Substrate [S] (mM)", 6]], "—", "v = Vmax[S] / (Km + [S])")}
      ${renderToolCard("rc", "RC low-pass filter", "Estimate cutoff frequency and sinusoidal gain.", "∿", [["resistance", "Resistance R (kΩ)", 10], ["capacitance", "Capacitance C (μF)", 1], ["frequency", "Input frequency f (Hz)", 10]], "—", "fc = 1/(2πRC); |H| = 1/√(1+(f/fc)²)")}
      ${renderToolCard("diffusion", "Diffusion timescale", "Estimate L²/D for a characteristic distance.", "⇢", [["length", "Length L (μm)", 200], ["diffusivity", "Diffusivity D (μm²/s)", 1000]], "—", "td ≈ L² / D · (geometry and boundaries omitted)")}
      ${renderToolCard("ohm", "Ohm’s law", "Check current and power for a resistive load.", "ϟ", [["voltage", "Voltage V (V)", 5], ["load", "Resistance R (kΩ)", 10]], "—", "I = V/R; P = V²/R")}
    </div>
    <div class="tool-callout"><strong>Model boundaries.</strong> These tools are dimensional learning aids. Real buffers require activity and temperature corrections; enzyme kinetics may violate the single-substrate model; RC circuits contain nonideal components; tissue diffusion depends on geometry, consumption, and boundary conditions. Check the assumptions before using an estimate in a design or experiment.</div>`;
}

function renderToolCard(id, title, description, icon, fields, result, formula) {
  return `<article class="tool-card" data-tool="${id}"><div class="tool-card-header"><span class="tool-icon" aria-hidden="true">${icon}</span><div><h3>${esc(title)}</h3><p>${esc(description)}</p></div></div><div class="tool-form">${fields.map(([name, label, value]) => `<div class="field"><label for="${id}-${name}">${esc(label)}</label><input class="field-input" id="${id}-${name}" data-tool-input="${id}" data-name="${name}" type="number" step="any" value="${value}"/></div>`).join("")}</div><div class="tool-result"><strong id="${id}-result">${result}</strong><span id="${id}-detail">Enter values to calculate</span></div><div class="tool-formula">${esc(formula)}</div></article>`;
}

function renderToolResult(toolId) {
  const read = (name) => Number(document.querySelector(`#${toolId}-${name}`)?.value);
  const out = document.querySelector(`#${toolId}-result`);
  const detail = document.querySelector(`#${toolId}-detail`);
  if (!out || !detail) return;
  const validByField = {
    dilution: { stock: (value) => value > 0, target: (value) => value >= 0, volume: (value) => value > 0 },
    buffer: { pka: () => true, ratio: (value) => value > 0 },
    enzyme: { vmax: (value) => value > 0, km: (value) => value > 0, substrate: (value) => value >= 0 },
    rc: { resistance: (value) => value > 0, capacitance: (value) => value > 0, frequency: (value) => value >= 0 },
    diffusion: { length: (value) => value > 0, diffusivity: (value) => value > 0 },
    ohm: { voltage: () => true, load: (value) => value > 0 },
  }[toolId];
  const invalidInput = [...document.querySelectorAll(`[data-tool-input="${toolId}"]`)].some((input) => {
    const value = Number(input.value);
    return !Number.isFinite(value) || !validByField?.[input.dataset.name]?.(value);
  });
  if (invalidInput) {
    out.textContent = "Check inputs"; detail.textContent = "Use finite values and quantities allowed by the model."; return;
  }
  let value = NaN;
  let units = "";
  let aux = "";
  if (toolId === "dilution") {
    const c1 = read("stock"), c2 = read("target"), v2 = read("volume");
    if (c2 > c1) {
      out.textContent = "Not achievable by dilution";
      detail.textContent = "The target concentration exceeds the stock; use a more concentrated stock or a different preparation method.";
      return;
    }
    value = c2 * v2 / c1; units = "mL stock"; aux = Number.isFinite(value) && value <= v2 ? `Bring ${formatNum(v2 - value, 3)} mL stock to ${formatNum(v2, 3)} mL final volume.` : "Target cannot exceed the stock concentration.";
  } else if (toolId === "buffer") {
    const pka = read("pka"), ratio = read("ratio");
    value = pka + Math.log10(ratio); units = "estimated pH"; aux = "Assumes an ideal dilute buffer and both species present.";
  } else if (toolId === "enzyme") {
    const vmax = read("vmax"), km = read("km"), s = read("substrate");
    value = vmax * s / (km + s); units = "μmol/min"; aux = `${formatNum(value / vmax * 100, 1)}% of Vmax · simple single-substrate model`;
  } else if (toolId === "rc") {
    const resistance = read("resistance") * 1000, capacitance = read("capacitance") * 1e-6, f = read("frequency");
    const cutoff = 1 / (2 * Math.PI * resistance * capacitance);
    value = cutoff; units = "Hz cutoff"; aux = `Gain at ${formatNum(f, 2)} Hz: ${formatNum(1 / Math.sqrt(1 + (f / cutoff) ** 2), 3)} · first-order model`;
  } else if (toolId === "diffusion") {
    const length = read("length"), diffusivity = read("diffusivity");
    value = length ** 2 / diffusivity; units = "s characteristic time"; aux = `For L=${formatNum(length, 2)} μm and D=${formatNum(diffusivity, 2)} μm²/s.`;
  } else if (toolId === "ohm") {
    const voltage = read("voltage"), resistance = read("load") * 1000;
    value = voltage / resistance * 1000; units = "mA"; aux = `Power: ${formatNum(voltage ** 2 / resistance * 1000, 3)} mW.`;
  }
  if (!Number.isFinite(value)) {
    out.textContent = "Check inputs"; detail.textContent = "Use values within the model's numeric range."; return;
  }
  out.textContent = `${formatNum(value, toolId === "buffer" ? 2 : 3)} ${units}`;
  detail.textContent = aux;
}

function formatNum(value, digits = 3) {
  if (!Number.isFinite(value)) return "—";
  return Number(value.toPrecision(digits)).toLocaleString("en-US", { maximumFractionDigits: digits });
}

function checkNumeric(value, q) {
  const text = String(value || "").trim();
  const match = text.match(/^([+-]?(?:\d+\.?\d*|\.\d+)(?:e[+-]?\d+)?)\s*(.*)$/i);
  if (!match) return false;
  const numericValue = Number(match[1]);
  if (!Number.isFinite(numericValue) || Math.abs(numericValue - q.answer) > q.tolerance) return false;
  const enteredUnit = match[2].toLowerCase().replace(/[\s·]/g, "").replace(/μ/g, "u").replace(/µ/g, "u");
  const expectedUnit = String(q.unit || "").toLowerCase().replace(/[\s·]/g, "").replace(/μ/g, "u").replace(/µ/g, "u");
  return !enteredUnit || !expectedUnit || enteredUnit === expectedUnit;
}

function gradeQuestion(key, unit) {
  const item = courseById[route.courseId];
  const module = item?.modules[route.moduleIndex];
  const q = module?.check;
  if (!q) return;
  let value;
  let correct;
  if (q.type === "choice") {
    value = document.querySelector(`input[name="${CSS.escape(key)}"]:checked`)?.value;
    if (value === undefined) return;
    correct = Number(value) === q.answer;
  } else {
    value = document.querySelector(`#answer-${CSS.escape(key)}`)?.value;
    if (!String(value || "").trim()) return;
    correct = checkNumeric(value, q);
  }
  const priorAttempts = state.answers[key]?.attempts || 0;
  state.answers[key] = { correct, value, attempts: priorAttempts + 1, updatedAt: Date.now() };
  if (correct) state.completed[unit] = true;
  saveState();
  render();
}

function updateNote(element, key) {
  state.notes[key] = element.value;
  saveState();
  const status = document.querySelector(`#note-status-${CSS.escape(key)}`);
  if (status) status.textContent = "Saved locally";
}

function scheduleCard(cardId, rating) {
  const intervals = { again: 60_000, hard: 86_400_000, good: 3 * 86_400_000, easy: 7 * 86_400_000 };
  state.cardSchedule[cardId] = { dueAt: Date.now() + intervals[rating], rating };
  saveState();
  selectedCardId = null;
  cardFlipped = false;
  render();
}

function saveCapstone(element, courseId) {
  state.capstoneDrafts[courseId] = element.value;
  saveState();
  const status = document.querySelector("#case-status");
  if (status) status.textContent = `${(state.rubricChecks[`${courseId}:case`] || []).filter(Boolean).length}/${courseById[courseId].capstone.rubric.length} criteria self-checked · draft saved locally`;
}

function setRubricCheck(courseId, index, value) {
  const key = `${courseId}:case`;
  const checks = [...(state.rubricChecks[key] || Array(courseById[courseId].capstone.rubric.length).fill(false))];
  checks[index] = value;
  state.rubricChecks[key] = checks;
  saveState();
  const status = document.querySelector("#case-status");
  if (status) status.textContent = `${checks.filter(Boolean).length}/${checks.length} criteria self-checked · draft saved locally`;
}

function handleClick(event) {
  const target = event.target.closest("[data-page], [data-open-course], [data-open-module], [data-module-index], [data-course-tab], [data-grade], [data-reset-answer], [data-bookmark], [data-select-card], [data-flip-card], [data-rate-card], [data-reset-queue], [data-domain]");
  if (!target) return;
  if (target.dataset.openCourse) {
    const index = target.dataset.openModule === undefined ? 0 : Number(target.dataset.openModule);
    openCourse(target.dataset.openCourse, index);
  } else if (target.dataset.page) {
    navigate(target.dataset.page);
  } else if (target.dataset.domain) {
    domainFilter = target.dataset.domain;
    render();
  } else if (target.dataset.courseTab) {
    const index = Number(target.dataset.moduleIndex ?? route.moduleIndex ?? 0);
    navigate(`course/${route.courseId}/${index}/${target.dataset.courseTab}`);
  } else if (target.dataset.moduleIndex !== undefined) {
    const index = Math.max(0, Math.min(courseById[route.courseId].modules.length - 1, Number(target.dataset.moduleIndex)));
    state.visited[courseById[route.courseId].modules[index].id] = true;
    saveState();
    navigate(`course/${route.courseId}/${index}/learn`);
  } else if (target.dataset.grade) {
    gradeQuestion(target.dataset.grade, target.dataset.unit);
  } else if (target.dataset.resetAnswer) {
    delete state.answers[target.dataset.resetAnswer];
    saveState();
    render();
  } else if (target.dataset.bookmark) {
    const id = target.dataset.bookmark;
    state.bookmarks = state.bookmarks.includes(id) ? state.bookmarks.filter((value) => value !== id) : [...state.bookmarks, id];
    saveState(); render();
  } else if (target.dataset.selectCard) {
    selectedCardId = target.dataset.selectCard; cardFlipped = false; render();
  } else if (target.hasAttribute("data-flip-card")) {
    cardFlipped = true; render();
  } else if (target.dataset.rateCard) {
    const current = selectedCardId ? allCards.find((card) => card.id === selectedCardId) : dueCards()[0];
    if (current) scheduleCard(current.id, target.dataset.rateCard);
  } else if (target.hasAttribute("data-reset-queue")) {
    selectedCardId = dueCards()[0]?.id || null; cardFlipped = false; render();
  }
}

function handleInput(event) {
  const element = event.target;
  if (element.matches("[data-note]")) updateNote(element, element.dataset.note);
  if (element.matches("[data-global-note]")) { state.notes.global = element.value; saveState(); }
  if (element.matches("[data-capstone]")) saveCapstone(element, element.dataset.capstone);
  if (element.matches("[data-tool-input]")) renderToolResult(element.dataset.toolInput);
  if (element.matches("#card-search")) {
    studySearch = element.value;
    const list = document.querySelector(".card-library-list");
    if (list) {
      const filtered = allCards.filter((card) => !studySearch || `${card.front} ${card.back} ${card.courseCode} ${card.lessonTitle}`.toLowerCase().includes(studySearch.toLowerCase())).slice(0, 35);
      list.innerHTML = filtered.map((card) => `<div class="library-card-row"><span class="library-card-code">${esc(card.courseCode)}</span><button data-select-card="${card.id}">${esc(card.front)}</button></div>`).join("") || "<p>No cards match that search.</p>";
    }
  }
}

function handleChange(event) {
  const element = event.target;
  if (element.matches("[data-rubric]")) setRubricCheck(element.dataset.rubric, Number(element.dataset.rubricIndex), element.checked);
  if (element.matches("input[type=radio]")) {
    document.querySelectorAll(`input[name="${CSS.escape(element.name)}"]`).forEach((input) => input.closest(".choice-option")?.classList.toggle("selected", input.checked));
  }
}

function handleKeydown(event) {
  if (event.target.matches("#global-search") && event.key === "Enter") {
    query = event.target.value.trim();
    domainFilter = "All courses";
    navigate("catalog");
  }
  if ((event.target.matches(".course-card") || event.target.matches(".continue-card")) && (event.key === "Enter" || event.key === " ")) {
    event.preventDefault();
    openCourse(event.target.dataset.openCourse, Number(event.target.dataset.openModule || 0));
  }
}

appRoot.addEventListener("click", handleClick);
appRoot.addEventListener("input", handleInput);
appRoot.addEventListener("change", handleChange);
appRoot.addEventListener("keydown", handleKeydown);
window.addEventListener("hashchange", () => { route = parseRoute(); render(); });
render();

