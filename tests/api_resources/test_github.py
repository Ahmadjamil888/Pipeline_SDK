# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from pipeline_labs import Pipeline, AsyncPipeline
from pipeline_labs.types import (
    GitHubInitiateOAuthResponse,
    GitHubCheckConnectionStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGitHub:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_check_connection_status(self, client: Pipeline) -> None:
        github = client.github.check_connection_status(
            user_id="user_id",
        )
        assert_matches_type(GitHubCheckConnectionStatusResponse, github, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_check_connection_status(self, client: Pipeline) -> None:
        response = client.github.with_raw_response.check_connection_status(
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        github = response.parse()
        assert_matches_type(GitHubCheckConnectionStatusResponse, github, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_check_connection_status(self, client: Pipeline) -> None:
        with client.github.with_streaming_response.check_connection_status(
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            github = response.parse()
            assert_matches_type(GitHubCheckConnectionStatusResponse, github, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_initiate_oauth(self, client: Pipeline) -> None:
        github = client.github.initiate_oauth(
            user_id="user_id",
        )
        assert_matches_type(GitHubInitiateOAuthResponse, github, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_initiate_oauth(self, client: Pipeline) -> None:
        response = client.github.with_raw_response.initiate_oauth(
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        github = response.parse()
        assert_matches_type(GitHubInitiateOAuthResponse, github, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_initiate_oauth(self, client: Pipeline) -> None:
        with client.github.with_streaming_response.initiate_oauth(
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            github = response.parse()
            assert_matches_type(GitHubInitiateOAuthResponse, github, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGitHub:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_check_connection_status(self, async_client: AsyncPipeline) -> None:
        github = await async_client.github.check_connection_status(
            user_id="user_id",
        )
        assert_matches_type(GitHubCheckConnectionStatusResponse, github, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_check_connection_status(self, async_client: AsyncPipeline) -> None:
        response = await async_client.github.with_raw_response.check_connection_status(
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        github = await response.parse()
        assert_matches_type(GitHubCheckConnectionStatusResponse, github, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_check_connection_status(self, async_client: AsyncPipeline) -> None:
        async with async_client.github.with_streaming_response.check_connection_status(
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            github = await response.parse()
            assert_matches_type(GitHubCheckConnectionStatusResponse, github, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_initiate_oauth(self, async_client: AsyncPipeline) -> None:
        github = await async_client.github.initiate_oauth(
            user_id="user_id",
        )
        assert_matches_type(GitHubInitiateOAuthResponse, github, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_initiate_oauth(self, async_client: AsyncPipeline) -> None:
        response = await async_client.github.with_raw_response.initiate_oauth(
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        github = await response.parse()
        assert_matches_type(GitHubInitiateOAuthResponse, github, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_initiate_oauth(self, async_client: AsyncPipeline) -> None:
        async with async_client.github.with_streaming_response.initiate_oauth(
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            github = await response.parse()
            assert_matches_type(GitHubInitiateOAuthResponse, github, path=["response"])

        assert cast(Any, response.is_closed) is True
