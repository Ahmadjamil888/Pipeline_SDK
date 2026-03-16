# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BillingRetrieveSubscriptionStatusResponse", "Usage"]


class Usage(BaseModel):
    bandwidth: Optional[int] = None

    deployments: Optional[int] = None

    sandboxes: Optional[int] = None


class BillingRetrieveSubscriptionStatusResponse(BaseModel):
    plan: Literal["free", "starter", "pro", "team"]

    status: Literal["active", "canceled", "past_due", "unpaid"]

    user_id: str

    id: Optional[str] = None

    cancel_at_period_end: Optional[bool] = None

    current_period_end: Optional[datetime] = None

    current_period_start: Optional[datetime] = None

    stripe_customer_id: Optional[str] = None

    stripe_subscription_id: Optional[str] = None

    usage: Optional[Usage] = None
