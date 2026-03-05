# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["TrainingListResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None

    config: Optional[object] = None

    name: Optional[str] = None

    status: Optional[str] = None


class TrainingListResponse(BaseModel):
    data: Optional[List[Data]] = None

    total: Optional[int] = None
