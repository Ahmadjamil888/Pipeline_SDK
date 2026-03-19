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
    from .resources import repos, github, health, billing, webhooks, sandboxes, deployments
    from .resources.repos import ReposResource, AsyncReposResource
    from .resources.github import GitHubResource, AsyncGitHubResource
    from .resources.health import HealthResource, AsyncHealthResource
    from .resources.billing import BillingResource, AsyncBillingResource
    from .resources.webhooks import WebhooksResource, AsyncWebhooksResource
    from .resources.sandboxes import SandboxesResource, AsyncSandboxesResource
    from .resources.deployments import DeploymentsResource, AsyncDeploymentsResource

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
            base_url = f"https://pipeline-ai-labs-by-ahmad.up.railway.app/api/v1"

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
    def webhooks(self) -> WebhooksResource:
        from .resources.webhooks import WebhooksResource

        return WebhooksResource(self)

    @cached_property
    def github(self) -> GitHubResource:
        from .resources.github import GitHubResource

        return GitHubResource(self)

    @cached_property
    def repos(self) -> ReposResource:
        from .resources.repos import ReposResource

        return ReposResource(self)

    @cached_property
    def deployments(self) -> DeploymentsResource:
        from .resources.deployments import DeploymentsResource

        return DeploymentsResource(self)

    @cached_property
    def sandboxes(self) -> SandboxesResource:
        from .resources.sandboxes import SandboxesResource

        return SandboxesResource(self)

    @cached_property
    def health(self) -> HealthResource:
        from .resources.health import HealthResource

        return HealthResource(self)

    @cached_property
    def billing(self) -> BillingResource:
        from .resources.billing import BillingResource

        return BillingResource(self)

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
            **(self._bearer_auth if security.get("bearer_auth", False) else {}),
        }

    @property
    def _bearer_auth(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

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
            base_url = f"https://pipeline-ai-labs-by-ahmad.up.railway.app/api/v1"

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
    def webhooks(self) -> AsyncWebhooksResource:
        from .resources.webhooks import AsyncWebhooksResource

        return AsyncWebhooksResource(self)

    @cached_property
    def github(self) -> AsyncGitHubResource:
        from .resources.github import AsyncGitHubResource

        return AsyncGitHubResource(self)

    @cached_property
    def repos(self) -> AsyncReposResource:
        from .resources.repos import AsyncReposResource

        return AsyncReposResource(self)

    @cached_property
    def deployments(self) -> AsyncDeploymentsResource:
        from .resources.deployments import AsyncDeploymentsResource

        return AsyncDeploymentsResource(self)

    @cached_property
    def sandboxes(self) -> AsyncSandboxesResource:
        from .resources.sandboxes import AsyncSandboxesResource

        return AsyncSandboxesResource(self)

    @cached_property
    def health(self) -> AsyncHealthResource:
        from .resources.health import AsyncHealthResource

        return AsyncHealthResource(self)

    @cached_property
    def billing(self) -> AsyncBillingResource:
        from .resources.billing import AsyncBillingResource

        return AsyncBillingResource(self)

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
            **(self._bearer_auth if security.get("bearer_auth", False) else {}),
        }

    @property
    def _bearer_auth(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

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
    def webhooks(self) -> webhooks.WebhooksResourceWithRawResponse:
        from .resources.webhooks import WebhooksResourceWithRawResponse

        return WebhooksResourceWithRawResponse(self._client.webhooks)

    @cached_property
    def github(self) -> github.GitHubResourceWithRawResponse:
        from .resources.github import GitHubResourceWithRawResponse

        return GitHubResourceWithRawResponse(self._client.github)

    @cached_property
    def repos(self) -> repos.ReposResourceWithRawResponse:
        from .resources.repos import ReposResourceWithRawResponse

        return ReposResourceWithRawResponse(self._client.repos)

    @cached_property
    def deployments(self) -> deployments.DeploymentsResourceWithRawResponse:
        from .resources.deployments import DeploymentsResourceWithRawResponse

        return DeploymentsResourceWithRawResponse(self._client.deployments)

    @cached_property
    def sandboxes(self) -> sandboxes.SandboxesResourceWithRawResponse:
        from .resources.sandboxes import SandboxesResourceWithRawResponse

        return SandboxesResourceWithRawResponse(self._client.sandboxes)

    @cached_property
    def health(self) -> health.HealthResourceWithRawResponse:
        from .resources.health import HealthResourceWithRawResponse

        return HealthResourceWithRawResponse(self._client.health)

    @cached_property
    def billing(self) -> billing.BillingResourceWithRawResponse:
        from .resources.billing import BillingResourceWithRawResponse

        return BillingResourceWithRawResponse(self._client.billing)


class AsyncPipelineWithRawResponse:
    _client: AsyncPipeline

    def __init__(self, client: AsyncPipeline) -> None:
        self._client = client

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithRawResponse:
        from .resources.webhooks import AsyncWebhooksResourceWithRawResponse

        return AsyncWebhooksResourceWithRawResponse(self._client.webhooks)

    @cached_property
    def github(self) -> github.AsyncGitHubResourceWithRawResponse:
        from .resources.github import AsyncGitHubResourceWithRawResponse

        return AsyncGitHubResourceWithRawResponse(self._client.github)

    @cached_property
    def repos(self) -> repos.AsyncReposResourceWithRawResponse:
        from .resources.repos import AsyncReposResourceWithRawResponse

        return AsyncReposResourceWithRawResponse(self._client.repos)

    @cached_property
    def deployments(self) -> deployments.AsyncDeploymentsResourceWithRawResponse:
        from .resources.deployments import AsyncDeploymentsResourceWithRawResponse

        return AsyncDeploymentsResourceWithRawResponse(self._client.deployments)

    @cached_property
    def sandboxes(self) -> sandboxes.AsyncSandboxesResourceWithRawResponse:
        from .resources.sandboxes import AsyncSandboxesResourceWithRawResponse

        return AsyncSandboxesResourceWithRawResponse(self._client.sandboxes)

    @cached_property
    def health(self) -> health.AsyncHealthResourceWithRawResponse:
        from .resources.health import AsyncHealthResourceWithRawResponse

        return AsyncHealthResourceWithRawResponse(self._client.health)

    @cached_property
    def billing(self) -> billing.AsyncBillingResourceWithRawResponse:
        from .resources.billing import AsyncBillingResourceWithRawResponse

        return AsyncBillingResourceWithRawResponse(self._client.billing)


class PipelineWithStreamedResponse:
    _client: Pipeline

    def __init__(self, client: Pipeline) -> None:
        self._client = client

    @cached_property
    def webhooks(self) -> webhooks.WebhooksResourceWithStreamingResponse:
        from .resources.webhooks import WebhooksResourceWithStreamingResponse

        return WebhooksResourceWithStreamingResponse(self._client.webhooks)

    @cached_property
    def github(self) -> github.GitHubResourceWithStreamingResponse:
        from .resources.github import GitHubResourceWithStreamingResponse

        return GitHubResourceWithStreamingResponse(self._client.github)

    @cached_property
    def repos(self) -> repos.ReposResourceWithStreamingResponse:
        from .resources.repos import ReposResourceWithStreamingResponse

        return ReposResourceWithStreamingResponse(self._client.repos)

    @cached_property
    def deployments(self) -> deployments.DeploymentsResourceWithStreamingResponse:
        from .resources.deployments import DeploymentsResourceWithStreamingResponse

        return DeploymentsResourceWithStreamingResponse(self._client.deployments)

    @cached_property
    def sandboxes(self) -> sandboxes.SandboxesResourceWithStreamingResponse:
        from .resources.sandboxes import SandboxesResourceWithStreamingResponse

        return SandboxesResourceWithStreamingResponse(self._client.sandboxes)

    @cached_property
    def health(self) -> health.HealthResourceWithStreamingResponse:
        from .resources.health import HealthResourceWithStreamingResponse

        return HealthResourceWithStreamingResponse(self._client.health)

    @cached_property
    def billing(self) -> billing.BillingResourceWithStreamingResponse:
        from .resources.billing import BillingResourceWithStreamingResponse

        return BillingResourceWithStreamingResponse(self._client.billing)


class AsyncPipelineWithStreamedResponse:
    _client: AsyncPipeline

    def __init__(self, client: AsyncPipeline) -> None:
        self._client = client

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithStreamingResponse:
        from .resources.webhooks import AsyncWebhooksResourceWithStreamingResponse

        return AsyncWebhooksResourceWithStreamingResponse(self._client.webhooks)

    @cached_property
    def github(self) -> github.AsyncGitHubResourceWithStreamingResponse:
        from .resources.github import AsyncGitHubResourceWithStreamingResponse

        return AsyncGitHubResourceWithStreamingResponse(self._client.github)

    @cached_property
    def repos(self) -> repos.AsyncReposResourceWithStreamingResponse:
        from .resources.repos import AsyncReposResourceWithStreamingResponse

        return AsyncReposResourceWithStreamingResponse(self._client.repos)

    @cached_property
    def deployments(self) -> deployments.AsyncDeploymentsResourceWithStreamingResponse:
        from .resources.deployments import AsyncDeploymentsResourceWithStreamingResponse

        return AsyncDeploymentsResourceWithStreamingResponse(self._client.deployments)

    @cached_property
    def sandboxes(self) -> sandboxes.AsyncSandboxesResourceWithStreamingResponse:
        from .resources.sandboxes import AsyncSandboxesResourceWithStreamingResponse

        return AsyncSandboxesResourceWithStreamingResponse(self._client.sandboxes)

    @cached_property
    def health(self) -> health.AsyncHealthResourceWithStreamingResponse:
        from .resources.health import AsyncHealthResourceWithStreamingResponse

        return AsyncHealthResourceWithStreamingResponse(self._client.health)

    @cached_property
    def billing(self) -> billing.AsyncBillingResourceWithStreamingResponse:
        from .resources.billing import AsyncBillingResourceWithStreamingResponse

        return AsyncBillingResourceWithStreamingResponse(self._client.billing)


Client = Pipeline

AsyncClient = AsyncPipeline
