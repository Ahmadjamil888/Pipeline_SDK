# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .deployment_status import DeploymentStatus

__all__ = ["DeploymentListResponse"]


class DeploymentListResponse(BaseModel):
    deployments: List[DeploymentStatus]

    limit: int

    offset: int

    total: int
