export type Maturity =
  | "catalog-only"
  | "outlined"
  | "partial"
  | "beta"
  | "complete"
  | "externally reviewed";
export interface User {
  id: string;
  email: string | null;
  is_guest: boolean;
}
export interface Session {
  user: User | null;
  csrf_token: string | null;
}
export interface CourseSummary {
  id: string;
  title: string;
  description: string;
  domain: string;
  level: string;
  maturity: Maturity;
  version: string;
  lesson_count: number;
  limitations: string[];
}
export interface LearningObjective {
  id: string;
  description: string;
  bloom: string;
}
export interface LessonSummary {
  id: string;
  title: string;
  learning_objective_ids: string[];
}
export interface Course extends CourseSummary {
  prerequisites: {
    course_ids: string[];
    recommended_course_ids: string[];
    concurrent_course_ids: string[];
    knowledge: string[];
    statement: string;
  };
  outcomes: LearningObjective[];
  lesson_objectives: LearningObjective[];
  modules: {
    id: string;
    title: string;
    source_ids: string[];
    lessons: LessonSummary[];
  }[];
  syllabus_markdown: string;
  license: string;
  review_status: unknown;
  assessment_policy: unknown;
}
export interface Question {
  id: string;
  type: "single_choice" | "multiple_select" | "numeric";
  prompt: string;
  options: string[];
  unit?: string;
  significant_figures?: number | null;
  points: number;
  selection?: "single" | "multiple";
  partial_credit_policy?: string | null;
  variant_id?: string | null;
  variant_token?: string | null;
  learning_objective_ids: string[];
  assessment_role: "formative";
}
export interface Lesson {
  id: string;
  title: string;
  markdown: string;
  learning_objective_ids: string[];
  source_ids: string[];
  worked_example: string;
  questions: Question[];
}
export interface Enrollment {
  course_id: string;
  content_version: string;
  created_at: string;
}
export interface Progress {
  lesson_id: string;
  completed: boolean;
  evidence: "learner-marked";
  updated_at?: string;
}
export interface Note {
  lesson_id: string;
  body: string;
  updated_at?: string;
}
export interface Feedback {
  diagnosis: string;
  hint?: string;
  misconception: string | null;
  next_step: string;
  lesson_id: string;
  reasoning_assessed: boolean;
  provisional: boolean;
}
export interface Attempt {
  id: string;
  course_id: string;
  question_id: string;
  content_version: string;
  response: {
    response: string | number | number[];
    unit?: string;
    variant_id?: string;
  };
  score: number;
  max_score: number;
  result: {
    score: number;
    max_score: number;
    correct: boolean;
    assessment_role: "formative";
    grading_policy_version: string;
    feedback: Feedback;
  };
  objective_ids: string[];
  created_at: string;
}
export interface Gradebook {
  course_id: string;
  assessment_role: "formative";
  aggregation: string;
  score: number;
  max_score: number;
  attempt_count: number;
  objective_evidence: Record<
    string,
    { attempts: number; correct_results: number }
  >;
  limitations: string;
}
export interface Source {
  id: string;
  title: string;
  url: string;
  institution: string;
}
