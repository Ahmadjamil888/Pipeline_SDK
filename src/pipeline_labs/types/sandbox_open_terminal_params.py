# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["SandboxOpenTerminalParams"]


class SandboxOpenTerminalParams(TypedDict, total=False):
    environment_variables: Dict[str, str]

    shell: str

    working_directory: str
