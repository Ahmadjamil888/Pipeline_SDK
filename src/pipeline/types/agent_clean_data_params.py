# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

__all__ = ["AgentCleanDataParams"]


class AgentCleanDataParams(TypedDict, total=False):
    dataset_path: str

    preview_rows: Iterable[object]

    schema: object
