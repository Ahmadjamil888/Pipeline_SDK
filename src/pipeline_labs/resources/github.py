# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import github_setup_callback_params, github_list_repositories_params
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
from ..types.github_list_repositories_response import GitHubListRepositoriesResponse
from ..types.github_initiate_installation_response import GitHubInitiateInstallationResponse

__all__ = ["GitHubResource", "AsyncGitHubResource"]


class GitHubResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GitHubResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Ahmadjamil888/Pipeline_SDK#accessing-raw-response-data-eg-headers
        """
        return GitHubResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GitHubResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Ahmadjamil888/Pipeline_SDK#with_streaming_response
        """
        return GitHubResourceWithStreamingResponse(self)

    def initiate_installation(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GitHubInitiateInstallationResponse:
        """Returns the URL to install the GitHub App."""
        return self._get(
            "/github/connect",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GitHubInitiateInstallationResponse,
        )

    def list_repositories(
        self,
        *,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GitHubListRepositoriesResponse:
        """
        List repositories accessible via GitHub App installation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/github/repos",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"user_id": user_id}, github_list_repositories_params.GitHubListRepositoriesParams
                ),
            ),
            cast_to=GitHubListRepositoriesResponse,
        )

    def setup_callback(
        self,
        *,
        installation_id: int,
        setup_action: Literal["install", "update"] | Omit = omit,
        state: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Callback URL after GitHub App installation is complete.

        Stores installation_id
        and redirects to frontend.

        Args:
          state: User ID passed during installation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/github/setup",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "installation_id": installation_id,
                        "setup_action": setup_action,
                        "state": state,
                    },
                    github_setup_callback_params.GitHubSetupCallbackParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncGitHubResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGitHubResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Ahmadjamil888/Pipeline_SDK#accessing-raw-response-data-eg-headers
        """
        return AsyncGitHubResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGitHubResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Ahmadjamil888/Pipeline_SDK#with_streaming_response
        """
        return AsyncGitHubResourceWithStreamingResponse(self)

    async def initiate_installation(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GitHubInitiateInstallationResponse:
        """Returns the URL to install the GitHub App."""
        return await self._get(
            "/github/connect",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GitHubInitiateInstallationResponse,
        )

    async def list_repositories(
        self,
        *,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GitHubListRepositoriesResponse:
        """
        List repositories accessible via GitHub App installation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/github/repos",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"user_id": user_id}, github_list_repositories_params.GitHubListRepositoriesParams
                ),
            ),
            cast_to=GitHubListRepositoriesResponse,
        )

    async def setup_callback(
        self,
        *,
        installation_id: int,
        setup_action: Literal["install", "update"] | Omit = omit,
        state: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Callback URL after GitHub App installation is complete.

        Stores installation_id
        and redirects to frontend.

        Args:
          state: User ID passed during installation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/github/setup",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "installation_id": installation_id,
                        "setup_action": setup_action,
                        "state": state,
                    },
                    github_setup_callback_params.GitHubSetupCallbackParams,
                ),
            ),
            cast_to=NoneType,
        )


class GitHubResourceWithRawResponse:
    def __init__(self, github: GitHubResource) -> None:
        self._github = github

        self.initiate_installation = to_raw_response_wrapper(
            github.initiate_installation,
        )
        self.list_repositories = to_raw_response_wrapper(
            github.list_repositories,
        )
        self.setup_callback = to_raw_response_wrapper(
            github.setup_callback,
        )


class AsyncGitHubResourceWithRawResponse:
    def __init__(self, github: AsyncGitHubResource) -> None:
        self._github = github

        self.initiate_installation = async_to_raw_response_wrapper(
            github.initiate_installation,
        )
        self.list_repositories = async_to_raw_response_wrapper(
            github.list_repositories,
        )
        self.setup_callback = async_to_raw_response_wrapper(
            github.setup_callback,
        )


class GitHubResourceWithStreamingResponse:
    def __init__(self, github: GitHubResource) -> None:
        self._github = github

        self.initiate_installation = to_streamed_response_wrapper(
            github.initiate_installation,
        )
        self.list_repositories = to_streamed_response_wrapper(
            github.list_repositories,
        )
        self.setup_callback = to_streamed_response_wrapper(
            github.setup_callback,
        )


class AsyncGitHubResourceWithStreamingResponse:
    def __init__(self, github: AsyncGitHubResource) -> None:
        self._github = github

        self.initiate_installation = async_to_streamed_response_wrapper(
            github.initiate_installation,
        )
        self.list_repositories = async_to_streamed_response_wrapper(
            github.list_repositories,
        )
        self.setup_callback = async_to_streamed_response_wrapper(
            github.setup_callback,
        )
