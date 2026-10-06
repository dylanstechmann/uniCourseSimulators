# Running and deploying Lattice CourseLab

The default configuration runs a local learning system. `compose.production.yaml` is an operator example with Caddy HTTPS; it is not evidence of a public deployment or production security review. [VALIDATION_REPORT.md](VALIDATION_REPORT.md) records the checks actually performed. Courses remain partial, and the current server gradebook contains formative practice results only.

## Local startup

Install Docker Engine or Docker Desktop with the Compose plugin, then run from the repository root:

```sh
docker compose up --build
```

Open `http://localhost:8080`. No `.env` file, manually chosen database password or provider credential is needed. The `credentials` initialization service generates a random database password in a named volume. PostgreSQL starts on an internal Docker network, the `migrate` service applies Alembic revisions, the API starts after migration success, and nginx serves the compiled React application and proxies `/api/` to FastAPI. Only the web port is published, bound to loopback. A catalog/lesson can be read without an account; a guest or registered account is needed for persisted enrollment, attempts, notes and progress.

The database and credentials volumes persist across container recreation. Stop the foreground run with Ctrl+C, or use `docker compose down` after a detached run. Keep the volumes when learner records are needed. Removing a volume destroys its stored data; deleting only the credentials volume leaves the existing PostgreSQL password inconsistent with a newly generated secret. PostgreSQL initialization variables do not rotate an existing cluster's password.

Optional local configuration comes from `.env.example`; copy it to an untracked `.env` and edit only what is needed. If `COURSELAB_PORT` changes, update `ALLOWED_ORIGINS` to the exact matching localhost/127.0.0.1 origins. Development uses `COOKIE_SECURE=false` for local HTTP. Set `INSTRUCTOR_EMAILS` to a comma-separated list of registered reviewer accounts to enable the appeal queue; leave it empty to disable instructor review. The `.env` files, secrets, database files, backups and learner exports are excluded from Git, but an ignore rule is not a substitute for inspecting staged changes.

Set `INSTRUCTOR_EMAILS` to an explicit comma-separated allowlist of registered account emails to enable instructor review. An empty value keeps the review queue disabled. Protect account recovery and avoid exposing the instructor allowlist in frontend configuration.

Useful diagnostics:

```sh
docker compose ps
docker compose logs --tail=100 migrate api web
docker compose exec -T api python -c "import urllib.request; print(urllib.request.urlopen('http://127.0.0.1:8000/api/v1/health').status)"
```

The health endpoint checks database connectivity; it is not an assessment-quality, security or full learner-workflow certification. Do not enable SQL parameter logging or log request bodies containing passwords, notes or learner responses.

## Database migrations and updates

The API does not automatically create tables through ORM metadata. Alembic's versioned revisions are the deployment boundary. From a running local setup:

```sh
docker compose exec -T api alembic current
docker compose run --rm migrate
```

The second command runs `alembic upgrade head` using the same image, database and secret as the API. Revision 0002 adds an optional question-specification digest to attempts; revision 0003 adds learner appeals and append-only instructor review decisions. Old attempts are preserved and marked unpinned. For an application update, take and verify a backup, stop API/web writes, build the reviewed version, apply its migrations, and restart the application. Read each migration before applying it to valuable data. A downgrade is not a general data-recovery mechanism; some future changes may be irreversible. The initial, digest, and appeal revisions' upgrade/downgrade/schema comparison is covered by backend tests.

Content is copied into the API image at `/content`. Rebuild when course packages change. Enrollments record their course version; a changed version blocks version-dependent operations until the learner uses the explicit `PUT /api/v1/enrollments/{course_id}/version` action. This updates the enrollment pointer and preserves earlier attempts with their original course version. Do not rewrite published content under an unchanged version to bypass that boundary.

## Production example, domain and HTTPS

Use a host with Docker/Compose, a DNS hostname controlled by the operator, and network access suitable for certificate issuance. Set the hostname's A/AAAA records to that host, permit inbound TCP 80/443, and keep PostgreSQL/API ports unpublished. `COURSELAB_DOMAIN` must be the hostname alone, with no scheme, path or GitHub URL. The example does not depend on a particular cloud provider.

