"""Signed, reproducible selection for explicitly authored formative variants."""

import base64
import hashlib
import hmac
import json
import secrets
import time
from copy import deepcopy

TOKEN_TTL_SECONDS = 7 * 24 * 60 * 60
GENERATOR_ID = "authored-variants-v1"
VARIANT_FIELDS = ("prompt", "options", "solution_spec", "feedback")


class VariantTokenError(ValueError):
    """A missing, malformed, expired, or context-mismatched variant token."""


def variant_ids(question: dict) -> list[str]:
    config = question.get("randomization")
    if config is None:
        return []
    if (
        not isinstance(config, dict)
        or config.get("seeded") is not True
        or config.get("generator_id") != GENERATOR_ID
        or not isinstance(config.get("variants"), list)
        or not config["variants"]
    ):
        raise VariantTokenError("Authored variant configuration is unsupported")
    identifiers = ["base"]
    for variant in config["variants"]:
        if not isinstance(variant, dict) or not isinstance(variant.get("id"), str):
            raise VariantTokenError("Authored variant configuration is invalid")
        identifiers.append(variant["id"])
    if len(identifiers) != len(set(identifiers)):
        raise VariantTokenError("Authored variant identifiers must be unique")
    return identifiers


def resolve_variant(question: dict, variant_id: str | None) -> dict:
    """Return a standalone grader spec with the selected authored override applied."""
    identifiers = variant_ids(question)
    if not identifiers:
        if variant_id is not None:
            raise VariantTokenError("This question has no variants")
        return deepcopy(question)
    if variant_id not in identifiers:
        raise VariantTokenError("Variant identifier is not in this question bank")
    resolved = deepcopy(question)
    variants = resolved.pop("randomization")["variants"]
    if variant_id == "base":
        return resolved
    selected = next(variant for variant in variants if variant["id"] == variant_id)
    for field in VARIANT_FIELDS:
        if field in selected:
            resolved[field] = deepcopy(selected[field])
    return resolved


def _b64encode(value: bytes) -> str:
    return base64.urlsafe_b64encode(value).decode("ascii").rstrip("=")


def _b64decode(value: str) -> bytes:
    decoded = base64.urlsafe_b64decode(value + "=" * (-len(value) % 4))
    if _b64encode(decoded) != value:
        raise ValueError("Noncanonical base64")
    return decoded


def _seeded_variant_id(
    question: dict,
    course_id: str,
    content_version: str,
    seed: str,
    secret: bytes,
) -> str:
    ids = variant_ids(question)
    context = "\0".join((course_id, content_version, question["id"], seed)).encode("utf-8")
    selection = hmac.new(secret, context, hashlib.sha256).digest()
    return ids[int.from_bytes(selection[:8], "big") % len(ids)]


def issue_variant_token(
    question: dict,
    course_id: str,
    content_version: str,
    secret: bytes,
    *,
    now: int | None = None,
) -> tuple[str | None, str | None, dict]:
    """Issue a bounded bearer token and return its reproducible selected spec."""
    if not variant_ids(question):
        return None, None, resolve_variant(question, None)
    if len(secret) < 32:
        raise VariantTokenError("Variant signing key must be at least 32 bytes")
    seed = secrets.token_urlsafe(24)
    expires = (int(time.time()) if now is None else now) + TOKEN_TTL_SECONDS
    payload = {
        "v": 1,
        "course": course_id,
        "version": content_version,
        "question": question["id"],
        "seed": seed,
        "exp": expires,
    }
    encoded = _b64encode(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8"))
    signature = _b64encode(hmac.new(secret, encoded.encode("ascii"), hashlib.sha256).digest())
    token = f"{encoded}.{signature}"
    variant_id = _seeded_variant_id(question, course_id, content_version, seed, secret)
    return token, variant_id, resolve_variant(question, variant_id)


def verify_variant_token(
    question: dict,
    course_id: str,
    content_version: str,
    token: str | None,
    secret: bytes,
    *,
    now: int | None = None,
) -> tuple[dict, str | None]:
    """Verify that a submission uses the exact authored variant issued for it."""
    if not variant_ids(question):
        if token is not None:
            raise VariantTokenError("This question does not accept a variant token")
        return resolve_variant(question, None), None
    if not token or len(token) > 2048 or len(secret) < 32:
        raise VariantTokenError("Question variant token is missing or invalid")
    try:
        encoded, supplied_signature = token.split(".", maxsplit=1)
        signature = _b64decode(supplied_signature)
        expected_signature = hmac.new(secret, encoded.encode("ascii"), hashlib.sha256).digest()
        if not hmac.compare_digest(signature, expected_signature):
            raise ValueError("Invalid signature")
        payload = json.loads(_b64decode(encoded))
        if (
            not isinstance(payload, dict)
            or set(payload) != {"v", "course", "version", "question", "seed", "exp"}
            or payload["v"] != 1
            or payload["course"] != course_id
            or payload["version"] != content_version
            or payload["question"] != question["id"]
            or not isinstance(payload["seed"], str)
            or not 20 <= len(payload["seed"]) <= 100
            or type(payload["exp"]) is not int
            or payload["exp"] <= (int(time.time()) if now is None else now)
        ):
            raise ValueError("Token context or expiry is invalid")
        variant_id = _seeded_variant_id(question, course_id, content_version, payload["seed"], secret)
        return resolve_variant(question, variant_id), variant_id
    except (UnicodeError, ValueError, TypeError, KeyError, json.JSONDecodeError) as exc:
        raise VariantTokenError("Question variant token is invalid or expired") from exc
