# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["WebhookHandleGitHubParams", "Installation", "InstallationAccount", "Repository", "Sender"]


class WebhookHandleGitHubParams(TypedDict, total=False):
    action: Literal["created", "deleted", "push", "pull_request", "installation", "installation_repositories"]

    installation: Installation

    repository: Repository

    sender: Sender


class InstallationAccount(TypedDict, total=False):
    id: int

    login: str


class Installation(TypedDict, total=False):
    id: int

    account: InstallationAccount


class Repository(TypedDict, total=False):
    id: int

    clone_url: str

    default_branch: str

    full_name: str

    name: str


class Sender(TypedDict, total=False):
    id: int

    login: str
