# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from pipeline_labs import Pipeline, AsyncPipeline
from pipeline_labs._utils import parse_datetime
from pipeline_labs.types.github import (
    RepoListResponse,
    RepoConnectResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRepos:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Pipeline) -> None:
        repo = client.github.repos.list(
            user_id="user_id",
        )
        assert_matches_type(RepoListResponse, repo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Pipeline) -> None:
        response = client.github.repos.with_raw_response.list(
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        repo = response.parse()
        assert_matches_type(RepoListResponse, repo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Pipeline) -> None:
        with client.github.repos.with_streaming_response.list(
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            repo = response.parse()
            assert_matches_type(RepoListResponse, repo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_connect(self, client: Pipeline) -> None:
        repo = client.github.repos.connect(
            repo={},
            user_id="user_id",
        )
        assert_matches_type(RepoConnectResponse, repo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_connect_with_all_params(self, client: Pipeline) -> None:
        repo = client.github.repos.connect(
            repo={
                "id": 0,
                "clone_url": "clone_url",
                "default_branch": "default_branch",
                "description": "description",
                "full_name": "full_name",
                "language": "language",
                "name": "name",
                "private": True,
                "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "url": "https://example.com",
            },
            user_id="user_id",
        )
        assert_matches_type(RepoConnectResponse, repo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_connect(self, client: Pipeline) -> None:
        response = client.github.repos.with_raw_response.connect(
            repo={},
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        repo = response.parse()
        assert_matches_type(RepoConnectResponse, repo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_connect(self, client: Pipeline) -> None:
        with client.github.repos.with_streaming_response.connect(
            repo={},
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            repo = response.parse()
            assert_matches_type(RepoConnectResponse, repo, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRepos:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPipeline) -> None:
        repo = await async_client.github.repos.list(
            user_id="user_id",
        )
        assert_matches_type(RepoListResponse, repo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPipeline) -> None:
        response = await async_client.github.repos.with_raw_response.list(
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        repo = await response.parse()
        assert_matches_type(RepoListResponse, repo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPipeline) -> None:
        async with async_client.github.repos.with_streaming_response.list(
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            repo = await response.parse()
            assert_matches_type(RepoListResponse, repo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_connect(self, async_client: AsyncPipeline) -> None:
        repo = await async_client.github.repos.connect(
            repo={},
            user_id="user_id",
        )
        assert_matches_type(RepoConnectResponse, repo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_connect_with_all_params(self, async_client: AsyncPipeline) -> None:
        repo = await async_client.github.repos.connect(
            repo={
                "id": 0,
                "clone_url": "clone_url",
                "default_branch": "default_branch",
                "description": "description",
                "full_name": "full_name",
                "language": "language",
                "name": "name",
                "private": True,
                "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "url": "https://example.com",
            },
            user_id="user_id",
        )
        assert_matches_type(RepoConnectResponse, repo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_connect(self, async_client: AsyncPipeline) -> None:
        response = await async_client.github.repos.with_raw_response.connect(
            repo={},
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        repo = await response.parse()
        assert_matches_type(RepoConnectResponse, repo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_connect(self, async_client: AsyncPipeline) -> None:
        async with async_client.github.repos.with_streaming_response.connect(
            repo={},
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            repo = await response.parse()
            assert_matches_type(RepoConnectResponse, repo, path=["response"])

        assert cast(Any, response.is_closed) is True
