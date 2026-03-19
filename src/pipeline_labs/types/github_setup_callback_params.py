# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["GitHubSetupCallbackParams"]


class GitHubSetupCallbackParams(TypedDict, total=False):
    installation_id: Required[int]

    setup_action: Literal["install", "update"]

    state: str
    """User ID passed during installation"""
