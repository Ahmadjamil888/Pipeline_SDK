# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["GitHubInitiateOAuthResponse"]


class GitHubInitiateOAuthResponse(BaseModel):
    auth_url: Optional[str] = None
