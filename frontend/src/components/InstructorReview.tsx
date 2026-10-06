import { useEffect, useState, type FormEvent } from "react";
import { api, errorMessage } from "../api";
import type { InstructorAppeal } from "../types";

function responseText(response: InstructorAppeal["response"]) {
  const value = response.response;
  if (Array.isArray(value)) return value.join(", ");
  if (typeof value === "object") {
    return Object.entries(value)
      .map(([key, item]) => `${key}: ${item}`)
      .join("; ");
  }
  return `${value}${response.unit ? ` ${response.unit}` : ""}`;
}

function ReviewCard({
  appeal,
  onReviewed,
}: {
  appeal: InstructorAppeal;
  onReviewed: () => void;
}) {
  const [decision, setDecision] = useState<"adjusted" | "upheld" | "declined">(
    "upheld",
  );
  const [score, setScore] = useState(appeal.original_score.toString());
  const [note, setNote] = useState("");
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState("");
  async function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setBusy(true);
    setError("");
    try {
      await api.reviewAppeal(
        appeal.id,
        decision,
        note.trim(),
        decision === "adjusted" ? Number(score) : undefined,
      );
      onReviewed();
    } catch (problem) {
      setError(errorMessage(problem));
    } finally {
      setBusy(false);
    }
  }
  return (
    <article className="card instructor-appeal">
      <div className="section-heading">
        <div>
          <span className="eyebrow">
            {appeal.course_id} ·{" "}
            {appeal.content_is_current
              ? appeal.question_id
              : `${appeal.question_id} · old version`}
          </span>
          <h2>Review request from {appeal.learner}</h2>
        </div>
        <span className="tag">
          {appeal.original_score} / {appeal.max_score} automatic
        </span>
      </div>
      {appeal.content_is_current && appeal.question_prompt ? (
        <blockquote>{appeal.question_prompt}</blockquote>
      ) : (
        <p className="notice">
          This attempt’s original course version is unavailable. The response
          cannot be compared to the exact prompt; only a decline explaining this
          limitation can be recorded.
        </p>
      )}
      <h3>Learner response</h3>
      <p className="submitted-response">{responseText(appeal.response)}</p>
      <h3>Automatic feedback</h3>
      <p>{appeal.automatic_feedback.feedback.diagnosis.replaceAll("_", " ")}</p>
      <p>{appeal.automatic_feedback.feedback.next_step}</p>
      <h3>Request</h3>
      <p>{appeal.reason}</p>
      <form className="review-form" onSubmit={submit}>
        <fieldset>
          <legend>Decision</legend>
          <label>
            <input
              type="radio"
              name={`decision-${appeal.id}`}
              checked={decision === "adjusted"}
              onChange={() => setDecision("adjusted")}
              disabled={!appeal.content_is_current}
            />
            Adjust practice score
          </label>
          <label>
            <input
              type="radio"
              name={`decision-${appeal.id}`}
              checked={decision === "upheld"}
              onChange={() => setDecision("upheld")}
              disabled={!appeal.content_is_current}
            />
            Uphold automatic score
          </label>
          <label>
            <input
              type="radio"
              name={`decision-${appeal.id}`}
              checked={decision === "declined"}
              onChange={() => setDecision("declined")}
            />
            Decline request
          </label>
        </fieldset>
        {decision === "adjusted" ? (
          <label>
            Reviewed practice score (0–{appeal.max_score})
            <input
              type="number"
              min={0}
              max={appeal.max_score}
              step="any"
              value={score}
              onChange={(event) => setScore(event.target.value)}
              required
            />
          </label>
        ) : null}
        <label>
          Review note (visible to the learner)
          <textarea
            value={note}
            onChange={(event) => setNote(event.target.value)}
            minLength={10}
            maxLength={4000}
            rows={3}
            required
          />
        </label>
        <button
          className="primary"
          type="submit"
          disabled={busy || note.trim().length < 10}
        >
          {busy ? "Recording decision…" : "Record review decision"}
        </button>
        {error ? (
          <p role="alert" className="error">
            {error}
          </p>
        ) : null}
      </form>
    </article>
  );
}

export function InstructorReview() {
  const [appeals, setAppeals] = useState<InstructorAppeal[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  async function load() {
    setLoading(true);
    setError("");
    try {
      setAppeals(await api.instructorAppeals());
    } catch (problem) {
      setError(errorMessage(problem));
    } finally {
      setLoading(false);
    }
  }
  useEffect(() => {
    void load();
  }, []);
  return (
    <section className="instructor-review" aria-labelledby="review-title">
      <span className="eyebrow">Authorized instructor workspace</span>
      <h1 id="review-title">Human review requests</h1>
      <p className="notice">
        Decisions apply only to the formative practice record. The original
        deterministic score is retained, each decision is auditable, and
        reviewed points do not represent course credit.
      </p>
      {error ? (
        <p role="alert" className="error">
          {error}
        </p>
      ) : null}
      {loading ? <p role="status">Loading review requests…</p> : null}
      {!loading && appeals.length === 0 && !error ? (
        <p>No open requests.</p>
      ) : null}
      {appeals.map((appeal) => (
        <ReviewCard
          key={appeal.id}
          appeal={appeal}
          onReviewed={() => void load()}
        />
      ))}
    </section>
  );
}
