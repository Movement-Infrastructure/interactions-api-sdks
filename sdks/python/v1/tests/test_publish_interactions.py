"""POST /v1/interactions against a mock server.

The spec defines no ``operationId`` for the interactions endpoints, so
openapi-generator derives the method name from the HTTP verb and path.
That slug is an implementation detail and can shift, so the test discovers 
the single POST operation on ``InteractionsApi``at runtime and binds its 
arguments from the signature instead of hard-coding the name. 
The request/response bodies below match the committed OpenAPI spec.
"""

import inspect

from mi_interactions_api import (
    InteractionsApi,
    InteractionsBatchResultDto,
    InteractionsDto,
)

# Minimal request satisfying InteractionDto's required fields
# (attemptDateTime, committee, method, outcome, stateCode, vendorSource).
REQUEST_BODY = {
    "interactions": [
        {
            "stateCode": "CA",
            "attemptDateTime": "2026-07-30T10:00:00Z",
            "method": "phone_call",
            "committee": [{"type": "Matchbook", "id": "1"}],
            "vendorSource": "Matchbook",
            "outcome": "successful_contact",
        }
    ]
}

# Shape matches InteractionsBatchResultDto in the spec.
MOCK_RESPONSE = {
    "correlationId": "test-correlation-123",
    "totalInteractions": 1,
    "acceptedInteractions": {
        "count": 1,
        "data": [{"interactionId": "11111111-1111-1111-1111-111111111111", "index": 0}],
    },
    "rejectedInteractions": {"count": 0, "data": []},
}


def _post_interactions_method(api):
    """Return the single POST operation bound method on an InteractionsApi."""
    names = [
        n
        for n in dir(api)
        if n.startswith("post")
        and not n.endswith("_with_http_info")
        and not n.endswith("_without_preload_content")
        and callable(getattr(api, n))
    ]
    assert len(names) == 1, (
        "expected exactly one POST operation on InteractionsApi, found "
        f"{names!r}; public members: "
        f"{[n for n in dir(api) if not n.startswith('_')]!r}"
    )
    return getattr(api, names[0])


def _call(method, body):
    """Invoke `method`"""
    params = [
        name
        for name in inspect.signature(method).parameters
        if not name.startswith("_")
    ]
    kwargs = {}
    kwargs[params[0]] = body
    return method(**kwargs)


def test_publish_interactions_happy_path(api_client, httpserver):
    httpserver.expect_request(
        f"/v1/interactions", method="POST"
    ).respond_with_json(MOCK_RESPONSE)

    api = InteractionsApi(api_client)
    body = InteractionsDto.from_dict(REQUEST_BODY)

    result = _call(_post_interactions_method(api), body)

    assert isinstance(result, InteractionsBatchResultDto)
    assert result.total_interactions == 1
    assert result.correlation_id == "test-correlation-123"
    assert result.accepted_interactions.count == 1
