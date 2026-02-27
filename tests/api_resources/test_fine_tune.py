# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pipeline import Pipeline, AsyncPipeline

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFineTune:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_start(self, client: Pipeline) -> None:
        fine_tune = client.fine_tune.start(
            base_model="llama-3-8b",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert fine_tune is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_start_with_all_params(self, client: Pipeline) -> None:
        fine_tune = client.fine_tune.start(
            base_model="llama-3-8b",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            config={"gpu": "gpu"},
        )
        assert fine_tune is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_start(self, client: Pipeline) -> None:
        response = client.fine_tune.with_raw_response.start(
            base_model="llama-3-8b",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fine_tune = response.parse()
        assert fine_tune is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_start(self, client: Pipeline) -> None:
        with client.fine_tune.with_streaming_response.start(
            base_model="llama-3-8b",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fine_tune = response.parse()
            assert fine_tune is None

        assert cast(Any, response.is_closed) is True


class TestAsyncFineTune:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_start(self, async_client: AsyncPipeline) -> None:
        fine_tune = await async_client.fine_tune.start(
            base_model="llama-3-8b",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert fine_tune is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_start_with_all_params(self, async_client: AsyncPipeline) -> None:
        fine_tune = await async_client.fine_tune.start(
            base_model="llama-3-8b",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            config={"gpu": "gpu"},
        )
        assert fine_tune is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_start(self, async_client: AsyncPipeline) -> None:
        response = await async_client.fine_tune.with_raw_response.start(
            base_model="llama-3-8b",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fine_tune = await response.parse()
        assert fine_tune is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_start(self, async_client: AsyncPipeline) -> None:
        async with async_client.fine_tune.with_streaming_response.start(
            base_model="llama-3-8b",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fine_tune = await response.parse()
            assert fine_tune is None

        assert cast(Any, response.is_closed) is True