Create an untracked `.env.production` containing the intended `COURSELAB_DOMAIN`, an absolute `DB_PASSWORD_FILE` outside the checkout, and a stable random `VARIANT_TOKEN_SECRET` of at least 32 bytes. Generate a fresh secret only when initializing a new deployment and keep it stable across API restarts so unexpired practice variant tokens remain usable. A Linux host example below creates an operator-private directory and permits the API's uid 10001 to read the database secret without printing it:

```sh
sudo install -d -m 0700 /srv/courselab-secrets
sudo sh -c 'umask 077; test ! -e /srv/courselab-secrets/db-password && openssl rand -base64 32 > /srv/courselab-secrets/db-password'
sudo chown 10001:10001 /srv/courselab-secrets/db-password
sudo chmod 0440 /srv/courselab-secrets/db-password
openssl rand -hex 32
```

Store the generated `openssl` output as `VARIANT_TOKEN_SECRET` in `.env.production`; never commit it.

Set `DB_PASSWORD_FILE` to that file. Run subsequent production Docker commands as the host administrator (using `sudo` where needed), because the example secret directory is accessible only to that administrator. File-backed Compose secrets use host file permissions; uid/gid/mode remapping is not supported for that form. [Docker Compose secrets](https://docs.docker.com/reference/compose-file/services/#secrets). Check readability as the API's container user before starting; the following command reads without displaying the value:

```sh
docker compose --env-file .env.production -f compose.production.yaml config --quiet
docker compose --env-file .env.production -f compose.production.yaml build
docker compose --env-file .env.production -f compose.production.yaml run --rm --no-deps api python -c "from pathlib import Path; assert Path('/run/secrets/db-password').read_text().strip(); print('Secret is readable')"
docker compose --env-file .env.production -f compose.production.yaml up -d
```

The production file is a standalone configuration: use `-f compose.production.yaml`, rather than combining it with development port/cookie settings. It has its own Compose project name and volumes. Its API enables secure cookies and accepts only `https://<COURSELAB_DOMAIN>` as the mutation origin. Caddy loads [deploy/Caddyfile](../deploy/Caddyfile), terminates HTTPS and proxies to nginx; nginx routes API requests internally. Preserve Caddy's data/config volumes for certificate state. Caddy's public certificate automation depends on its documented DNS and reachability requirements. [Caddy automatic HTTPS](https://caddyserver.com/docs/automatic-https).

Inspect service status, certificate errors and the learner workflow over HTTPS before opening the service to learners. If using a custom port or another proxy, deliberately update allowed origins and trusted forwarding configuration. HTTPS cookies will not work over plain HTTP. Password rotation must update PostgreSQL's actual role password and the mounted secret together; changing a file alone does not rotate an existing database. Plan rotation and session revocation without putting secret values in shell history or logs.

## Backup

Learner exports are not a database backup. Keep encrypted, access-controlled, off-host backups of PostgreSQL, the matching code/content version, migration revision and the private deployment configuration/secret needed for recovery. Database dumps contain learner records, password hashes and session records; handle them as private data. A database dump does not include global role definitions or Caddy certificate volumes. Define retention and recovery objectives, and rehearse restoration on an isolated deployment.

The following commands use the **development** project and create a PostgreSQL custom-format archive. Create the ignored `backups/` directory first (`mkdir -p backups` in a POSIX shell, or `New-Item -ItemType Directory -Path backups -Force` in PowerShell). Use a unique filename for each backup, replacing the illustrative date below:

```sh
docker compose exec -T db pg_dump -U courselab -d courselab --format=custom --file=/tmp/courselab-backup.dump
docker compose exec -T db chmod 600 /tmp/courselab-backup.dump
docker compose cp db:/tmp/courselab-backup.dump backups/courselab-2026-10-05.dump
docker compose exec -T db rm /tmp/courselab-backup.dump
```

Inspect every command's exit status and dump warnings. Restrict permissions on the host copy and encrypt it before external storage. `docker compose cp` copies the binary archive directly; avoid PowerShell text redirection or text pipelines for custom-format dumps. In production, substitute `docker compose --env-file .env.production -f compose.production.yaml` for `docker compose` in each command. PostgreSQL documents the snapshot consistency and custom-archive behavior of [`pg_dump`](https://www.postgresql.org/docs/17/app-pgdump.html).

## Restore safely into a separate database

Use only a trusted archive from the intended deployment. Restore into a new database first, keeping the active `courselab` database unchanged. The commands below deliberately fail if `courselab_restore` already exists; choose a new recovery name instead of deleting an existing database to make the command pass.

```sh
docker compose cp backups/courselab-2026-10-05.dump db:/tmp/courselab-restore.dump
docker compose exec -T db pg_restore --list /tmp/courselab-restore.dump
docker compose exec -T db createdb -U courselab --template=template0 courselab_restore
docker compose exec -T db pg_restore -U courselab --dbname=courselab_restore --no-owner --no-privileges --exit-on-error --single-transaction /tmp/courselab-restore.dump
docker compose exec -T db psql -U courselab -d courselab_restore -c "SELECT version_num FROM alembic_version;"
docker compose exec -T db psql -U courselab -d courselab_restore -c "SELECT count(*) AS learner_count FROM users;"
docker compose exec -T db rm /tmp/courselab-restore.dump
```

Review the archive inventory before restoration. `--single-transaction` with `--exit-on-error` prevents a partially applied restore from being mistaken for success. `--no-owner --no-privileges` suits the current single-role deployment; when introducing least-privilege roles, restore ownership/grants through the reviewed role provisioning process. PostgreSQL explains these options and the execution of statements contained in trusted dumps in [`pg_restore`](https://www.postgresql.org/docs/17/app-pgrestore.html).

Run the matching application revision against the restored database in an isolated recovery configuration, inspect records, and exercise enrollment, lesson reading, submission, feedback and persisted progress. Do not expose restored learner data or restored sessions to the public during rehearsal. Plan a controlled maintenance cutover with writes stopped and a fresh backup. The example production file fixes the database name to `courselab`; a recovery override must set the API's `DB_NAME` to the restored name, and a reviewed migration/role plan must accompany any cutover. These commands document a recovery procedure; they do not assert that a public production recovery has been executed.

## Credential and execution boundaries

The application reads database credentials server-side from a secret file. `DATABASE_URL` overrides secret-file settings for tests or a deliberate operator configuration; it can contain a password and must never be printed or committed. The API uses hashed opaque session tokens, HttpOnly cookies, exact Origin/CSRF checks and application-level ownership filters. Learner data is stored in PostgreSQL; deleting browser storage is not server account deletion.

No provider credentials are required or supported by this milestone. LLM feedback and programming execution remain disabled. Future provider keys and restricted exam specifications need private server stores and disclosure policies. Neither the API nor the development containers should receive a Docker socket, host credential mount or arbitrary submission execution capability. The API image runs as uid 10001 with a read-only filesystem, dropped capabilities and a bounded temporary mount. Those controls do not constitute an isolated programming grader.

## Current hardening limits

Before public use, address the following concrete limitations of the example:

- The API and migrations currently share the PostgreSQL bootstrap role. Split database administration/migration privileges from a least-privilege runtime role; ownership isolation is currently enforced by application queries, not database row-level policies.
- Mutation throttling is an in-memory single-worker limiter. Configure a shared production limiter, deliberate proxy trust and real-client attribution; the default network peer behind nginx is not a reliable per-learner identity.
- Explicit CPU/memory limits, image digest pinning and operating-system image vulnerability checks remain operator work. Python dependency audit results are in [backend/DEPENDENCY_AUDIT.md](../backend/DEPENDENCY_AUDIT.md).
- Email verification, password recovery, shared session administration, guest-data retention/cleanup, privacy procedures, monitoring and incident response require implementation or operator policy. Expired guest sessions do not currently clean up their learner records automatically.
- Concurrent unique-key writes return a safe 409 and need retry; atomic upserts and robust client retry policy remain to be implemented.
- The production Compose example lacks a full deployment health/readiness and rollback strategy, automated backup scheduling and demonstrated recovery objectives. The root validation report records development checks; it does not certify the public example.
- Restricted exams, protected exams, advanced graders, a validated code runner, full-course content gates and human course review remain roadmap work. Public seed practice specifications cannot protect a high-stakes exam.
