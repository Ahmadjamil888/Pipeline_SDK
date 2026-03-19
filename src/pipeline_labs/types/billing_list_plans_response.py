# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BillingListPlansResponse", "Plan"]


class Plan(BaseModel):
    id: Literal["free", "pro", "team"]

    features: List[str]

    name: str

    price: int

    deployments_limit: Optional[int] = None

    price_id: Optional[str] = None

    priority: Optional[Literal["normal", "high", "priority"]] = None

    projects_limit: Optional[int] = None


class BillingListPlansResponse(BaseModel):
    plans: List[Plan]
