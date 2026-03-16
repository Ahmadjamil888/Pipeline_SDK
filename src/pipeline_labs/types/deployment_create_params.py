# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["DeploymentCreateParams", "Service", "ServiceRenderConfig", "ServiceVercelConfig"]


class DeploymentCreateParams(TypedDict, total=False):
    repo_id: Required[str]

    services: Required[Iterable[Service]]

    branch: str
    """Branch to deploy from"""

    env_variables: Dict[str, str]
    """Environment variables for all services"""

    environment: Literal["development", "staging", "production"]


class ServiceRenderConfig(TypedDict, total=False):
    plan: str

    service_name: str

    service_type: Literal["web_service", "static_site", "background_worker", "cron_job"]


class ServiceVercelConfig(TypedDict, total=False):
    framework: str

    project_name: str
    """Vercel project name"""

    team_id: str


class Service(TypedDict, total=False):
    name: Required[str]

    path: Required[str]

    platform: Required[Literal["vercel", "render", "docker"]]

    build_command: str

    env_variables: Dict[str, str]

    output_directory: str

    render_config: ServiceRenderConfig

    start_command: str

    vercel_config: ServiceVercelConfig
