# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .._models import BaseModel
from .log_entry import LogEntry

__all__ = ["DeploymentGetLogsResponse"]


class DeploymentGetLogsResponse(BaseModel):
    deployment_id: str

    logs: List[LogEntry]

    timestamp: datetime
