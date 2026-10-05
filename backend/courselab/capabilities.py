"""Future interfaces are explicit, disabled capabilities in this milestone.

An isolated runner implementation must live in a separate execution service.
The web server must never execute a submission, shell out, mount a Docker socket,
or expose host paths to a submission. Network-disabled ephemeral containers,
read-only images, limits, deadlines and an allowlisted environment are prerequisites.
"""

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class ExecutionRequest:
    submission_id: str
    assignment_revision: str
    source: str


@dataclass(frozen=True)
class ExecutionReport:
    state: str
    message: str


class IsolatedRunner(Protocol):
    def submit(self, request: ExecutionRequest) -> ExecutionReport: ...


class DisabledRunner:
    def submit(self, request: ExecutionRequest) -> ExecutionReport:
        return ExecutionReport("unavailable", "Programming grading is disabled until an isolated runner is validated.")


class FeedbackProvider(Protocol):
    """An implementation may elaborate feedback; it must not alter stored scores.

    Implementations must accept bounded rubric evidence without provider credentials
    in the request. Credentials are operator/user-supplied server-side secrets.
    LLM implementations and API credentials are not enabled in milestone 2.
    """
    def elaborate(self, rubric_evidence: dict) -> dict: ...
