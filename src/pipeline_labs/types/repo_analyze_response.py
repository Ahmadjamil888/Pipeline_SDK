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

    name: str

    path: str

    build_command: Optional[str] = None

    detected_files: Optional[List[str]] = None

    env_variables: Optional[List[str]] = None

    language: Optional[
        Literal["javascript", "typescript", "python", "go", "rust", "java", "ruby", "php", "unknown"]
    ] = None

    recommended_platform: Optional[Literal["vercel", "render", "docker"]] = None

    start_command: Optional[str] = None


class RepoAnalyzeResponse(BaseModel):
    analyzed_at: datetime

    is_monorepo: bool

    repo_id: str

    services: List[Service]

    detected_workspaces: Optional[List[str]] = None

    root_config: Optional[object] = None

    sandbox_id: Optional[str] = None
