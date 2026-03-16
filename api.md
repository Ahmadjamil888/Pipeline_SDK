# Repos

Types:

```python
from pipeline.types import RepoConnection, RepoAnalyzeResponse
```

Methods:

- <code title="get /repos/{repo_id}">client.repos.<a href="./src/pipeline/resources/repos.py">retrieve</a>(repo_id) -> <a href="./src/pipeline/types/repo_connection.py">RepoConnection</a></code>
- <code title="post /repos/{repo_id}/analyze">client.repos.<a href="./src/pipeline/resources/repos.py">analyze</a>(repo_id) -> <a href="./src/pipeline/types/repo_analyze_response.py">RepoAnalyzeResponse</a></code>
- <code title="post /repos/connect">client.repos.<a href="./src/pipeline/resources/repos.py">connect</a>(\*\*<a href="src/pipeline/types/repo_connect_params.py">params</a>) -> <a href="./src/pipeline/types/repo_connection.py">RepoConnection</a></code>

# Deployments

Types:

```python
from pipeline.types import (
    DeploymentExecution,
    DeploymentStatus,
    LogEntry,
    DeploymentCreateResponse,
    DeploymentListResponse,
    DeploymentGetLogsResponse,
)
```

Methods:

- <code title="post /deployments">client.deployments.<a href="./src/pipeline/resources/deployments.py">create</a>(\*\*<a href="src/pipeline/types/deployment_create_params.py">params</a>) -> <a href="./src/pipeline/types/deployment_create_response.py">DeploymentCreateResponse</a></code>
- <code title="get /deployments/{deployment_id}">client.deployments.<a href="./src/pipeline/resources/deployments.py">retrieve</a>(deployment_id) -> <a href="./src/pipeline/types/deployment_status.py">DeploymentStatus</a></code>
- <code title="get /deployments">client.deployments.<a href="./src/pipeline/resources/deployments.py">list</a>(\*\*<a href="src/pipeline/types/deployment_list_params.py">params</a>) -> <a href="./src/pipeline/types/deployment_list_response.py">DeploymentListResponse</a></code>
- <code title="post /deployments/{deployment_id}/cancel">client.deployments.<a href="./src/pipeline/resources/deployments.py">cancel</a>(deployment_id) -> None</code>
- <code title="post /deployments/{deployment_id}/run">client.deployments.<a href="./src/pipeline/resources/deployments.py">execute</a>(deployment_id) -> <a href="./src/pipeline/types/deployment_execution.py">DeploymentExecution</a></code>
- <code title="get /deployments/{deployment_id}/logs">client.deployments.<a href="./src/pipeline/resources/deployments.py">get_logs</a>(deployment_id, \*\*<a href="src/pipeline/types/deployment_get_logs_params.py">params</a>) -> <a href="./src/pipeline/types/deployment_get_logs_response.py">DeploymentGetLogsResponse</a></code>
- <code title="post /deployments/{deployment_id}/retry">client.deployments.<a href="./src/pipeline/resources/deployments.py">retry</a>(deployment_id) -> <a href="./src/pipeline/types/deployment_execution.py">DeploymentExecution</a></code>

# Sandboxes

Types:

```python
from pipeline.types import (
    Sandbox,
    SandboxResources,
    SandboxListResponse,
    SandboxExecuteResponse,
    SandboxGetLogsResponse,
    SandboxOpenTerminalResponse,
    SandboxStartResponse,
    SandboxStopResponse,
)
```

Methods:

