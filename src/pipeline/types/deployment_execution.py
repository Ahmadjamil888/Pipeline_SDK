# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["DeploymentExecution"]


class DeploymentExecution(BaseModel):
    deployment_id: str

    message: str

    status: str

    estimated_duration_seconds: Optional[int] = None
