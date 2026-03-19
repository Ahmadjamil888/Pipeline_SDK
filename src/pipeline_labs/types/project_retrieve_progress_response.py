# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ProjectRetrieveProgressResponse", "ProgressStep"]


class ProgressStep(BaseModel):
    id: Optional[str] = None

    created_at: Optional[datetime] = None

    message: Optional[str] = None

    stage: Optional[str] = None


class ProjectRetrieveProgressResponse(BaseModel):
    progress_steps: Optional[List[ProgressStep]] = None

    project: Optional[object] = None
