# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pipeline import Pipeline, AsyncPipeline
from tests.utils import assert_matches_type
from pipeline.types import TrainingStartResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTraining:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_start(self, client: Pipeline) -> None:
        training = client.training.start(
            config={},
            name="llama-3-train",
        )
        assert_matches_type(TrainingStartResponse, training, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_start_with_all_params(self, client: Pipeline) -> None:
        training = client.training.start(
            config={
                "distributed": True,
                "gpu": "gpu",
                "workers": 0,
            },
            name="llama-3-train",
        )
        assert_matches_type(TrainingStartResponse, training, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_start(self, client: Pipeline) -> None:
        response = client.training.with_raw_response.start(
            config={},
            name="llama-3-train",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training = response.parse()
        assert_matches_type(TrainingStartResponse, training, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_start(self, client: Pipeline) -> None:
        with client.training.with_streaming_response.start(
            config={},
            name="llama-3-train",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training = response.parse()
            assert_matches_type(TrainingStartResponse, training, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTraining:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_start(self, async_client: AsyncPipeline) -> None:
        training = await async_client.training.start(
            config={},
            name="llama-3-train",
        )
        assert_matches_type(TrainingStartResponse, training, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_start_with_all_params(self, async_client: AsyncPipeline) -> None:
        training = await async_client.training.start(
            config={
                "distributed": True,
                "gpu": "gpu",
                "workers": 0,
            },
            name="llama-3-train",
        )
        assert_matches_type(TrainingStartResponse, training, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_start(self, async_client: AsyncPipeline) -> None:
        response = await async_client.training.with_raw_response.start(
            config={},
            name="llama-3-train",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training = await response.parse()
        assert_matches_type(TrainingStartResponse, training, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_start(self, async_client: AsyncPipeline) -> None:
        async with async_client.training.with_streaming_response.start(
            config={},
            name="llama-3-train",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training = await response.parse()
            assert_matches_type(TrainingStartResponse, training, path=["response"])

        assert cast(Any, response.is_closed) is True
