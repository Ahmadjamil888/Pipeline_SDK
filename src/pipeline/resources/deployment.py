# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NoneType, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["DeploymentResource", "AsyncDeploymentResource"]


class DeploymentResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DeploymentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Ahmadjamil888/Pipeline_SDK#accessing-raw-response-data-eg-headers
        """
        return DeploymentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeploymentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Ahmadjamil888/Pipeline_SDK#with_streaming_response
        """
        return DeploymentResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Deploy model to managed inference endpoint"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/deployment",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncDeploymentResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDeploymentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Ahmadjamil888/Pipeline_SDK#accessing-raw-response-data-eg-headers
        """
        return AsyncDeploymentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeploymentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Ahmadjamil888/Pipeline_SDK#with_streaming_response
        """
        return AsyncDeploymentResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Deploy model to managed inference endpoint"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/deployment",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class DeploymentResourceWithRawResponse:
    def __init__(self, deployment: DeploymentResource) -> None:
        self._deployment = deployment

        self.create = to_raw_response_wrapper(
            deployment.create,
        )


class AsyncDeploymentResourceWithRawResponse:
    def __init__(self, deployment: AsyncDeploymentResource) -> None:
        self._deployment = deployment

        self.create = async_to_raw_response_wrapper(
            deployment.create,
        )


class DeploymentResourceWithStreamingResponse:
    def __init__(self, deployment: DeploymentResource) -> None:
        self._deployment = deployment

        self.create = to_streamed_response_wrapper(
            deployment.create,
        )


class AsyncDeploymentResourceWithStreamingResponse:
    def __init__(self, deployment: AsyncDeploymentResource) -> None:
        self._deployment = deployment

        self.create = async_to_streamed_response_wrapper(
            deployment.create,
        )
