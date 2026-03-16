# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BillingListPlansResponse", "Plan"]


class Plan(BaseModel):
    id: Literal["starter", "pro", "team"]

    features: List[str]

    name: str

    price: int
    """Monthly price in USD"""

    deployments_limit: Optional[int] = None

    price_id: Optional[str] = None
    """Stripe price ID (null for free plan)"""

    priority: Optional[Literal["normal", "high", "priority"]] = None

    projects_limit: Optional[int] = None
    """-1 for unlimited"""


class BillingListPlansResponse(BaseModel):
    plans: List[Plan]
