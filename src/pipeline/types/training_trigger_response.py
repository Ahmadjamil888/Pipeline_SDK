# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["TrainingTriggerResponse"]


class TrainingTriggerResponse(BaseModel):
    id: Optional[str] = None

    compute_provider: Optional[str] = None

    logs_url: Optional[str] = None

    status: Optional[str] = None
