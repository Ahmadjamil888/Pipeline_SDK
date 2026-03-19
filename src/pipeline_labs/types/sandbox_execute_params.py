# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["SandboxExecuteParams"]


class SandboxExecuteParams(TypedDict, total=False):
    command: Required[str]

    env_variables: Dict[str, str]

    timeout_seconds: int

    working_directory: str
