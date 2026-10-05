import { useState, type FormEvent } from "react";
import { errorMessage } from "../api";
import type { Attempt, Question } from "../types";
import { FeedbackView } from "./FeedbackView";

export function Assessment({
  question,
  enabled,
  previousAttempt,
  onSubmit,
}: {
  question: Question;
  enabled: boolean;
  previousAttempt?: Attempt;
  onSubmit: (response: string | number, unit?: string) => Promise<Attempt>;
}) {
  const [choice, setChoice] = useState<number | null>(null);
  const [value, setValue] = useState("");
  const [unit, setUnit] = useState("");
  const [attempt, setAttempt] = useState<Attempt | undefined>();
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState("");
  async function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setError("");
    if (question.type === "single_choice" && choice === null) {
      setError("Select an answer before submitting.");
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
    setBusy(true);
    try {
      setAttempt(
        await onSubmit(
          question.type === "single_choice" ? choice! : value.trim(),
          unit.trim() || undefined,
        ),
      );
    } catch (error) {
      setError(errorMessage(error));
    } finally {
      setBusy(false);
    }
  }
  return (
    <section className="assessment card" aria-label="Formative practice">
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
          ) : (
            <div className="input-grid">
              <label>
                Numerical value
                <input
                  name="value"
                  inputMode="decimal"
                  value={value}
                  onChange={(event) => setValue(event.target.value)}
                  required
                  autoComplete="off"
                />
              </label>
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
          )}
          <button className="primary" type="submit">
            {busy ? "Submitting…" : "Submit practice response"}
          </button>
        </fieldset>
        {!enabled && (
          <p className="muted">
            Enroll with a guest session or account to save attempts and receive
            feedback.
          </p>
        )}
        {error && (
          <p role="alert" className="error">
            {error}
          </p>
        )}
      </form>
      {(attempt || previousAttempt) && (
        <FeedbackView attempt={(attempt || previousAttempt)!} />
      )}
    </section>
  );
}
