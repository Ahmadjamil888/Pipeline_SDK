# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["SandboxOpenTerminalResponse"]


class SandboxOpenTerminalResponse(BaseModel):
    created_at: datetime

    sandbox_id: str

    session_id: str

    websocket_url: str

    expires_at: Optional[datetime] = None

    shell: Optional[str] = None

    working_directory: Optional[str] = None
