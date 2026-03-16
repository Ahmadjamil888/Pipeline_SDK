# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LogEntry"]


class LogEntry(BaseModel):
    level: Literal["debug", "info", "warning", "error", "fatal"]

    message: str

    timestamp: datetime

    source: Optional[str] = None
    """Component that generated the log"""
