# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import fine_tune_start_params
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

__all__ = ["FineTuneResource", "AsyncFineTuneResource"]


class FineTuneResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FineTuneResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Ahmadjamil888/Pipeline_SDK#accessing-raw-response-data-eg-headers
        """
        return FineTuneResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FineTuneResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Ahmadjamil888/Pipeline_SDK#with_streaming_response
        """
        return FineTuneResourceWithStreamingResponse(self)

    def start(
        self,
        *,
        base_model: str,
        dataset_id: str,
        config: fine_tune_start_params.Config | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Optimizes a base model using a specified dataset.

        Plan restrictions for GPU
        apply identically to training jobs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/fine-tune",
            body=maybe_transform(
                {
                    "base_model": base_model,
                    "dataset_id": dataset_id,
                    "config": config,
                },
                fine_tune_start_params.FineTuneStartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncFineTuneResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFineTuneResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Ahmadjamil888/Pipeline_SDK#accessing-raw-response-data-eg-headers
        """
        return AsyncFineTuneResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFineTuneResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Ahmadjamil888/Pipeline_SDK#with_streaming_response
        """
        return AsyncFineTuneResourceWithStreamingResponse(self)

    async def start(
        self,
        *,
        base_model: str,
        dataset_id: str,
        config: fine_tune_start_params.Config | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Optimizes a base model using a specified dataset.

        Plan restrictions for GPU
        apply identically to training jobs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/fine-tune",
            body=await async_maybe_transform(
                {
                    "base_model": base_model,
                    "dataset_id": dataset_id,
                    "config": config,
                },
                fine_tune_start_params.FineTuneStartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class FineTuneResourceWithRawResponse:
    def __init__(self, fine_tune: FineTuneResource) -> None:
        self._fine_tune = fine_tune

        self.start = to_raw_response_wrapper(
            fine_tune.start,
        )


class AsyncFineTuneResourceWithRawResponse:
    def __init__(self, fine_tune: AsyncFineTuneResource) -> None:
        self._fine_tune = fine_tune

        self.start = async_to_raw_response_wrapper(
            fine_tune.start,
        )


class FineTuneResourceWithStreamingResponse:
    def __init__(self, fine_tune: FineTuneResource) -> None:
        self._fine_tune = fine_tune

        self.start = to_streamed_response_wrapper(
            fine_tune.start,
        )


class AsyncFineTuneResourceWithStreamingResponse:
    def __init__(self, fine_tune: AsyncFineTuneResource) -> None:
        self._fine_tune = fine_tune

        self.start = async_to_streamed_response_wrapper(
            fine_tune.start,
        )
