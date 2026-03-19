# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .repository import Repository

__all__ = ["RepoListResponse"]


class RepoListResponse(BaseModel):
    repos: Optional[List[Repository]] = None
