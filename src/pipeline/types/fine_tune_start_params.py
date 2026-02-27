# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FineTuneStartParams", "Config"]


class FineTuneStartParams(TypedDict, total=False):
    base_model: Required[str]

    dataset_id: Required[str]

    config: Config


class Config(TypedDict, total=False):
    gpu: str