- <code title="post /sandboxes">client.sandboxes.<a href="./src/pipeline/resources/sandboxes.py">create</a>(\*\*<a href="src/pipeline/types/sandbox_create_params.py">params</a>) -> <a href="./src/pipeline/types/sandbox.py">Sandbox</a></code>
- <code title="get /sandboxes/{sandbox_id}">client.sandboxes.<a href="./src/pipeline/resources/sandboxes.py">retrieve</a>(sandbox_id) -> <a href="./src/pipeline/types/sandbox.py">Sandbox</a></code>
- <code title="get /sandboxes">client.sandboxes.<a href="./src/pipeline/resources/sandboxes.py">list</a>(\*\*<a href="src/pipeline/types/sandbox_list_params.py">params</a>) -> <a href="./src/pipeline/types/sandbox_list_response.py">SandboxListResponse</a></code>
- <code title="delete /sandboxes/{sandbox_id}">client.sandboxes.<a href="./src/pipeline/resources/sandboxes.py">delete</a>(sandbox_id) -> None</code>
- <code title="post /sandboxes/{sandbox_id}/execute">client.sandboxes.<a href="./src/pipeline/resources/sandboxes.py">execute</a>(sandbox_id, \*\*<a href="src/pipeline/types/sandbox_execute_params.py">params</a>) -> <a href="./src/pipeline/types/sandbox_execute_response.py">SandboxExecuteResponse</a></code>
- <code title="get /sandboxes/{sandbox_id}/logs">client.sandboxes.<a href="./src/pipeline/resources/sandboxes.py">get_logs</a>(sandbox_id, \*\*<a href="src/pipeline/types/sandbox_get_logs_params.py">params</a>) -> <a href="./src/pipeline/types/sandbox_get_logs_response.py">SandboxGetLogsResponse</a></code>
- <code title="post /sandboxes/{sandbox_id}/terminal">client.sandboxes.<a href="./src/pipeline/resources/sandboxes.py">open_terminal</a>(sandbox_id, \*\*<a href="src/pipeline/types/sandbox_open_terminal_params.py">params</a>) -> <a href="./src/pipeline/types/sandbox_open_terminal_response.py">SandboxOpenTerminalResponse</a></code>
- <code title="post /sandboxes/{sandbox_id}/start">client.sandboxes.<a href="./src/pipeline/resources/sandboxes.py">start</a>(sandbox_id) -> <a href="./src/pipeline/types/sandbox_start_response.py">SandboxStartResponse</a></code>
- <code title="post /sandboxes/{sandbox_id}/stop">client.sandboxes.<a href="./src/pipeline/resources/sandboxes.py">stop</a>(sandbox_id) -> <a href="./src/pipeline/types/sandbox_stop_response.py">SandboxStopResponse</a></code>

# Health

Types:

```python
from pipeline.types import HealthCheckResponse
```

Methods:

- <code title="get /health">client.health.<a href="./src/pipeline/resources/health.py">check</a>() -> <a href="./src/pipeline/types/health_check_response.py">HealthCheckResponse</a></code>

# Billing

Types:

```python
from pipeline.types import (
    BillingCancelSubscriptionResponse,
    BillingCreateCheckoutSessionResponse,
    BillingCreatePortalSessionResponse,
    BillingHandleWebhookResponse,
    BillingListPlansResponse,
    BillingRetrieveSubscriptionStatusResponse,
)
```

Methods:

- <code title="post /billing/cancel-subscription">client.billing.<a href="./src/pipeline/resources/billing.py">cancel_subscription</a>(\*\*<a href="src/pipeline/types/billing_cancel_subscription_params.py">params</a>) -> <a href="./src/pipeline/types/billing_cancel_subscription_response.py">BillingCancelSubscriptionResponse</a></code>
- <code title="post /billing/checkout">client.billing.<a href="./src/pipeline/resources/billing.py">create_checkout_session</a>(\*\*<a href="src/pipeline/types/billing_create_checkout_session_params.py">params</a>) -> <a href="./src/pipeline/types/billing_create_checkout_session_response.py">BillingCreateCheckoutSessionResponse</a></code>
- <code title="post /billing/portal-session">client.billing.<a href="./src/pipeline/resources/billing.py">create_portal_session</a>(\*\*<a href="src/pipeline/types/billing_create_portal_session_params.py">params</a>) -> <a href="./src/pipeline/types/billing_create_portal_session_response.py">BillingCreatePortalSessionResponse</a></code>
- <code title="post /billing/webhook">client.billing.<a href="./src/pipeline/resources/billing.py">handle_webhook</a>(\*\*<a href="src/pipeline/types/billing_handle_webhook_params.py">params</a>) -> <a href="./src/pipeline/types/billing_handle_webhook_response.py">BillingHandleWebhookResponse</a></code>
- <code title="get /billing/plans">client.billing.<a href="./src/pipeline/resources/billing.py">list_plans</a>() -> <a href="./src/pipeline/types/billing_list_plans_response.py">BillingListPlansResponse</a></code>
- <code title="get /billing/subscription/{user_id}">client.billing.<a href="./src/pipeline/resources/billing.py">retrieve_subscription_status</a>(user_id) -> <a href="./src/pipeline/types/billing_retrieve_subscription_status_response.py">BillingRetrieveSubscriptionStatusResponse</a></code>
