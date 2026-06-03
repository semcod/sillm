"""Shell LLM client control plane.

``sllm`` owns the shell-client side of semcod/coru LLM automation:
detecting vendor CLIs, building controlled invocations, mapping simple NLP
intents to drive DSL, and exposing a small compatibility layer for Koru.
"""

from sllm.controller import (
    ShellDrivePlan,
    ShellDriveRequest,
    ShellDriveResult,
    build_drive_plan,
    drive_shell_llm,
    save_prompt,
)
from sllm.registry import (
    ShellClientSpec,
    detect_clients,
    get_client_spec,
    iter_client_specs,
    normalize_client_id,
)

__all__ = [
    "ShellClientSpec",
    "ShellDrivePlan",
    "ShellDriveRequest",
    "ShellDriveResult",
    "build_drive_plan",
    "detect_clients",
    "drive_shell_llm",
    "get_client_spec",
    "iter_client_specs",
    "normalize_client_id",
    "save_prompt",
]
