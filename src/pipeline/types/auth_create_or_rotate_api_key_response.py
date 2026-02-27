# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AuthCreateOrRotateAPIKeyResponse"]


class AuthCreateOrRotateAPIKeyResponse(BaseModel):
    key_value: Optional[str] = None
