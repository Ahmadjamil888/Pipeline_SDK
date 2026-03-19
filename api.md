# GitHub

Types:

```python
from pipeline_labs.types import GitHubCheckConnectionStatusResponse, GitHubInitiateOAuthResponse
```

Methods:

- <code title="get /github/status">client.github.<a href="./src/pipeline_labs/resources/github/github.py">check_connection_status</a>(\*\*<a href="src/pipeline_labs/types/github_check_connection_status_params.py">params</a>) -> <a href="./src/pipeline_labs/types/github_check_connection_status_response.py">GitHubCheckConnectionStatusResponse</a></code>
- <code title="get /github/connect">client.github.<a href="./src/pipeline_labs/resources/github/github.py">initiate_oauth</a>(\*\*<a href="src/pipeline_labs/types/github_initiate_oauth_params.py">params</a>) -> <a href="./src/pipeline_labs/types/github_initiate_oauth_response.py">GitHubInitiateOAuthResponse</a></code>

## Repos

Types:

```python
from pipeline_labs.types.github import Repository, RepoListResponse, RepoConnectResponse
```

Methods:

- <code title="get /github/repos">client.github.repos.<a href="./src/pipeline_labs/resources/github/repos.py">list</a>(\*\*<a href="src/pipeline_labs/types/github/repo_list_params.py">params</a>) -> <a href="./src/pipeline_labs/types/github/repo_list_response.py">RepoListResponse</a></code>
- <code title="post /github/repos/connect">client.github.repos.<a href="./src/pipeline_labs/resources/github/repos.py">connect</a>(\*\*<a href="src/pipeline_labs/types/github/repo_connect_params.py">params</a>) -> <a href="./src/pipeline_labs/types/github/repo_connect_response.py">RepoConnectResponse</a></code>

# Projects

Types:

```python
from pipeline_labs.types import ProjectRetrieveProgressResponse
```

Methods:

- <code title="get /projects/{project_id}/progress">client.projects.<a href="./src/pipeline_labs/resources/projects.py">retrieve_progress</a>(project_id) -> <a href="./src/pipeline_labs/types/project_retrieve_progress_response.py">ProjectRetrieveProgressResponse</a></code>

# Repos

Types:

```python
from pipeline_labs.types import RepoConnection
```

Methods:

- <code title="get /repos/{repo_id}">client.repos.<a href="./src/pipeline_labs/resources/repos.py">retrieve</a>(repo_id) -> <a href="./src/pipeline_labs/types/repo_connection.py">RepoConnection</a></code>
- <code title="post /repos/connect">client.repos.<a href="./src/pipeline_labs/resources/repos.py">connect</a>(\*\*<a href="src/pipeline_labs/types/repo_connect_params.py">params</a>) -> <a href="./src/pipeline_labs/types/repo_connection.py">RepoConnection</a></code>

# Deployments

Types:

```python
from pipeline_labs.types import (
    DeploymentStatus,
    LogEntry,
    DeploymentCreateResponse,
    DeploymentListResponse,
    DeploymentExecuteResponse,
    DeploymentGetLogsResponse,
)
```

Methods:

- <code title="post /deployments">client.deployments.<a href="./src/pipeline_labs/resources/deployments.py">create</a>(\*\*<a href="src/pipeline_labs/types/deployment_create_params.py">params</a>) -> <a href="./src/pipeline_labs/types/deployment_create_response.py">DeploymentCreateResponse</a></code>
- <code title="get /deployments/{deployment_id}">client.deployments.<a href="./src/pipeline_labs/resources/deployments.py">retrieve</a>(deployment_id) -> <a href="./src/pipeline_labs/types/deployment_status.py">DeploymentStatus</a></code>
- <code title="get /deployments">client.deployments.<a href="./src/pipeline_labs/resources/deployments.py">list</a>(\*\*<a href="src/pipeline_labs/types/deployment_list_params.py">params</a>) -> <a href="./src/pipeline_labs/types/deployment_list_response.py">DeploymentListResponse</a></code>
- <code title="post /deployments/{deployment_id}/run">client.deployments.<a href="./src/pipeline_labs/resources/deployments.py">execute</a>(deployment_id) -> <a href="./src/pipeline_labs/types/deployment_execute_response.py">DeploymentExecuteResponse</a></code>
- <code title="get /deployments/{deployment_id}/logs">client.deployments.<a href="./src/pipeline_labs/resources/deployments.py">get_logs</a>(deployment_id, \*\*<a href="src/pipeline_labs/types/deployment_get_logs_params.py">params</a>) -> <a href="./src/pipeline_labs/types/deployment_get_logs_response.py">DeploymentGetLogsResponse</a></code>

# Sandboxes

Types:

