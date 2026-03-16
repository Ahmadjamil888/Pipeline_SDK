# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .log_entry import LogEntry

__all__ = ["SandboxGetLogsResponse"]


class SandboxGetLogsResponse(BaseModel):
    logs: List[LogEntry]

    sandbox_id: str
