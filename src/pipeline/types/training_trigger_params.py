# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TrainingTriggerParams"]


class TrainingTriggerParams(TypedDict, total=False):
    compute: Literal["auto", "local", "aws"]

    config: object

    name: str
