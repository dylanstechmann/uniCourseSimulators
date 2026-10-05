# Dependency audit — 2026-10-05

`pip-audit 2.10.1` inspected the resolved graph of `backend/requirements.txt` through the workspace Docker `dev` service. The initial graph reported 16 advisory entries across two packages; the entries included duplicate advisory aliases. The affected packages were Starlette 0.46.2, selected by FastAPI 0.115.12, and pytest 8.3.5.

The requirements now explicitly pin FastAPI 0.142.2, Starlette 1.7.0 and pytest 9.1.1. These releases were confirmed through the PyPI registry and tested together with the remaining existing pins. The explicit Starlette pin prevents resolution back to an affected transitive version. Security-sensitive rate-limit classification additionally uses the router's raw ASGI path instead of a URL reconstructed from a caller-controlled Host header.

After the update, Ruff passed, all 71 backend tests passed in 11.31 seconds (including Alembic upgrade/downgrade/metadata comparison), the migrated 25-package/100-practice-item learner integration check passed, and `pip-audit -r requirements.txt` reported **no known vulnerabilities**. The test suite emitted one upstream deprecation warning about Starlette's future preferred test HTTP client; it did not affect the results.

Primary advisory evidence:

- [Starlette multipart rollover denial of service, CVE-2025-54121](https://github.com/Kludex/starlette/security/advisories/GHSA-2c2j-9gv5-cj73): corrected in 0.47.2.
- [Starlette Range parsing denial of service, CVE-2025-62727](https://github.com/Kludex/starlette/security/advisories/GHSA-7f5h-v6xp-fcq8): corrected in 0.49.1.
- [Starlette Host reconstruction, CVE-2026-48710](https://github.com/Kludex/starlette/security/advisories/GHSA-86qp-5c8j-p5mr): corrected in 1.0.1.
- [Starlette arbitrary method dispatch](https://github.com/Kludex/starlette/security/advisories/GHSA-x746-7m8f-x49c): corrected in 1.1.0.
- [Starlette Windows StaticFiles UNC resolution](https://github.com/Kludex/starlette/security/advisories/GHSA-wqp7-x3pw-xc5r): corrected in 1.1.0.
- [Starlette request-path reconstruction, CVE-2026-54282](https://github.com/Kludex/starlette/security/advisories/GHSA-jp82-jpqv-5vv3): corrected in 1.3.0.
- [Starlette urlencoded parser limits, CVE-2026-54283](https://github.com/Kludex/starlette/security/advisories/GHSA-82w8-qh3p-5jfq): corrected in 1.3.1.
- [pytest temporary-directory handling, CVE-2025-71176](https://github.com/advisories/GHSA-6w46-j5rx-g56g): corrected in 9.0.3.

The CourseLab API uses JSON requests and responses; it does not parse form uploads, register `HTTPEndpoint` subclasses, serve `StaticFiles` or emit `FileResponse`. Docker runs Linux, so the Windows UNC issue was not applicable to that runtime. The underlying packages were upgraded without excluding or suppressing these findings. Pytest is used for validation, and upgrading it protects the test environment as well.

Reproduce with a transient environment inside the workspace `dev` service:

```sh
python3 -m venv /tmp/courselab-backend-check
/tmp/courselab-backend-check/bin/pip install -r /workspace/lattice-courselab-backend-wt/backend/requirements.txt pip-audit
cd /workspace/lattice-courselab-backend-wt/backend
/tmp/courselab-backend-check/bin/ruff check .
/tmp/courselab-backend-check/bin/pytest
/tmp/courselab-backend-check/bin/pip-audit -r requirements.txt
```

An audit describes advisories known to the queried database at the time of the run. It does not prove that the application, dependency graph or container operating-system packages are free of vulnerabilities. Re-run on dependency changes and routinely in CI. The container base image requires its own image/OS vulnerability scan.

After adding SymPy 1.14.0 for bounded rational-expression grading, the backend dependency graph was audited again on 2026-10-05 with `uv run --project backend --with pip-audit pip-audit -r backend/requirements.txt`. `pip-audit` reported no known vulnerabilities. The resolver printed transitive-version normalization warnings during setup; the audit completed successfully without advisory findings.
