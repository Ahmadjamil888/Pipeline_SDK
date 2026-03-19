# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["Repository"]


class Repository(BaseModel):
    id: Optional[int] = None

    clone_url: Optional[str] = None

    default_branch: Optional[str] = None

    description: Optional[str] = None

    full_name: Optional[str] = None

    language: Optional[str] = None

    name: Optional[str] = None

    private: Optional[bool] = None

    updated_at: Optional[datetime] = None

    url: Optional[str] = None
