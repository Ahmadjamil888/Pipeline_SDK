from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `pipeline_labs.resources` module.

    This is used so that we can lazily import `pipeline_labs.resources` only when
    needed *and* so that users can just import `pipeline_labs` and reference `pipeline_labs.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("pipeline_labs.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
