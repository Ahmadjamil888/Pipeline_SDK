# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["ComputeResource", "AsyncComputeResource"]


class ComputeResource(SyncAPIResource):
    """Hardware & Cloud Configuration"""

    @cached_property
    def with_raw_response(self) -> ComputeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Ahmadjamil888/Pipeline_SDK#accessing-raw-response-data-eg-headers
        """
        return ComputeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ComputeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Ahmadjamil888/Pipeline_SDK#with_streaming_response
        """
        return ComputeResourceWithStreamingResponse(self)

    def retrieve_provider(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Get active compute provider info"""
        return self._get(
            "/compute/provider",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncComputeResource(AsyncAPIResource):
    """Hardware & Cloud Configuration"""

    @cached_property
    def with_raw_response(self) -> AsyncComputeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Ahmadjamil888/Pipeline_SDK#accessing-raw-response-data-eg-headers
        """
        return AsyncComputeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncComputeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Ahmadjamil888/Pipeline_SDK#with_streaming_response
        """
        return AsyncComputeResourceWithStreamingResponse(self)

    async def retrieve_provider(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Get active compute provider info"""
        return await self._get(
            "/compute/provider",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class ComputeResourceWithRawResponse:
    def __init__(self, compute: ComputeResource) -> None:
        self._compute = compute

        self.retrieve_provider = to_raw_response_wrapper(
            compute.retrieve_provider,
        )


class AsyncComputeResourceWithRawResponse:
    def __init__(self, compute: AsyncComputeResource) -> None:
        self._compute = compute

        self.retrieve_provider = async_to_raw_response_wrapper(
            compute.retrieve_provider,
        )


class ComputeResourceWithStreamingResponse:
    def __init__(self, compute: ComputeResource) -> None:
        self._compute = compute

        self.retrieve_provider = to_streamed_response_wrapper(
            compute.retrieve_provider,
        )


class AsyncComputeResourceWithStreamingResponse:
    def __init__(self, compute: AsyncComputeResource) -> None:
        self._compute = compute

        self.retrieve_provider = async_to_streamed_response_wrapper(
            compute.retrieve_provider,
        )
