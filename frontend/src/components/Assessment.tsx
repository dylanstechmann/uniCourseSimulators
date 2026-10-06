import { useState, type FormEvent } from "react";
import { errorMessage } from "../api";
import type { Appeal, Attempt, Question } from "../types";
import { FeedbackView } from "./FeedbackView";

function fileAsBase64(file: File): Promise<string> {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = () => {
      if (typeof reader.result !== "string") {
        reject(new Error("The selected file could not be read."));
        return;
      }
      const separator = reader.result.indexOf(",");
      if (separator < 0) {
        reject(new Error("The selected file could not be encoded."));
        return;
      }
      resolve(reader.result.slice(separator + 1));
    };
    reader.onerror = () =>
      reject(reader.error ?? new Error("The selected file could not be read."));
    reader.readAsDataURL(file);
  });
}

function GraphResponse({
  question,
  values,
  onChange,
}: {
  question: Question;
  values: Record<string, { x: string; y: string }>;
  onChange: (pointId: string, coordinate: "x" | "y", value: string) => void;
}) {
  const graph = question.graph_spec;
  if (!graph) return null;
  const width = 640;
  const height = 360;
  const left = 76;
  const right = 22;
  const top = 22;
  const bottom = 58;
  const plotWidth = width - left - right;
  const plotHeight = height - top - bottom;
  const { x_axis: xAxis, y_axis: yAxis } = graph;
  const xPosition = (value: number) =>
    left +
    ((value - xAxis.minimum) / (xAxis.maximum - xAxis.minimum)) * plotWidth;
  const yPosition = (value: number) =>
    top +
    ((yAxis.maximum - value) / (yAxis.maximum - yAxis.minimum)) * plotHeight;
  const xTicks = Array.from(
    { length: 5 },
    (_, index) => xAxis.minimum + ((xAxis.maximum - xAxis.minimum) * index) / 4,
  );
  const yTicks = Array.from(
    { length: 5 },
    (_, index) => yAxis.minimum + ((yAxis.maximum - yAxis.minimum) * index) / 4,
  );
  const formatted = (value: number) => Number(value.toPrecision(4)).toString();
  const plotted = graph.points.flatMap((point) => {
    const pair = values[point.id];
    if (!pair?.x.trim() || !pair.y.trim()) return [];
    const x = Number(pair.x);
    const y = Number(pair.y);
    if (
      !Number.isFinite(x) ||
      !Number.isFinite(y) ||
      x < xAxis.minimum ||
      x > xAxis.maximum ||
      y < yAxis.minimum ||
      y > yAxis.maximum
    ) {
      return [];
    }
    return [{ id: point.id, label: point.label, x, y }];
  });
  const plotDescription = graph.points
    .map((point) => {
      const pair = values[point.id];
      if (!pair?.x.trim() || !pair.y.trim())
        return `${point.label}: not plotted`;
      const x = Number(pair.x);
      const y = Number(pair.y);
      if (!Number.isFinite(x) || !Number.isFinite(y)) {
        return `${point.label}: enter finite coordinates`;
      }
      if (
        x < xAxis.minimum ||
        x > xAxis.maximum ||
        y < yAxis.minimum ||
        y > yAxis.maximum
      ) {
        return `${point.label}: coordinate is outside the displayed axes`;
      }
      return `${point.label}: x ${formatted(x)}, y ${formatted(y)}`;
    })
    .join("; ");

  return (
    <div className="graph-activity stack">
      <p className="muted">
        Calculate the mean for each row, then enter its x and mean-y coordinates
        using the units shown on the axes. The plot updates as you type; each
        coordinate receives separate credit.
      </p>
      <table className="graph-data-table">
        <caption>Replicate measurements supplied for this graph</caption>
        <thead>
          <tr>
            <th scope="col">Group</th>
            <th scope="col">{xAxis.label}</th>
            <th scope="col">Replicate values · {yAxis.label}</th>
          </tr>
        </thead>
        <tbody>
          {graph.observations.map((observation) => (
            <tr key={observation.id}>
              <th scope="row">
                {graph.points.find((point) => point.id === observation.id)
                  ?.label ?? observation.id}
              </th>
              <td>{formatted(observation.x)}</td>
              <td>{observation.values.map(formatted).join(", ")}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <figure className="graph-figure">
        <svg
          viewBox={`0 0 ${width} ${height}`}
          role="img"
          aria-label={`Graph preview. Horizontal axis: ${xAxis.label}, from ${formatted(xAxis.minimum)} to ${formatted(xAxis.maximum)}. Vertical axis: ${yAxis.label}, from ${formatted(yAxis.minimum)} to ${formatted(yAxis.maximum)}. ${plotDescription}.`}
        >
          <rect
            x={left}
            y={top}
            width={plotWidth}
            height={plotHeight}
            className="graph-plot-background"
          />
          {xTicks.map((tick) => (
            <g key={`x-${tick}`}>
              <line
                x1={xPosition(tick)}
                y1={top}
                x2={xPosition(tick)}
                y2={top + plotHeight}
                className="graph-grid-line"
              />
              <text
                x={xPosition(tick)}
                y={top + plotHeight + 20}
                className="graph-tick-label"
                textAnchor="middle"
              >
                {formatted(tick)}
              </text>
            </g>
          ))}
          {yTicks.map((tick) => (
            <g key={`y-${tick}`}>
              <line
                x1={left}
                y1={yPosition(tick)}
                x2={left + plotWidth}
                y2={yPosition(tick)}
                className="graph-grid-line"
              />
              <text
                x={left - 10}
                y={yPosition(tick) + 4}
                className="graph-tick-label"
                textAnchor="end"
              >
                {formatted(tick)}
              </text>
            </g>
          ))}
          <line
            x1={left}
            y1={top + plotHeight}
            x2={left + plotWidth}
            y2={top + plotHeight}
            className="graph-axis-line"
          />
          <line
            x1={left}
            y1={top}
            x2={left}
            y2={top + plotHeight}
            className="graph-axis-line"
          />
          <text
            x={left + plotWidth / 2}
            y={height - 9}
            className="graph-axis-label"
            textAnchor="middle"
          >
            {xAxis.label}
          </text>
          <text
            x={16}
            y={top + plotHeight / 2}
            className="graph-axis-label"
            textAnchor="middle"
            transform={`rotate(-90 16 ${top + plotHeight / 2})`}
          >
            {yAxis.label}
          </text>
          {plotted.map((point) => (
            <g key={point.id}>
              <circle
                cx={xPosition(point.x)}
                cy={yPosition(point.y)}
                r={7}
                className="graph-point-marker"
              />
              <text
                x={xPosition(point.x) + 9}
                y={yPosition(point.y) - 8}
                className="graph-point-label"
              >
                {point.label}
              </text>
            </g>
          ))}
        </svg>
        <figcaption>
          Point preview. Axis limits are supplied by the exercise; this check
          does not assess axis selection or scientific interpretation.
        </figcaption>
      </figure>
      <div className="graph-point-entries">
        {graph.points.map((point) => (
          <fieldset className="graph-point-entry" key={point.id}>
            <legend>{point.label}</legend>
            <div className="input-grid">
              {(["x", "y"] as const).map((coordinate) => {
                const axis = coordinate === "x" ? xAxis : yAxis;
                const inputId = `${question.id}-${point.id}-${coordinate}`;
                return (
                  <div key={coordinate}>
                    <label htmlFor={inputId}>{axis.label} coordinate</label>
                    <input
                      id={inputId}
                      name={`${point.id}_${coordinate}`}
                      type="number"
                      inputMode="decimal"
                      step="any"
                      value={values[point.id]?.[coordinate] ?? ""}
                      onChange={(event) =>
                        onChange(point.id, coordinate, event.target.value)
                      }
                      autoComplete="off"
                    />
                  </div>
                );
              })}
            </div>
          </fieldset>
        ))}
      </div>
    </div>
  );
}

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
  const [graphResponses, setGraphResponses] = useState<
    Record<string, { x: string; y: string }>
  >({});
  const [uploadFile, setUploadFile] = useState<File | null>(null);
  const [attempt, setAttempt] = useState<Attempt | undefined>();
  const [busy, setBusy] = useState(false);
  const [appealReason, setAppealReason] = useState("");
  const [appealBusy, setAppealBusy] = useState(false);
  const [appealError, setAppealError] = useState("");
  const [error, setError] = useState("");
  const graphResponse = Object.fromEntries(
    Object.entries(graphResponses)
      .flatMap(([pointId, point]) => [
        [`${pointId}_x`, point.x.trim()],
        [`${pointId}_y`, point.y.trim()],
      ])
      .filter(([, coordinate]) => coordinate !== ""),
  );
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
    if (question.type === "file_upload" && !uploadFile) {
      setError("Choose a CSV file before submitting.");
      return;
    }
    if (
      question.type === "file_upload" &&
      uploadFile &&
      uploadFile.size > (question.max_upload_bytes ?? 32768)
    ) {
      setError(
        `The selected file is larger than ${question.max_upload_bytes ?? 32768} bytes.`,
      );
      return;
    }
    const structuredResponse = Object.fromEntries(
      Object.entries(fieldResponses)
        .map(([fieldId, answer]) => [fieldId, answer.trim()])
        .filter(([, answer]) => answer !== ""),
    );
    if (
      (question.type === "data_interpretation" ||
        question.type === "structured") &&
      Object.keys(structuredResponse).length === 0
    ) {
      setError("Enter or select at least one field before submitting.");
      return;
    }
    if (question.type === "graph" && Object.keys(graphResponse).length === 0) {
      setError("Enter at least one graph coordinate before submitting.");
      return;
    }
    setBusy(true);
    try {
      let response: string | number | number[] | Record<string, string>;
      if (
        question.type === "data_interpretation" ||
        question.type === "structured"
      ) {
        response = structuredResponse;
      } else if (question.type === "graph") {
        response = graphResponse;
      } else if (question.type === "single_choice") {
        response = choice!;
      } else if (question.type === "multiple_select") {
        response = [...selected].sort((a, b) => a - b);
      } else if (question.type === "file_upload" && uploadFile) {
        response = { content_base64: await fileAsBase64(uploadFile) };
      } else {
        response = value.trim();
      }
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
          ) : question.type === "data_interpretation" ||
            question.type === "structured" ? (
            <div className="stack">
              <p className="muted">
                {question.type === "structured"
                  ? "Each analytic criterion is scored separately from its structured response. Unanswered criteria receive no credit; free-form prose is not scored."
                  : "Each field is scored independently. Unanswered fields receive no credit; open-ended reasoning is not graded."}
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
          ) : question.type === "graph" ? (
            <GraphResponse
              question={question}
              values={graphResponses}
              onChange={(pointId, coordinate, coordinateValue) =>
                setGraphResponses((previous) => ({
                  ...previous,
                  [pointId]: {
                    x: previous[pointId]?.x ?? "",
                    y: previous[pointId]?.y ?? "",
                    [coordinate]: coordinateValue,
                  },
                }))
              }
            />
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
          ) : question.type === "file_upload" ? (
            <div>
              <label htmlFor={`${question.id}-file`}>CSV file upload</label>
              <input
                id={`${question.id}-file`}
                name="csv-file"
                type="file"
                accept={(question.accepted_media_types?.length
                  ? question.accepted_media_types
                  : ["text/csv"]
                ).join(",")}
                onChange={(event) =>
                  setUploadFile(event.target.files?.[0] ?? null)
                }
                aria-required="true"
                aria-describedby={`${question.id}-upload-help`}
              />
              <small id={`${question.id}-upload-help`}>
                Upload UTF-8 CSV, up to {question.max_upload_bytes ?? 32768}{" "}
                bytes. The file is parsed as data; uploaded content is never
                executed.
              </small>
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
