# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import training_start_params
from .._types import Body, Query, Headers, NotGiven, not_given
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
from ..types.training_start_response import TrainingStartResponse

__all__ = ["TrainingResource", "AsyncTrainingResource"]


class TrainingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TrainingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/pipeline-python#accessing-raw-response-data-eg-headers
        """
        return TrainingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TrainingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/pipeline-python#with_streaming_response
        """
        return TrainingResourceWithStreamingResponse(self)

    def start(
        self,
        *,
        config: training_start_params.Config,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrainingStartResponse:
        """Launches a SageMaker training job using server-side AWS credentials.

        Basic plan
        is restricted to CPU (ml.m5.xlarge), while Pro/Enterprise can access GPUs
        (ml.g5.xlarge).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/training",
            body=maybe_transform(
                {
                    "config": config,
                    "name": name,
                },
                training_start_params.TrainingStartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrainingStartResponse,
        )


class AsyncTrainingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTrainingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/pipeline-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTrainingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTrainingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/pipeline-python#with_streaming_response
        """
        return AsyncTrainingResourceWithStreamingResponse(self)

    async def start(
        self,
        *,
        config: training_start_params.Config,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrainingStartResponse:
        """Launches a SageMaker training job using server-side AWS credentials.

        Basic plan
        is restricted to CPU (ml.m5.xlarge), while Pro/Enterprise can access GPUs
        (ml.g5.xlarge).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/training",
            body=await async_maybe_transform(
                {
                    "config": config,
                    "name": name,
                },
                training_start_params.TrainingStartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrainingStartResponse,
        )


class TrainingResourceWithRawResponse:
    def __init__(self, training: TrainingResource) -> None:
        self._training = training

        self.start = to_raw_response_wrapper(
            training.start,
        )


class AsyncTrainingResourceWithRawResponse:
    def __init__(self, training: AsyncTrainingResource) -> None:
        self._training = training

        self.start = async_to_raw_response_wrapper(
            training.start,
        )


class TrainingResourceWithStreamingResponse:
    def __init__(self, training: TrainingResource) -> None:
        self._training = training

        self.start = to_streamed_response_wrapper(
            training.start,
        )


class AsyncTrainingResourceWithStreamingResponse:
    def __init__(self, training: AsyncTrainingResource) -> None:
        self._training = training

        self.start = async_to_streamed_response_wrapper(
            training.start,
        )
