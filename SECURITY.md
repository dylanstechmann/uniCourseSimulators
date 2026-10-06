# Security policy

This is development software. The preserved browser reader contains public practice answers and editable scores. It is unsuitable for secure examinations or confidential student records.

Use synthetic data. Server account records, session secrets, provider credentials and production assessment specifications must be excluded from Git/frontend assets. Public repository authoring solutions are intentionally discoverable; production exam secrecy requires a separate private content store and release policy.

Never execute submitted code in the API. The future runner requires ephemeral containers with no network, Docker socket, host mounts or writable base filesystem; bounded CPU, memory, processes and runtime; temporary submission storage; and an explicit dependency allowlist. Code assignments stay disabled until isolation is implemented and adversarially tested.

Provider keys remain server-side, logs scrubbed, deterministic scores authoritative. Learner text, sources and model output are untrusted. Feedback cannot authorize tools, access solutions or change policy.

Instructor appeal review is disabled unless an operator sets `INSTRUCTOR_EMAILS` to a comma-separated allowlist. Reviewers must register accounts for those exact normalized email addresses; guest sessions cannot adjudicate, and instructors cannot review their own attempts. Keep the allowlist limited to qualified staff and protect account recovery. Appeal requests and decisions are stored separately from immutable automatic attempts; each attempt permits one request and one review. The original course version must still be available for an adjustment or upheld decision. Deleting a learner removes their own appeal data; deleting a reviewer anonymizes the reviewer reference while preserving the decision audit. There is no general role-management UI or protected exam workflow.

Report vulnerabilities through GitHub private vulnerability reporting if enabled, or an established private channel to the owner. Include version, synthetic reproduction and impact; omit credentials and personal data. No penetration test or security certification is claimed.
