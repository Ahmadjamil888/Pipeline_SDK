# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pipeline import Pipeline, AsyncPipeline
from tests.utils import assert_matches_type
from pipeline.types import (
    AgentCleanDataResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_clean_data(self, client: Pipeline) -> None:
        agent = client.agents.clean_data()
        assert_matches_type(AgentCleanDataResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_clean_data_with_all_params(self, client: Pipeline) -> None:
        agent = client.agents.clean_data(
            dataset_path="dataset_path",
            preview_rows=[{}],
            schema={},
        )
        assert_matches_type(AgentCleanDataResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_clean_data(self, client: Pipeline) -> None:
        response = client.agents.with_raw_response.clean_data()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentCleanDataResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_clean_data(self, client: Pipeline) -> None:
        with client.agents.with_streaming_response.clean_data() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentCleanDataResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_monitor_training(self, client: Pipeline) -> None:
        agent = client.agents.monitor_training()
        assert agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_monitor_training_with_all_params(self, client: Pipeline) -> None:
        agent = client.agents.monitor_training(
            logs="logs",
            metrics={},
            run_id="run_id",
        )
        assert agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_monitor_training(self, client: Pipeline) -> None:
        response = client.agents.with_raw_response.monitor_training()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_monitor_training(self, client: Pipeline) -> None:
        with client.agents.with_streaming_response.monitor_training() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert agent is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_optimize_dataset(self, client: Pipeline) -> None:
        agent = client.agents.optimize_dataset()
        assert agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_optimize_dataset_with_all_params(self, client: Pipeline) -> None:
        agent = client.agents.optimize_dataset(
            dataset_summary={},
            task_type="task_type",
        )
        assert agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_optimize_dataset(self, client: Pipeline) -> None:
        response = client.agents.with_raw_response.optimize_dataset()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_optimize_dataset(self, client: Pipeline) -> None:
        with client.agents.with_streaming_response.optimize_dataset() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert agent is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_summarize_experiment(self, client: Pipeline) -> None:
        agent = client.agents.summarize_experiment()
        assert agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_summarize_experiment_with_all_params(self, client: Pipeline) -> None:
        agent = client.agents.summarize_experiment(
            experiment_metadata={},
            logs_summary="logs_summary",
            metrics={},
        )
        assert agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_summarize_experiment(self, client: Pipeline) -> None:
        response = client.agents.with_raw_response.summarize_experiment()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_summarize_experiment(self, client: Pipeline) -> None:
        with client.agents.with_streaming_response.summarize_experiment() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert agent is None

        assert cast(Any, response.is_closed) is True


class TestAsyncAgents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_clean_data(self, async_client: AsyncPipeline) -> None:
        agent = await async_client.agents.clean_data()
        assert_matches_type(AgentCleanDataResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_clean_data_with_all_params(self, async_client: AsyncPipeline) -> None:
        agent = await async_client.agents.clean_data(
            dataset_path="dataset_path",
            preview_rows=[{}],
            schema={},
        )
        assert_matches_type(AgentCleanDataResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_clean_data(self, async_client: AsyncPipeline) -> None:
        response = await async_client.agents.with_raw_response.clean_data()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentCleanDataResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_clean_data(self, async_client: AsyncPipeline) -> None:
        async with async_client.agents.with_streaming_response.clean_data() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentCleanDataResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_monitor_training(self, async_client: AsyncPipeline) -> None:
        agent = await async_client.agents.monitor_training()
        assert agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_monitor_training_with_all_params(self, async_client: AsyncPipeline) -> None:
        agent = await async_client.agents.monitor_training(
            logs="logs",
            metrics={},
            run_id="run_id",
        )
        assert agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_monitor_training(self, async_client: AsyncPipeline) -> None:
        response = await async_client.agents.with_raw_response.monitor_training()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_monitor_training(self, async_client: AsyncPipeline) -> None:
        async with async_client.agents.with_streaming_response.monitor_training() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert agent is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_optimize_dataset(self, async_client: AsyncPipeline) -> None:
        agent = await async_client.agents.optimize_dataset()
        assert agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_optimize_dataset_with_all_params(self, async_client: AsyncPipeline) -> None:
        agent = await async_client.agents.optimize_dataset(
            dataset_summary={},
            task_type="task_type",
        )
        assert agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_optimize_dataset(self, async_client: AsyncPipeline) -> None:
        response = await async_client.agents.with_raw_response.optimize_dataset()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_optimize_dataset(self, async_client: AsyncPipeline) -> None:
        async with async_client.agents.with_streaming_response.optimize_dataset() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert agent is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_summarize_experiment(self, async_client: AsyncPipeline) -> None:
        agent = await async_client.agents.summarize_experiment()
        assert agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_summarize_experiment_with_all_params(self, async_client: AsyncPipeline) -> None:
        agent = await async_client.agents.summarize_experiment(
            experiment_metadata={},
            logs_summary="logs_summary",
            metrics={},
        )
        assert agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_summarize_experiment(self, async_client: AsyncPipeline) -> None:
        response = await async_client.agents.with_raw_response.summarize_experiment()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_summarize_experiment(self, async_client: AsyncPipeline) -> None:
        async with async_client.agents.with_streaming_response.summarize_experiment() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert agent is None

        assert cast(Any, response.is_closed) is True
