# Interactions API SDKs

Client libraries for the [DDx Interactions API](https://docs.movementinfrastructure.org/docs/interactions-api-overview), generated from its OpenAPI specification.

The Interactions API moves voter and supporter outreach data — canvass responses, event signups, activist codes, communication consent — from a Source to one or more Destinations. These SDKs give you a typed client for it instead of hand-rolled HTTP.

New to the API itself? Start with the [overview](https://docs.movementinfrastructure.org/docs/interactions-api-overview) and the [setup guides](https://docs.movementinfrastructure.org/docs/interactions-api-set-up).

## Available SDKs

| Language | Package | Status |
| --- | --- | --- |
| Python | [`ddx-interactions-api`](https://test.pypi.org/project/ddx-interactions-api/) | Pre-release |
| Node.js | — | Planned |
| C# | — | Planned |
| Ruby | — | Planned |

Each SDK lives under `sdks/<language>/v1/` and is generated from `openapi/v1/swagger.json`.

## Python

Requires Python 3.8+. The package is a pre-release on TestPyPI while the API stabilizes:

```sh
pip install \
  --index-url https://test.pypi.org/simple/ \
  --extra-index-url https://pypi.org/simple/ \
  ddx-interactions-api
```

The extra index lets the runtime dependencies resolve from PyPI. Once the first stable release ships, this becomes `pip install ddx-interactions-api`.

### Authentication

HTTP Basic, with your API key in the **password** field and the username left empty. [Authentication](https://docs.movementinfrastructure.org/docs/interactions-api-authentication) covers how to request a key.

| Host | Use |
| --- | --- |
| `https://api.movementinfrastructure.org` | Production (SDK default) |
| `https://api-dev.movementinfrastructure.org` | Public test server |

### Quick start

Posting a batch of interactions, up to 100 per request:

```python
import os

import ddx_interactions_api
from ddx_interactions_api.rest import ApiException

configuration = ddx_interactions_api.Configuration(
    host="https://api-dev.movementinfrastructure.org",
    username="",
    password=os.environ["DDX_API_KEY"],
)

with ddx_interactions_api.ApiClient(configuration) as api_client:
    interactions = ddx_interactions_api.InteractionsApi(api_client)
    payload = ddx_interactions_api.InteractionsDto(
        # See docs/InteractionsDto.md in the package for the full shape.
    )

    try:
        result = interactions.vversion_interactions_post("1", interactions_dto=payload)
    except ApiException as e:
        print(f"Interactions API returned {e.status}: {e.body}")
```

The response carries a correlation ID for following the batch through the Exchange:

```python
statuses = interactions.vversion_interactions_exchange_status_get(
    "1", correlation_id=result.correlation_id
)
```

### Endpoints

| Method | Endpoint |
| --- | --- |
| `vversion_interactions_post` | `POST /v1/interactions` |
| `vversion_interactions_exchange_status_get` | `GET /v1/interactions/exchange-status` |
| `vversion_interactions_exchange_status_range_get` | `GET /v1/interactions/exchange-status/range` |
| `vversion_interactions_interaction_id_transactions_get` | `GET /v1/interactions/{interactionId}/transactions` |
| `vversion_interactions_transactions_get` | `GET /v1/interactions/transactions` |
| `vversion_auth_me_get` | `GET /v1/auth/me` |

Full models are documented in [`sdks/python/v1/README.md`](sdks/python/v1/README.md) and its `docs/` directory. The interactive reference is at [docs.movementinfrastructure.org/reference](https://docs.movementinfrastructure.org/reference/interactions).

## Versioning

SDK versions are semantic; a major bump means the API changed in a way that requires work on your side. Each SDK ships a changelog generated from a diff of the specification, with breaking entries marked: [Python changelog](sdks/python/v1/CHANGELOG.md).

The SDK version tracks the package, not the API. The API version (`v1`) appears in the request path and changes far less often.

## Reporting problems

SDK code is generated, and local edits are overwritten on the next sync — a broken client is almost always a specification bug.

- SDK bugs and questions: open an issue here.
- The API itself, keys, or Destinations: <api@demexchange.com>.

## License

MIT. See [LICENSE](LICENSE).

## Contributing

A pull request that edits `sdks/` directly will not survive the next sync. [CONTRIBUTING.md](CONTRIBUTING.md) explains where a change actually belongs.
