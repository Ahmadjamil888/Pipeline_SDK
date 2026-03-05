# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import (
    agent_clean_data_params,
    agent_monitor_training_params,
    agent_optimize_dataset_params,
    agent_summarize_experiment_params,
)
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
from ..types.agent_clean_data_response import AgentCleanDataResponse

__all__ = ["AgentsResource", "AsyncAgentsResource"]


class AgentsResource(SyncAPIResource):
    """Agentic AI services (Data Clean, Monitor, Optimize, Summarize)"""

    @cached_property
    def with_raw_response(self) -> AgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Ahmadjamil888/Pipeline_SDK#accessing-raw-response-data-eg-headers
        """
        return AgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Ahmadjamil888/Pipeline_SDK#with_streaming_response
        """
        return AgentsResourceWithStreamingResponse(self)

    def clean_data(
        self,
        *,
        dataset_path: str | Omit = omit,
        preview_rows: Iterable[object] | Omit = omit,
        schema: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentCleanDataResponse:
        """
        Detect and suggest dataset cleaning steps

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/agents/data_clean",
            body=maybe_transform(
                {
                    "dataset_path": dataset_path,
                    "preview_rows": preview_rows,
                    "schema": schema,
                },
                agent_clean_data_params.AgentCleanDataParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentCleanDataResponse,
        )

    def monitor_training(
        self,
        *,
        logs: str | Omit = omit,
        metrics: object | Omit = omit,
        run_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Monitor training logs and suggest adjustments

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/agents/monitor",
            body=maybe_transform(
                {
                    "logs": logs,
                    "metrics": metrics,
                    "run_id": run_id,
                },
                agent_monitor_training_params.AgentMonitorTrainingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def optimize_dataset(
        self,
        *,
        dataset_summary: object | Omit = omit,
        task_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Suggest augmentation and feature engineering

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/agents/dataset_optimize",
            body=maybe_transform(
                {
                    "dataset_summary": dataset_summary,
                    "task_type": task_type,
                },
                agent_optimize_dataset_params.AgentOptimizeDatasetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def summarize_experiment(
        self,
        *,
        experiment_metadata: object | Omit = omit,
        logs_summary: str | Omit = omit,
        metrics: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Summarize experiment and generate report

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/agents/experiment_summarize",
            body=maybe_transform(
                {
                    "experiment_metadata": experiment_metadata,
                    "logs_summary": logs_summary,
                    "metrics": metrics,
                },
                agent_summarize_experiment_params.AgentSummarizeExperimentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAgentsResource(AsyncAPIResource):
    """Agentic AI services (Data Clean, Monitor, Optimize, Summarize)"""

    @cached_property
    def with_raw_response(self) -> AsyncAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Ahmadjamil888/Pipeline_SDK#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Ahmadjamil888/Pipeline_SDK#with_streaming_response
        """
        return AsyncAgentsResourceWithStreamingResponse(self)

    async def clean_data(
        self,
        *,
        dataset_path: str | Omit = omit,
        preview_rows: Iterable[object] | Omit = omit,
        schema: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentCleanDataResponse:
        """
        Detect and suggest dataset cleaning steps

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/agents/data_clean",
            body=await async_maybe_transform(
                {
                    "dataset_path": dataset_path,
                    "preview_rows": preview_rows,
                    "schema": schema,
                },
                agent_clean_data_params.AgentCleanDataParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentCleanDataResponse,
        )

    async def monitor_training(
        self,
        *,
        logs: str | Omit = omit,
        metrics: object | Omit = omit,
        run_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Monitor training logs and suggest adjustments

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/agents/monitor",
            body=await async_maybe_transform(
                {
                    "logs": logs,
                    "metrics": metrics,
                    "run_id": run_id,
                },
                agent_monitor_training_params.AgentMonitorTrainingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def optimize_dataset(
        self,
        *,
        dataset_summary: object | Omit = omit,
        task_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Suggest augmentation and feature engineering

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/agents/dataset_optimize",
            body=await async_maybe_transform(
                {
                    "dataset_summary": dataset_summary,
                    "task_type": task_type,
                },
                agent_optimize_dataset_params.AgentOptimizeDatasetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def summarize_experiment(
        self,
        *,
        experiment_metadata: object | Omit = omit,
        logs_summary: str | Omit = omit,
        metrics: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Summarize experiment and generate report

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/agents/experiment_summarize",
            body=await async_maybe_transform(
                {
                    "experiment_metadata": experiment_metadata,
                    "logs_summary": logs_summary,
                    "metrics": metrics,
                },
                agent_summarize_experiment_params.AgentSummarizeExperimentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AgentsResourceWithRawResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.clean_data = to_raw_response_wrapper(
            agents.clean_data,
        )
        self.monitor_training = to_raw_response_wrapper(
            agents.monitor_training,
        )
        self.optimize_dataset = to_raw_response_wrapper(
            agents.optimize_dataset,
        )
        self.summarize_experiment = to_raw_response_wrapper(
            agents.summarize_experiment,
        )


class AsyncAgentsResourceWithRawResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.clean_data = async_to_raw_response_wrapper(
            agents.clean_data,
        )
        self.monitor_training = async_to_raw_response_wrapper(
            agents.monitor_training,
        )
        self.optimize_dataset = async_to_raw_response_wrapper(
            agents.optimize_dataset,
        )
        self.summarize_experiment = async_to_raw_response_wrapper(
            agents.summarize_experiment,
        )


class AgentsResourceWithStreamingResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.clean_data = to_streamed_response_wrapper(
            agents.clean_data,
        )
        self.monitor_training = to_streamed_response_wrapper(
            agents.monitor_training,
        )
        self.optimize_dataset = to_streamed_response_wrapper(
            agents.optimize_dataset,
        )
        self.summarize_experiment = to_streamed_response_wrapper(
            agents.summarize_experiment,
        )


class AsyncAgentsResourceWithStreamingResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.clean_data = async_to_streamed_response_wrapper(
            agents.clean_data,
        )
        self.monitor_training = async_to_streamed_response_wrapper(
            agents.monitor_training,
        )
        self.optimize_dataset = async_to_streamed_response_wrapper(
            agents.optimize_dataset,
        )
        self.summarize_experiment = async_to_streamed_response_wrapper(
            agents.summarize_experiment,
        )
