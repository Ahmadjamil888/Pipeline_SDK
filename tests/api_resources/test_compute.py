# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pipeline import Pipeline, AsyncPipeline
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompute:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_provider(self, client: Pipeline) -> None:
        compute = client.compute.retrieve_provider()
        assert_matches_type(object, compute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_provider(self, client: Pipeline) -> None:
        response = client.compute.with_raw_response.retrieve_provider()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        compute = response.parse()
        assert_matches_type(object, compute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_provider(self, client: Pipeline) -> None:
        with client.compute.with_streaming_response.retrieve_provider() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            compute = response.parse()
            assert_matches_type(object, compute, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCompute:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_provider(self, async_client: AsyncPipeline) -> None:
        compute = await async_client.compute.retrieve_provider()
        assert_matches_type(object, compute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_provider(self, async_client: AsyncPipeline) -> None:
        response = await async_client.compute.with_raw_response.retrieve_provider()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        compute = await response.parse()
        assert_matches_type(object, compute, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_provider(self, async_client: AsyncPipeline) -> None:
        async with async_client.compute.with_streaming_response.retrieve_provider() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            compute = await response.parse()
            assert_matches_type(object, compute, path=["response"])

        assert cast(Any, response.is_closed) is True
