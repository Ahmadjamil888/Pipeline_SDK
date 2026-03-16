# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DeploymentCreateResponse", "Service"]


class Service(BaseModel):
    name: str

    path: str

    platform: Literal["vercel", "render", "docker"]

    estimated_duration_seconds: Optional[int] = None
    """Estimated deployment duration"""

    status: Optional[Literal["pending", "deploying", "deployed", "failed", "skipped"]] = None


class DeploymentCreateResponse(BaseModel):
    id: str

    created_at: datetime

    repo_id: str

    services: List[Service]

    status: Literal["pending", "planned", "approved"]

    branch: Optional[str] = None

    environment: Optional[str] = None
