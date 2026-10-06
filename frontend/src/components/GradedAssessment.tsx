import { useEffect, useState, type FormEvent } from "react";
import { api, errorMessage } from "../api";
import type {
  AssessmentAnswer,
  GradedAssessment as GradedAssessmentData,
  GradedSubmissionAppeal,
  GradedSubmission,
  Question,
} from "../types";

async function fileAsBase64(file: File): Promise<string> {
  const bytes = new Uint8Array(await file.arrayBuffer());
  let binary = "";
  for (const byte of bytes) binary += String.fromCharCode(byte);
  return btoa(binary);
}

function textValue(answer: AssessmentAnswer | undefined) {
  return typeof answer?.response === "string" ? answer.response : "";
}

function objectValue(answer: AssessmentAnswer | undefined) {
  return answer?.response &&
    typeof answer.response === "object" &&
    !Array.isArray(answer.response)
    ? answer.response
    : {};
}

function GradedQuestion({
  question,
  answer,
  disabled,
  onChange,
}: {
  question: Question;
  answer?: AssessmentAnswer;
  disabled: boolean;
  onChange: (value: AssessmentAnswer) => void;
}) {
  const response = answer?.response;
  const checked = Array.isArray(response) ? response : [];
  const fields = objectValue(answer);
  return (
    <fieldset className="assessment card" disabled={disabled}>
      <legend>
        {question.prompt}{" "}
        <span className="muted">· {question.points} points</span>
      </legend>
      {question.type === "single_choice" ? (
        <div className="choices">
          {question.options.map((option, index) => (
            <label className="choice" key={index}>
              <input
                type="radio"
                name={`graded-${question.id}`}
                checked={response === index}
                onChange={() => onChange({ response: index })}
              />
              <span>{option}</span>
            </label>
          ))}
        </div>
      ) : question.type === "multiple_select" ? (
        <>
          <p className="muted">
            Select all that apply. The stated scoring policy is applied to this
            saved attempt.
          </p>
          <div className="choices">
            {question.options.map((option, index) => (
              <label className="choice" key={index}>
                <input
                  type="checkbox"
                  checked={checked.includes(index)}
                  onChange={() =>
                    onChange({
                      response: checked.includes(index)
                        ? checked.filter((item) => item !== index)
                        : [...checked, index].sort((a, b) => a - b),
                    })
                  }
                />
                <span>{option}</span>
              </label>
            ))}
          </div>
        </>
      ) : question.type === "numeric" || question.type === "symbolic" ? (
        <div className="input-grid">
          <div>
            <label htmlFor={`graded-${question.id}-answer`}>
              {question.type === "numeric" ? "Numerical answer" : "Expression"}
            </label>
            <input
              id={`graded-${question.id}-answer`}
              value={textValue(answer)}
              onChange={(event) =>
                onChange({ response: event.target.value, unit: answer?.unit })
              }
              maxLength={1000}
              autoComplete="off"
            />
          </div>
          {question.type === "numeric" && question.unit && (
            <div>
              <label htmlFor={`graded-${question.id}-unit`}>Unit</label>
              <input
                id={`graded-${question.id}-unit`}
                value={answer?.unit ?? ""}
                onChange={(event) =>
                  onChange({
                    response: textValue(answer),
                    unit: event.target.value,
                  })
                }
                maxLength={100}
                placeholder={question.unit}
              />
            </div>
          )}
        </div>
      ) : question.type === "structured" ||
        question.type === "data_interpretation" ? (
        <div className="stack">
          <p className="muted">
            Each field is scored independently by its published deterministic
            rubric.
          </p>
          {(question.response_fields ?? []).map((field) => (
            <div className="input-grid" key={field.id}>
              {field.type === "numeric" ? (
                <div>
                  <label htmlFor={`graded-${question.id}-${field.id}`}>
                    {field.prompt} · {field.points} points
                  </label>
                  <input
                    id={`graded-${question.id}-${field.id}`}
                    value={fields[field.id] ?? ""}
                    onChange={(event) =>
                      onChange({
                        response: {
                          ...fields,
                          [field.id]: event.target.value,
                        },
                      })
                    }
                    maxLength={1000}
                    placeholder={`Value with unit${field.unit ? ` · ${field.unit}` : ""}`}
                  />
                </div>
              ) : (
                <div>
                  <label htmlFor={`graded-${question.id}-${field.id}`}>
                    {field.prompt} · {field.points} points
                  </label>
                  <select
                    id={`graded-${question.id}-${field.id}`}
                    value={fields[field.id] ?? ""}
                    onChange={(event) =>
                      onChange({
                        response: {
                          ...fields,
                          [field.id]: event.target.value,
                        },
                      })
                    }
                  >
                    <option value="">Choose an answer</option>
                    {field.options.map((option, index) => (
                      <option value={index} key={index}>
                        {option}
                      </option>
                    ))}
                  </select>
                </div>
              )}
            </div>
          ))}
        </div>
      ) : question.type === "graph" && question.graph_spec ? (
        <div className="stack">
          <p className="muted">
            Enter the requested coordinates. Axes:{" "}
            {question.graph_spec.x_axis.label};{" "}
            {question.graph_spec.y_axis.label}.
          </p>
          <table>
            <caption>Replicate measurements for the graph</caption>
            <thead>
              <tr>
                <th scope="col">Group</th>
                <th scope="col">{question.graph_spec.x_axis.label}</th>
                <th scope="col">
                  Replicate values · {question.graph_spec.y_axis.label}
                </th>
              </tr>
            </thead>
            <tbody>
              {question.graph_spec.observations.map((observation) => (
                <tr key={observation.id}>
                  <th scope="row">
                    {question.graph_spec?.points.find(
                      (item) => item.id === observation.id,
                    )?.label ?? observation.id}
                  </th>
                  <td>{observation.x}</td>
                  <td>{observation.values.join(", ")}</td>
                </tr>
              ))}
            </tbody>
          </table>
          <div className="input-grid">
            {question.graph_spec.points.map((point) => (
              <fieldset key={point.id}>
                <legend>{point.label}</legend>
                {(["x", "y"] as const).map((coordinate) => {
                  const key = `${point.id}_${coordinate}`;
                  const axis =
                    coordinate === "x"
                      ? question.graph_spec!.x_axis
                      : question.graph_spec!.y_axis;
                  return (
                    <div key={coordinate}>
                      <label htmlFor={`graded-${question.id}-${key}`}>
                        {axis.label}
                      </label>
                      <input
                        id={`graded-${question.id}-${key}`}
                        inputMode="decimal"
                        value={fields[key] ?? ""}
                        onChange={(event) =>
                          onChange({
                            response: { ...fields, [key]: event.target.value },
                          })
                        }
                      />
                    </div>
                  );
                })}
              </fieldset>
            ))}
          </div>
        </div>
      ) : question.type === "file_upload" ? (
        <div>
          <label htmlFor={`graded-${question.id}-file`}>
            Upload CSV analysis
          </label>
          <input
            id={`graded-${question.id}-file`}
            type="file"
            accept={question.accepted_media_types?.join(",") || ".csv,text/csv"}
            onChange={async (event) => {
              const file = event.currentTarget.files?.[0];
              if (!file) return;
              if (file.size > (question.max_upload_bytes ?? 32768)) {
                onChange({ response: "" });
                return;
              }
              onChange({
                response: { content_base64: await fileAsBase64(file) },
              });
            }}
          />
          {question.max_upload_bytes && (
            <small>Maximum size: {question.max_upload_bytes} bytes.</small>
          )}
        </div>
      ) : (
        <p role="alert">
          This question type does not have a supported response form.
        </p>
      )}
    </fieldset>
  );
}

