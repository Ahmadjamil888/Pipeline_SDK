# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["SandboxExecuteResponse"]


class SandboxExecuteResponse(BaseModel):
    duration_ms: int

    exit_code: int

    stderr: str

    stdout: str

    executed_at: Optional[datetime] = None
