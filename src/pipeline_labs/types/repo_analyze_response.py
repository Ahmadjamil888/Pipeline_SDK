# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RepoAnalyzeResponse", "Service"]


class Service(BaseModel):
    framework: Literal[
        "nextjs",
        "react",
        "vue",
        "angular",
        "svelte",
        "nuxtjs",
        "remix",
        "fastapi",
        "flask",
        "django",
        "express",
        "nestjs",
        "go",
        "rust",
        "unknown",
    ]
    """Detected framework"""

    name: str
    """Service name (e.g., frontend, api, backend)"""

    path: str
    """Relative path within the repository"""

    build_command: Optional[str] = None
    """Detected or suggested build command"""

    detected_files: Optional[List[str]] = None
    """Key files that helped identify the service"""

    env_variables: Optional[List[str]] = None
    """Detected environment variable requirements"""

    language: Optional[
        Literal["javascript", "typescript", "python", "go", "rust", "java", "ruby", "php", "unknown"]
    ] = None
    """Primary programming language"""

    recommended_platform: Optional[Literal["vercel", "render", "docker"]] = None
    """Recommended deployment platform"""

    start_command: Optional[str] = None
    """Detected or suggested start command"""


class RepoAnalyzeResponse(BaseModel):
    analyzed_at: datetime

    is_monorepo: bool
    """Whether the repository is a monorepo"""

    repo_id: str

    services: List[Service]

    detected_workspaces: Optional[List[str]] = None
    """Workspace tools detected (e.g., turborepo, nx, pnpm)"""

    root_config: Optional[object] = None
    """Root-level configuration files"""

    sandbox_id: Optional[str] = None
    """ID of the sandbox used for analysis"""
