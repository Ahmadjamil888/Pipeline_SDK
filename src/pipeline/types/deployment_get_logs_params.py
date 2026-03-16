# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DeploymentGetLogsParams"]


class DeploymentGetLogsParams(TypedDict, total=False):
    since: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Return logs since this timestamp (ISO 8601)"""

    tail: int
    """Number of log lines to return from the end"""
