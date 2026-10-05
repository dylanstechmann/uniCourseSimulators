export const STORAGE_KEY = "lattice-courselab:guest:v2";
const PREVIOUS_KEY = "lattice-academy:v1"; // Read-only compatibility for existing learner data.
export const BACKUP_KEY = "lattice-courselab:guest:pre-migration-backup";

export const freshState = () => ({ completed: {}, visited: {}, answers: {}, notes: {}, capstoneDrafts: {}, rubricChecks: {}, cardSchedule: {}, bookmarks: [], lastCourseId: "cell-biology" });
const record = (value) => value && typeof value === "object" && !Array.isArray(value);
const mapValues = (value, valid) => record(value) ? Object.fromEntries(Object.entries(value).filter(([key, item]) => key.length < 200 && !["__proto__", "constructor", "prototype"].includes(key) && valid(item))) : {};

export function sanitizeState(value) {
  const state = freshState();
  if (!record(value)) return state;
  state.completed = mapValues(value.completed, (v) => v === true);
  state.visited = mapValues(value.visited, (v) => v === true);
  state.notes = mapValues(value.notes, (v) => typeof v === "string" && v.length <= 100000);
  state.capstoneDrafts = mapValues(value.capstoneDrafts, (v) => typeof v === "string" && v.length <= 100000);
  state.rubricChecks = mapValues(value.rubricChecks, (v) => Array.isArray(v) && v.every((x) => typeof x === "boolean"));
  state.answers = mapValues(value.answers, (v) => record(v) && typeof v.correct === "boolean" && ["string", "number"].includes(typeof v.value) && Number.isInteger(v.attempts) && v.attempts >= 1);
  state.cardSchedule = mapValues(value.cardSchedule, (v) => record(v) && Number.isFinite(v.dueAt) && ["again", "hard", "good", "easy"].includes(v.rating));
  state.bookmarks = Array.isArray(value.bookmarks) ? [...new Set(value.bookmarks.filter((v) => typeof v === "string" && v.length < 200))] : [];
  if (typeof value.lastCourseId === "string") state.lastCourseId = value.lastCourseId;
  return state;
}

export function loadGuestState(storage) {
  try {
    const current = storage.getItem(STORAGE_KEY);
    if (current !== null) return sanitizeState(JSON.parse(current));
    const previous = storage.getItem(PREVIOUS_KEY);
    if (previous === null) return freshState();
    const migrated = sanitizeState(JSON.parse(previous));
    storage.setItem(BACKUP_KEY, previous);
    storage.setItem(STORAGE_KEY, JSON.stringify(migrated));
    storage.setItem(`${STORAGE_KEY}:migration`, JSON.stringify({ version: 2, importedAt: new Date().toISOString(), trust: "unverified browser practice" }));
    return migrated;
  } catch { return freshState(); }
}
