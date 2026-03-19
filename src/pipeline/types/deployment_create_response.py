# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DeploymentCreateResponse"]


class DeploymentCreateResponse(BaseModel):
    deployment_id: str

    message: str

    status: Literal["started", "analyzing", "deploying", "success", "failed"]
