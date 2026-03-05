# Auth

Types:

```python
from pipeline.types import AuthAuthenticateResponse
```

Methods:

- <code title="post /auth">client.auth.<a href="./src/pipeline/resources/auth/auth.py">authenticate</a>() -> <a href="./src/pipeline/types/auth_authenticate_response.py">AuthAuthenticateResponse</a></code>

## Keys

Types:

```python
from pipeline.types.auth import KeyCreateResponse, KeyListResponse
```

Methods:

- <code title="post /auth/keys">client.auth.keys.<a href="./src/pipeline/resources/auth/keys.py">create</a>() -> <a href="./src/pipeline/types/auth/key_create_response.py">KeyCreateResponse</a></code>
- <code title="get /auth/keys">client.auth.keys.<a href="./src/pipeline/resources/auth/keys.py">list</a>() -> <a href="./src/pipeline/types/auth/key_list_response.py">KeyListResponse</a></code>

# Agents

Types:

```python
from pipeline.types import AgentCleanDataResponse
```

Methods:

- <code title="post /agents/data_clean">client.agents.<a href="./src/pipeline/resources/agents.py">clean_data</a>(\*\*<a href="src/pipeline/types/agent_clean_data_params.py">params</a>) -> <a href="./src/pipeline/types/agent_clean_data_response.py">AgentCleanDataResponse</a></code>
- <code title="post /agents/monitor">client.agents.<a href="./src/pipeline/resources/agents.py">monitor_training</a>(\*\*<a href="src/pipeline/types/agent_monitor_training_params.py">params</a>) -> None</code>
- <code title="post /agents/dataset_optimize">client.agents.<a href="./src/pipeline/resources/agents.py">optimize_dataset</a>(\*\*<a href="src/pipeline/types/agent_optimize_dataset_params.py">params</a>) -> None</code>
- <code title="post /agents/experiment_summarize">client.agents.<a href="./src/pipeline/resources/agents.py">summarize_experiment</a>(\*\*<a href="src/pipeline/types/agent_summarize_experiment_params.py">params</a>) -> None</code>

# Training

Types:

```python
from pipeline.types import (
    TrainingListResponse,
    TrainingTriggerResponse,
    TrainingUpdateStatusResponse,
)
```

Methods:

- <code title="get /training">client.training.<a href="./src/pipeline/resources/training/training.py">list</a>() -> <a href="./src/pipeline/types/training_list_response.py">TrainingListResponse</a></code>
- <code title="post /training">client.training.<a href="./src/pipeline/resources/training/training.py">trigger</a>(\*\*<a href="src/pipeline/types/training_trigger_params.py">params</a>) -> <a href="./src/pipeline/types/training_trigger_response.py">TrainingTriggerResponse</a></code>
- <code title="patch /training/{id}">client.training.<a href="./src/pipeline/resources/training/training.py">update_status</a>(id, \*\*<a href="src/pipeline/types/training_update_status_params.py">params</a>) -> <a href="./src/pipeline/types/training_update_status_response.py">TrainingUpdateStatusResponse</a></code>

## Logs

Types:

```python
from pipeline.types.training import LogRetrieveResponse
```

Methods:

- <code title="get /training/{id}/logs">client.training.logs.<a href="./src/pipeline/resources/training/logs.py">retrieve</a>(id) -> <a href="./src/pipeline/types/training/log_retrieve_response.py">LogRetrieveResponse</a></code>
- <code title="post /training/{id}/logs">client.training.logs.<a href="./src/pipeline/resources/training/logs.py">push</a>(id, \*\*<a href="src/pipeline/types/training/log_push_params.py">params</a>) -> None</code>

# Compute

Methods:

- <code title="get /compute/provider">client.compute.<a href="./src/pipeline/resources/compute.py">retrieve_provider</a>() -> object</code>

# Cloud

Methods:

- <code title="post /cloud/configure">client.cloud.<a href="./src/pipeline/resources/cloud.py">configure</a>(\*\*<a href="src/pipeline/types/cloud_configure_params.py">params</a>) -> object</code>
