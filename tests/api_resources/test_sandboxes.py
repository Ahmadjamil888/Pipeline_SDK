# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pipeline import Pipeline, AsyncPipeline
from tests.utils import assert_matches_type
from pipeline.types import (
    Sandbox,
    SandboxListResponse,
    SandboxStopResponse,
    SandboxStartResponse,
    SandboxExecuteResponse,
    SandboxGetLogsResponse,
    SandboxOpenTerminalResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSandboxes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Pipeline) -> None:
        sandbox = client.sandboxes.create()
        assert_matches_type(Sandbox, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Pipeline) -> None:
        sandbox = client.sandboxes.create(
            branch="branch",
            environment_variables={"foo": "string"},
            repo_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            repo_url="https://example.com",
            resources={
                "cpu_cores": 0,
                "disk_gb": 0,
                "memory_mb": 0,
            },
        )
        assert_matches_type(Sandbox, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Pipeline) -> None:
        response = client.sandboxes.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = response.parse()
        assert_matches_type(Sandbox, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Pipeline) -> None:
        with client.sandboxes.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = response.parse()
            assert_matches_type(Sandbox, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Pipeline) -> None:
        sandbox = client.sandboxes.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Sandbox, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Pipeline) -> None:
        response = client.sandboxes.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = response.parse()
        assert_matches_type(Sandbox, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Pipeline) -> None:
        with client.sandboxes.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = response.parse()
            assert_matches_type(Sandbox, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Pipeline) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sandbox_id` but received ''"):
            client.sandboxes.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Pipeline) -> None:
        sandbox = client.sandboxes.list()
        assert_matches_type(SandboxListResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Pipeline) -> None:
        sandbox = client.sandboxes.list(
            limit=0,
            status="creating",
        )
        assert_matches_type(SandboxListResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Pipeline) -> None:
        response = client.sandboxes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = response.parse()
        assert_matches_type(SandboxListResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Pipeline) -> None:
        with client.sandboxes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = response.parse()
            assert_matches_type(SandboxListResponse, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Pipeline) -> None:
        sandbox = client.sandboxes.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert sandbox is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Pipeline) -> None:
        response = client.sandboxes.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = response.parse()
        assert sandbox is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Pipeline) -> None:
        with client.sandboxes.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = response.parse()
            assert sandbox is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Pipeline) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sandbox_id` but received ''"):
            client.sandboxes.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_execute(self, client: Pipeline) -> None:
        sandbox = client.sandboxes.execute(
            sandbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            command="command",
        )
        assert_matches_type(SandboxExecuteResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_execute_with_all_params(self, client: Pipeline) -> None:
        sandbox = client.sandboxes.execute(
            sandbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            command="command",
            env_variables={"foo": "string"},
            timeout_seconds=0,
            working_directory="working_directory",
        )
        assert_matches_type(SandboxExecuteResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_execute(self, client: Pipeline) -> None:
        response = client.sandboxes.with_raw_response.execute(
            sandbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            command="command",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = response.parse()
        assert_matches_type(SandboxExecuteResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_execute(self, client: Pipeline) -> None:
        with client.sandboxes.with_streaming_response.execute(
            sandbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            command="command",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = response.parse()
            assert_matches_type(SandboxExecuteResponse, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_execute(self, client: Pipeline) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sandbox_id` but received ''"):
            client.sandboxes.with_raw_response.execute(
                sandbox_id="",
                command="command",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_logs(self, client: Pipeline) -> None:
        sandbox = client.sandboxes.get_logs(
            sandbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SandboxGetLogsResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_logs_with_all_params(self, client: Pipeline) -> None:
        sandbox = client.sandboxes.get_logs(
            sandbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tail=0,
        )
        assert_matches_type(SandboxGetLogsResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_logs(self, client: Pipeline) -> None:
        response = client.sandboxes.with_raw_response.get_logs(
            sandbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = response.parse()
        assert_matches_type(SandboxGetLogsResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_logs(self, client: Pipeline) -> None:
        with client.sandboxes.with_streaming_response.get_logs(
            sandbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = response.parse()
            assert_matches_type(SandboxGetLogsResponse, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_logs(self, client: Pipeline) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sandbox_id` but received ''"):
            client.sandboxes.with_raw_response.get_logs(
                sandbox_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_open_terminal(self, client: Pipeline) -> None:
        sandbox = client.sandboxes.open_terminal(
            sandbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SandboxOpenTerminalResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_open_terminal_with_all_params(self, client: Pipeline) -> None:
        sandbox = client.sandboxes.open_terminal(
            sandbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            environment_variables={"foo": "string"},
            shell="shell",
            working_directory="working_directory",
        )
        assert_matches_type(SandboxOpenTerminalResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_open_terminal(self, client: Pipeline) -> None:
        response = client.sandboxes.with_raw_response.open_terminal(
            sandbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = response.parse()
        assert_matches_type(SandboxOpenTerminalResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_open_terminal(self, client: Pipeline) -> None:
        with client.sandboxes.with_streaming_response.open_terminal(
            sandbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = response.parse()
            assert_matches_type(SandboxOpenTerminalResponse, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_open_terminal(self, client: Pipeline) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sandbox_id` but received ''"):
            client.sandboxes.with_raw_response.open_terminal(
                sandbox_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_start(self, client: Pipeline) -> None:
        sandbox = client.sandboxes.start(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SandboxStartResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_start(self, client: Pipeline) -> None:
        response = client.sandboxes.with_raw_response.start(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = response.parse()
        assert_matches_type(SandboxStartResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_start(self, client: Pipeline) -> None:
        with client.sandboxes.with_streaming_response.start(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = response.parse()
            assert_matches_type(SandboxStartResponse, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_start(self, client: Pipeline) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sandbox_id` but received ''"):
            client.sandboxes.with_raw_response.start(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stop(self, client: Pipeline) -> None:
        sandbox = client.sandboxes.stop(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SandboxStopResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stop(self, client: Pipeline) -> None:
        response = client.sandboxes.with_raw_response.stop(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = response.parse()
        assert_matches_type(SandboxStopResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stop(self, client: Pipeline) -> None:
        with client.sandboxes.with_streaming_response.stop(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = response.parse()
            assert_matches_type(SandboxStopResponse, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_stop(self, client: Pipeline) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sandbox_id` but received ''"):
            client.sandboxes.with_raw_response.stop(
                "",
            )


class TestAsyncSandboxes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncPipeline) -> None:
        sandbox = await async_client.sandboxes.create()
        assert_matches_type(Sandbox, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPipeline) -> None:
        sandbox = await async_client.sandboxes.create(
            branch="branch",
            environment_variables={"foo": "string"},
            repo_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            repo_url="https://example.com",
            resources={
                "cpu_cores": 0,
                "disk_gb": 0,
                "memory_mb": 0,
            },
        )
        assert_matches_type(Sandbox, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPipeline) -> None:
        response = await async_client.sandboxes.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = await response.parse()
        assert_matches_type(Sandbox, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPipeline) -> None:
        async with async_client.sandboxes.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = await response.parse()
            assert_matches_type(Sandbox, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPipeline) -> None:
        sandbox = await async_client.sandboxes.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Sandbox, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPipeline) -> None:
        response = await async_client.sandboxes.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = await response.parse()
        assert_matches_type(Sandbox, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPipeline) -> None:
        async with async_client.sandboxes.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = await response.parse()
            assert_matches_type(Sandbox, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPipeline) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sandbox_id` but received ''"):
            await async_client.sandboxes.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPipeline) -> None:
        sandbox = await async_client.sandboxes.list()
        assert_matches_type(SandboxListResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPipeline) -> None:
        sandbox = await async_client.sandboxes.list(
            limit=0,
            status="creating",
        )
        assert_matches_type(SandboxListResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPipeline) -> None:
        response = await async_client.sandboxes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = await response.parse()
        assert_matches_type(SandboxListResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPipeline) -> None:
        async with async_client.sandboxes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = await response.parse()
            assert_matches_type(SandboxListResponse, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncPipeline) -> None:
        sandbox = await async_client.sandboxes.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert sandbox is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPipeline) -> None:
        response = await async_client.sandboxes.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = await response.parse()
        assert sandbox is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPipeline) -> None:
        async with async_client.sandboxes.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = await response.parse()
            assert sandbox is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPipeline) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sandbox_id` but received ''"):
            await async_client.sandboxes.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_execute(self, async_client: AsyncPipeline) -> None:
        sandbox = await async_client.sandboxes.execute(
            sandbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            command="command",
        )
        assert_matches_type(SandboxExecuteResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_execute_with_all_params(self, async_client: AsyncPipeline) -> None:
        sandbox = await async_client.sandboxes.execute(
            sandbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            command="command",
            env_variables={"foo": "string"},
            timeout_seconds=0,
            working_directory="working_directory",
        )
        assert_matches_type(SandboxExecuteResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_execute(self, async_client: AsyncPipeline) -> None:
        response = await async_client.sandboxes.with_raw_response.execute(
            sandbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            command="command",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = await response.parse()
        assert_matches_type(SandboxExecuteResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_execute(self, async_client: AsyncPipeline) -> None:
        async with async_client.sandboxes.with_streaming_response.execute(
            sandbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            command="command",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = await response.parse()
            assert_matches_type(SandboxExecuteResponse, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_execute(self, async_client: AsyncPipeline) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sandbox_id` but received ''"):
            await async_client.sandboxes.with_raw_response.execute(
                sandbox_id="",
                command="command",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_logs(self, async_client: AsyncPipeline) -> None:
        sandbox = await async_client.sandboxes.get_logs(
            sandbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SandboxGetLogsResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_logs_with_all_params(self, async_client: AsyncPipeline) -> None:
        sandbox = await async_client.sandboxes.get_logs(
            sandbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tail=0,
        )
        assert_matches_type(SandboxGetLogsResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_logs(self, async_client: AsyncPipeline) -> None:
        response = await async_client.sandboxes.with_raw_response.get_logs(
            sandbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = await response.parse()
        assert_matches_type(SandboxGetLogsResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_logs(self, async_client: AsyncPipeline) -> None:
        async with async_client.sandboxes.with_streaming_response.get_logs(
            sandbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = await response.parse()
            assert_matches_type(SandboxGetLogsResponse, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_logs(self, async_client: AsyncPipeline) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sandbox_id` but received ''"):
            await async_client.sandboxes.with_raw_response.get_logs(
                sandbox_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_open_terminal(self, async_client: AsyncPipeline) -> None:
        sandbox = await async_client.sandboxes.open_terminal(
            sandbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SandboxOpenTerminalResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_open_terminal_with_all_params(self, async_client: AsyncPipeline) -> None:
        sandbox = await async_client.sandboxes.open_terminal(
            sandbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            environment_variables={"foo": "string"},
            shell="shell",
            working_directory="working_directory",
        )
        assert_matches_type(SandboxOpenTerminalResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_open_terminal(self, async_client: AsyncPipeline) -> None:
        response = await async_client.sandboxes.with_raw_response.open_terminal(
            sandbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = await response.parse()
        assert_matches_type(SandboxOpenTerminalResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_open_terminal(self, async_client: AsyncPipeline) -> None:
        async with async_client.sandboxes.with_streaming_response.open_terminal(
            sandbox_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = await response.parse()
            assert_matches_type(SandboxOpenTerminalResponse, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_open_terminal(self, async_client: AsyncPipeline) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sandbox_id` but received ''"):
            await async_client.sandboxes.with_raw_response.open_terminal(
                sandbox_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_start(self, async_client: AsyncPipeline) -> None:
        sandbox = await async_client.sandboxes.start(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SandboxStartResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_start(self, async_client: AsyncPipeline) -> None:
        response = await async_client.sandboxes.with_raw_response.start(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = await response.parse()
        assert_matches_type(SandboxStartResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_start(self, async_client: AsyncPipeline) -> None:
        async with async_client.sandboxes.with_streaming_response.start(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = await response.parse()
            assert_matches_type(SandboxStartResponse, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_start(self, async_client: AsyncPipeline) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sandbox_id` but received ''"):
            await async_client.sandboxes.with_raw_response.start(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stop(self, async_client: AsyncPipeline) -> None:
        sandbox = await async_client.sandboxes.stop(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SandboxStopResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stop(self, async_client: AsyncPipeline) -> None:
        response = await async_client.sandboxes.with_raw_response.stop(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = await response.parse()
        assert_matches_type(SandboxStopResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stop(self, async_client: AsyncPipeline) -> None:
        async with async_client.sandboxes.with_streaming_response.stop(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = await response.parse()
            assert_matches_type(SandboxStopResponse, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_stop(self, async_client: AsyncPipeline) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sandbox_id` but received ''"):
            await async_client.sandboxes.with_raw_response.stop(
                "",
            )
