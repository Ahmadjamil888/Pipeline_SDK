# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["SandboxResources"]


class SandboxResources(BaseModel):
    cpu_cores: Optional[int] = None

    disk_gb: Optional[int] = None

    memory_mb: Optional[int] = None
