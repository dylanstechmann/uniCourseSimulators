import type {
  CardRating,
  CardReviewResult,
  ReviewQueue,
  ReviewQueueCard,
} from "../types";
import { CardRatingControls } from "./CardRatingControls";
import { MarkdownReader } from "./MarkdownReader";

function ReviewCard({
  courseId,
  card,
  enabled,
  onRate,
}: {
  courseId: string;
  card: ReviewQueueCard;
  enabled: boolean;
  onRate: (cardId: string, rating: CardRating) => Promise<CardReviewResult>;
}) {
  return (
    <li className="review-card">
      <h4>{card.front}</h4>
      <p className="muted">
        From{" "}
        <a
          href={`#/course/${encodeURIComponent(courseId)}/lesson/${encodeURIComponent(card.lesson_id)}`}
        >
          {card.lesson_title}
        </a>
        {card.content_changed_since_last_review &&
          " · card text changed since your last review, so its schedule restarted"}
      </p>
      <details aria-label={`Answer for card ${card.card_id}`}>
        <summary>Reveal answer</summary>
        <MarkdownReader>{card.back}</MarkdownReader>
        <CardRatingControls
          cardId={card.card_id}
          schedule={card.schedule}
          enabled={enabled}
          onRate={(rating) => onRate(card.card_id, rating)}
        />
      </details>
    </li>
  );
}

export function ReviewQueueView({
  courseId,
  queue,
  enabled,
  onRate,
}: {
  courseId: string;
  queue: ReviewQueue;
  enabled: boolean;
  onRate: (cardId: string, rating: CardRating) => Promise<CardReviewResult>;
}) {
  return (
    <section className="card" aria-labelledby="review-queue-heading">
      <h2 id="review-queue-heading">Spaced retrieval review</h2>
      <p className="score" aria-live="polite">
        {queue.counts.due} due now · {queue.counts.new} not yet reviewed ·{" "}
        {queue.counts.upcoming} scheduled later
      </p>
      <p className="notice">{queue.limitations}</p>
      <details>
        <summary>How the schedule works</summary>
        <p>{queue.policy}</p>
      </details>
      <h3>Due now</h3>
      {queue.due.length === 0 ? (
        <p>No cards are due right now.</p>
      ) : (
        <ol aria-label="Cards due now">
          {queue.due.map((card) => (
            <ReviewCard
              key={card.card_id}
              courseId={courseId}
              card={card}
              enabled={enabled}
              onRate={onRate}
            />
          ))}
        </ol>
      )}
      <h3>Not yet reviewed</h3>
      {queue.new.length === 0 ? (
        <p>Every published card in this package has a schedule.</p>
      ) : (
        <ol aria-label="Cards not yet reviewed">
          {queue.new.map((card) => (
            <ReviewCard
              key={card.card_id}
              courseId={courseId}
              card={card}
              enabled={enabled}
              onRate={onRate}
            />
          ))}
        </ol>
      )}
      <h3>Scheduled later</h3>
      {queue.upcoming.length === 0 ? (
        <p>No cards are scheduled for later yet.</p>
      ) : (
        <div
          className="table-scroll"
          role="region"
          aria-label="Scrollable review schedule table"
          tabIndex={0}
        >
          <table>
            <caption>
              Upcoming reviews, earliest first. Dates are shown in your
              browser&apos;s time zone.
            </caption>
            <thead>
              <tr>
                <th scope="col">Card</th>
                <th scope="col">Lesson</th>
                <th scope="col">Next review</th>
                <th scope="col">Last rating</th>
              </tr>
            </thead>
            <tbody>
              {queue.upcoming.map((card) => (
                <tr key={card.card_id}>
                  <th scope="row">{card.front}</th>
                  <td>{card.lesson_title}</td>
                  <td>
                    {card.schedule
                      ? new Date(card.schedule.due_at).toLocaleString()
                      : "—"}
                  </td>
                  <td>{card.schedule?.last_rating ?? "—"}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </section>
  );
}
