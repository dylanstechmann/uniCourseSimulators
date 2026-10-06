import type { AssessmentPlan } from "../types";

function formatDate(value: string | null) {
  return value ? new Date(value).toLocaleString() : "Not scheduled";
}

export function AssessmentPlanView({ plan }: { plan: AssessmentPlan }) {
  return (
    <section
      className="card assessment-plan"
      aria-label="Course assessment plan"
    >
      <div className="section-heading">
        <div>
          <h2>Course assessment plan</h2>
          <p>Enrollment snapshot · content v{plan.content_version}</p>
        </div>
        <span className="tag">
          {plan.grading_mode === "formative-only"
            ? "Formative only"
            : "Graded policy configured"}
        </span>
      </div>
      {plan.course_grade_status === "not_configured" ? (
        <p className="notice">
          No course grade is configured for this package. Practice points are
          study feedback and do not count as a university course grade.
        </p>
      ) : (
        <p className="notice">
          This version defines weighted grade categories, but graded submissions
          and course-grade calculations are not available yet. No course grade
          is being reported.
        </p>
      )}
      {plan.categories.length > 0 && (
        <>
          <h3>Grade weights</h3>
          <ul>
            {plan.categories.map((category) => (
              <li key={category.id}>
                {category.title || category.id}:{" "}
                {Math.round(category.weight * 100)}%
              </li>
            ))}
          </ul>
          <p className="muted">
            Category aggregation:{" "}
            {plan.category_aggregation.replaceAll("-", " ")}.
          </p>
        </>
      )}
      <h3>Assignments and practice</h3>
      {plan.assessments.length === 0 ? (
        <p>No assessment records are defined in this course version.</p>
      ) : (
        <div
          className="table-scroll"
          role="region"
          aria-label="Scrollable assessment schedule"
          tabIndex={0}
        >
          <table>
            <caption>
              Versioned assessment metadata. Private answer specifications are
              not included in this plan.
            </caption>
            <thead>
              <tr>
                <th scope="col">Activity</th>
                <th scope="col">Role</th>
                <th scope="col">Week</th>
                <th scope="col">Points</th>
                <th scope="col">Release</th>
                <th scope="col">Due</th>
                <th scope="col">Status</th>
              </tr>
            </thead>
            <tbody>
              {plan.assessments.map((assessment) => (
                <tr key={assessment.id}>
                  <th scope="row">{assessment.title}</th>
                  <td>{assessment.mode.replaceAll("-", " ")}</td>
                  <td>{assessment.week ?? "—"}</td>
                  <td>{assessment.points}</td>
                  <td>{formatDate(assessment.release_at)}</td>
                  <td>{formatDate(assessment.due_at)}</td>
                  <td>{assessment.schedule_status.replaceAll("_", " ")}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
      <details>
        <summary>Assessment policies</summary>
        <dl>
          <dt>Attempts</dt>
          <dd>{plan.attempt_policy}</dd>
          <dt>Solution release</dt>
          <dd>{plan.solution_release}</dd>
          <dt>Late work</dt>
          <dd>{plan.late_policy}</dd>
          <dt>Appeals</dt>
          <dd>{plan.appeals}</dd>
        </dl>
      </details>
    </section>
  );
}