```python
from pipeline_labs.types import (
    Sandbox,
    SandboxResources,
    SandboxListResponse,
    SandboxExecuteResponse,
    SandboxGetLogsResponse,
    SandboxStartResponse,
    SandboxStopResponse,
)
```

Methods:

- <code title="post /sandboxes">client.sandboxes.<a href="./src/pipeline_labs/resources/sandboxes.py">create</a>(\*\*<a href="src/pipeline_labs/types/sandbox_create_params.py">params</a>) -> <a href="./src/pipeline_labs/types/sandbox.py">Sandbox</a></code>
- <code title="get /sandboxes/{sandbox_id}">client.sandboxes.<a href="./src/pipeline_labs/resources/sandboxes.py">retrieve</a>(sandbox_id) -> <a href="./src/pipeline_labs/types/sandbox.py">Sandbox</a></code>
- <code title="get /sandboxes">client.sandboxes.<a href="./src/pipeline_labs/resources/sandboxes.py">list</a>(\*\*<a href="src/pipeline_labs/types/sandbox_list_params.py">params</a>) -> <a href="./src/pipeline_labs/types/sandbox_list_response.py">SandboxListResponse</a></code>
- <code title="post /sandboxes/{sandbox_id}/execute">client.sandboxes.<a href="./src/pipeline_labs/resources/sandboxes.py">execute</a>(sandbox_id, \*\*<a href="src/pipeline_labs/types/sandbox_execute_params.py">params</a>) -> <a href="./src/pipeline_labs/types/sandbox_execute_response.py">SandboxExecuteResponse</a></code>
- <code title="get /sandboxes/{sandbox_id}/logs">client.sandboxes.<a href="./src/pipeline_labs/resources/sandboxes.py">get_logs</a>(sandbox_id, \*\*<a href="src/pipeline_labs/types/sandbox_get_logs_params.py">params</a>) -> <a href="./src/pipeline_labs/types/sandbox_get_logs_response.py">SandboxGetLogsResponse</a></code>
- <code title="post /sandboxes/{sandbox_id}/start">client.sandboxes.<a href="./src/pipeline_labs/resources/sandboxes.py">start</a>(sandbox_id) -> <a href="./src/pipeline_labs/types/sandbox_start_response.py">SandboxStartResponse</a></code>
- <code title="post /sandboxes/{sandbox_id}/stop">client.sandboxes.<a href="./src/pipeline_labs/resources/sandboxes.py">stop</a>(sandbox_id) -> <a href="./src/pipeline_labs/types/sandbox_stop_response.py">SandboxStopResponse</a></code>

# Health

Types:

```python
from pipeline_labs.types import HealthCheckResponse
```

Methods:

- <code title="get /health">client.health.<a href="./src/pipeline_labs/resources/health.py">check</a>() -> <a href="./src/pipeline_labs/types/health_check_response.py">HealthCheckResponse</a></code>

# Billing

Types:

```python
from pipeline_labs.types import (
    BillingCancelSubscriptionResponse,
    BillingCreateBillingPortalSessionResponse,
    BillingCreateCheckoutSessionResponse,
    BillingListPlansResponse,
    BillingRetrieveSubscriptionStatusResponse,
)
```

Methods:

- <code title="post /billing/cancel-subscription">client.billing.<a href="./src/pipeline_labs/resources/billing.py">cancel_subscription</a>(\*\*<a href="src/pipeline_labs/types/billing_cancel_subscription_params.py">params</a>) -> <a href="./src/pipeline_labs/types/billing_cancel_subscription_response.py">BillingCancelSubscriptionResponse</a></code>
- <code title="post /billing/portal-session">client.billing.<a href="./src/pipeline_labs/resources/billing.py">create_billing_portal_session</a>(\*\*<a href="src/pipeline_labs/types/billing_create_billing_portal_session_params.py">params</a>) -> <a href="./src/pipeline_labs/types/billing_create_billing_portal_session_response.py">BillingCreateBillingPortalSessionResponse</a></code>
- <code title="post /billing/checkout">client.billing.<a href="./src/pipeline_labs/resources/billing.py">create_checkout_session</a>(\*\*<a href="src/pipeline_labs/types/billing_create_checkout_session_params.py">params</a>) -> <a href="./src/pipeline_labs/types/billing_create_checkout_session_response.py">BillingCreateCheckoutSessionResponse</a></code>
- <code title="get /billing/plans">client.billing.<a href="./src/pipeline_labs/resources/billing.py">list_plans</a>() -> <a href="./src/pipeline_labs/types/billing_list_plans_response.py">BillingListPlansResponse</a></code>
- <code title="get /billing/subscription/{user_id}">client.billing.<a href="./src/pipeline_labs/resources/billing.py">retrieve_subscription_status</a>(user_id) -> <a href="./src/pipeline_labs/types/billing_retrieve_subscription_status_response.py">BillingRetrieveSubscriptionStatusResponse</a></code>
