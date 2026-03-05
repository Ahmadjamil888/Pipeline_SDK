# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AgentSummarizeExperimentParams"]


class AgentSummarizeExperimentParams(TypedDict, total=False):
    experiment_metadata: object

    logs_summary: str

    metrics: object
