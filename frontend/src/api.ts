import type {
  Attempt,
  Course,
  CurriculumMap,
  CourseSummary,
  Enrollment,
  Appeal,
  AssessmentAnswer,
  AssessmentPlan,
  InstructorAppeal,
  Gradebook,
  GradedAssessment,
  GradedSubmission,
  Lesson,
  Note,
  Progress,
  Session,
  Source,
} from "./types";

const base = "/api/v1";
let csrfToken: string | null = null;

export class ApiError extends Error {
  constructor(
    message: string,
    public status: number,
  ) {
    super(message);
    this.name = "ApiError";
  }
}

async function request<T>(
  path: string,
  method = "GET",
  body?: unknown,
): Promise<T> {
  const headers: Record<string, string> = { Accept: "application/json" };
  if (body !== undefined) headers["Content-Type"] = "application/json";
  if (method !== "GET" && csrfToken) headers["X-CSRF-Token"] = csrfToken;
  const response = await fetch(`${base}${path}`, {
    method,
    credentials: "include",
    headers,
    ...(body !== undefined ? { body: JSON.stringify(body) } : {}),
  });
  if (!response.ok) {
    const error = (await response.json().catch(() => ({}))) as {
      detail?: unknown;
    };
    const message =
      typeof error.detail === "string"
        ? error.detail
        : `Request failed (${response.status}). Please review your input or try again.`;
    throw new ApiError(message, response.status);
  }
  if (response.status === 204) return undefined as T;
  return response.json() as Promise<T>;
}

const encode = encodeURIComponent;
export const api = {
  async session() {
    const session = await request<Session>("/auth/session");
    csrfToken = session.csrf_token;
    return session;
  },
  async guest() {
    await request("/auth/guest", "POST", {});
    return this.session();
  },
  async register(email: string, password: string) {
    await request("/auth/register", "POST", { email, password });
    return this.session();
  },
  async login(email: string, password: string) {
    await request("/auth/login", "POST", { email, password });
    return this.session();
  },
  async logout() {
    await request("/auth/logout", "POST");
    csrfToken = null;
  },
  courses: () => request<CourseSummary[]>("/courses"),
  curriculum: () => request<CurriculumMap>("/curriculum"),
  course: (id: string) => request<Course>(`/courses/${encode(id)}`),
  lesson: (id: string, lesson: string) =>
    request<Lesson>(`/courses/${encode(id)}/lessons/${encode(lesson)}`),
  sources: () => request<Source[]>("/sources"),
  enrollments: () => request<Enrollment[]>("/enrollments"),
  enroll: (course_id: string) =>
    request<Enrollment>("/enrollments", "POST", { course_id }),
  upgradeEnrollment: (id: string) =>
    request<Enrollment>(`/enrollments/${encode(id)}/version`, "PUT", {}),
  assessmentPlan: (id: string) =>
    request<AssessmentPlan>(`/assessments/${encode(id)}`),
  gradedAssessment: (id: string, assessmentId: string) =>
    request<GradedAssessment>(
      `/assessments/${encode(id)}/${encode(assessmentId)}/questions`,
    ),
  submitGradedAssessment: (
    id: string,
    assessmentId: string,
    responses: Record<string, AssessmentAnswer>,
  ) =>
    request<GradedSubmission>(
      `/assessments/${encode(id)}/${encode(assessmentId)}/submissions`,
      "POST",
      { responses },
    ),
  gradedSubmissions: (id: string) =>
    request<GradedSubmission[]>(`/assessments/${encode(id)}/submissions`),
  progress: (id: string) => request<Progress[]>(`/progress/${encode(id)}`),
  setProgress: (id: string, lesson: string, completed: boolean) =>
    request<Progress>(`/progress/${encode(id)}/${encode(lesson)}`, "PATCH", {
      completed,
    }),
  notes: (id: string) => request<Note[]>(`/notes/${encode(id)}`),
  saveNote: (id: string, lesson: string, body: string) =>
    request<Note>(`/notes/${encode(id)}/${encode(lesson)}`, "PUT", { body }),
  bookmarks: () => request<string[]>("/bookmarks"),
  bookmark: (id: string, saved: boolean) =>
    request(`/bookmarks/${encode(id)}`, "PUT", { saved }),
  attempt: (
    id: string,
    question: string,
    response: string | number | number[] | Record<string, string>,
    unit?: string,
    variantToken?: string | null,
  ) =>
    request<Attempt>(
      `/courses/${encode(id)}/questions/${encode(question)}/attempts`,
      "POST",
      {
        response,
        ...(unit ? { unit } : {}),
        ...(variantToken ? { variant_token: variantToken } : {}),
      },
    ),
  attempts: (id: string) =>
    request<Attempt[]>(`/attempts?course_id=${encode(id)}`),
  requestAppeal: (attemptId: string, reason: string) =>
    request<Appeal>(`/attempts/${encode(attemptId)}/appeals`, "POST", {
      reason,
    }),
  instructorAppeals: (status = "open") =>
    request<InstructorAppeal[]>(`/instructor/appeals?status=${encode(status)}`),
  reviewAppeal: (
    appealId: string,
    decision: "adjusted" | "upheld" | "declined",
    review_note: string,
    override_score?: number,
  ) =>
    request<InstructorAppeal>(
      `/instructor/appeals/${encode(appealId)}/review`,
      "POST",
      {
        decision,
        review_note,
        ...(override_score !== undefined ? { override_score } : {}),
      },
    ),
  gradebook: (id: string) => request<Gradebook>(`/gradebook/${encode(id)}`),
  exportData: () => request<unknown>("/learner/export"),
  async deleteLearner() {
    await request("/learner", "DELETE");
    csrfToken = null;
  },
};

export function errorMessage(error: unknown): string {
  return error instanceof Error
    ? error.message
    : "Unable to complete this action. Please try again.";
}
