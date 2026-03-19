# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RepoConnectParams"]


class RepoConnectParams(TypedDict, total=False):
    provider: Required[Literal["github", "gitlab"]]

    repo_url: Required[str]

    branch: str

    name: str
