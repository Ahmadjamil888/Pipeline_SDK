# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TrainingStartResponse"]


class TrainingStartResponse(BaseModel):
    id: Optional[str] = None

    status: Optional[Literal["PENDING", "PROVISIONING", "RUNNING", "COMPLETED", "FAILED"]] = None
