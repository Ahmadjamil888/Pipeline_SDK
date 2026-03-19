# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["HealthCheckResponse"]


class HealthCheckResponse(BaseModel):
    status: Literal["healthy", "unhealthy", "degraded"]

    timestamp: datetime

    version: str

    services: Optional[Dict[str, Literal["healthy", "unhealthy"]]] = None
