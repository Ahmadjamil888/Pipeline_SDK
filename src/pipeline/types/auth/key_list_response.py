# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["KeyListResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None

    key: Optional[str] = None

    name: Optional[str] = None


class KeyListResponse(BaseModel):
    data: Optional[List[Data]] = None

    total: Optional[int] = None