function SubmissionFeedback({
  submission,
  onAppeal,
}: {
  submission: GradedSubmission;
  onAppeal: (
    submissionId: string,
    reason: string,
  ) => Promise<GradedSubmissionAppeal>;
}) {
  const [reason, setReason] = useState("");
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState("");
  async function requestReview(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (reason.trim().length < 20) return;
    setBusy(true);
    setError("");
    try {
      await onAppeal(submission.id, reason.trim());
      setReason("");
    } catch (problem) {
      setError(errorMessage(problem));
    } finally {
      setBusy(false);
    }
  }
  return (
    <section
      className="notice"
      aria-label={`Attempt ${submission.attempt_number} results`}
    >
      <h3>
        Attempt {submission.attempt_number}: {submission.effective_score} /{" "}
        {submission.max_score} points
      </h3>
      <p>
        {submission.effective_score_percent}% after review. Automatic score:{" "}
        {submission.score} / {submission.max_score}. Deterministic criteria set
        the original score; instructor adjustments are recorded separately.
      </p>
      <ul>
        {submission.results.map((result) => (
          <li key={result.question_id}>
            <strong>{result.question_id}</strong>: {result.score} /{" "}
            {result.max_score} ·{" "}
            {result.feedback.diagnosis.replaceAll("_", " ")}.
            {result.feedback.hint && <span> Hint: {result.feedback.hint}</span>}
            <div>{result.feedback.next_step}</div>
          </li>
        ))}
      </ul>
      {submission.appeal ? (
        <div className="appeal-status" aria-label="Assignment review status">
          <h4>Human review · {submission.appeal.status}</h4>
          <p>{submission.appeal.reason}</p>
          {submission.appeal.review_note && (
            <p>{submission.appeal.review_note}</p>
          )}
          {submission.appeal.status === "open" ? (
            <p>Your request is saved for an authorized instructor to review.</p>
          ) : submission.appeal.status === "adjusted" ? (
            <p>
              The reviewed score is {submission.appeal.effective_score} /{" "}
              {submission.appeal.max_score}. The automatic score remains saved
              as {submission.appeal.original_score}.
            </p>
          ) : (
            <p>
              The automatic score remains {submission.appeal.original_score}.
            </p>
          )}
        </div>
      ) : (
        <form className="appeal-form" onSubmit={requestReview}>
          <label htmlFor={`graded-${submission.id}-appeal-reason`}>
            Request human review
          </label>
          <textarea
            id={`graded-${submission.id}-appeal-reason`}
            value={reason}
            onChange={(event) => setReason(event.target.value)}
            minLength={20}
            maxLength={4000}
            rows={3}
            required
            placeholder="Explain what the grader or rubric may have missed."
          />
          <button type="submit" disabled={busy || reason.trim().length < 20}>
            {busy ? "Saving request…" : "Send for human review"}
          </button>
          {error && (
            <p role="alert" className="error">
              {error}
            </p>
          )}
        </form>
      )}
    </section>
  );
}

