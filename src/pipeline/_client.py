# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._models import SecurityOptions
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import PipelineError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import auth, cloud, agents, compute, training
    from .resources.cloud import CloudResource, AsyncCloudResource
    from .resources.agents import AgentsResource, AsyncAgentsResource
    from .resources.compute import ComputeResource, AsyncComputeResource
    from .resources.auth.auth import AuthResource, AsyncAuthResource
    from .resources.training.training import TrainingResource, AsyncTrainingResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Pipeline",
    "AsyncPipeline",
    "Client",
    "AsyncClient",
]


class Pipeline(SyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Pipeline client instance.

        This automatically infers the `api_key` argument from the `PIPELINE_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("PIPELINE_API_KEY")
        if api_key is None:
            raise PipelineError(
                "The api_key client option must be set either by passing api_key to the client or by setting the PIPELINE_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("PIPELINE_BASE_URL")
        if base_url is None:
            base_url = f"http://localhost:8000/api/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def auth(self) -> AuthResource:
        """Auth & Key Management"""
        from .resources.auth import AuthResource

        return AuthResource(self)

    @cached_property
    def agents(self) -> AgentsResource:
        """Agentic AI services (Data Clean, Monitor, Optimize, Summarize)"""
        from .resources.agents import AgentsResource

        return AgentsResource(self)

    @cached_property
    def training(self) -> TrainingResource:
        """BYOC Training Orchestration"""
        from .resources.training import TrainingResource

        return TrainingResource(self)

    @cached_property
    def compute(self) -> ComputeResource:
        """Hardware & Cloud Configuration"""
        from .resources.compute import ComputeResource

        return ComputeResource(self)

    @cached_property
    def cloud(self) -> CloudResource:
        """Hardware & Cloud Configuration"""
        from .resources.cloud import CloudResource

        return CloudResource(self)

    @cached_property
    def with_raw_response(self) -> PipelineWithRawResponse:
        return PipelineWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PipelineWithStreamedResponse:
        return PipelineWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._api_key_auth if security.get("api_key_auth", False) else {}),
        }

    @property
    def _api_key_auth(self) -> dict[str, str]:
        api_key = self.api_key
        return {"X-API-KEY": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncPipeline(AsyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncPipeline client instance.

        This automatically infers the `api_key` argument from the `PIPELINE_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("PIPELINE_API_KEY")
        if api_key is None:
            raise PipelineError(
                "The api_key client option must be set either by passing api_key to the client or by setting the PIPELINE_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("PIPELINE_BASE_URL")
        if base_url is None:
            base_url = f"http://localhost:8000/api/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def auth(self) -> AsyncAuthResource:
        """Auth & Key Management"""
        from .resources.auth import AsyncAuthResource

        return AsyncAuthResource(self)

    @cached_property
    def agents(self) -> AsyncAgentsResource:
        """Agentic AI services (Data Clean, Monitor, Optimize, Summarize)"""
        from .resources.agents import AsyncAgentsResource

        return AsyncAgentsResource(self)

    @cached_property
    def training(self) -> AsyncTrainingResource:
        """BYOC Training Orchestration"""
        from .resources.training import AsyncTrainingResource

        return AsyncTrainingResource(self)

    @cached_property
    def compute(self) -> AsyncComputeResource:
        """Hardware & Cloud Configuration"""
        from .resources.compute import AsyncComputeResource

        return AsyncComputeResource(self)

    @cached_property
    def cloud(self) -> AsyncCloudResource:
        """Hardware & Cloud Configuration"""
        from .resources.cloud import AsyncCloudResource

        return AsyncCloudResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncPipelineWithRawResponse:
        return AsyncPipelineWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPipelineWithStreamedResponse:
        return AsyncPipelineWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._api_key_auth if security.get("api_key_auth", False) else {}),
        }

    @property
    def _api_key_auth(self) -> dict[str, str]:
        api_key = self.api_key
        return {"X-API-KEY": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class PipelineWithRawResponse:
    _client: Pipeline

    def __init__(self, client: Pipeline) -> None:
        self._client = client

    @cached_property
    def auth(self) -> auth.AuthResourceWithRawResponse:
        """Auth & Key Management"""
        from .resources.auth import AuthResourceWithRawResponse

        return AuthResourceWithRawResponse(self._client.auth)

    @cached_property
    def agents(self) -> agents.AgentsResourceWithRawResponse:
        """Agentic AI services (Data Clean, Monitor, Optimize, Summarize)"""
        from .resources.agents import AgentsResourceWithRawResponse

        return AgentsResourceWithRawResponse(self._client.agents)

    @cached_property
    def training(self) -> training.TrainingResourceWithRawResponse:
        """BYOC Training Orchestration"""
        from .resources.training import TrainingResourceWithRawResponse

        return TrainingResourceWithRawResponse(self._client.training)

    @cached_property
    def compute(self) -> compute.ComputeResourceWithRawResponse:
        """Hardware & Cloud Configuration"""
        from .resources.compute import ComputeResourceWithRawResponse

        return ComputeResourceWithRawResponse(self._client.compute)

    @cached_property
    def cloud(self) -> cloud.CloudResourceWithRawResponse:
        """Hardware & Cloud Configuration"""
        from .resources.cloud import CloudResourceWithRawResponse

        return CloudResourceWithRawResponse(self._client.cloud)


class AsyncPipelineWithRawResponse:
    _client: AsyncPipeline

    def __init__(self, client: AsyncPipeline) -> None:
        self._client = client

    @cached_property
    def auth(self) -> auth.AsyncAuthResourceWithRawResponse:
        """Auth & Key Management"""
        from .resources.auth import AsyncAuthResourceWithRawResponse

        return AsyncAuthResourceWithRawResponse(self._client.auth)

    @cached_property
    def agents(self) -> agents.AsyncAgentsResourceWithRawResponse:
        """Agentic AI services (Data Clean, Monitor, Optimize, Summarize)"""
        from .resources.agents import AsyncAgentsResourceWithRawResponse

        return AsyncAgentsResourceWithRawResponse(self._client.agents)

    @cached_property
    def training(self) -> training.AsyncTrainingResourceWithRawResponse:
        """BYOC Training Orchestration"""
        from .resources.training import AsyncTrainingResourceWithRawResponse

        return AsyncTrainingResourceWithRawResponse(self._client.training)

    @cached_property
    def compute(self) -> compute.AsyncComputeResourceWithRawResponse:
        """Hardware & Cloud Configuration"""
        from .resources.compute import AsyncComputeResourceWithRawResponse

        return AsyncComputeResourceWithRawResponse(self._client.compute)

    @cached_property
    def cloud(self) -> cloud.AsyncCloudResourceWithRawResponse:
        """Hardware & Cloud Configuration"""
        from .resources.cloud import AsyncCloudResourceWithRawResponse

        return AsyncCloudResourceWithRawResponse(self._client.cloud)


class PipelineWithStreamedResponse:
    _client: Pipeline

    def __init__(self, client: Pipeline) -> None:
        self._client = client

    @cached_property
    def auth(self) -> auth.AuthResourceWithStreamingResponse:
        """Auth & Key Management"""
        from .resources.auth import AuthResourceWithStreamingResponse

        return AuthResourceWithStreamingResponse(self._client.auth)

    @cached_property
    def agents(self) -> agents.AgentsResourceWithStreamingResponse:
        """Agentic AI services (Data Clean, Monitor, Optimize, Summarize)"""
        from .resources.agents import AgentsResourceWithStreamingResponse

        return AgentsResourceWithStreamingResponse(self._client.agents)

    @cached_property
    def training(self) -> training.TrainingResourceWithStreamingResponse:
        """BYOC Training Orchestration"""
        from .resources.training import TrainingResourceWithStreamingResponse

        return TrainingResourceWithStreamingResponse(self._client.training)

    @cached_property
    def compute(self) -> compute.ComputeResourceWithStreamingResponse:
        """Hardware & Cloud Configuration"""
        from .resources.compute import ComputeResourceWithStreamingResponse

        return ComputeResourceWithStreamingResponse(self._client.compute)

    @cached_property
    def cloud(self) -> cloud.CloudResourceWithStreamingResponse:
        """Hardware & Cloud Configuration"""
        from .resources.cloud import CloudResourceWithStreamingResponse

        return CloudResourceWithStreamingResponse(self._client.cloud)


class AsyncPipelineWithStreamedResponse:
    _client: AsyncPipeline

    def __init__(self, client: AsyncPipeline) -> None:
        self._client = client

    @cached_property
    def auth(self) -> auth.AsyncAuthResourceWithStreamingResponse:
        """Auth & Key Management"""
        from .resources.auth import AsyncAuthResourceWithStreamingResponse

        return AsyncAuthResourceWithStreamingResponse(self._client.auth)

    @cached_property
    def agents(self) -> agents.AsyncAgentsResourceWithStreamingResponse:
        """Agentic AI services (Data Clean, Monitor, Optimize, Summarize)"""
        from .resources.agents import AsyncAgentsResourceWithStreamingResponse

        return AsyncAgentsResourceWithStreamingResponse(self._client.agents)

    @cached_property
    def training(self) -> training.AsyncTrainingResourceWithStreamingResponse:
        """BYOC Training Orchestration"""
        from .resources.training import AsyncTrainingResourceWithStreamingResponse

        return AsyncTrainingResourceWithStreamingResponse(self._client.training)

    @cached_property
    def compute(self) -> compute.AsyncComputeResourceWithStreamingResponse:
        """Hardware & Cloud Configuration"""
        from .resources.compute import AsyncComputeResourceWithStreamingResponse

        return AsyncComputeResourceWithStreamingResponse(self._client.compute)

    @cached_property
    def cloud(self) -> cloud.AsyncCloudResourceWithStreamingResponse:
        """Hardware & Cloud Configuration"""
        from .resources.cloud import AsyncCloudResourceWithStreamingResponse

        return AsyncCloudResourceWithStreamingResponse(self._client.cloud)


Client = Pipeline

AsyncClient = AsyncPipeline
