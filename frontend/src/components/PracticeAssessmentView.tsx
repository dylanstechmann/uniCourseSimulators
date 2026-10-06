import { useEffect, useState } from "react";
import { api, errorMessage } from "../api";
import type { Appeal, Attempt, PracticeAssessment } from "../types";
import { Assessment } from "./Assessment";

export function PracticeAssessmentView({
  courseId,
  assessmentId,
  enabled,
  attempts,
  onSubmit,
  onAppeal,
  onClose,
}: {
  courseId: string;
  assessmentId: string;
  enabled: boolean;
  attempts: Attempt[];
  onSubmit: (
    questionId: string,
    response: string | number | number[] | Record<string, string>,
    unit?: string,
    variantToken?: string | null,
  ) => Promise<Attempt>;
  onAppeal: (attemptId: string, reason: string) => Promise<Appeal>;
  onClose: () => void;
}) {
  const [assessment, setAssessment] = useState<PracticeAssessment | null>(null);
  const [error, setError] = useState("");

  useEffect(() => {
    let active = true;
    setAssessment(null);
    setError("");
    api
      .practiceAssessment(courseId, assessmentId)
      .then((data) => {
        if (active) setAssessment(data);
      })
      .catch((reason) => {
        if (active) setError(errorMessage(reason));
      });
    return () => {
      active = false;
    };
  }, [courseId, assessmentId]);

  return (
    <section
      className="card practice-assessment-set"
      aria-labelledby="practice-set-title"
    >
      <div className="section-heading">
        <div>
          <span className="eyebrow">Ungraded cumulative practice</span>
          <h2 id="practice-set-title">
            {assessment?.title ?? "Loading practice set…"}
          </h2>
        </div>
        <button type="button" onClick={onClose}>
          Close practice set
        </button>
      </div>
      <p className="notice">
        This is a self-paced review of publicly answer-bearing practice items.
        It is not a midterm or other summative exam. Each response is graded as
        formative practice and may show feedback immediately.
      </p>
      {assessment && (
        <p className="muted">
          {assessment.questions.length} questions · {assessment.points} practice
          points · course content v{assessment.content_version}
        </p>
      )}
      {error && (
        <p role="alert" className="error">
          {error}
        </p>
      )}
      {assessment?.questions.map((question, index) => {
        const previousAttempt = [...attempts]
          .reverse()
          .find(
            (attempt) =>
              attempt.question_id === question.id &&
              attempt.content_version === assessment.content_version,
          );
        return (
          <div key={question.id} className="practice-set-item">
            <h3>
              Question {index + 1} of {assessment.questions.length}
            </h3>
            <Assessment
              question={question}
              enabled={enabled}
              previousAttempt={previousAttempt}
              onSubmit={(response, unit, variantToken) =>
                onSubmit(question.id, response, unit, variantToken)
              }
              onAppeal={onAppeal}
            />
          </div>
        );
      })}
    </section>
  );
}