export function GradedAssessment({
  courseId,
  assessmentId,
  enabled,
  history,
  onSubmitted,
  onAppeal,
}: {
  courseId: string;
  assessmentId: string;
  enabled: boolean;
  history: GradedSubmission[];
  onSubmitted: (submission: GradedSubmission) => Promise<void>;
  onAppeal: (
    submissionId: string,
    reason: string,
  ) => Promise<GradedSubmissionAppeal>;
}) {
  const [assessment, setAssessment] = useState<GradedAssessmentData | null>(
    null,
  );
  const [answers, setAnswers] = useState<Record<string, AssessmentAnswer>>({});
  const [localSubmissions, setLocalSubmissions] = useState<GradedSubmission[]>(
    [],
  );
  const [loading, setLoading] = useState(true);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    let active = true;
    setLoading(true);
    setError("");
    setAssessment(null);
    setAnswers({});
    setLocalSubmissions([]);
    api
      .gradedAssessment(courseId, assessmentId)
      .then((data) => {
        if (active) setAssessment(data);
      })
      .catch((loadError) => {
        if (active) setError(errorMessage(loadError));
      })
      .finally(() => {
        if (active) setLoading(false);
      });
    return () => {
      active = false;
    };
  }, [courseId, assessmentId]);

  const assessmentHistory = [...history, ...localSubmissions]
    .filter((item) => item.assessment_id === assessmentId)
    .filter(
      (item, index, all) =>
        all.findIndex((candidate) => candidate.id === item.id) === index,
    )
    .sort((left, right) => left.attempt_number - right.attempt_number);
  const limitReached = Boolean(
    assessment?.attempt_limit !== null &&
    assessment?.attempt_limit !== undefined &&
    assessment.attempts_used >= assessment.attempt_limit,
  );

  function setAnswer(question: Question, answer: AssessmentAnswer) {
    setAnswers((previous) => ({ ...previous, [question.id]: answer }));
  }

  async function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (!assessment || !enabled || assessment.schedule_status !== "open")
      return;
    setError("");
    const missing = assessment.questions.find((question) => {
      const response = answers[question.id]?.response;
      if (response === undefined || response === "") return true;
      if (Array.isArray(response)) return response.length === 0;
      if (typeof response === "object")
        return Object.keys(response).length === 0;
      return false;
    });
    if (missing) {
      setError(`Enter a response for ${missing.id} before submitting.`);
      return;
    }
    setBusy(true);
    try {
      const submission = await api.submitGradedAssessment(
        courseId,
        assessmentId,
        answers,
      );
      setAnswers({});
      setLocalSubmissions((previous) => [...previous, submission]);
      await onSubmitted(submission);
    } catch (submitError) {
      setError(errorMessage(submitError));
    } finally {
      setBusy(false);
    }
  }

  return (
    <section className="card stack" aria-label="Graded assignment">
      <h2>{assessment?.title ?? "Graded assignment"}</h2>
      {loading ? (
        <p role="status">Loading protected assignment content…</p>
      ) : error && !assessment ? (
        <p role="alert" className="error">
          {error}
        </p>
      ) : assessment ? (
        <>
          <p>
            {assessment.points} total points · content v
            {assessment.content_version} · attempts used:{" "}
            {assessment.attempts_used}
            {assessment.attempt_limit ? ` of ${assessment.attempt_limit}` : ""}.
          </p>
          {assessment.schedule_status === "closed" && (
            <p className="notice">
              The deadline has passed. Saved results remain available below.
            </p>
          )}
          {assessmentHistory.map((submission) => (
            <SubmissionFeedback
              key={submission.id}
              submission={submission}
              onAppeal={onAppeal}
            />
          ))}
          {assessment.schedule_status === "open" && (
            <form onSubmit={submit} className="stack">
              <fieldset
                disabled={!enabled || busy || limitReached}
                className="stack"
              >
                <legend>Submit answers</legend>
                {assessment.questions.map((question) => (
                  <GradedQuestion
                    key={question.id}
                    question={question}
                    answer={answers[question.id]}
                    disabled={!enabled || busy || limitReached}
                    onChange={(answer) => setAnswer(question, answer)}
                  />
                ))}
                {error && (
                  <p role="alert" className="error">
                    {error}
                  </p>
                )}
                {limitReached ? (
                  <p className="notice">
                    The configured attempt limit has been reached.
                  </p>
                ) : (
                  <button
                    className="primary"
                    type="submit"
                    disabled={!enabled || busy}
                  >
                    {busy ? "Saving and grading…" : "Submit assignment"}
                  </button>
                )}
              </fieldset>
            </form>
          )}
          <p className="muted">
            Original scores are deterministic. A learner may request one human
            review per saved attempt; adjustments remain separate and auditable.
          </p>
        </>
      ) : null}
    </section>
  );
}
