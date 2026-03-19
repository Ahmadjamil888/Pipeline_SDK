# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["GitHubInitiateInstallationResponse"]


class GitHubInitiateInstallationResponse(BaseModel):
    url: Optional[str] = None
    """GitHub App installation URL"""
