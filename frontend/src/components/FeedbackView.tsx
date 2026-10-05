import type { Attempt } from "../types";

const diagnoses: Record<string, string> = {
  correct_result_reasoning_not_assessed:
    "Correct result. Reasoning has not been assessed.",
  incorrect_result:
    "The result does not match this question’s answer specification.",
  numerical_mismatch: "The numerical result is outside the accepted tolerance.",
  unit_mistake: "The supplied unit is inconsistent with the expected quantity.",
  malformed_response:
    "The response could not be interpreted in the required format.",
};

export function FeedbackView({ attempt }: { attempt: Attempt }) {
  const feedback = attempt.result.feedback;
  return (
    <section
      className={`feedback ${attempt.result.correct ? "feedback-correct" : ""}`}
      aria-label="Submission feedback"
      aria-live="polite"
    >
      <h3>
        {attempt.score} / {attempt.max_score} practice points
      </h3>
      <p>
        {diagnoses[feedback.diagnosis] ||
          feedback.diagnosis.replaceAll("_", " ")}
      </p>
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
