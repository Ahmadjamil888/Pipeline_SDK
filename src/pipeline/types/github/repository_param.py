# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RepositoryParam"]


class RepositoryParam(TypedDict, total=False):
    id: int

    clone_url: str

    default_branch: str

    description: Optional[str]

    full_name: str

    language: Optional[str]

    name: str

    private: bool

    updated_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    url: str
