# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from pipeline_labs import Pipeline, AsyncPipeline
from pipeline_labs.types import WebhookHandleGitHubResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_handle_github(self, client: Pipeline) -> None:
        webhook = client.webhooks.handle_github()
        assert_matches_type(WebhookHandleGitHubResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_handle_github_with_all_params(self, client: Pipeline) -> None:
        webhook = client.webhooks.handle_github(
            action="created",
            installation={
                "id": 0,
                "account": {
                    "id": 0,
                    "login": "login",
                },
            },
            repository={
                "id": 0,
                "clone_url": "clone_url",
                "default_branch": "default_branch",
                "full_name": "full_name",
                "name": "name",
            },
            sender={
                "id": 0,
                "login": "login",
            },
        )
        assert_matches_type(WebhookHandleGitHubResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_handle_github(self, client: Pipeline) -> None:
        response = client.webhooks.with_raw_response.handle_github()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookHandleGitHubResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_handle_github(self, client: Pipeline) -> None:
        with client.webhooks.with_streaming_response.handle_github() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookHandleGitHubResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_handle_github(self, async_client: AsyncPipeline) -> None:
        webhook = await async_client.webhooks.handle_github()
        assert_matches_type(WebhookHandleGitHubResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_handle_github_with_all_params(self, async_client: AsyncPipeline) -> None:
        webhook = await async_client.webhooks.handle_github(
            action="created",
            installation={
                "id": 0,
                "account": {
                    "id": 0,
                    "login": "login",
                },
            },
            repository={
                "id": 0,
                "clone_url": "clone_url",
                "default_branch": "default_branch",
                "full_name": "full_name",
                "name": "name",
            },
            sender={
                "id": 0,
                "login": "login",
            },
        )
        assert_matches_type(WebhookHandleGitHubResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_handle_github(self, async_client: AsyncPipeline) -> None:
        response = await async_client.webhooks.with_raw_response.handle_github()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookHandleGitHubResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_handle_github(self, async_client: AsyncPipeline) -> None:
        async with async_client.webhooks.with_streaming_response.handle_github() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookHandleGitHubResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True
