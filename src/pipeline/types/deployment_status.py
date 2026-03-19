# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DeploymentStatus", "Service"]


class Service(BaseModel):
    name: str

    path: str

    platform: Literal["vercel", "render", "docker"]

    status: Literal["pending", "building", "deploying", "deployed", "failed", "skipped"]

    build_logs_url: Optional[str] = None

    completed_at: Optional[datetime] = None

    deployment_url: Optional[str] = None

    error_message: Optional[str] = None

    platform_deployment_id: Optional[str] = None

    started_at: Optional[datetime] = None


class DeploymentStatus(BaseModel):
    id: str

    created_at: datetime

    status: Literal["pending", "running", "succeeded", "failed", "cancelled", "retrying"]

    branch: Optional[str] = None

    completed_at: Optional[datetime] = None

    duration_seconds: Optional[int] = None

    environment: Optional[str] = None

    error_message: Optional[str] = None

    retry_count: Optional[int] = None

    services: Optional[List[Service]] = None

    started_at: Optional[datetime] = None
