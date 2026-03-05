# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pipeline import Pipeline, AsyncPipeline
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCloud:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_configure(self, client: Pipeline) -> None:
        cloud = client.cloud.configure()
        assert_matches_type(object, cloud, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_configure_with_all_params(self, client: Pipeline) -> None:
        cloud = client.cloud.configure(
            config={},
            provider="provider",
        )
        assert_matches_type(object, cloud, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_configure(self, client: Pipeline) -> None:
        response = client.cloud.with_raw_response.configure()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cloud = response.parse()
        assert_matches_type(object, cloud, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_configure(self, client: Pipeline) -> None:
        with client.cloud.with_streaming_response.configure() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cloud = response.parse()
            assert_matches_type(object, cloud, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCloud:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_configure(self, async_client: AsyncPipeline) -> None:
        cloud = await async_client.cloud.configure()
        assert_matches_type(object, cloud, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_configure_with_all_params(self, async_client: AsyncPipeline) -> None:
        cloud = await async_client.cloud.configure(
            config={},
            provider="provider",
        )
        assert_matches_type(object, cloud, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_configure(self, async_client: AsyncPipeline) -> None:
        response = await async_client.cloud.with_raw_response.configure()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cloud = await response.parse()
        assert_matches_type(object, cloud, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_configure(self, async_client: AsyncPipeline) -> None:
        async with async_client.cloud.with_streaming_response.configure() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cloud = await response.parse()
            assert_matches_type(object, cloud, path=["response"])

        assert cast(Any, response.is_closed) is True
