# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["BillingCreateCheckoutSessionParams"]


class BillingCreateCheckoutSessionParams(TypedDict, total=False):
    cancel_url: Required[str]

    plan_id: Required[Literal["starter", "pro", "team"]]

    success_url: Required[str]

    user_id: Required[str]
