# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from pipeline_labs import Pipeline, AsyncPipeline
from pipeline_labs.types import (
    GitHubListRepositoriesResponse,
    GitHubInitiateInstallationResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGitHub:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_initiate_installation(self, client: Pipeline) -> None:
        github = client.github.initiate_installation()
        assert_matches_type(GitHubInitiateInstallationResponse, github, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_initiate_installation(self, client: Pipeline) -> None:
        response = client.github.with_raw_response.initiate_installation()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        github = response.parse()
        assert_matches_type(GitHubInitiateInstallationResponse, github, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_initiate_installation(self, client: Pipeline) -> None:
        with client.github.with_streaming_response.initiate_installation() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            github = response.parse()
            assert_matches_type(GitHubInitiateInstallationResponse, github, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_repositories(self, client: Pipeline) -> None:
        github = client.github.list_repositories(
            user_id="user_id",
        )
        assert_matches_type(GitHubListRepositoriesResponse, github, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_repositories(self, client: Pipeline) -> None:
        response = client.github.with_raw_response.list_repositories(
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        github = response.parse()
        assert_matches_type(GitHubListRepositoriesResponse, github, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_repositories(self, client: Pipeline) -> None:
        with client.github.with_streaming_response.list_repositories(
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            github = response.parse()
            assert_matches_type(GitHubListRepositoriesResponse, github, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_setup_callback(self, client: Pipeline) -> None:
        github = client.github.setup_callback(
            installation_id=0,
        )
        assert github is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_setup_callback_with_all_params(self, client: Pipeline) -> None:
        github = client.github.setup_callback(
            installation_id=0,
            setup_action="install",
            state="state",
        )
        assert github is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_setup_callback(self, client: Pipeline) -> None:
        response = client.github.with_raw_response.setup_callback(
            installation_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        github = response.parse()
        assert github is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_setup_callback(self, client: Pipeline) -> None:
        with client.github.with_streaming_response.setup_callback(
            installation_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            github = response.parse()
            assert github is None

        assert cast(Any, response.is_closed) is True


class TestAsyncGitHub:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_initiate_installation(self, async_client: AsyncPipeline) -> None:
        github = await async_client.github.initiate_installation()
        assert_matches_type(GitHubInitiateInstallationResponse, github, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_initiate_installation(self, async_client: AsyncPipeline) -> None:
        response = await async_client.github.with_raw_response.initiate_installation()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        github = await response.parse()
        assert_matches_type(GitHubInitiateInstallationResponse, github, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_initiate_installation(self, async_client: AsyncPipeline) -> None:
        async with async_client.github.with_streaming_response.initiate_installation() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            github = await response.parse()
            assert_matches_type(GitHubInitiateInstallationResponse, github, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_repositories(self, async_client: AsyncPipeline) -> None:
        github = await async_client.github.list_repositories(
            user_id="user_id",
        )
        assert_matches_type(GitHubListRepositoriesResponse, github, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_repositories(self, async_client: AsyncPipeline) -> None:
        response = await async_client.github.with_raw_response.list_repositories(
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        github = await response.parse()
        assert_matches_type(GitHubListRepositoriesResponse, github, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_repositories(self, async_client: AsyncPipeline) -> None:
        async with async_client.github.with_streaming_response.list_repositories(
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            github = await response.parse()
            assert_matches_type(GitHubListRepositoriesResponse, github, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_setup_callback(self, async_client: AsyncPipeline) -> None:
        github = await async_client.github.setup_callback(
            installation_id=0,
        )
        assert github is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_setup_callback_with_all_params(self, async_client: AsyncPipeline) -> None:
        github = await async_client.github.setup_callback(
            installation_id=0,
            setup_action="install",
            state="state",
        )
        assert github is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_setup_callback(self, async_client: AsyncPipeline) -> None:
        response = await async_client.github.with_raw_response.setup_callback(
            installation_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        github = await response.parse()
        assert github is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_setup_callback(self, async_client: AsyncPipeline) -> None:
        async with async_client.github.with_streaming_response.setup_callback(
            installation_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            github = await response.parse()
            assert github is None

        assert cast(Any, response.is_closed) is True
