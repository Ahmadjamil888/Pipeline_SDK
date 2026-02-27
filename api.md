# Auth

Types:

```python
from pipeline.types import AuthCreateOrRotateAPIKeyResponse
```

Methods:

- <code title="post /auth">client.auth.<a href="./src/pipeline/resources/auth.py">create_or_rotate_api_key</a>() -> <a href="./src/pipeline/types/auth_create_or_rotate_api_key_response.py">AuthCreateOrRotateAPIKeyResponse</a></code>

# Training

Types:

```python
from pipeline.types import TrainingStartResponse
```

Methods:

- <code title="post /training">client.training.<a href="./src/pipeline/resources/training.py">start</a>(\*\*<a href="src/pipeline/types/training_start_params.py">params</a>) -> <a href="./src/pipeline/types/training_start_response.py">TrainingStartResponse</a></code>

# FineTune

Methods:

- <code title="post /fine-tune">client.fine_tune.<a href="./src/pipeline/resources/fine_tune.py">start</a>(\*\*<a href="src/pipeline/types/fine_tune_start_params.py">params</a>) -> None</code>

# Datasets

Methods:

- <code title="post /datasets">client.datasets.<a href="./src/pipeline/resources/datasets.py">create</a>() -> None</code>
- <code title="get /datasets">client.datasets.<a href="./src/pipeline/resources/datasets.py">list</a>() -> None</code>

# Registry

Methods:

- <code title="get /registry">client.registry.<a href="./src/pipeline/resources/registry.py">list</a>() -> None</code>

# Deployment

Methods:

- <code title="post /deployment">client.deployment.<a href="./src/pipeline/resources/deployment.py">create</a>() -> None</code>
