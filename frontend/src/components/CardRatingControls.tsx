import { useState } from "react";
import { errorMessage } from "../api";
import type { CardRating, CardReviewResult, CardSchedule } from "../types";

const RATINGS: { value: CardRating; label: string; hint: string }[] = [
  { value: "again", label: "Again", hint: "I could not recall the answer" },
  { value: "hard", label: "Hard", hint: "I recalled it with real effort" },
  { value: "good", label: "Good", hint: "I recalled it after a short pause" },
  { value: "easy", label: "Easy", hint: "I recalled it immediately" },
];

function plural(value: number, unit: string) {
  const rounded = Math.round(value * 10) / 10;
  return `${rounded} ${unit}${rounded === 1 ? "" : "s"}`;
}

export function describeSchedule(
  schedule: CardSchedule,
  nowMs: number = Date.now(),
): string {
  if (schedule.due) return "Due for review now.";
  const due = new Date(schedule.due_at);
  if (schedule.interval_days === 0) {
    const minutes = Math.max(1, Math.round((due.getTime() - nowMs) / 60000));
    return `Shown again in about ${plural(minutes, "minute")}.`;
  }
  return `Next review in ${plural(schedule.interval_days, "day")} (${due.toLocaleDateString(
    undefined,
    { year: "numeric", month: "short", day: "numeric" },
  )}).`;
}

export function CardRatingControls({
  cardId,
  schedule,
  enabled,
  onRate,
}: {
  cardId: string;
  schedule?: CardSchedule | null;
  enabled: boolean;
  onRate: (rating: CardRating) => Promise<CardReviewResult>;
}) {
  const [busy, setBusy] = useState(false);
  const [status, setStatus] = useState("");
  const [error, setError] = useState("");
  async function rate(rating: CardRating) {
    setBusy(true);
    setError("");
    setStatus("");
    try {
      const result = await onRate(rating);
      setStatus(`Saved “${rating}”. ${describeSchedule(result.schedule)}`);
    } catch (error) {
      setError(errorMessage(error));
    } finally {
      setBusy(false);
    }
  }
  return (
    <div
      className="card-rating"
      role="group"
      aria-label={`Rate your recall for card ${cardId}`}
    >
      <p className="muted">
        After revealing the answer, rate your own recall to schedule the next
        review. This is a self-assessment, not a score.
      </p>
      <div className="actions">
        {RATINGS.map((item) => (
          <button
            key={item.value}
            type="button"
            title={item.hint}
            aria-label={`${item.label}: ${item.hint}`}
            disabled={!enabled || busy}
            onClick={() => rate(item.value)}
          >
            {item.label}
          </button>
        ))}
      </div>
      {schedule && !status && (
        <p className="muted">{describeSchedule(schedule)}</p>
      )}
      {status && <p role="status">{status}</p>}
      {error && (
        <p role="alert" className="error">
          {error}
        </p>
      )}
    </div>
  );
}
