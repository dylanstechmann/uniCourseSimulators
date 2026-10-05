import { useMemo, useState } from "react";
import type { CourseSummary, Enrollment } from "../types";
import { MaturityBadge } from "./MaturityBadge";

export function CourseCatalog({
  courses,
  enrollments,
  bookmarks,
  compact = false,
}: {
  courses: CourseSummary[];
  enrollments: Enrollment[];
  bookmarks: string[];
  compact?: boolean;
}) {
  const [search, setSearch] = useState("");
  const [domain, setDomain] = useState("all");
  const domains = [...new Set(courses.map((course) => course.domain))].sort();
  const filtered = useMemo(
    () =>
      courses.filter(
        (course) =>
          (domain === "all" || course.domain === domain) &&
          `${course.title} ${course.description}`
            .toLowerCase()
            .includes(search.toLowerCase()),
      ),
    [courses, search, domain],
  );
  return (
    <>
      {!compact && (
        <div className="hero">
          <span className="eyebrow">A course platform in development</span>
          <h1>
            Learn through models,
            <br />
            evidence, and practice.
          </h1>
          <p className="lead">
            Interactive, source-grounded courses across science, mathematics,
            engineering, computing, and biomedicine.
          </p>
        </div>
      )}
      <aside className="notice" aria-label="Content maturity">
        <strong>Honest course depth.</strong> Current migrated packages are
        partial prototypes. Four short lessons do not constitute a semester
        course. No course currently satisfies the project’s complete-course
        standard.
      </aside>
      <div className="section-heading">
        <div>
          <h2>Course catalog</h2>
          <p>{courses.length} packages with explicit maturity labels</p>
        </div>
        <div className="filters">
          <label>
            Search courses
            <input
              type="search"
              value={search}
              onChange={(event) => setSearch(event.target.value)}
              placeholder="e.g. cell biology or circuits"
            />
          </label>
          <label>
            Domain
            <select
              value={domain}
              onChange={(event) => setDomain(event.target.value)}
            >
              <option value="all">All domains</option>
              {domains.map((value) => (
                <option key={value}>{value}</option>
              ))}
            </select>
          </label>
        </div>
      </div>
      <p className="sr-only" aria-live="polite">
        {filtered.length} courses shown
      </p>
      <div className="course-grid">
        {filtered.map((course) => (
          <article className="card course-card" key={course.id}>
            <div className="card-top">
              <span className="eyebrow">{course.domain}</span>
              <MaturityBadge maturity={course.maturity} />
            </div>
            <h3>
              <a href={`#/course/${encodeURIComponent(course.id)}`}>
                {course.title}
              </a>
            </h3>
            <p>{course.description}</p>
            <div className="course-meta">
              <span>{course.level}</span>
              <span>{course.lesson_count} available lessons</span>
            </div>
            <div className="card-bottom">
              <span className="muted">v{course.version}</span>
              {enrollments.some((item) => item.course_id === course.id) && (
                <span className="tag">Enrolled</span>
              )}
              {bookmarks.includes(course.id) && (
                <span className="tag">Bookmarked</span>
              )}
            </div>
          </article>
        ))}
      </div>
      {filtered.length === 0 && (
        <p className="empty">No courses match these filters.</p>
      )}
    </>
  );
}
