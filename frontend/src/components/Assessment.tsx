import { useState, type FormEvent } from "react";
import { errorMessage } from "../api";
import type { Appeal, Attempt, Question } from "../types";
import { FeedbackView } from "./FeedbackView";

export function Assessment({
  question,
  enabled,
  disabledMessage,
  previousAttempt,
  onSubmit,
  onAppeal,
}: {
  question: Question;
  enabled: boolean;
  disabledMessage?: string;
  previousAttempt?: Attempt;
  onAppeal?: (attemptId: string, reason: string) => Promise<Appeal>;
  onSubmit: (
    response: string | number | number[] | Record<string, string>,
    unit?: string,
    variantToken?: string | null,
  ) => Promise<Attempt>;
}) {
  const [choice, setChoice] = useState<number | null>(null);
  const [selected, setSelected] = useState<number[]>([]);
  const [value, setValue] = useState("");
  const [unit, setUnit] = useState("");
  const [fieldResponses, setFieldResponses] = useState<Record<string, string>>(
    {},
  );
  const [attempt, setAttempt] = useState<Attempt | undefined>();
  const [busy, setBusy] = useState(false);
  const [appealReason, setAppealReason] = useState("");
  const [appealBusy, setAppealBusy] = useState(false);
  const [appealError, setAppealError] = useState("");
  const [error, setError] = useState("");
  async function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setError("");
    if (question.type === "single_choice" && choice === null) {
      setError("Select an answer before submitting.");
      return;
    }
    if (question.type === "multiple_select" && selected.length === 0) {
      setError("Select at least one option before submitting.");
      return;
    }
    if (question.type === "symbolic" && !value.trim()) {
      setError("Enter an algebraic expression before submitting.");
      return;
    }
    if (
      question.type === "numeric" &&
      (!value.trim() || !Number.isFinite(Number(value)))
    ) {
      setError("Enter a finite numerical value.");
      return;
    }
    if (question.type === "numeric" && question.unit && !unit.trim()) {
      setError("Enter the unit for this quantity.");
      return;
    }
    const structuredResponse = Object.fromEntries(
      Object.entries(fieldResponses)
        .map(([fieldId, answer]) => [fieldId, answer.trim()])
        .filter(([, answer]) => answer !== ""),
    );
    if (
      question.type === "data_interpretation" &&
      Object.keys(structuredResponse).length === 0
    ) {
      setError("Enter or select at least one field before submitting.");
      return;
    }
    setBusy(true);
    try {
      const response: string | number | number[] | Record<string, string> =
        question.type === "data_interpretation"
          ? structuredResponse
          : question.type === "single_choice"
            ? choice!
            : question.type === "multiple_select"
              ? [...selected].sort((a, b) => a - b)
              : value.trim();
      const normalizedUnit = unit.trim() || undefined;
      const pendingAttempt = question.variant_token
        ? onSubmit(response, normalizedUnit, question.variant_token)
        : onSubmit(response, normalizedUnit);
      setAttempt(await pendingAttempt);
    } catch (error) {
      setError(errorMessage(error));
    } finally {
      setBusy(false);
    }
  }
  async function requestReview(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const submitted = attempt || previousAttempt;
    if (!submitted || !onAppeal) return;
    setAppealError("");
    if (appealReason.trim().length < 20) {
      setAppealError(
        "Please explain what may have been missed in at least 20 characters.",
      );
      return;
    }
    setAppealBusy(true);
    try {
      const appeal = await onAppeal(submitted.id, appealReason.trim());
      setAttempt({
        ...submitted,
        appeal,
        effective_score: appeal.effective_score,
      });
      setAppealReason("");
    } catch (error) {
      setAppealError(errorMessage(error));
    } finally {
      setAppealBusy(false);
    }
  }
  const submittedAttempt = attempt || previousAttempt;
  const appeal = submittedAttempt?.appeal;
  return (
    <section
      className="assessment card"
      aria-label="Formative practice"
      data-question-id={question.id}
    >
      <span className="eyebrow">
        Formative practice · {question.points} points
      </span>
      <form onSubmit={submit}>
        <fieldset disabled={!enabled || busy}>
          <legend>{question.prompt}</legend>
          {question.type === "single_choice" ? (
            <div className="choices">
              {question.options.map((option, index) => (
                <label key={index} className="choice">
                  <input
                    type="radio"
                    name={question.id}
                    value={index}
                    checked={choice === index}
                    onChange={() => setChoice(index)}
                    required
                  />
                  <span>{option}</span>
                </label>
              ))}
            </div>
          ) : question.type === "multiple_select" ? (
            <>
              <p className="muted">
                Select all that apply.{" "}
                {question.partial_credit_policy ===
                "correct-minus-incorrect-clamped-v1"
                  ? "Each correct selection earns equal credit; each incorrect selection subtracts one equal share, to a minimum of zero."
                  : "Credit requires selecting exactly the complete set."}
              </p>
              <div className="choices">
                {question.options.map((option, index) => (
                  <label key={index} className="choice">
                    <input
                      type="checkbox"
                      name={question.id}
                      value={index}
                      checked={selected.includes(index)}
                      onChange={() =>
                        setSelected((previous) =>
                          previous.includes(index)
                            ? previous.filter((item) => item !== index)
                            : [...previous, index],
                        )
                      }
                    />
                    <span>{option}</span>
                  </label>
                ))}
              </div>
            </>
          ) : question.type === "data_interpretation" ? (
            <div className="stack">
              <p className="muted">
                Each field is scored independently. Unanswered fields receive no
                credit; open-ended reasoning is not graded.
              </p>
              {(question.response_fields ?? []).map((field) => (
                <div key={field.id} className="input-grid">
                  {field.type === "numeric" ? (
                    <div>
                      <label htmlFor={`${question.id}-${field.id}`}>
                        {field.prompt} · {field.points} points
                      </label>
                      <input
                        id={`${question.id}-${field.id}`}
                        name={field.id}
                        type="text"
                        inputMode="text"
                        value={fieldResponses[field.id] ?? ""}
                        onChange={(event) =>
                          setFieldResponses((previous) => ({
                            ...previous,
                            [field.id]: event.target.value,
                          }))
                        }
                        maxLength={1000}
                        autoComplete="off"
                        aria-describedby={`${question.id}-${field.id}-help`}
                      />
                      <small id={`${question.id}-${field.id}-help`}>
                        Include a unit compatible with{" "}
                        {field.unit || "the requested quantity"}.
                      </small>
                    </div>
                  ) : (
                    <div>
                      <label htmlFor={`${question.id}-${field.id}`}>
                        {field.prompt} · {field.points} points
                      </label>
                      <select
                        id={`${question.id}-${field.id}`}
                        name={field.id}
                        value={fieldResponses[field.id] ?? ""}
                        onChange={(event) =>
                          setFieldResponses((previous) => ({
                            ...previous,
                            [field.id]: event.target.value,
                          }))
                        }
                      >
                        <option value="">Choose an answer</option>
                        {field.options.map((option, index) => (
                          <option key={index} value={index}>
                            {option}
                          </option>
                        ))}
                      </select>
                    </div>
                  )}
                </div>
              ))}
            </div>
          ) : question.type === "numeric" ? (
            <div className="input-grid">
              <div>
                <label htmlFor={`${question.id}-value`}>Numerical value</label>
                <input
                  id={`${question.id}-value`}
                  name="value"
                  inputMode="decimal"
                  value={value}
                  onChange={(event) => setValue(event.target.value)}
                  required
                  autoComplete="off"
                  aria-describedby={
                    question.significant_figures
                      ? `${question.id}-precision-help`
                      : undefined
                  }
                />
                {question.significant_figures ? (
                  <small id={`${question.id}-precision-help`}>
                    Report exactly {question.significant_figures} significant
                    figures. Use a decimal point or scientific notation to make
                    trailing zeros explicit.
                  </small>
                ) : null}
              </div>
              {question.unit ? (
                <div>
                  <label htmlFor={`${question.id}-unit`}>Unit</label>
                  <input
                    id={`${question.id}-unit`}
                    name="unit"
                    value={unit}
                    onChange={(event) => setUnit(event.target.value)}
                    required
                    autoComplete="off"
                    aria-describedby={`${question.id}-unit-help`}
                  />
                  <small id={`${question.id}-unit-help`}>
                    Enter a unit explicitly. The grader checks the unit as well
                    as the value.
                  </small>
                </div>
              ) : (
                <p className="muted">This quantity is dimensionless.</p>
              )}
            </div>
          ) : (
            <div>
              <label htmlFor={`${question.id}-value`}>
                Algebraic expression
              </label>
              <input
                id={`${question.id}-value`}
                name="value"
                type="text"
                inputMode="text"
                value={value}
                onChange={(event) => setValue(event.target.value)}
                required
                maxLength={256}
                autoComplete="off"
                autoCapitalize="off"
                spellCheck={false}
                aria-describedby={`${question.id}-expression-help`}
              />
              <small id={`${question.id}-expression-help`}>
                Use explicit multiplication (2*x) and ^ or ** for powers.
                Arithmetic expressions only; function calls are not supported.
              </small>
            </div>
          )}
          <button className="primary" type="submit">
            {busy ? "Submitting…" : "Submit practice response"}
          </button>
        </fieldset>
        {!enabled && (
          <p className="muted">
            {disabledMessage ||
              "Enroll with a guest session or account to save attempts and receive feedback."}
          </p>
        )}
        {error && (
          <p role="alert" className="error">
            {error}
          </p>
        )}
      </form>
      {submittedAttempt && (
        <>
          <FeedbackView attempt={submittedAttempt} />
          {appeal ? (
            <section className="appeal-status" aria-label="Human review status">
              <h4>Human review · {appeal.status}</h4>
              {appeal.status === "open" ? (
                <p>
                  Your request is saved for an authorized instructor to review.
                </p>
              ) : (
                <>
                  <p>{appeal.review_note}</p>
                  {appeal.status === "adjusted" ? (
                    <p>
                      Practice score after review: {appeal.effective_score} /{" "}
                      {appeal.max_score}. The automatic score remains recorded
                      separately.
                    </p>
                  ) : null}
                </>
              )}
            </section>
          ) : onAppeal ? (
            <form className="appeal-form" onSubmit={requestReview}>
              <h4>Request human review</h4>
              <p className="muted">
                Explain the evidence or rubric issue. An instructor may adjust
                the practice score; the automatic result will remain in the
                audit history.
              </p>
              <label htmlFor={`${question.id}-appeal-reason`}>
                Reason for review
              </label>
              <textarea
                id={`${question.id}-appeal-reason`}
                value={appealReason}
                onChange={(event) => setAppealReason(event.target.value)}
                minLength={20}
                maxLength={4000}
                rows={4}
                required
              />
              <button type="submit" disabled={!enabled || appealBusy}>
                {appealBusy ? "Saving request…" : "Send for human review"}
              </button>
              {appealError ? (
                <p role="alert" className="error">
                  {appealError}
                </p>
              ) : null}
            </form>
          ) : null}
        </>
      )}
    </section>
  );
}
