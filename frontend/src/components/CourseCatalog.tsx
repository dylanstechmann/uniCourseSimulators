import { useMemo, useState } from "react";
import type {
  CourseSummary,
  CurriculumMap,
  Enrollment,
  Source,
} from "../types";
import { MaturityBadge } from "./MaturityBadge";

export function CourseCatalog({
  courses,
  enrollments,
  bookmarks,
  curriculum,
  sources = [],
  compact = false,
}: {
  courses: CourseSummary[];
  enrollments: Enrollment[];
  bookmarks: string[];
  curriculum?: CurriculumMap | null;
  sources?: Source[];
  compact?: boolean;
}) {
  const [search, setSearch] = useState("");
  const [domain, setDomain] = useState("all");
  const domains = [...new Set(courses.map((course) => course.domain))].sort();
  const nodes = new Map(
    (curriculum?.nodes ?? []).map((node) => [node.id, node]),
  );
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
        <strong>Honest course depth.</strong> Current packages contain short
        prototype material with uneven depth. They do not constitute semester
        courses. No course currently satisfies the project’s complete-course
        standard.
      </aside>
      {!compact && curriculum && (
        <section className="pathway-section" aria-labelledby="pathways-heading">
          <div className="section-heading pathway-heading">
            <div>
              <h2 id="pathways-heading">Curriculum pathways</h2>
              <p>
                {curriculum.pathways.length} study maps · prerequisite edges
                shown for planning
              </p>
            </div>
          </div>
          <p className="notice pathway-disclaimer">
            {curriculum.description} Pathway order and prerequisites are project
            planning guidance. They do not establish university equivalency,
            admission eligibility, transfer credit, or affiliation.
          </p>
          <div className="pathway-grid">
            {curriculum.pathways.map((pathway) => (
              <details className="card pathway-card" key={pathway.id}>
                <summary>
                  <span className="pathway-title">{pathway.title}</span>
                  <span className="pathway-count">
                    {pathway.course_ids.length} topics ·{" "}
                    {
                      pathway.course_ids.filter(
                        (id) => nodes.get(id)?.maturity === "catalog-only",
                      ).length
                    }{" "}
                    catalog-only
                  </span>
                </summary>
                <p>{pathway.description}</p>
                <p className="muted">{pathway.sequence_note}</p>
                <ol className="pathway-steps">
                  {pathway.course_ids.map((id, index) => {
                    const node = nodes.get(id);
                    if (!node) return null;
                    const prerequisites = node.prerequisites.course_ids.map(
                      (ref) => nodes.get(ref)?.title ?? ref,
                    );
                    const recommended =
                      node.prerequisites.recommended_course_ids.map(
                        (ref) => nodes.get(ref)?.title ?? ref,
                      );
                    const concurrent =
                      node.prerequisites.concurrent_course_ids.map(
                        (ref) => nodes.get(ref)?.title ?? ref,
                      );
                    return (
                      <li className="pathway-step" key={`${pathway.id}-${id}`}>
                        <span className="pathway-number" aria-hidden="true">
                          {index + 1}
                        </span>
                        <div className="pathway-step-content">
                          <div className="pathway-step-heading">
                            <h3>{node.title}</h3>
                            <MaturityBadge maturity={node.maturity} />
                          </div>
                          <p className="pathway-domain">
                            {node.domain} · {node.level}
                          </p>
                          <p>{node.description}</p>
                          {(prerequisites.length > 0 ||
                            recommended.length > 0 ||
                            concurrent.length > 0 ||
                            node.prerequisites.knowledge.length > 0) && (
                            <p className="pathway-prereqs">
                              <strong>Preparation:</strong>{" "}
                              {[
                                prerequisites.length
                                  ? `Prerequisites: ${prerequisites.join(", ")}`
                                  : "",
                                recommended.length
                                  ? `Recommended: ${recommended.join(", ")}`
                                  : "",
                                concurrent.length
                                  ? `Concurrent: ${concurrent.join(", ")}`
                                  : "",
                                node.prerequisites.knowledge.length
                                  ? `Knowledge: ${node.prerequisites.knowledge.join(", ")}`
                                  : "",
                              ]
                                .filter(Boolean)
                                .join(" · ")}
                            </p>
                          )}
                          {node.package_id && (
                            <a
                              href={`#/course/${encodeURIComponent(node.package_id)}`}
                            >
                              Open available {node.maturity} package:{" "}
                              {node.title}
                            </a>
                          )}
                          {!node.package_id &&
                            node.related_package_ids.length > 0 && (
                              <div className="related-packages">
                                <p>{node.relation_note}</p>
                                {node.related_package_ids.map((packageId) => {
                                  const related = courses.find(
                                    (course) => course.id === packageId,
                                  );
                                  if (!related) return null;
                                  return (
                                    <a
                                      key={packageId}
                                      href={`#/course/${encodeURIComponent(packageId)}`}
                                    >
                                      Related {related.maturity} package:{" "}
                                      {related.title}
                                    </a>
                                  );
                                })}
                              </div>
                            )}
                          {!node.package_id &&
                            node.related_package_ids.length === 0 && (
                              <p className="catalog-only-note">
                                Catalog entry only. Original lessons and
                                assessments have not been authored.
                              </p>
                            )}
                        </div>
                      </li>
                    );
                  })}
                </ol>
                {pathway.source_ids.length > 0 && (
                  <div className="pathway-sources">
                    <strong>Curriculum references</strong>
                    <ul>
                      {pathway.source_ids.map((id) => {
                        const source = sources.find((item) => item.id === id);
                        return source ? (
                          <li key={id}>
                            <a
                              href={source.url}
                              target="_blank"
                              rel="noreferrer"
                            >
                              {source.institution}: {source.title}
                              <span className="sr-only">
                                {" "}
                                (opens in a new tab)
                              </span>
                            </a>
                          </li>
                        ) : null;
                      })}
                    </ul>
                  </div>
                )}
              </details>
            ))}
          </div>
        </section>
      )}
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
