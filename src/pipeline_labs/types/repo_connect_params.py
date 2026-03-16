# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RepoConnectParams"]


class RepoConnectParams(TypedDict, total=False):
    provider: Required[Literal["github", "gitlab"]]
    """Git provider"""

    repo_url: Required[str]
    """Full URL to the Git repository"""

    branch: str
    """Default branch to use"""

    name: str
    """Optional custom name for the repository"""
