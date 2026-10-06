import { useEffect, useState } from "react";
import { api, errorMessage } from "../api";
import type {
  Attempt,
  Course,
  CourseSummary,
  Gradebook,
  Lesson,
  Note,
  Progress,
  Source,
} from "../types";
import { GradebookView } from "./GradebookView";
import { LessonStudy } from "./LessonStudy";
import { MarkdownReader } from "./MarkdownReader";
import { MaturityBadge } from "./MaturityBadge";

export function CourseWorkspace({
  id,
  lessonId,
  showGradebook,
  enrollmentVersion,
  catalog,
  enrolled,
  hasSession,
  bookmarked,
  sources,
  onEnroll,
  onUpgrade,
  onBookmark,
}: {
  id: string;
  lessonId?: string;
  showGradebook: boolean;
  enrollmentVersion?: string;
  catalog: CourseSummary[];
  enrolled: boolean;
  hasSession: boolean;
  bookmarked: boolean;
  sources: Source[];
  onEnroll: () => Promise<void>;
  onUpgrade: () => Promise<void>;
  onBookmark: (saved: boolean) => Promise<void>;
}) {
  const [course, setCourse] = useState<Course | null>(null);
  const [lesson, setLesson] = useState<Lesson | null>(null);
  const [progress, setProgress] = useState<Progress[]>([]);
  const [notes, setNotes] = useState<Note[]>([]);
  const [attempts, setAttempts] = useState<Attempt[]>([]);
  const [gradebook, setGradebook] = useState<Gradebook | null>(null);
  const [error, setError] = useState("");
  const [busy, setBusy] = useState(false);
  useEffect(() => {
    let active = true;
    setCourse(null);
    setError("");
    api
      .course(id)
      .then((data) => {
        if (active) setCourse(data);
      })
      .catch((error) => {
        if (active) setError(errorMessage(error));
      });
    return () => {
      active = false;
    };
  }, [id]);
  useEffect(() => {
    let active = true;
    setLesson(null);
    if (lessonId)
      api
        .lesson(id, lessonId)
        .then((data) => {
          if (active) setLesson(data);
        })
        .catch((error) => {
          if (active) setError(errorMessage(error));
        });
    return () => {
      active = false;
    };
  }, [id, lessonId]);
  useEffect(() => {
    let active = true;
    if (
      !enrolled ||
      !course ||
      (enrollmentVersion && enrollmentVersion !== course.version)
    ) {
      setProgress([]);
      setNotes([]);
      setAttempts([]);
      setGradebook(null);
      return;
    }
    Promise.all([
      api.progress(id),
      api.notes(id),
      api.attempts(id),
      api.gradebook(id),
    ])
      .then(([progress, notes, attempts, gradebook]) => {
        if (active) {
          setProgress(progress);
          setNotes(notes);
          setAttempts(attempts);
          setGradebook(gradebook);
        }
      })
      .catch((error) => {
        if (active) setError(errorMessage(error));
      });
    return () => {
      active = false;
    };
  }, [id, enrolled, course, enrollmentVersion]);
  async function enroll() {
    setBusy(true);
    setError("");
    try {
      await onEnroll();
    } catch (error) {
      setError(errorMessage(error));
    } finally {
      setBusy(false);
    }
  }
  async function bookmark() {
    setBusy(true);
    setError("");
    try {
      await onBookmark(!bookmarked);
    } catch (error) {
      setError(errorMessage(error));
    } finally {
      setBusy(false);
    }
  }
  async function upgrade() {
    setBusy(true);
    setError("");
    try {
      await onUpgrade();
    } catch (error) {
      setError(errorMessage(error));
    } finally {
      setBusy(false);
    }
  }
  async function submit(
    question: string,
    response: string | number | number[] | Record<string, string>,
    unit?: string,
    variantToken?: string | null,
  ) {
    const attempt = await api.attempt(
      id,
      question,
      response,
      unit,
      variantToken,
    );
    setAttempts((previous) => [...previous, attempt]);
    setGradebook(await api.gradebook(id));
    return attempt;
  }
  async function requestAppeal(attemptId: string, reason: string) {
    const appeal = await api.requestAppeal(attemptId, reason);
    setAttempts((previous) =>
      previous.map((attempt) =>
        attempt.id === attemptId
          ? { ...attempt, appeal, effective_score: appeal.effective_score }
          : attempt,
      ),
    );
    setGradebook(await api.gradebook(id));
    return appeal;
  }
  async function saveNote(body: string) {
    const note = await api.saveNote(id, lessonId!, body);
    setNotes((previous) => [
      ...previous.filter((item) => item.lesson_id !== lessonId),
      note,
    ]);
  }
  async function markProgress(completed: boolean) {
    const mark = await api.setProgress(id, lessonId!, completed);
    setProgress((previous) => [
      ...previous.filter((item) => item.lesson_id !== lessonId),
      mark,
    ]);
  }
  const courseLink = `#/course/${encodeURIComponent(id)}`;
  function prerequisites(ids: string[]) {
    return ids.length ? (
      <ul>
        {ids.map((prerequisite) => (
          <li key={prerequisite}>
            <a href={`#/course/${encodeURIComponent(prerequisite)}`}>
              {catalog.find((item) => item.id === prerequisite)?.title ||
                prerequisite}
            </a>
          </li>
        ))}
      </ul>
    ) : (
      <p>None represented in the current course graph.</p>
    );
  }
  if (!course)
    return (
      <>
        <h1>Course workspace</h1>
        {error ? (
          <p className="error" role="alert">
            {error}
          </p>
        ) : (
          <p role="status">Loading course…</p>
        )}
      </>
    );
  const needsVersionReview = Boolean(
    enrolled && enrollmentVersion && enrollmentVersion !== course.version,
  );
  return (
    <>
      <div className="section-heading">
        <div>
          <span className="eyebrow">
            {course.domain} · {course.level}
          </span>
          <h1>{course.title}</h1>
          <div className="inline-meta">
            <MaturityBadge maturity={course.maturity} />
            <span>Content v{course.version}</span>
            <span>{course.lesson_count} available lessons</span>
          </div>
        </div>
        <div className="actions">
          {!enrolled && (
            <button
              className="primary"
              onClick={enroll}
              disabled={!hasSession || busy}
            >
              Enroll in partial course
            </button>
          )}
          {enrolled && <span className="tag">Enrolled</span>}
          <button
            onClick={bookmark}
            disabled={!hasSession || busy}
            aria-pressed={bookmarked}
          >
            {bookmarked ? "Remove bookmark" : "Bookmark course"}
          </button>
        </div>
      </div>
      <p className="lead">{course.description}</p>
      {needsVersionReview && (
        <aside className="notice" aria-label="Course content update">
          <strong>Course content updated</strong>
          <p>
            Your saved attempts and reading marks remain attached to version{" "}
            {enrollmentVersion}. Review the current partial package and update
            your enrollment to continue saving work.
          </p>
          <button
            className="primary"
            onClick={upgrade}
            disabled={!hasSession || busy}
          >
            Update enrollment to version {course.version}
          </button>
        </aside>
      )}
      {!hasSession && (
        <p className="notice">
          <a href="#/account">Start a guest session or sign in</a> to enroll and
          save work. Public lesson reading remains available.
        </p>
      )}
      {course.limitations.length > 0 && (
        <aside className="notice" aria-label="Course limitations">
          <strong>Current limitations</strong>
          <ul>
            {course.limitations.map((limitation, index) => (
              <li key={index}>{limitation}</li>
            ))}
          </ul>
        </aside>
      )}
      {error && (
        <p role="alert" className="error">
          {error}
        </p>
      )}
      <nav className="tabs" aria-label="Course views">
        <a
          href={courseLink}
          aria-current={!lessonId && !showGradebook ? "page" : undefined}
        >
          Syllabus and lessons
        </a>
        <a
          href={`${courseLink}/gradebook`}
          aria-current={showGradebook ? "page" : undefined}
        >
          Practice gradebook
        </a>
      </nav>
      <div className="workspace-grid">
        <aside className="card lesson-navigation">
          <h2>Available lessons</h2>
          <p className="muted">
            {progress.filter((item) => item.completed).length} marked read. This
            is self-reported progress.
          </p>
          <nav aria-label="Lessons">
            {course.modules.map((module) => (
              <section key={module.id}>
                <h3>{module.title}</h3>
                <ol>
                  {module.lessons.map((item) => (
                    <li key={item.id}>
                      <a
                        href={`${courseLink}/lesson/${encodeURIComponent(item.id)}`}
                        aria-current={lessonId === item.id ? "page" : undefined}
                      >
                        {item.title}
                      </a>
                      {progress.some(
                        (mark) => mark.lesson_id === item.id && mark.completed,
                      ) && <span className="read-label">Read</span>}
                    </li>
                  ))}
                </ol>
              </section>
            ))}
          </nav>
        </aside>
        <div className="workspace-main">
          {showGradebook ? (
            enrolled && !needsVersionReview && gradebook ? (
              <GradebookView
                gradebook={gradebook}
                attempts={attempts}
                course={course}
              />
            ) : (
              <section className="card">
                <h2>Practice gradebook</h2>
                <p>
                  {needsVersionReview
                    ? "Update your enrollment to access current practice tools. Prior attempts and feedback remain available after the update."
                    : enrolled
                      ? "Loading saved practice evidence…"
                      : "Enroll to view your practice attempts and gradebook."}
                </p>
              </section>
            )
          ) : lessonId ? (
            lesson ? (
              <LessonStudy
                key={lesson.id}
                lesson={lesson}
                enabled={enrolled && !needsVersionReview}
                disabledMessage={
                  needsVersionReview
                    ? "Update your enrollment before saving new attempts or reading progress."
                    : undefined
                }
                note={notes.find((item) => item.lesson_id === lessonId)}
                completed={progress.some(
                  (item) => item.lesson_id === lessonId && item.completed,
                )}
                attempts={attempts}
                sources={sources}
                onAttempt={submit}
                onAppeal={requestAppeal}
                onSaveNote={saveNote}
                onProgress={markProgress}
              />
            ) : (
              <p role="status">Loading lesson…</p>
            )
          ) : (
            <>
              <section className="card">
                <h2>Syllabus</h2>
                <MarkdownReader>{course.syllabus_markdown}</MarkdownReader>
                <h3>Prerequisite knowledge</h3>
                <p>{course.prerequisites.statement}</p>
                <ul>
                  {course.prerequisites.knowledge.map((knowledge, index) => (
                    <li key={index}>{knowledge}</li>
                  ))}
                </ul>
                <h3>Required course dependencies</h3>
                {prerequisites(course.prerequisites.course_ids)}
                <h3>Recommended preparation</h3>
                {prerequisites(course.prerequisites.recommended_course_ids)}
                <h3>Concurrent course dependencies</h3>
                {prerequisites(course.prerequisites.concurrent_course_ids)}
                <p className="muted">
                  These are uniStemCourseSimulators learning dependencies. They
                  do not establish university prerequisite equivalency.
                </p>
              </section>
              <section className="card">
                <h2>Learning outcomes</h2>
                <ul className="objectives">
                  {course.outcomes.map((objective) => (
                    <li key={objective.id}>
                      <span className="tag">{objective.bloom}</span>{" "}
                      {objective.description}
                    </li>
                  ))}
                </ul>
                <p className="muted">
                  Content license: {course.license}. Completion and external
                  review are not claimed for this partial package.
                </p>
              </section>
            </>
          )}
        </div>
      </div>
    </>
  );
}
