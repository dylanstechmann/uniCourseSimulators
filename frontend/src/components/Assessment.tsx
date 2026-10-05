import { useState, type FormEvent } from "react";
import { errorMessage } from "../api";
import type { Attempt, Question } from "../types";
import { FeedbackView } from "./FeedbackView";

export function Assessment({
  question,
  enabled,
  disabledMessage,
  previousAttempt,
  onSubmit,
}: {
  question: Question;
  enabled: boolean;
  disabledMessage?: string;
  previousAttempt?: Attempt;
  onSubmit: (
    response: string | number | number[],
    unit?: string,
    variantToken?: string | null,
  ) => Promise<Attempt>;
}) {
  const [choice, setChoice] = useState<number | null>(null);
  const [selected, setSelected] = useState<number[]>([]);
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
    setBusy(true);
    try {
      const response =
        question.type === "single_choice"
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
      {(attempt || previousAttempt) && (
        <FeedbackView attempt={(attempt || previousAttempt)!} />
      )}
    </section>
  );
}
