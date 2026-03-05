# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AgentCleanDataResponse"]


class AgentCleanDataResponse(BaseModel):
    cleaning_steps: Optional[List[str]] = None

    issues_detected: Optional[List[str]] = None

    recommended_script: Optional[str] = None

    risk_level: Optional[Literal["low", "medium", "high"]] = None
