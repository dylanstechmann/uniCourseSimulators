import type { Attempt, Course, Gradebook } from "../types";

export function GradebookView({
  gradebook,
  attempts,
  course,
}: {
  gradebook: Gradebook;
  attempts: Attempt[];
  course: Course;
}) {
  const objectives = [...course.outcomes, ...course.lesson_objectives];
  return (
    <>
      {gradebook.course_grade && (
        <section className="card" aria-labelledby="course-grade-heading">
          <h2 id="course-grade-heading">Current weighted course grade</h2>
          {gradebook.course_grade.score_percent === null ? (
            <p>No released graded work is included yet.</p>
          ) : (
            <p className="score">
              {gradebook.course_grade.score_percent}% under the configured
              assessment policy
            </p>
          )}
          <p className="muted">
            {Math.round(gradebook.course_grade.active_weight * 100)}% of the
            configured category weight currently has released work in the
            calculation. This is a course-package result, not transferable
            credit or a university equivalency.
          </p>
          <ul aria-label="Current grade by category">
            {Object.entries(gradebook.course_grade.category_scores).map(
              ([category, score]) => (
                <li key={category}>
                  {category.replaceAll("-", " ")}:{" "}
                  {score === null ? "—" : `${score}%`}
                </li>
              ),
            )}
          </ul>
          {gradebook.course_grade.manual_override_count > 0 && (
            <p className="muted">
              Instructor adjustments applied to saved submissions:{" "}
              {gradebook.course_grade.manual_override_count}. Original automatic
              scores remain in attempt history.
            </p>
          )}
          <p>{gradebook.course_grade.explanation}</p>
        </section>
      )}
      <section aria-label="Practice gradebook">
        <div className="section-heading">
          <div>
            <h2>Practice gradebook</h2>
            <p>Formative checks · {gradebook.aggregation}</p>
          </div>
          <strong className="score">
            {gradebook.score} / {gradebook.max_score} practice points
          </strong>
        </div>
        <p className="notice">
          These results are practice evidence. They are not a course grade,
          mastery certification, or transferable credit.
        </p>
        <p className="muted">{gradebook.limitations}</p>
        <h3>Practice evidence by learning objective</h3>
        <p>
          Provisional indicator rule: at least{" "}
          {gradebook.objective_evidence_policy.minimum_distinct_items} distinct
          items, at least{" "}
          {Math.round(
            gradebook.objective_evidence_policy.minimum_item_coverage * 100,
          )}
          % of tagged items attempted, and at least{" "}
          {Math.round(
            gradebook.objective_evidence_policy.minimum_performance * 100,
          )}
          % best points. This is a study signal, not a mastery certification.
        </p>
        <div
          className="table-scroll"
          role="region"
          aria-label="Scrollable practice evidence table"
          tabIndex={0}
        >
          <table>
            <caption>
              Best reviewed result per distinct formative question; retries do
              not count as new items. Automatic scores remain in attempt
              history.
            </caption>
            <thead>
              <tr>
                <th scope="col">Objective</th>
                <th scope="col">Attempts</th>
                <th scope="col">Correct results</th>
                <th scope="col">Distinct items</th>
                <th scope="col">Best points on attempted items</th>
                <th scope="col">Practice indicator</th>
              </tr>
            </thead>
            <tbody>
              {Object.entries(gradebook.objective_evidence).map(
                ([id, evidence]) => (
                  <tr key={id}>
                    <th scope="row">
                      {objectives.find((objective) => objective.id === id)
                        ?.description || id}
                    </th>
                    <td>{evidence.attempts}</td>
                    <td>{evidence.correct_results}</td>
                    <td>
                      {evidence.attempted_items} / {evidence.item_count}
                    </td>
                    <td>
                      {evidence.performance === null
                        ? "—"
                        : `${evidence.best_score} / ${evidence.best_possible_score} (${Math.round(evidence.performance * 100)}%)`}
                    </td>
                    <td>{evidence.status.replaceAll("_", " ")}</td>
                  </tr>
                ),
              )}
            </tbody>
          </table>
        </div>
        {Object.keys(gradebook.objective_evidence).length === 0 && (
          <p>No practice evidence recorded yet.</p>
        )}
        {Object.keys(gradebook.objective_evidence).length > 0 && (
          <p className="muted">
            Correct-result counts reflect attempt history; repeated attempts do
            not increase distinct-item coverage.
          </p>
        )}
        <h3>Attempt and feedback history</h3>
        {attempts.length === 0 ? (
          <p>No submitted attempts yet.</p>
        ) : (
          <div
            className="table-scroll"
            role="region"
            aria-label="Scrollable attempt history table"
            tabIndex={0}
          >
            <table>
              <caption>
                Saved attempts for this course, including the content version.
              </caption>
              <thead>
                <tr>
                  <th scope="col">Question</th>
                  <th scope="col">Response</th>
                  <th scope="col">Practice points</th>
                  <th scope="col">Feedback</th>
                  <th scope="col">Version / date</th>
                </tr>
              </thead>
              <tbody>
                {attempts.map((attempt) => (
                  <tr key={attempt.id}>
                    <th scope="row">
                      {attempt.question_id}
                      {attempt.response.variant_id ? (
                        <>
                          <br />
                          <small>Variant: {attempt.response.variant_id}</small>
                        </>
                      ) : null}
                    </th>
                    <td>
                      {Array.isArray(attempt.response.response)
                        ? attempt.response.response.join(", ")
                        : typeof attempt.response.response === "object"
                          ? Object.entries(attempt.response.response)
                              .map(([field, value]) => `${field}: ${value}`)
                              .join("; ")
                          : attempt.response.response}{" "}
                      {attempt.response.unit || ""}
                    </td>
                    <td>
                      {attempt.effective_score ?? attempt.score} /{" "}
                      {attempt.max_score}
                      {attempt.effective_score !== undefined &&
                      attempt.effective_score !== attempt.score ? (
                        <small>
                          {" "}
                          (manual review; automatic {attempt.score})
                        </small>
                      ) : null}
                      {attempt.appeal ? (
                        <small> Review: {attempt.appeal.status}</small>
                      ) : null}
                    </td>
                    <td>
                      {attempt.result.feedback.diagnosis.replaceAll("_", " ")}
                      <br />
                      <details>
                        <summary>Feedback details</summary>
                        {attempt.result.feedback.hint ? (
                          <p>
                            <strong>Hint:</strong>{" "}
                            {attempt.result.feedback.hint}
                          </p>
                        ) : null}
                        <p>
                          <strong>Next step:</strong>{" "}
                          {attempt.result.feedback.next_step}
                        </p>
                      </details>
                      {attempt.result.feedback.lesson_id && (
                        <a
                          href={`#/course/${encodeURIComponent(course.id)}/lesson/${encodeURIComponent(attempt.result.feedback.lesson_id)}`}
                        >
                          Review lesson and feedback
                        </a>
                      )}
                    </td>
                    <td>
                      {attempt.content_version}
                      <br />
                      <time dateTime={attempt.created_at}>
                        {new Date(attempt.created_at).toLocaleString()}
                      </time>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </section>
    </>
  );
}
