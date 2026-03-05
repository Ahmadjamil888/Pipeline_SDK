# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pipeline import Pipeline, AsyncPipeline
from tests.utils import assert_matches_type
from pipeline.types import AuthAuthenticateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuth:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_authenticate(self, client: Pipeline) -> None:
        auth = client.auth.authenticate()
        assert_matches_type(AuthAuthenticateResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_authenticate(self, client: Pipeline) -> None:
        response = client.auth.with_raw_response.authenticate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthAuthenticateResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_authenticate(self, client: Pipeline) -> None:
        with client.auth.with_streaming_response.authenticate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthAuthenticateResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAuth:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_authenticate(self, async_client: AsyncPipeline) -> None:
        auth = await async_client.auth.authenticate()
        assert_matches_type(AuthAuthenticateResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_authenticate(self, async_client: AsyncPipeline) -> None:
        response = await async_client.auth.with_raw_response.authenticate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthAuthenticateResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_authenticate(self, async_client: AsyncPipeline) -> None:
        async with async_client.auth.with_streaming_response.authenticate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthAuthenticateResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True
