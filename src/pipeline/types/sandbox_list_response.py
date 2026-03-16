# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .sandbox import Sandbox
from .._models import BaseModel

__all__ = ["SandboxListResponse"]


class SandboxListResponse(BaseModel):
    sandboxes: List[Sandbox]

    total: int
