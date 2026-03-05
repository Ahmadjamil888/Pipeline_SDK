# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AuthAuthenticateResponse"]


class AuthAuthenticateResponse(BaseModel):
    api_key: Optional[str] = None
