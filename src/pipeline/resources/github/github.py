# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .repos import (
    ReposResource,
    AsyncReposResource,
    ReposResourceWithRawResponse,
    AsyncReposResourceWithRawResponse,
    ReposResourceWithStreamingResponse,
    AsyncReposResourceWithStreamingResponse,
)
from ...types import github_initiate_oauth_params, github_handle_callback_params, github_check_connection_status_params
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.github_initiate_oauth_response import GitHubInitiateOAuthResponse
from ...types.github_check_connection_status_response import GitHubCheckConnectionStatusResponse

__all__ = ["GitHubResource", "AsyncGitHubResource"]


class GitHubResource(SyncAPIResource):
    @cached_property
    def repos(self) -> ReposResource:
        return ReposResource(self._client)

    @cached_property
    def with_raw_response(self) -> GitHubResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/pipeline-python#accessing-raw-response-data-eg-headers
        """
        return GitHubResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GitHubResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/pipeline-python#with_streaming_response
        """
        return GitHubResourceWithStreamingResponse(self)

    def check_connection_status(
        self,
        *,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GitHubCheckConnectionStatusResponse:
        """
        Check GitHub connection status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/github/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"user_id": user_id}, github_check_connection_status_params.GitHubCheckConnectionStatusParams
                ),
            ),
            cast_to=GitHubCheckConnectionStatusResponse,
        )

    def handle_callback(
        self,
        *,
        code: str,
        state: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Handles the OAuth callback after user authorizes GitHub access.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/github/callback",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "code": code,
                        "state": state,
                    },
                    github_handle_callback_params.GitHubHandleCallbackParams,
                ),
            ),
            cast_to=NoneType,
        )

    def initiate_oauth(
        self,
        *,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GitHubInitiateOAuthResponse:
        """
        Returns the GitHub OAuth URL to redirect the user to.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/github/connect",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"user_id": user_id}, github_initiate_oauth_params.GitHubInitiateOAuthParams),
            ),
            cast_to=GitHubInitiateOAuthResponse,
        )


class AsyncGitHubResource(AsyncAPIResource):
    @cached_property
    def repos(self) -> AsyncReposResource:
        return AsyncReposResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGitHubResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/pipeline-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGitHubResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGitHubResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/pipeline-python#with_streaming_response
        """
        return AsyncGitHubResourceWithStreamingResponse(self)

    async def check_connection_status(
        self,
        *,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GitHubCheckConnectionStatusResponse:
        """
        Check GitHub connection status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/github/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"user_id": user_id}, github_check_connection_status_params.GitHubCheckConnectionStatusParams
                ),
            ),
            cast_to=GitHubCheckConnectionStatusResponse,
        )

    async def handle_callback(
        self,
        *,
        code: str,
        state: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Handles the OAuth callback after user authorizes GitHub access.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/github/callback",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "code": code,
                        "state": state,
                    },
                    github_handle_callback_params.GitHubHandleCallbackParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def initiate_oauth(
        self,
        *,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GitHubInitiateOAuthResponse:
        """
        Returns the GitHub OAuth URL to redirect the user to.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/github/connect",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"user_id": user_id}, github_initiate_oauth_params.GitHubInitiateOAuthParams
                ),
            ),
            cast_to=GitHubInitiateOAuthResponse,
        )


class GitHubResourceWithRawResponse:
    def __init__(self, github: GitHubResource) -> None:
        self._github = github

        self.check_connection_status = to_raw_response_wrapper(
            github.check_connection_status,
        )
        self.handle_callback = to_raw_response_wrapper(
            github.handle_callback,
        )
        self.initiate_oauth = to_raw_response_wrapper(
            github.initiate_oauth,
        )

    @cached_property
    def repos(self) -> ReposResourceWithRawResponse:
        return ReposResourceWithRawResponse(self._github.repos)


class AsyncGitHubResourceWithRawResponse:
    def __init__(self, github: AsyncGitHubResource) -> None:
        self._github = github

        self.check_connection_status = async_to_raw_response_wrapper(
            github.check_connection_status,
        )
        self.handle_callback = async_to_raw_response_wrapper(
            github.handle_callback,
        )
        self.initiate_oauth = async_to_raw_response_wrapper(
            github.initiate_oauth,
        )

    @cached_property
    def repos(self) -> AsyncReposResourceWithRawResponse:
        return AsyncReposResourceWithRawResponse(self._github.repos)


class GitHubResourceWithStreamingResponse:
    def __init__(self, github: GitHubResource) -> None:
        self._github = github

        self.check_connection_status = to_streamed_response_wrapper(
            github.check_connection_status,
        )
        self.handle_callback = to_streamed_response_wrapper(
            github.handle_callback,
        )
        self.initiate_oauth = to_streamed_response_wrapper(
            github.initiate_oauth,
        )

    @cached_property
    def repos(self) -> ReposResourceWithStreamingResponse:
        return ReposResourceWithStreamingResponse(self._github.repos)


class AsyncGitHubResourceWithStreamingResponse:
    def __init__(self, github: AsyncGitHubResource) -> None:
        self._github = github

        self.check_connection_status = async_to_streamed_response_wrapper(
            github.check_connection_status,
        )
        self.handle_callback = async_to_streamed_response_wrapper(
            github.handle_callback,
        )
        self.initiate_oauth = async_to_streamed_response_wrapper(
            github.initiate_oauth,
        )

    @cached_property
    def repos(self) -> AsyncReposResourceWithStreamingResponse:
        return AsyncReposResourceWithStreamingResponse(self._github.repos)
