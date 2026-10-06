# uniStemCourseSimulators frontend

React and TypeScript render public course metadata and Markdown returned by
the FastAPI API. Course packages and private answer specifications are never
imported into the frontend. Raw HTML in Markdown is disabled; unsafe URL
schemes are rejected by the Markdown renderer. Learner notes render as text.

The production image uses nginx and proxies `/api/` to `api:8000`. Its build
context is this directory only. The historical local reader is not included
in the image. The link to `http://localhost:4173/` is a separate local tool;
its browser scores are explicitly unverified and do not feed this gradebook.

## Developer commands

Use the repository's Compose development service for `npm ci`, `npm run lint`,
`npm run test`, `npm run build`, and `npm run test:e2e`. The parent README
documents the complete application's one-command Compose startup.

For a standalone Vite development server, `npm run dev` binds port 5173.
`API_PROXY_TARGET` selects its API proxy destination (default `http://api:8000`).
The API must allow the actual browser Origin. Production uses the same-origin
nginx proxy and does not need browser API credentials in environment variables.

Playwright expects a running complete application at `E2E_BASE_URL`
(default `http://localhost:8080`). Install the Chromium browser and its system
dependencies in the test container using `npx playwright install --with-deps
chromium` before running end-to-end tests. Do not use the frontend's nginx
runtime container to run tests. Pin the Playwright container/browser version
to the version in `package-lock.json` if using a prebuilt test image.

## Current behavior and limits

The app supports guest/account sessions, enrollment, safe lesson reading,
single-choice and numerical formative submissions, layered result feedback,
reading marks, notes, course bookmarks, practice evidence/history, learner-data
export, account deletion with typed confirmation, and text/contrast controls.
Session cookies are HttpOnly. Mutations use the API-issued CSRF token;
authentication and account ownership are enforced by the backend.

A read mark is a learner self-report. A correct practice result does not assess
reasoning, mastery, transfer, or course completion. The current gradebook
aggregates practice results and does not claim a weighted semester grade.
Exams, deadlines, objective mastery models, appeals, and advanced graders are
future milestones. Content maturity and omissions remain visible.

Vitest exercises the Markdown boundary, numerical value/unit validation,
disabled non-enrolled submission, result-versus-reasoning feedback, maturity
labels/filtering, and CSRF request behavior. Playwright exercises real saved
enrollment/submission/feedback/notes/progress, guest-to-account preservation,
export/deletion, public DTO answer exclusion, and axe WCAG checks on catalog
and lesson views. Automated accessibility checks supplement manual review.
