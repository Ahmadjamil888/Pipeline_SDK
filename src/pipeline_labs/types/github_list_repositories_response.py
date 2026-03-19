# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["GitHubListRepositoriesResponse", "Repository"]


class Repository(BaseModel):
    id: Optional[int] = None

    clone_url: Optional[str] = None

    default_branch: Optional[str] = None

    description: Optional[str] = None

    forks_count: Optional[int] = None

    full_name: Optional[str] = None

    html_url: Optional[str] = None

    language: Optional[str] = None

    name: Optional[str] = None

    private: Optional[bool] = None

    stargazers_count: Optional[int] = None

    updated_at: Optional[str] = None


class GitHubListRepositoriesResponse(BaseModel):
    repositories: Optional[List[Repository]] = None
