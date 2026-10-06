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
  can_review?: boolean;
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
export interface CurriculumNode {
  id: string;
  title: string;
  domain: string;
  level: string;
  maturity: Maturity;
  description: string;
  prerequisites: {
    course_ids: string[];
    recommended_course_ids: string[];
    concurrent_course_ids: string[];
    knowledge: string[];
    statement: string;
  };
  package_id: string | null;
  related_package_ids: string[];
  relation_note: string | null;
}
export interface CurriculumPathway {
  id: string;
  title: string;
  description: string;
  course_ids: string[];
  source_ids: string[];
  sequence_note: string;
}
export interface CurriculumMap {
  schema_version: string;
  description: string;
  nodes: CurriculumNode[];
  pathways: CurriculumPathway[];
  alignment_maps: {
    id: string;
    title: string;
    source_ids: string[];
    foundational_nodes: string[];
    advanced_nodes: string[];
    disclaimer: string;
  }[];
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
  type:
    | "single_choice"
    | "multiple_select"
    | "numeric"
    | "symbolic"
    | "structured"
    | "data_interpretation"
    | "graph"
    | "file_upload";
  prompt: string;
  options: string[];
  unit?: string;
  significant_figures?: number | null;
  points: number;
  selection?: "single" | "multiple";
  partial_credit_policy?: string | null;
  response_fields?: {
    id: string;
    type: "single_choice" | "numeric";
    prompt: string;
    options: string[];
    unit?: string | null;
    points: number;
  }[];
  graph_spec?: {
    x_axis: { label: string; minimum: number; maximum: number };
    y_axis: { label: string; minimum: number; maximum: number };
    points: { id: string; label: string }[];
    observations: { id: string; x: number; values: number[] }[];
  } | null;
  accepted_media_types?: string[];
  max_upload_bytes?: number | null;
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
  retrieval_cards: {
    id: string;
    front: string;
    back: string;
    learning_objective_ids: string[];
  }[];
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
  components?: {
    field_id: string;
    label: string;
    score: number;
    max_score: number;
    diagnosis: string;
  }[];
}
export interface Attempt {
  id: string;
  course_id: string;
  question_id: string;
  content_version: string;
  response: {
    response: string | number | number[] | Record<string, string>;
    unit?: string;
    variant_id?: string;
  };
  score: number;
  effective_score: number;
  max_score: number;
  appeal: Appeal | null;
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
export interface Appeal {
  id: string;
  attempt_id: string;
  course_id: string;
  question_id: string;
  reason: string;
  status: "open" | "adjusted" | "upheld" | "declined";
  decision: "adjusted" | "upheld" | "declined" | null;
  review_note: string | null;
  original_score: number;
  effective_score: number;
  max_score: number;
  created_at: string;
  reviewed_at: string | null;
}
export interface InstructorAppeal extends Appeal {
  learner: string;
  content_is_current: boolean;
  question_prompt: string | null;
  response: Attempt["response"];
  automatic_feedback: Attempt["result"];
  specification_pinned: boolean;
}
export interface Gradebook {
  course_id: string;
  assessment_role: "formative";
  aggregation: string;
  score: number;
  max_score: number;
  attempt_count: number;
  manual_override_count: number;
  objective_evidence_policy: {
    version: "practice-evidence-v1";
    minimum_distinct_items: number;
    minimum_item_coverage: number;
    minimum_performance: number;
  };
  objective_evidence: Record<
    string,
    {
      attempts: number;
      correct_results: number;
      attempted_items: number;
      item_count: number;
      best_score: number;
      best_possible_score: number;
      performance: number | null;
      status:
        | "no_evidence"
        | "insufficient_evidence"
        | "needs_practice"
        | "provisional_practice_mastery";
    }
  >;
  limitations: string;
}
export interface Source {
  id: string;
  title: string;
  url: string;
  institution: string;
  license?: string;
}
