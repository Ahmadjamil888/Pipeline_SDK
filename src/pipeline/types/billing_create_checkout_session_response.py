# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["BillingCreateCheckoutSessionResponse"]


class BillingCreateCheckoutSessionResponse(BaseModel):
    checkout_url: str

    session_id: str
