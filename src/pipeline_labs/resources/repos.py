# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import repo_connect_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.repo_connection import RepoConnection

__all__ = ["ReposResource", "AsyncReposResource"]


class ReposResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReposResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Ahmadjamil888/Pipeline_SDK#accessing-raw-response-data-eg-headers
        """
        return ReposResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReposResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Ahmadjamil888/Pipeline_SDK#with_streaming_response
        """
        return ReposResourceWithStreamingResponse(self)

    def retrieve(
        self,
        repo_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RepoConnection:
        """
        Get repository details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not repo_id:
            raise ValueError(f"Expected a non-empty value for `repo_id` but received {repo_id!r}")
        return self._get(
            f"/repos/{repo_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RepoConnection,
        )

    def connect(
        self,
        *,
        provider: Literal["github", "gitlab"],
        repo_url: str,
        branch: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RepoConnection:
        """
        Connect a Git repository

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/repos/connect",
            body=maybe_transform(
                {
                    "provider": provider,
                    "repo_url": repo_url,
                    "branch": branch,
                    "name": name,
                },
                repo_connect_params.RepoConnectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RepoConnection,
        )


class AsyncReposResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReposResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Ahmadjamil888/Pipeline_SDK#accessing-raw-response-data-eg-headers
        """
        return AsyncReposResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReposResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Ahmadjamil888/Pipeline_SDK#with_streaming_response
        """
        return AsyncReposResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        repo_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RepoConnection:
        """
        Get repository details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not repo_id:
            raise ValueError(f"Expected a non-empty value for `repo_id` but received {repo_id!r}")
        return await self._get(
            f"/repos/{repo_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RepoConnection,
        )

    async def connect(
        self,
        *,
        provider: Literal["github", "gitlab"],
        repo_url: str,
        branch: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RepoConnection:
        """
        Connect a Git repository

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/repos/connect",
            body=await async_maybe_transform(
                {
                    "provider": provider,
                    "repo_url": repo_url,
                    "branch": branch,
                    "name": name,
                },
                repo_connect_params.RepoConnectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RepoConnection,
        )


class ReposResourceWithRawResponse:
    def __init__(self, repos: ReposResource) -> None:
        self._repos = repos

        self.retrieve = to_raw_response_wrapper(
            repos.retrieve,
        )
        self.connect = to_raw_response_wrapper(
            repos.connect,
        )


class AsyncReposResourceWithRawResponse:
    def __init__(self, repos: AsyncReposResource) -> None:
        self._repos = repos

        self.retrieve = async_to_raw_response_wrapper(
            repos.retrieve,
        )
        self.connect = async_to_raw_response_wrapper(
            repos.connect,
        )


class ReposResourceWithStreamingResponse:
    def __init__(self, repos: ReposResource) -> None:
        self._repos = repos

        self.retrieve = to_streamed_response_wrapper(
            repos.retrieve,
        )
        self.connect = to_streamed_response_wrapper(
            repos.connect,
        )


class AsyncReposResourceWithStreamingResponse:
    def __init__(self, repos: AsyncReposResource) -> None:
        self._repos = repos

        self.retrieve = async_to_streamed_response_wrapper(
            repos.retrieve,
        )
        self.connect = async_to_streamed_response_wrapper(
            repos.connect,
        )
