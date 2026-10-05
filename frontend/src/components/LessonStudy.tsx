import { useEffect, useState } from "react";
import { errorMessage } from "../api";
import type { Attempt, Lesson, Note, Source } from "../types";
import { Assessment } from "./Assessment";
import { MarkdownReader } from "./MarkdownReader";

export function LessonStudy({
  lesson,
  enabled,
  disabledMessage,
  note,
  completed,
  attempts,
  sources,
  onAttempt,
  onSaveNote,
  onProgress,
}: {
  lesson: Lesson;
  enabled: boolean;
  disabledMessage?: string;
  note?: Note;
  completed: boolean;
  attempts: Attempt[];
  sources: Source[];
  onAttempt: (
    question: string,
    response: string | number | number[],
    unit?: string,
    variantToken?: string | null,
  ) => Promise<Attempt>;
  onSaveNote: (body: string) => Promise<void>;
  onProgress: (completed: boolean) => Promise<void>;
}) {
  const [body, setBody] = useState(note?.body || "");
  const [status, setStatus] = useState("");
  const [error, setError] = useState("");
  const [busy, setBusy] = useState(false);
  useEffect(() => {
    setBody(note?.body || "");
  }, [note?.body, lesson.id]);
  async function saveNote() {
    setBusy(true);
    setError("");
    try {
      await onSaveNote(body);
      setStatus("Note saved.");
    } catch (error) {
      setError(errorMessage(error));
    } finally {
      setBusy(false);
    }
  }
  async function markRead() {
    setBusy(true);
    setError("");
    try {
      await onProgress(!completed);
      setStatus(
        completed
          ? "Reading mark removed."
          : "Lesson marked as read. This is a self-report, not mastery.",
      );
    } catch (error) {
      setError(errorMessage(error));
    } finally {
      setBusy(false);
    }
  }
  return (
    <>
      <article className="card lesson-reader">
        <span className="eyebrow">Lesson · original content</span>
        <h2>{lesson.title}</h2>
        <MarkdownReader>{lesson.markdown}</MarkdownReader>
        {lesson.worked_example && (
          <section className="worked-example">
            <h3>Worked example</h3>
            <MarkdownReader>{lesson.worked_example}</MarkdownReader>
          </section>
        )}
        <section className="sources">
          <h3>Source alignment references</h3>
          <ul>
            {lesson.source_ids.map((id) => {
              const source = sources.find((item) => item.id === id);
              return (
                <li key={id}>
                  {source ? (
                    <a href={source.url} rel="noreferrer" target="_blank">
                      {source.title}{" "}
                      <span className="sr-only">(opens in a new tab)</span>
                    </a>
                  ) : (
                    <span>{id}</span>
                  )}
                </li>
              );
            })}
          </ul>
          <p className="muted">
            Sources are scope comparators. They do not establish equivalent
            content depth or institutional endorsement.
          </p>
        </section>
        <button
          onClick={markRead}
          disabled={!enabled || busy}
          aria-pressed={completed}
        >
          {completed ? "Marked as read — undo" : "Mark as read"}
        </button>
        <p className="muted">
          Reading progress is learner-marked and separate from practice results.
        </p>
      </article>
      {lesson.questions.map((question) => (
        <Assessment
          key={question.id}
          question={question}
          enabled={enabled}
          disabledMessage={disabledMessage}
          previousAttempt={[...attempts]
            .reverse()
            .find(
              (attempt) =>
                attempt.question_id === question.id &&
                (attempt.response.variant_id ?? null) ===
                  (question.variant_id ?? null),
            )}
          onSubmit={(response, unit, variantToken) =>
            onAttempt(question.id, response, unit, variantToken)
          }
        />
      ))}
      <section className="card">
        <h2>Lesson notes</h2>
        <label>
          Your private note
          <textarea
            value={body}
            onChange={(event) => {
              setBody(event.target.value);
              setStatus("");
            }}
            maxLength={20000}
            rows={6}
            disabled={!enabled}
          />
        </label>
        <button onClick={saveNote} disabled={!enabled || busy}>
          {busy ? "Saving…" : "Save note"}
        </button>
        {!enabled && (
          <p className="muted">
            {disabledMessage ||
              "Enroll to save notes to your account or guest session."}
          </p>
        )}
        {status && <p role="status">{status}</p>}
        {error && (
          <p role="alert" className="error">
            {error}
          </p>
        )}
      </section>
    </>
  );
}
