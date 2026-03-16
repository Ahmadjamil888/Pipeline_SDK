# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RepoConnection"]


class RepoConnection(BaseModel):
    id: str
    """Unique identifier for the connected repository"""

    created_at: datetime

    provider: Literal["github", "gitlab"]

    repo_url: str

    status: Literal["pending", "connected", "analyzing", "error"]

    branch: Optional[str] = None

    name: Optional[str] = None

    updated_at: Optional[datetime] = None
