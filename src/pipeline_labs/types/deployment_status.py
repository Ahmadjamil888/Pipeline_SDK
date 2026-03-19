# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DeploymentStatus"]


class DeploymentStatus(BaseModel):
    id: str

    created_at: datetime

    status: Literal[
        "started",
        "analyzing",
        "cloning",
        "ai_analyzing",
        "analyzed",
        "deploying_backend",
        "deploying_frontend",
        "success",
        "failed",
    ]

    analysis: Optional[object] = None

    backend_url: Optional[str] = None

    error: Optional[str] = None

    frontend_url: Optional[str] = None

    updated_at: Optional[datetime] = None
