"""POST /v1/interactions against a mock server.

The spec defines no ``operationId`` for the interactions endpoints, so
openapi-generator derives the method name from the path and verb, giving
``vversion_interactions_post``. That slug is an implementation detail and can
shift, so the test discovers the operation at runtime and binds its arguments
by name rather than hard-coding either.

The request/response bodies below match the committed OpenAPI spec.
"""

import inspect

from ddx_interactions_api import (
    InteractionsApi,
    InteractionsBatchResultDto,
    InteractionsDto,
)

# The spec templates its paths as `/v{version}/...`, so `version` is a required
# path parameter and the generated methods take it as their first argument.
API_VERSION = "1"

# Minimal request satisfying InteractionDto's required fields
# (attemptDateTime, committee, method, outcome, stateCode, vendorSource).
#
# `person` is not in the spec's `required` list but the API rejects the request
# without it: for non-VAN destinations the backend demands either a non-empty
# `person` array or valid `contactInfo` (email, phone, or address). A body
# without one comes back 400, "Person ID or valid form of contact information
# (email, phone, or address) required." Since the mock below answers with a
# canned success no matter what is posted, leaving `person` out kept this test
# green while asserting a request the real API refuses — found by the MIG-1929
# staging run.
REQUEST_BODY = {
    "interactions": [
        {
            "stateCode": "CA",
            "attemptDateTime": "2026-07-30T10:00:00Z",
            "method": "phone_call",
            "committee": [{"type": "Matchbook", "id": "1"}],
            "vendorSource": "Matchbook",
            "outcome": "successful_contact",
            "person": [{"type": "Matchbook", "id": "1"}],
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
    """Return the single POST operation bound method on an InteractionsApi.

    Generated names are `<path>_<verb>`, so the verb is a suffix. The
    `_with_http_info` and `_without_preload_content` variants therefore fall out
    on their own.
    """
    names = [
        n
        for n in dir(api)
        if n.endswith("post") and not n.startswith("_") and callable(getattr(api, n))
    ]
    assert len(names) == 1, (
        "expected exactly one POST operation on InteractionsApi, found "
        f"{names!r}; public members: "
        f"{[n for n in dir(api) if not n.startswith('_')]!r}"
    )
    return getattr(api, names[0])


def _call(method, body):
    """Invoke `method`, binding every argument by name.

    Binding positionally is what broke this test before: the generated
    signature leads with the `version` path parameter, so the body landed in
    `version` and the request never took the shape under test. Anything the
    signature requires and we cannot supply is an assertion, not a silent
    mis-bind.
    """
    params = inspect.signature(method).parameters
    kwargs = {}

    if "version" in params:
        kwargs["version"] = API_VERSION

    body_params = [
        name
        for name, param in params.items()
        if not name.startswith("_")
        and name not in kwargs
        and "InteractionsDto" in str(param.annotation)
    ]
    assert len(body_params) == 1, (
        "expected exactly one InteractionsDto parameter to bind the request "
        f"body to, found {body_params!r} in signature "
        f"{inspect.signature(method)}"
    )
    kwargs[body_params[0]] = body

    unbound = [
        name
        for name, param in params.items()
        if not name.startswith("_")
        and name not in kwargs
        and param.default is inspect.Parameter.empty
    ]
    assert not unbound, (
        f"operation has required parameters this test does not supply: "
        f"{unbound!r}; signature {inspect.signature(method)}"
    )

    return method(**kwargs)


def test_publish_interactions_happy_path(api_client, httpserver):
    httpserver.expect_request(
        f"/v{API_VERSION}/interactions", method="POST"
    ).respond_with_json(MOCK_RESPONSE)

    api = InteractionsApi(api_client)
    body = InteractionsDto.from_dict(REQUEST_BODY)

    result = _call(_post_interactions_method(api), body)

    assert isinstance(result, InteractionsBatchResultDto)
    assert result.total_interactions == 1
    assert result.correlation_id == "test-correlation-123"
    assert result.accepted_interactions.count == 1
