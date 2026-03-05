# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .keys import (
    KeysResource,
    AsyncKeysResource,
    KeysResourceWithRawResponse,
    AsyncKeysResourceWithRawResponse,
    KeysResourceWithStreamingResponse,
    AsyncKeysResourceWithStreamingResponse,
)
from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.auth_authenticate_response import AuthAuthenticateResponse

__all__ = ["AuthResource", "AsyncAuthResource"]


class AuthResource(SyncAPIResource):
    """Auth & Key Management"""

    @cached_property
    def keys(self) -> KeysResource:
        """Auth & Key Management"""
        return KeysResource(self._client)

    @cached_property
    def with_raw_response(self) -> AuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/pipeline-python#accessing-raw-response-data-eg-headers
        """
        return AuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/pipeline-python#with_streaming_response
        """
        return AuthResourceWithStreamingResponse(self)

    def authenticate(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthAuthenticateResponse:
        """Authenticate and retrieve an API key"""
        return self._post(
            "/auth",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthAuthenticateResponse,
        )


class AsyncAuthResource(AsyncAPIResource):
    """Auth & Key Management"""

    @cached_property
    def keys(self) -> AsyncKeysResource:
        """Auth & Key Management"""
        return AsyncKeysResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/pipeline-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/pipeline-python#with_streaming_response
        """
        return AsyncAuthResourceWithStreamingResponse(self)

    async def authenticate(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthAuthenticateResponse:
        """Authenticate and retrieve an API key"""
        return await self._post(
            "/auth",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthAuthenticateResponse,
        )


class AuthResourceWithRawResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

        self.authenticate = to_raw_response_wrapper(
            auth.authenticate,
        )

    @cached_property
    def keys(self) -> KeysResourceWithRawResponse:
        """Auth & Key Management"""
        return KeysResourceWithRawResponse(self._auth.keys)


class AsyncAuthResourceWithRawResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

        self.authenticate = async_to_raw_response_wrapper(
            auth.authenticate,
        )

    @cached_property
    def keys(self) -> AsyncKeysResourceWithRawResponse:
        """Auth & Key Management"""
        return AsyncKeysResourceWithRawResponse(self._auth.keys)


class AuthResourceWithStreamingResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

        self.authenticate = to_streamed_response_wrapper(
            auth.authenticate,
        )

    @cached_property
    def keys(self) -> KeysResourceWithStreamingResponse:
        """Auth & Key Management"""
        return KeysResourceWithStreamingResponse(self._auth.keys)


class AsyncAuthResourceWithStreamingResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

        self.authenticate = async_to_streamed_response_wrapper(
            auth.authenticate,
        )

    @cached_property
    def keys(self) -> AsyncKeysResourceWithStreamingResponse:
        """Auth & Key Management"""
        return AsyncKeysResourceWithStreamingResponse(self._auth.keys)
