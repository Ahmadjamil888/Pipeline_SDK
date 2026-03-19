# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SandboxListParams"]


class SandboxListParams(TypedDict, total=False):
    limit: int

    status: Literal["creating", "running", "stopped", "error", "destroyed"]
