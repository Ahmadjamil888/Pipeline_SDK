# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from pipeline import Pipeline, AsyncPipeline
from tests.utils import assert_matches_type
from pipeline.types import (
    BillingListPlansResponse,
    BillingHandleWebhookResponse,
    BillingCancelSubscriptionResponse,
    BillingCreatePortalSessionResponse,
    BillingCreateCheckoutSessionResponse,
    BillingRetrieveSubscriptionStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBilling:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel_subscription(self, client: Pipeline) -> None:
        billing = client.billing.cancel_subscription(
            subscription_id="subscription_id",
        )
        assert_matches_type(BillingCancelSubscriptionResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_cancel_subscription(self, client: Pipeline) -> None:
        response = client.billing.with_raw_response.cancel_subscription(
            subscription_id="subscription_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert_matches_type(BillingCancelSubscriptionResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_cancel_subscription(self, client: Pipeline) -> None:
        with client.billing.with_streaming_response.cancel_subscription(
            subscription_id="subscription_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert_matches_type(BillingCancelSubscriptionResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_checkout_session(self, client: Pipeline) -> None:
        billing = client.billing.create_checkout_session(
            cancel_url="https://example.com",
            plan_id="pro",
            success_url="https://example.com",
            user_id="user_id",
        )
        assert_matches_type(BillingCreateCheckoutSessionResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_checkout_session(self, client: Pipeline) -> None:
        response = client.billing.with_raw_response.create_checkout_session(
            cancel_url="https://example.com",
            plan_id="pro",
            success_url="https://example.com",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert_matches_type(BillingCreateCheckoutSessionResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_checkout_session(self, client: Pipeline) -> None:
        with client.billing.with_streaming_response.create_checkout_session(
            cancel_url="https://example.com",
            plan_id="pro",
            success_url="https://example.com",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert_matches_type(BillingCreateCheckoutSessionResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_portal_session(self, client: Pipeline) -> None:
        billing = client.billing.create_portal_session(
            customer_id="customer_id",
            return_url="https://example.com",
        )
        assert_matches_type(BillingCreatePortalSessionResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_portal_session(self, client: Pipeline) -> None:
        response = client.billing.with_raw_response.create_portal_session(
            customer_id="customer_id",
            return_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert_matches_type(BillingCreatePortalSessionResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_portal_session(self, client: Pipeline) -> None:
        with client.billing.with_streaming_response.create_portal_session(
            customer_id="customer_id",
            return_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert_matches_type(BillingCreatePortalSessionResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_handle_webhook(self, client: Pipeline) -> None:
        billing = client.billing.handle_webhook(
            body={},
        )
        assert_matches_type(BillingHandleWebhookResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_handle_webhook(self, client: Pipeline) -> None:
        response = client.billing.with_raw_response.handle_webhook(
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert_matches_type(BillingHandleWebhookResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_handle_webhook(self, client: Pipeline) -> None:
        with client.billing.with_streaming_response.handle_webhook(
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert_matches_type(BillingHandleWebhookResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_plans(self, client: Pipeline) -> None:
        billing = client.billing.list_plans()
        assert_matches_type(BillingListPlansResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_plans(self, client: Pipeline) -> None:
        response = client.billing.with_raw_response.list_plans()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert_matches_type(BillingListPlansResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_plans(self, client: Pipeline) -> None:
        with client.billing.with_streaming_response.list_plans() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert_matches_type(BillingListPlansResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_subscription_status(self, client: Pipeline) -> None:
        billing = client.billing.retrieve_subscription_status(
            "user_id",
        )
        assert_matches_type(BillingRetrieveSubscriptionStatusResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_subscription_status(self, client: Pipeline) -> None:
        response = client.billing.with_raw_response.retrieve_subscription_status(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert_matches_type(BillingRetrieveSubscriptionStatusResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_subscription_status(self, client: Pipeline) -> None:
        with client.billing.with_streaming_response.retrieve_subscription_status(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert_matches_type(BillingRetrieveSubscriptionStatusResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_subscription_status(self, client: Pipeline) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.billing.with_raw_response.retrieve_subscription_status(
                "",
            )


class TestAsyncBilling:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel_subscription(self, async_client: AsyncPipeline) -> None:
        billing = await async_client.billing.cancel_subscription(
            subscription_id="subscription_id",
        )
        assert_matches_type(BillingCancelSubscriptionResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_cancel_subscription(self, async_client: AsyncPipeline) -> None:
        response = await async_client.billing.with_raw_response.cancel_subscription(
            subscription_id="subscription_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert_matches_type(BillingCancelSubscriptionResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_cancel_subscription(self, async_client: AsyncPipeline) -> None:
        async with async_client.billing.with_streaming_response.cancel_subscription(
            subscription_id="subscription_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert_matches_type(BillingCancelSubscriptionResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_checkout_session(self, async_client: AsyncPipeline) -> None:
        billing = await async_client.billing.create_checkout_session(
            cancel_url="https://example.com",
            plan_id="pro",
            success_url="https://example.com",
            user_id="user_id",
        )
        assert_matches_type(BillingCreateCheckoutSessionResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_checkout_session(self, async_client: AsyncPipeline) -> None:
        response = await async_client.billing.with_raw_response.create_checkout_session(
            cancel_url="https://example.com",
            plan_id="pro",
            success_url="https://example.com",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert_matches_type(BillingCreateCheckoutSessionResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_checkout_session(self, async_client: AsyncPipeline) -> None:
        async with async_client.billing.with_streaming_response.create_checkout_session(
            cancel_url="https://example.com",
            plan_id="pro",
            success_url="https://example.com",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert_matches_type(BillingCreateCheckoutSessionResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_portal_session(self, async_client: AsyncPipeline) -> None:
        billing = await async_client.billing.create_portal_session(
            customer_id="customer_id",
            return_url="https://example.com",
        )
        assert_matches_type(BillingCreatePortalSessionResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_portal_session(self, async_client: AsyncPipeline) -> None:
        response = await async_client.billing.with_raw_response.create_portal_session(
            customer_id="customer_id",
            return_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert_matches_type(BillingCreatePortalSessionResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_portal_session(self, async_client: AsyncPipeline) -> None:
        async with async_client.billing.with_streaming_response.create_portal_session(
            customer_id="customer_id",
            return_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert_matches_type(BillingCreatePortalSessionResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_handle_webhook(self, async_client: AsyncPipeline) -> None:
        billing = await async_client.billing.handle_webhook(
            body={},
        )
        assert_matches_type(BillingHandleWebhookResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_handle_webhook(self, async_client: AsyncPipeline) -> None:
        response = await async_client.billing.with_raw_response.handle_webhook(
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert_matches_type(BillingHandleWebhookResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_handle_webhook(self, async_client: AsyncPipeline) -> None:
        async with async_client.billing.with_streaming_response.handle_webhook(
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert_matches_type(BillingHandleWebhookResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_plans(self, async_client: AsyncPipeline) -> None:
        billing = await async_client.billing.list_plans()
        assert_matches_type(BillingListPlansResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_plans(self, async_client: AsyncPipeline) -> None:
        response = await async_client.billing.with_raw_response.list_plans()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert_matches_type(BillingListPlansResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_plans(self, async_client: AsyncPipeline) -> None:
        async with async_client.billing.with_streaming_response.list_plans() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert_matches_type(BillingListPlansResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_subscription_status(self, async_client: AsyncPipeline) -> None:
        billing = await async_client.billing.retrieve_subscription_status(
            "user_id",
        )
        assert_matches_type(BillingRetrieveSubscriptionStatusResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_subscription_status(self, async_client: AsyncPipeline) -> None:
        response = await async_client.billing.with_raw_response.retrieve_subscription_status(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert_matches_type(BillingRetrieveSubscriptionStatusResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_subscription_status(self, async_client: AsyncPipeline) -> None:
        async with async_client.billing.with_streaming_response.retrieve_subscription_status(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert_matches_type(BillingRetrieveSubscriptionStatusResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_subscription_status(self, async_client: AsyncPipeline) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.billing.with_raw_response.retrieve_subscription_status(
                "",
            )
