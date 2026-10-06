export const STORAGE_KEY = "uni-stem-course-simulators:guest:v3";
// Read-only compatibility identifiers for both previous product names.
const PREVIOUS_KEYS = ["lattice-courselab:guest:v2", "lattice-academy:v1"];
export const BACKUP_KEY = "uni-stem-course-simulators:guest:pre-migration-backup";

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
    for (const sourceKey of PREVIOUS_KEYS) {
      const previous = storage.getItem(sourceKey);
      if (previous === null) continue;
      let parsed;
      try { parsed = JSON.parse(previous); } catch { continue; }
      if (!record(parsed)) continue;
      const migrated = sanitizeState(parsed);
      // Do not overwrite retained backups or delete previous notebooks.
      try {
        if (storage.getItem(BACKUP_KEY) === null) storage.setItem(BACKUP_KEY, previous);
        storage.setItem(STORAGE_KEY, JSON.stringify(migrated));
        storage.setItem(`${STORAGE_KEY}:migration`, JSON.stringify({ version: 3, sourceKey, importedAt: new Date().toISOString(), trust: "unverified browser practice" }));
      } catch { /* A full/read-only store must not hide a readable previous notebook. */ }
      return migrated;
    }
    return freshState();
  } catch { return freshState(); }
}
