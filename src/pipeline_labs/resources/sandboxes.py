# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal

import httpx

from ..types import (
    sandbox_list_params,
    sandbox_create_params,
    sandbox_execute_params,
    sandbox_get_logs_params,
    sandbox_open_terminal_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.sandbox import Sandbox
from ..types.sandbox_list_response import SandboxListResponse
from ..types.sandbox_stop_response import SandboxStopResponse
from ..types.sandbox_start_response import SandboxStartResponse
from ..types.sandbox_resources_param import SandboxResourcesParam
from ..types.sandbox_execute_response import SandboxExecuteResponse
from ..types.sandbox_get_logs_response import SandboxGetLogsResponse
from ..types.sandbox_open_terminal_response import SandboxOpenTerminalResponse

__all__ = ["SandboxesResource", "AsyncSandboxesResource"]


class SandboxesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SandboxesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/pipeline-python#accessing-raw-response-data-eg-headers
        """
        return SandboxesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SandboxesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/pipeline-python#with_streaming_response
        """
        return SandboxesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        branch: str | Omit = omit,
        environment_variables: Dict[str, str] | Omit = omit,
        repo_id: str | Omit = omit,
        repo_url: str | Omit = omit,
        resources: SandboxResourcesParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Sandbox:
        """
        Create a new Daytona workspace for isolated execution

        Args:
          repo_id: Optional repo to pre-clone

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/sandboxes",
            body=maybe_transform(
                {
                    "branch": branch,
                    "environment_variables": environment_variables,
                    "repo_id": repo_id,
                    "repo_url": repo_url,
                    "resources": resources,
                },
                sandbox_create_params.SandboxCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Sandbox,
        )

    def retrieve(
        self,
        sandbox_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Sandbox:
        """
        Get sandbox details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sandbox_id:
            raise ValueError(f"Expected a non-empty value for `sandbox_id` but received {sandbox_id!r}")
        return self._get(
            f"/sandboxes/{sandbox_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Sandbox,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        status: Literal["creating", "running", "stopped", "error", "destroyed"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxListResponse:
        """
        List all sandboxes

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/sandboxes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "status": status,
                    },
                    sandbox_list_params.SandboxListParams,
                ),
            ),
            cast_to=SandboxListResponse,
        )

    def delete(
        self,
        sandbox_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Destroy the Daytona workspace and free resources

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sandbox_id:
            raise ValueError(f"Expected a non-empty value for `sandbox_id` but received {sandbox_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/sandboxes/{sandbox_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def execute(
        self,
        sandbox_id: str,
        *,
        command: str,
        env_variables: Dict[str, str] | Omit = omit,
        timeout_seconds: int | Omit = omit,
        working_directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxExecuteResponse:
        """
        Run a command inside the Daytona workspace

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sandbox_id:
            raise ValueError(f"Expected a non-empty value for `sandbox_id` but received {sandbox_id!r}")
        return self._post(
            f"/sandboxes/{sandbox_id}/execute",
            body=maybe_transform(
                {
                    "command": command,
                    "env_variables": env_variables,
                    "timeout_seconds": timeout_seconds,
                    "working_directory": working_directory,
                },
                sandbox_execute_params.SandboxExecuteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxExecuteResponse,
        )

    def get_logs(
        self,
        sandbox_id: str,
        *,
        tail: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxGetLogsResponse:
        """
        Retrieve execution logs from the sandbox

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sandbox_id:
            raise ValueError(f"Expected a non-empty value for `sandbox_id` but received {sandbox_id!r}")
        return self._get(
            f"/sandboxes/{sandbox_id}/logs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"tail": tail}, sandbox_get_logs_params.SandboxGetLogsParams),
            ),
            cast_to=SandboxGetLogsResponse,
        )

    def open_terminal(
        self,
        sandbox_id: str,
        *,
        environment_variables: Dict[str, str] | Omit = omit,
        shell: str | Omit = omit,
        working_directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxOpenTerminalResponse:
        """
        Open an interactive terminal session inside the sandbox

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sandbox_id:
            raise ValueError(f"Expected a non-empty value for `sandbox_id` but received {sandbox_id!r}")
        return self._post(
            f"/sandboxes/{sandbox_id}/terminal",
            body=maybe_transform(
                {
                    "environment_variables": environment_variables,
                    "shell": shell,
                    "working_directory": working_directory,
                },
                sandbox_open_terminal_params.SandboxOpenTerminalParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxOpenTerminalResponse,
        )

    def start(
        self,
        sandbox_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxStartResponse:
        """
        Start sandbox

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sandbox_id:
            raise ValueError(f"Expected a non-empty value for `sandbox_id` but received {sandbox_id!r}")
        return self._post(
            f"/sandboxes/{sandbox_id}/start",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxStartResponse,
        )

    def stop(
        self,
        sandbox_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxStopResponse:
        """
        Stop sandbox

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sandbox_id:
            raise ValueError(f"Expected a non-empty value for `sandbox_id` but received {sandbox_id!r}")
        return self._post(
            f"/sandboxes/{sandbox_id}/stop",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxStopResponse,
        )


class AsyncSandboxesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSandboxesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/pipeline-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSandboxesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSandboxesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/pipeline-python#with_streaming_response
        """
        return AsyncSandboxesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        branch: str | Omit = omit,
        environment_variables: Dict[str, str] | Omit = omit,
        repo_id: str | Omit = omit,
        repo_url: str | Omit = omit,
        resources: SandboxResourcesParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Sandbox:
        """
        Create a new Daytona workspace for isolated execution

        Args:
          repo_id: Optional repo to pre-clone

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/sandboxes",
            body=await async_maybe_transform(
                {
                    "branch": branch,
                    "environment_variables": environment_variables,
                    "repo_id": repo_id,
                    "repo_url": repo_url,
                    "resources": resources,
                },
                sandbox_create_params.SandboxCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Sandbox,
        )

    async def retrieve(
        self,
        sandbox_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Sandbox:
        """
        Get sandbox details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sandbox_id:
            raise ValueError(f"Expected a non-empty value for `sandbox_id` but received {sandbox_id!r}")
        return await self._get(
            f"/sandboxes/{sandbox_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Sandbox,
        )

    async def list(
        self,
        *,
        limit: int | Omit = omit,
        status: Literal["creating", "running", "stopped", "error", "destroyed"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxListResponse:
        """
        List all sandboxes

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/sandboxes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "status": status,
                    },
                    sandbox_list_params.SandboxListParams,
                ),
            ),
            cast_to=SandboxListResponse,
        )

    async def delete(
        self,
        sandbox_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Destroy the Daytona workspace and free resources

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sandbox_id:
            raise ValueError(f"Expected a non-empty value for `sandbox_id` but received {sandbox_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/sandboxes/{sandbox_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def execute(
        self,
        sandbox_id: str,
        *,
        command: str,
        env_variables: Dict[str, str] | Omit = omit,
        timeout_seconds: int | Omit = omit,
        working_directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxExecuteResponse:
        """
        Run a command inside the Daytona workspace

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sandbox_id:
            raise ValueError(f"Expected a non-empty value for `sandbox_id` but received {sandbox_id!r}")
        return await self._post(
            f"/sandboxes/{sandbox_id}/execute",
            body=await async_maybe_transform(
                {
                    "command": command,
                    "env_variables": env_variables,
                    "timeout_seconds": timeout_seconds,
                    "working_directory": working_directory,
                },
                sandbox_execute_params.SandboxExecuteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxExecuteResponse,
        )

    async def get_logs(
        self,
        sandbox_id: str,
        *,
        tail: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxGetLogsResponse:
        """
        Retrieve execution logs from the sandbox

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sandbox_id:
            raise ValueError(f"Expected a non-empty value for `sandbox_id` but received {sandbox_id!r}")
        return await self._get(
            f"/sandboxes/{sandbox_id}/logs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"tail": tail}, sandbox_get_logs_params.SandboxGetLogsParams),
            ),
            cast_to=SandboxGetLogsResponse,
        )

    async def open_terminal(
        self,
        sandbox_id: str,
        *,
        environment_variables: Dict[str, str] | Omit = omit,
        shell: str | Omit = omit,
        working_directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxOpenTerminalResponse:
        """
        Open an interactive terminal session inside the sandbox

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sandbox_id:
            raise ValueError(f"Expected a non-empty value for `sandbox_id` but received {sandbox_id!r}")
        return await self._post(
            f"/sandboxes/{sandbox_id}/terminal",
            body=await async_maybe_transform(
                {
                    "environment_variables": environment_variables,
                    "shell": shell,
                    "working_directory": working_directory,
                },
                sandbox_open_terminal_params.SandboxOpenTerminalParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxOpenTerminalResponse,
        )

    async def start(
        self,
        sandbox_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxStartResponse:
        """
        Start sandbox

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sandbox_id:
            raise ValueError(f"Expected a non-empty value for `sandbox_id` but received {sandbox_id!r}")
        return await self._post(
            f"/sandboxes/{sandbox_id}/start",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxStartResponse,
        )

    async def stop(
        self,
        sandbox_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxStopResponse:
        """
        Stop sandbox

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sandbox_id:
            raise ValueError(f"Expected a non-empty value for `sandbox_id` but received {sandbox_id!r}")
        return await self._post(
            f"/sandboxes/{sandbox_id}/stop",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxStopResponse,
        )


class SandboxesResourceWithRawResponse:
    def __init__(self, sandboxes: SandboxesResource) -> None:
        self._sandboxes = sandboxes

        self.create = to_raw_response_wrapper(
            sandboxes.create,
        )
        self.retrieve = to_raw_response_wrapper(
            sandboxes.retrieve,
        )
        self.list = to_raw_response_wrapper(
            sandboxes.list,
        )
        self.delete = to_raw_response_wrapper(
            sandboxes.delete,
        )
        self.execute = to_raw_response_wrapper(
            sandboxes.execute,
        )
        self.get_logs = to_raw_response_wrapper(
            sandboxes.get_logs,
        )
        self.open_terminal = to_raw_response_wrapper(
            sandboxes.open_terminal,
        )
        self.start = to_raw_response_wrapper(
            sandboxes.start,
        )
        self.stop = to_raw_response_wrapper(
            sandboxes.stop,
        )


class AsyncSandboxesResourceWithRawResponse:
    def __init__(self, sandboxes: AsyncSandboxesResource) -> None:
        self._sandboxes = sandboxes

        self.create = async_to_raw_response_wrapper(
            sandboxes.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            sandboxes.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            sandboxes.list,
        )
        self.delete = async_to_raw_response_wrapper(
            sandboxes.delete,
        )
        self.execute = async_to_raw_response_wrapper(
            sandboxes.execute,
        )
        self.get_logs = async_to_raw_response_wrapper(
            sandboxes.get_logs,
        )
        self.open_terminal = async_to_raw_response_wrapper(
            sandboxes.open_terminal,
        )
        self.start = async_to_raw_response_wrapper(
            sandboxes.start,
        )
        self.stop = async_to_raw_response_wrapper(
            sandboxes.stop,
        )


class SandboxesResourceWithStreamingResponse:
    def __init__(self, sandboxes: SandboxesResource) -> None:
        self._sandboxes = sandboxes

        self.create = to_streamed_response_wrapper(
            sandboxes.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            sandboxes.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            sandboxes.list,
        )
        self.delete = to_streamed_response_wrapper(
            sandboxes.delete,
        )
        self.execute = to_streamed_response_wrapper(
            sandboxes.execute,
        )
        self.get_logs = to_streamed_response_wrapper(
            sandboxes.get_logs,
        )
        self.open_terminal = to_streamed_response_wrapper(
            sandboxes.open_terminal,
        )
        self.start = to_streamed_response_wrapper(
            sandboxes.start,
        )
        self.stop = to_streamed_response_wrapper(
            sandboxes.stop,
        )


class AsyncSandboxesResourceWithStreamingResponse:
    def __init__(self, sandboxes: AsyncSandboxesResource) -> None:
        self._sandboxes = sandboxes

        self.create = async_to_streamed_response_wrapper(
            sandboxes.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            sandboxes.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            sandboxes.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            sandboxes.delete,
        )
        self.execute = async_to_streamed_response_wrapper(
            sandboxes.execute,
        )
        self.get_logs = async_to_streamed_response_wrapper(
            sandboxes.get_logs,
        )
        self.open_terminal = async_to_streamed_response_wrapper(
            sandboxes.open_terminal,
        )
        self.start = async_to_streamed_response_wrapper(
            sandboxes.start,
        )
        self.stop = async_to_streamed_response_wrapper(
            sandboxes.stop,
        )
