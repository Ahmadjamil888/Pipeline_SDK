# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["LogRetrieveResponse", "LogRetrieveResponseItem"]


class LogRetrieveResponseItem(BaseModel):
    content: Optional[str] = None

    timestamp: Optional[datetime] = None


LogRetrieveResponse: TypeAlias = List[LogRetrieveResponseItem]
