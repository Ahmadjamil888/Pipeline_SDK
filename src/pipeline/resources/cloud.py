# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import cloud_configure_params
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

__all__ = ["CloudResource", "AsyncCloudResource"]


class CloudResource(SyncAPIResource):
    """Hardware & Cloud Configuration"""

    @cached_property
    def with_raw_response(self) -> CloudResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Ahmadjamil888/Pipeline_SDK#accessing-raw-response-data-eg-headers
        """
        return CloudResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CloudResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Ahmadjamil888/Pipeline_SDK#with_streaming_response
        """
        return CloudResourceWithStreamingResponse(self)

    def configure(
        self,
        *,
        config: object | Omit = omit,
        provider: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Configure optional cloud provider (AWS)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cloud/configure",
            body=maybe_transform(
                {
                    "config": config,
                    "provider": provider,
                },
                cloud_configure_params.CloudConfigureParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncCloudResource(AsyncAPIResource):
    """Hardware & Cloud Configuration"""

    @cached_property
    def with_raw_response(self) -> AsyncCloudResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Ahmadjamil888/Pipeline_SDK#accessing-raw-response-data-eg-headers
        """
        return AsyncCloudResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCloudResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Ahmadjamil888/Pipeline_SDK#with_streaming_response
        """
        return AsyncCloudResourceWithStreamingResponse(self)

    async def configure(
        self,
        *,
        config: object | Omit = omit,
        provider: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Configure optional cloud provider (AWS)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cloud/configure",
            body=await async_maybe_transform(
                {
                    "config": config,
                    "provider": provider,
                },
                cloud_configure_params.CloudConfigureParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class CloudResourceWithRawResponse:
    def __init__(self, cloud: CloudResource) -> None:
        self._cloud = cloud

        self.configure = to_raw_response_wrapper(
            cloud.configure,
        )


class AsyncCloudResourceWithRawResponse:
    def __init__(self, cloud: AsyncCloudResource) -> None:
        self._cloud = cloud

        self.configure = async_to_raw_response_wrapper(
            cloud.configure,
        )


class CloudResourceWithStreamingResponse:
    def __init__(self, cloud: CloudResource) -> None:
        self._cloud = cloud

        self.configure = to_streamed_response_wrapper(
            cloud.configure,
        )


class AsyncCloudResourceWithStreamingResponse:
    def __init__(self, cloud: AsyncCloudResource) -> None:
        self._cloud = cloud

        self.configure = async_to_streamed_response_wrapper(
            cloud.configure,
        )
