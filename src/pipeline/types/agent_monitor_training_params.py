# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AgentMonitorTrainingParams"]


class AgentMonitorTrainingParams(TypedDict, total=False):
    logs: str

    metrics: object

    run_id: str
