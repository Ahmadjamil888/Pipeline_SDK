# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TrainingStartParams", "Config"]


class TrainingStartParams(TypedDict, total=False):
    config: Required[Config]

    name: Required[str]


class Config(TypedDict, total=False):
    distributed: bool

    gpu: str
    """Set to GPU for high-perf training (Pro/Enterprise only)"""

    workers: int
