# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .repository_param import RepositoryParam

__all__ = ["RepoConnectParams"]


class RepoConnectParams(TypedDict, total=False):
    repo: Required[RepositoryParam]

    user_id: Required[str]
