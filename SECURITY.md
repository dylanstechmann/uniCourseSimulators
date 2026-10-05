# Security policy

This is development software. The preserved browser reader contains public practice answers and editable scores. It is unsuitable for secure examinations or confidential student records.

Use synthetic data. Server account records, session secrets, provider credentials and production assessment specifications must be excluded from Git/frontend assets. Public repository authoring solutions are intentionally discoverable; production exam secrecy requires a separate private content store and release policy.

Never execute submitted code in the API. The future runner requires ephemeral containers with no network, Docker socket, host mounts or writable base filesystem; bounded CPU, memory, processes and runtime; temporary submission storage; and an explicit dependency allowlist. Code assignments stay disabled until isolation is implemented and adversarially tested.

Provider keys remain server-side, logs scrubbed, deterministic scores authoritative. Learner text, sources and model output are untrusted. Feedback cannot authorize tools, access solutions or change policy.

Report vulnerabilities through GitHub private vulnerability reporting if enabled, or an established private channel to the owner. Include version, synthetic reproduction and impact; omit credentials and personal data. No penetration test or security certification is claimed.
