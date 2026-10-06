import type { Attempt } from "../types";

const diagnoses: Record<string, string> = {
  correct_result_reasoning_not_assessed:
    "Correct result. Reasoning has not been assessed.",
  incorrect_result:
    "The result does not match this question’s answer specification.",
  data_interpretation_partial:
    "Some fields are correct. Calculation and interpretation receive separate credit.",
  data_interpretation_incorrect:
    "The submitted fields do not match the answer specification.",
  structured_rubric_complete:
    "All structured analytic criteria met their deterministic checks.",
  structured_rubric_partial:
    "Some structured analytic criteria met their deterministic checks.",
  structured_rubric_incorrect:
    "The structured responses did not meet the analytic rubric criteria.",
  csv_results_complete:
    "The uploaded CSV contains the expected numeric results for every rubric criterion.",
  csv_results_partial:
    "Some uploaded CSV results met their deterministic checks.",
  csv_results_incomplete:
    "The CSV table is valid, but one or more required result cells are missing.",
  csv_results_incorrect:
    "The uploaded table is valid, but its numeric results do not meet the rubric checks.",
  graph_coordinates_complete:
    "Every plotted coordinate matched within its authored tolerance. Axis selection and scientific interpretation were not assessed.",
  graph_coordinates_partial:
    "Some plotted coordinates met their deterministic checks. Each x and y coordinate receives separate credit.",
  graph_coordinates_incorrect:
    "The plotted coordinates did not meet the analytic checks.",
  malformed_upload:
    "The file could not be scored. Check the required UTF-8 CSV format, header, and unique row labels.",
  missing_response: "No response was submitted for this field.",
  numerical_mismatch: "The numerical result is outside the accepted tolerance.",
  significant_figures_mistake:
    "The value is within tolerance, but its written precision does not match the required significant figures.",
  unit_mistake: "The supplied unit is inconsistent with the expected quantity.",
  malformed_response:
    "The response could not be interpreted in the required format.",
  partially_correct_selection:
    "Partially correct selection. Review which features explain the mechanism.",
  incorrect_selection:
    "The selected set does not match the answer specification.",
};

export function FeedbackView({ attempt }: { attempt: Attempt }) {
  const feedback = attempt.result.feedback;
  const effectiveScore = attempt.effective_score ?? attempt.score;
  return (
    <section
      className={`feedback ${attempt.result.correct ? "feedback-correct" : ""}`}
      aria-label="Submission feedback"
      aria-live="polite"
    >
      <h3>
        {effectiveScore} / {attempt.max_score} practice points
        {attempt.appeal?.status === "adjusted" ? " after human review" : ""}
      </h3>
      {effectiveScore !== attempt.score ? (
        <p>
          <strong>Automatic score:</strong> {attempt.score} /{" "}
          {attempt.max_score}. The instructor adjustment is recorded separately.
        </p>
      ) : null}
      <p>
        {diagnoses[feedback.diagnosis] ||
          feedback.diagnosis.replaceAll("_", " ")}
      </p>
      {feedback.components && feedback.components.length > 0 && (
        <ul aria-label="Field-level scoring">
          {feedback.components.map((component) => (
            <li key={component.field_id}>
              <strong>{component.label}</strong>: {component.score} /{" "}
              {component.max_score} point
              {component.max_score === 1 ? "" : "s"}.{" "}
              {diagnoses[component.diagnosis] ||
                component.diagnosis.replaceAll("_", " ")}
            </li>
          ))}
        </ul>
      )}
      {!feedback.reasoning_assessed && (
        <p className="muted">
          This check evaluates the submitted result. It does not establish sound
          reasoning or learning mastery.
        </p>
      )}
      {feedback.hint && (
        <p>
          <strong>Targeted hint:</strong> {feedback.hint}
        </p>
      )}
      {feedback.misconception && (
        <p>
          <strong>Possible misconception:</strong> {feedback.misconception}
        </p>
      )}
      <p>
        <strong>Next step:</strong> {feedback.next_step}
      </p>
      <a
        href={`#/course/${encodeURIComponent(attempt.course_id)}/lesson/${encodeURIComponent(feedback.lesson_id)}`}
      >
        Review the relevant lesson
      </a>
      {feedback.provisional && <p className="badge">Provisional feedback</p>}
    </section>
  );
}
