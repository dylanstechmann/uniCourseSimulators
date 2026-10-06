import { useEffect, useRef, useState } from "react";
import { api, errorMessage } from "./api";
import type {
  CourseSummary,
  CurriculumMap,
  Enrollment,
  Session,
  Source,
} from "./types";
import { AccountPanel } from "./components/AccountPanel";
import { CourseCatalog } from "./components/CourseCatalog";
import { CourseWorkspace } from "./components/CourseWorkspace";
import { InstructorReview } from "./components/InstructorReview";

function currentRoute() {
  return window.location.hash.slice(1) || "/courses";
}
function decode(value?: string) {
  try {
    return value ? decodeURIComponent(value) : undefined;
  } catch {
    return undefined;
  }
}

export default function App() {
  const [route, setRoute] = useState(currentRoute);
  const [session, setSession] = useState<Session>({
    user: null,
    csrf_token: null,
  });
  const [sessionReady, setSessionReady] = useState(false);
  const [courses, setCourses] = useState<CourseSummary[]>([]);
  const [curriculum, setCurriculum] = useState<CurriculumMap | null>(null);
  const [sources, setSources] = useState<Source[]>([]);
  const [enrollments, setEnrollments] = useState<Enrollment[]>([]);
  const [bookmarks, setBookmarks] = useState<string[]>([]);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(true);
  const [largeText, setLargeText] = useState(false);
  const [highContrast, setHighContrast] = useState(false);
  const mainRef = useRef<HTMLElement>(null);
  useEffect(() => {
    const update = () => setRoute(currentRoute());
    window.addEventListener("hashchange", update);
    return () => window.removeEventListener("hashchange", update);
  }, []);
  useEffect(() => {
    let active = true;
    Promise.all([api.session(), api.courses(), api.sources(), api.curriculum()])
      .then(([session, courses, sources, curriculum]) => {
        if (active) {
          setSession(session);
          setSessionReady(true);
          setCourses(courses);
          setSources(sources);
          setCurriculum(curriculum);
        }
      })
      .catch((error) => {
        if (active) setError(errorMessage(error));
      })
      .finally(() => {
        if (active) setLoading(false);
      });
    return () => {
      active = false;
    };
  }, []);
  useEffect(() => {
    let active = true;
    if (!session.user) {
      setEnrollments([]);
      setBookmarks([]);
      return;
    }
    Promise.all([api.enrollments(), api.bookmarks()])
      .then(([enrollments, bookmarks]) => {
        if (active) {
          setEnrollments(enrollments);
          setBookmarks(bookmarks);
        }
      })
      .catch((error) => {
        if (active) setError(errorMessage(error));
      });
    return () => {
      active = false;
    };
  }, [session.user?.id, session.user?.is_guest]);
  useEffect(() => {
    mainRef.current?.focus();
  }, [route]);
  async function enroll(course_id: string) {
    const enrollment = await api.enroll(course_id);
    setEnrollments((previous) => [
      ...previous.filter((item) => item.course_id !== course_id),
      enrollment,
    ]);
  }
  async function upgradeEnrollment(course_id: string) {
    const enrollment = await api.upgradeEnrollment(course_id);
    setEnrollments((previous) => [
      ...previous.filter((item) => item.course_id !== course_id),
      enrollment,
    ]);
  }
  async function bookmark(id: string, saved: boolean) {
    await api.bookmark(id, saved);
    setBookmarks((previous) =>
      saved
        ? [...new Set([...previous, id])]
        : previous.filter((item) => item !== id),
    );
  }
  const segments = route.split("/").filter(Boolean);
  const courseId = segments[0] === "course" ? decode(segments[1]) : undefined;
  const lessonId = segments[2] === "lesson" ? decode(segments[3]) : undefined;
  const page = courseId
    ? "course"
    : segments[0] === "account"
      ? "account"
      : segments[0] === "instructor"
        ? "instructor"
        : segments[0] === "learning"
          ? "learning"
          : "courses";
  return (
    <div
      className={`app-shell${largeText ? " large-text" : ""}${highContrast ? " high-contrast" : ""}`}
    >
      <a
        className="skip-link"
        href="#main-content"
        onClick={(event) => {
          event.preventDefault();
          mainRef.current?.focus();
          mainRef.current?.scrollIntoView();
        }}
      >
        Skip to main content
      </a>
      <aside className="sidebar">
        <a className="brand" href="#/courses">
          <span className="brand-mark" aria-hidden="true">
            ✣
          </span>
          <span>
            uniStemCourseSimulators
            <span className="brand-sub">Think · Model · Practice</span>
          </span>
        </a>
        <nav aria-label="Main navigation">
          <a
            href="#/courses"
            aria-current={page === "courses" ? "page" : undefined}
          >
            Course catalog
          </a>
          <a
            href="#/learning"
            aria-current={page === "learning" ? "page" : undefined}
          >
            My learning <span className="nav-count">{enrollments.length}</span>
          </a>
          {session.can_review ? (
            <a
              href="#/instructor"
              aria-current={page === "instructor" ? "page" : undefined}
            >
              Instructor review
            </a>
          ) : null}
          <a
            href="#/account"
            aria-current={page === "account" ? "page" : undefined}
          >
            Account and data
          </a>
        </nav>
        <div className="sidebar-note">
          <strong>Explicit maturity</strong>
          <p>
            Partial content is labeled. uniStemCourseSimulators does not confer
            credit or establish university prerequisite equivalency.
          </p>
        </div>
        <div className="legacy">
          <a href="http://localhost:4173/" target="_blank" rel="noreferrer">
            Legacy local study tools{" "}
            <span className="sr-only">(opens in a new tab)</span>
          </a>
          <p>
            Run the preserved local reader separately; browser scores
            unverified.
          </p>
        </div>
      </aside>
      <div className="main-shell">
        <header className="topbar">
          <span className="session-status">
            {!sessionReady
              ? "Session loading…"
              : session.user
                ? session.user.is_guest
                  ? "Guest session"
                  : "Account session"
                : "Public reader"}
          </span>
          <div className="topbar-controls">
            <button
              aria-pressed={largeText}
              onClick={() => setLargeText(!largeText)}
            >
              Larger text
            </button>
            <button
              aria-pressed={highContrast}
              onClick={() => setHighContrast(!highContrast)}
            >
              Higher contrast
            </button>
            <a href="#/account">
              {session.user ? "Manage account" : "Guest / sign in"}
            </a>
          </div>
        </header>
        <main
          id="main-content"
          tabIndex={-1}
          ref={mainRef}
          className="page-content"
        >
          {error && (
            <p className="error" role="alert">
              {error}
            </p>
          )}
          {loading ? (
            <>
              <h1>uniStemCourseSimulators</h1>
              <p role="status">Loading the learning platform…</p>
            </>
          ) : page === "account" ? (
            <AccountPanel session={session} onSession={setSession} />
          ) : page === "instructor" ? (
            <InstructorReview />
          ) : courseId ? (
            <CourseWorkspace
              key={courseId}
              id={courseId}
              lessonId={lessonId}
              showGradebook={segments[2] === "gradebook"}
              catalog={courses}
              enrollmentVersion={
                enrollments.find((item) => item.course_id === courseId)
                  ?.content_version
              }
              enrolled={enrollments.some((item) => item.course_id === courseId)}
              hasSession={sessionReady && !!session.user}
              bookmarked={bookmarks.includes(courseId)}
              sources={sources}
              onEnroll={() => enroll(courseId)}
              onUpgrade={() => upgradeEnrollment(courseId)}
              onBookmark={(saved) => bookmark(courseId, saved)}
            />
          ) : page === "learning" ? (
            <>
              <span className="eyebrow">Your enrolled packages</span>
              <h1>My learning</h1>
              {!session.user && (
                <p className="notice">
                  <a href="#/account">Start a guest session or sign in</a> to
                  save enrollment and practice evidence.
                </p>
              )}
              {enrollments.length ? (
                <CourseCatalog
                  compact
                  courses={courses.filter((course) =>
                    enrollments.some((item) => item.course_id === course.id),
                  )}
                  enrollments={enrollments}
                  bookmarks={bookmarks}
                  curriculum={curriculum}
                  sources={sources}
                />
              ) : (
                <p>
                  No enrollments yet.{" "}
                  <a href="#/courses">Explore the course catalog.</a>
                </p>
              )}
            </>
          ) : (
            <CourseCatalog
              courses={courses}
              enrollments={enrollments}
              bookmarks={bookmarks}
              curriculum={curriculum}
              sources={sources}
            />
          )}
        </main>
        <footer>
          Open-source learning tools · No accreditation or transferable credit ·
          Course depth and review status are reported explicitly.
        </footer>
      </div>
    </div>
  );
}
