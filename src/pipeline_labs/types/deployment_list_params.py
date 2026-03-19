# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["DeploymentListParams"]


class DeploymentListParams(TypedDict, total=False):
    limit: int

    offset: int

    repo_id: str

    status: Literal["pending", "running", "succeeded", "failed", "cancelled"]
