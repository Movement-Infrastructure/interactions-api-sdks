"""Shared fixtures for the Python v1 SDK smoke suite (MIG-1918).

The SDK is generated with ``library: urllib3`` (a real synchronous HTTP
client), so the happy-path test points the client at a live localhost server
provided by ``pytest-httpserver`` rather than monkeypatching the transport.
"""

import pytest

from mi_interactions_api import ApiClient, Configuration


@pytest.fixture
def api_client(httpserver):
    """An ``ApiClient`` configured to talk to the local mock server.

    ``httpserver`` is the fixture provided by pytest-httpserver; it starts a
    real werkzeug server on an ephemeral localhost port for the duration of
    the test.
    """
    config = Configuration(host=f"http://{httpserver.host}:{httpserver.port}")
    # The endpoint is behind HTTP basic auth; the mock server ignores it, but
    # setting credentials exercises the client's auth path.
    config.username = "test"
    config.password = "test"
    with ApiClient(config) as client:
        yield client
