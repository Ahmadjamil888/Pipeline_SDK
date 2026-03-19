# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

from .sandbox_resources_param import SandboxResourcesParam

__all__ = ["SandboxCreateParams"]


class SandboxCreateParams(TypedDict, total=False):
    branch: str

    environment_variables: Dict[str, str]

    repo_id: str

    repo_url: str

    resources: SandboxResourcesParam
