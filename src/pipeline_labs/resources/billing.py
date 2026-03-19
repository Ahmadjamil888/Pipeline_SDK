# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import (
    billing_handle_webhook_params,
    billing_cancel_subscription_params,
    billing_create_portal_session_params,
    billing_create_checkout_session_params,
)
from .._types import Body, Query, Headers, NotGiven, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.billing_list_plans_response import BillingListPlansResponse
from ..types.billing_handle_webhook_response import BillingHandleWebhookResponse
from ..types.billing_cancel_subscription_response import BillingCancelSubscriptionResponse
from ..types.billing_create_portal_session_response import BillingCreatePortalSessionResponse
from ..types.billing_create_checkout_session_response import BillingCreateCheckoutSessionResponse
from ..types.billing_retrieve_subscription_status_response import BillingRetrieveSubscriptionStatusResponse

__all__ = ["BillingResource", "AsyncBillingResource"]


class BillingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BillingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Ahmadjamil888/Pipeline_SDK#accessing-raw-response-data-eg-headers
        """
        return BillingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BillingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Ahmadjamil888/Pipeline_SDK#with_streaming_response
        """
        return BillingResourceWithStreamingResponse(self)

    def cancel_subscription(
        self,
        *,
        subscription_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingCancelSubscriptionResponse:
        """
        Cancel user subscription

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/billing/cancel-subscription",
            body=maybe_transform(
                {"subscription_id": subscription_id}, billing_cancel_subscription_params.BillingCancelSubscriptionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingCancelSubscriptionResponse,
        )

    def create_checkout_session(
        self,
        *,
        cancel_url: str,
        plan_id: Literal["pro", "team"],
        success_url: str,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingCreateCheckoutSessionResponse:
        """
        Create Polar checkout session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/billing/checkout",
            body=maybe_transform(
                {
                    "cancel_url": cancel_url,
                    "plan_id": plan_id,
                    "success_url": success_url,
                    "user_id": user_id,
                },
                billing_create_checkout_session_params.BillingCreateCheckoutSessionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingCreateCheckoutSessionResponse,
        )

    def create_portal_session(
        self,
        *,
        customer_id: str,
        return_url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingCreatePortalSessionResponse:
        """
        Create billing portal session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/billing/portal-session",
            body=maybe_transform(
                {
                    "customer_id": customer_id,
                    "return_url": return_url,
                },
                billing_create_portal_session_params.BillingCreatePortalSessionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingCreatePortalSessionResponse,
        )

    def handle_webhook(
        self,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingHandleWebhookResponse:
        """
        Polar webhook handler

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/billing/webhook",
            body=maybe_transform(body, billing_handle_webhook_params.BillingHandleWebhookParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingHandleWebhookResponse,
        )

    def list_plans(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingListPlansResponse:
        """Get available subscription plans"""
        return self._get(
            "/billing/plans",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingListPlansResponse,
        )

    def retrieve_subscription_status(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingRetrieveSubscriptionStatusResponse:
        """
        Get user subscription status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            f"/billing/subscription/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingRetrieveSubscriptionStatusResponse,
        )


class AsyncBillingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBillingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Ahmadjamil888/Pipeline_SDK#accessing-raw-response-data-eg-headers
        """
        return AsyncBillingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBillingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Ahmadjamil888/Pipeline_SDK#with_streaming_response
        """
        return AsyncBillingResourceWithStreamingResponse(self)

    async def cancel_subscription(
        self,
        *,
        subscription_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingCancelSubscriptionResponse:
        """
        Cancel user subscription

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/billing/cancel-subscription",
            body=await async_maybe_transform(
                {"subscription_id": subscription_id}, billing_cancel_subscription_params.BillingCancelSubscriptionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingCancelSubscriptionResponse,
        )

    async def create_checkout_session(
        self,
        *,
        cancel_url: str,
        plan_id: Literal["pro", "team"],
        success_url: str,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingCreateCheckoutSessionResponse:
        """
        Create Polar checkout session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/billing/checkout",
            body=await async_maybe_transform(
                {
                    "cancel_url": cancel_url,
                    "plan_id": plan_id,
                    "success_url": success_url,
                    "user_id": user_id,
                },
                billing_create_checkout_session_params.BillingCreateCheckoutSessionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingCreateCheckoutSessionResponse,
        )

    async def create_portal_session(
        self,
        *,
        customer_id: str,
        return_url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingCreatePortalSessionResponse:
        """
        Create billing portal session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/billing/portal-session",
            body=await async_maybe_transform(
                {
                    "customer_id": customer_id,
                    "return_url": return_url,
                },
                billing_create_portal_session_params.BillingCreatePortalSessionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingCreatePortalSessionResponse,
        )

    async def handle_webhook(
        self,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingHandleWebhookResponse:
        """
        Polar webhook handler

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/billing/webhook",
            body=await async_maybe_transform(body, billing_handle_webhook_params.BillingHandleWebhookParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingHandleWebhookResponse,
        )

    async def list_plans(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingListPlansResponse:
        """Get available subscription plans"""
        return await self._get(
            "/billing/plans",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingListPlansResponse,
        )

    async def retrieve_subscription_status(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingRetrieveSubscriptionStatusResponse:
        """
        Get user subscription status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            f"/billing/subscription/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingRetrieveSubscriptionStatusResponse,
        )


class BillingResourceWithRawResponse:
    def __init__(self, billing: BillingResource) -> None:
        self._billing = billing

        self.cancel_subscription = to_raw_response_wrapper(
            billing.cancel_subscription,
        )
        self.create_checkout_session = to_raw_response_wrapper(
            billing.create_checkout_session,
        )
        self.create_portal_session = to_raw_response_wrapper(
            billing.create_portal_session,
        )
        self.handle_webhook = to_raw_response_wrapper(
            billing.handle_webhook,
        )
        self.list_plans = to_raw_response_wrapper(
            billing.list_plans,
        )
        self.retrieve_subscription_status = to_raw_response_wrapper(
            billing.retrieve_subscription_status,
        )


class AsyncBillingResourceWithRawResponse:
    def __init__(self, billing: AsyncBillingResource) -> None:
        self._billing = billing

        self.cancel_subscription = async_to_raw_response_wrapper(
            billing.cancel_subscription,
        )
        self.create_checkout_session = async_to_raw_response_wrapper(
            billing.create_checkout_session,
        )
        self.create_portal_session = async_to_raw_response_wrapper(
            billing.create_portal_session,
        )
        self.handle_webhook = async_to_raw_response_wrapper(
            billing.handle_webhook,
        )
        self.list_plans = async_to_raw_response_wrapper(
            billing.list_plans,
        )
        self.retrieve_subscription_status = async_to_raw_response_wrapper(
            billing.retrieve_subscription_status,
        )


class BillingResourceWithStreamingResponse:
    def __init__(self, billing: BillingResource) -> None:
        self._billing = billing

        self.cancel_subscription = to_streamed_response_wrapper(
            billing.cancel_subscription,
        )
        self.create_checkout_session = to_streamed_response_wrapper(
            billing.create_checkout_session,
        )
        self.create_portal_session = to_streamed_response_wrapper(
            billing.create_portal_session,
        )
        self.handle_webhook = to_streamed_response_wrapper(
            billing.handle_webhook,
        )
        self.list_plans = to_streamed_response_wrapper(
            billing.list_plans,
        )
        self.retrieve_subscription_status = to_streamed_response_wrapper(
            billing.retrieve_subscription_status,
        )


class AsyncBillingResourceWithStreamingResponse:
    def __init__(self, billing: AsyncBillingResource) -> None:
        self._billing = billing

        self.cancel_subscription = async_to_streamed_response_wrapper(
            billing.cancel_subscription,
        )
        self.create_checkout_session = async_to_streamed_response_wrapper(
            billing.create_checkout_session,
        )
        self.create_portal_session = async_to_streamed_response_wrapper(
            billing.create_portal_session,
        )
        self.handle_webhook = async_to_streamed_response_wrapper(
            billing.handle_webhook,
        )
        self.list_plans = async_to_streamed_response_wrapper(
            billing.list_plans,
        )
        self.retrieve_subscription_status = async_to_streamed_response_wrapper(
            billing.retrieve_subscription_status,
        )
