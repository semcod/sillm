"""Lightweight validation hooks for SLLM ecosystem integration."""

from __future__ import annotations

import importlib.util
from dataclasses import dataclass

from sllm.nlp import ShellIntent
from sllm.registry import get_client_spec


@dataclass(frozen=True)
class ValidationResult:
    ok: bool
    errors: tuple[str, ...] = ()

    def to_dict(self) -> dict[str, object]:
        return {"ok": self.ok, "errors": list(self.errors)}


def validate_intent(intent: ShellIntent) -> ValidationResult:
    errors: list[str] = []
    if get_client_spec(intent.client_id) is None:
        errors.append(f"unknown client: {intent.client_id}")
    if not intent.prompt.strip():
        errors.append("prompt is empty")
    return ValidationResult(ok=not errors, errors=tuple(errors))


def ecosystem_status() -> dict[str, object]:
    packages = {
        "nlp2dsl": "nlp2dsl_sdk",
        "intract": "intract",
        "redsl": "redsl",
        "proxym": "proxym",
        "llx": "llx",
    }
    return {
        "ok": True,
        "packages": {
            name: {"import": module, "available": importlib.util.find_spec(module) is not None}
            for name, module in packages.items()
        },
    }


__all__ = ["ValidationResult", "ecosystem_status", "validate_intent"]
