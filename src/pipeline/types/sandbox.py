# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .sandbox_resources import SandboxResources

__all__ = ["Sandbox"]


class Sandbox(BaseModel):
    id: str

    created_at: datetime

    status: Literal["creating", "running", "stopped", "error", "destroyed"]

    branch: Optional[str] = None

    destroyed_at: Optional[datetime] = None

    environment_variables: Optional[Dict[str, str]] = None

    repo_id: Optional[str] = None

    repo_url: Optional[str] = None

    resources: Optional[SandboxResources] = None

    started_at: Optional[datetime] = None

    stopped_at: Optional[datetime] = None

    workspace_url: Optional[str] = None
