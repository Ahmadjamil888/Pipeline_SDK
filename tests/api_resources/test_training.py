# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pipeline import Pipeline, AsyncPipeline
from tests.utils import assert_matches_type
from pipeline.types import (
    TrainingListResponse,
    TrainingTriggerResponse,
    TrainingUpdateStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTraining:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Pipeline) -> None:
        training = client.training.list()
        assert_matches_type(TrainingListResponse, training, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Pipeline) -> None:
        response = client.training.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training = response.parse()
        assert_matches_type(TrainingListResponse, training, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Pipeline) -> None:
        with client.training.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training = response.parse()
            assert_matches_type(TrainingListResponse, training, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_trigger(self, client: Pipeline) -> None:
        training = client.training.trigger()
        assert_matches_type(TrainingTriggerResponse, training, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_trigger_with_all_params(self, client: Pipeline) -> None:
        training = client.training.trigger(
            compute="auto",
            config={},
            name="name",
        )
        assert_matches_type(TrainingTriggerResponse, training, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_trigger(self, client: Pipeline) -> None:
        response = client.training.with_raw_response.trigger()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training = response.parse()
        assert_matches_type(TrainingTriggerResponse, training, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_trigger(self, client: Pipeline) -> None:
        with client.training.with_streaming_response.trigger() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training = response.parse()
            assert_matches_type(TrainingTriggerResponse, training, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_status(self, client: Pipeline) -> None:
        training = client.training.update_status(
            id="id",
        )
        assert_matches_type(TrainingUpdateStatusResponse, training, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_status_with_all_params(self, client: Pipeline) -> None:
        training = client.training.update_status(
            id="id",
            status="RUNNING",
        )
        assert_matches_type(TrainingUpdateStatusResponse, training, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_status(self, client: Pipeline) -> None:
        response = client.training.with_raw_response.update_status(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training = response.parse()
        assert_matches_type(TrainingUpdateStatusResponse, training, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_status(self, client: Pipeline) -> None:
        with client.training.with_streaming_response.update_status(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training = response.parse()
            assert_matches_type(TrainingUpdateStatusResponse, training, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_status(self, client: Pipeline) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.training.with_raw_response.update_status(
                id="",
            )


class TestAsyncTraining:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPipeline) -> None:
        training = await async_client.training.list()
        assert_matches_type(TrainingListResponse, training, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPipeline) -> None:
        response = await async_client.training.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training = await response.parse()
        assert_matches_type(TrainingListResponse, training, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPipeline) -> None:
        async with async_client.training.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training = await response.parse()
            assert_matches_type(TrainingListResponse, training, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_trigger(self, async_client: AsyncPipeline) -> None:
        training = await async_client.training.trigger()
        assert_matches_type(TrainingTriggerResponse, training, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_trigger_with_all_params(self, async_client: AsyncPipeline) -> None:
        training = await async_client.training.trigger(
            compute="auto",
            config={},
            name="name",
        )
        assert_matches_type(TrainingTriggerResponse, training, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_trigger(self, async_client: AsyncPipeline) -> None:
        response = await async_client.training.with_raw_response.trigger()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training = await response.parse()
        assert_matches_type(TrainingTriggerResponse, training, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_trigger(self, async_client: AsyncPipeline) -> None:
        async with async_client.training.with_streaming_response.trigger() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training = await response.parse()
            assert_matches_type(TrainingTriggerResponse, training, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_status(self, async_client: AsyncPipeline) -> None:
        training = await async_client.training.update_status(
            id="id",
        )
        assert_matches_type(TrainingUpdateStatusResponse, training, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_status_with_all_params(self, async_client: AsyncPipeline) -> None:
        training = await async_client.training.update_status(
            id="id",
            status="RUNNING",
        )
        assert_matches_type(TrainingUpdateStatusResponse, training, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_status(self, async_client: AsyncPipeline) -> None:
        response = await async_client.training.with_raw_response.update_status(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training = await response.parse()
        assert_matches_type(TrainingUpdateStatusResponse, training, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_status(self, async_client: AsyncPipeline) -> None:
        async with async_client.training.with_streaming_response.update_status(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training = await response.parse()
            assert_matches_type(TrainingUpdateStatusResponse, training, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_status(self, async_client: AsyncPipeline) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.training.with_raw_response.update_status(
                id="",
            )
