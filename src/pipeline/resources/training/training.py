# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .logs import (
    LogsResource,
    AsyncLogsResource,
    LogsResourceWithRawResponse,
    AsyncLogsResourceWithRawResponse,
    LogsResourceWithStreamingResponse,
    AsyncLogsResourceWithStreamingResponse,
)
from ...types import training_trigger_params, training_update_status_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ...types.training_list_response import TrainingListResponse
from ...types.training_trigger_response import TrainingTriggerResponse
from ...types.training_update_status_response import TrainingUpdateStatusResponse

__all__ = ["TrainingResource", "AsyncTrainingResource"]


class TrainingResource(SyncAPIResource):
    """BYOC Training Orchestration"""

    @cached_property
    def logs(self) -> LogsResource:
        """BYOC Training Orchestration"""
        return LogsResource(self._client)

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

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrainingListResponse:
        """List all training jobs"""
        return self._get(
            "/training",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrainingListResponse,
        )

    def trigger(
        self,
        *,
        compute: Literal["auto", "local", "aws"] | Omit = omit,
        config: object | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrainingTriggerResponse:
        """
        Trigger a training run (BYOC or Cloud)

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
                    "compute": compute,
                    "config": config,
                    "name": name,
                },
                training_trigger_params.TrainingTriggerParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrainingTriggerResponse,
        )

    def update_status(
        self,
        id: str,
        *,
        status: Literal["RUNNING", "COMPLETED", "FAILED"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrainingUpdateStatusResponse:
        """
        Update training job status (Worker only)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/training/{id}",
            body=maybe_transform({"status": status}, training_update_status_params.TrainingUpdateStatusParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrainingUpdateStatusResponse,
        )


class AsyncTrainingResource(AsyncAPIResource):
    """BYOC Training Orchestration"""

    @cached_property
    def logs(self) -> AsyncLogsResource:
        """BYOC Training Orchestration"""
        return AsyncLogsResource(self._client)

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

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrainingListResponse:
        """List all training jobs"""
        return await self._get(
            "/training",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrainingListResponse,
        )

    async def trigger(
        self,
        *,
        compute: Literal["auto", "local", "aws"] | Omit = omit,
        config: object | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrainingTriggerResponse:
        """
        Trigger a training run (BYOC or Cloud)

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
                    "compute": compute,
                    "config": config,
                    "name": name,
                },
                training_trigger_params.TrainingTriggerParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrainingTriggerResponse,
        )

    async def update_status(
        self,
        id: str,
        *,
        status: Literal["RUNNING", "COMPLETED", "FAILED"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrainingUpdateStatusResponse:
        """
        Update training job status (Worker only)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/training/{id}",
            body=await async_maybe_transform(
                {"status": status}, training_update_status_params.TrainingUpdateStatusParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrainingUpdateStatusResponse,
        )


class TrainingResourceWithRawResponse:
    def __init__(self, training: TrainingResource) -> None:
        self._training = training

        self.list = to_raw_response_wrapper(
            training.list,
        )
        self.trigger = to_raw_response_wrapper(
            training.trigger,
        )
        self.update_status = to_raw_response_wrapper(
            training.update_status,
        )

    @cached_property
    def logs(self) -> LogsResourceWithRawResponse:
        """BYOC Training Orchestration"""
        return LogsResourceWithRawResponse(self._training.logs)


class AsyncTrainingResourceWithRawResponse:
    def __init__(self, training: AsyncTrainingResource) -> None:
        self._training = training

        self.list = async_to_raw_response_wrapper(
            training.list,
        )
        self.trigger = async_to_raw_response_wrapper(
            training.trigger,
        )
        self.update_status = async_to_raw_response_wrapper(
            training.update_status,
        )

    @cached_property
    def logs(self) -> AsyncLogsResourceWithRawResponse:
        """BYOC Training Orchestration"""
        return AsyncLogsResourceWithRawResponse(self._training.logs)


class TrainingResourceWithStreamingResponse:
    def __init__(self, training: TrainingResource) -> None:
        self._training = training

        self.list = to_streamed_response_wrapper(
            training.list,
        )
        self.trigger = to_streamed_response_wrapper(
            training.trigger,
        )
        self.update_status = to_streamed_response_wrapper(
            training.update_status,
        )

    @cached_property
    def logs(self) -> LogsResourceWithStreamingResponse:
        """BYOC Training Orchestration"""
        return LogsResourceWithStreamingResponse(self._training.logs)


class AsyncTrainingResourceWithStreamingResponse:
    def __init__(self, training: AsyncTrainingResource) -> None:
        self._training = training

        self.list = async_to_streamed_response_wrapper(
            training.list,
        )
        self.trigger = async_to_streamed_response_wrapper(
            training.trigger,
        )
        self.update_status = async_to_streamed_response_wrapper(
            training.update_status,
        )

    @cached_property
    def logs(self) -> AsyncLogsResourceWithStreamingResponse:
        """BYOC Training Orchestration"""
        return AsyncLogsResourceWithStreamingResponse(self._training.logs)
