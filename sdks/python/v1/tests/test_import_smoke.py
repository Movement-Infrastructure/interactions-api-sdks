"""Import smoke test

Confirms the freshly generated package imports cleanly and exposes the public
surface consumers depend on. These names are stable across regenerations: the
package name comes from ``openapi-generator-config.yaml``, the API classes from
the spec's tags ("Interactions", "Authentication Details"), and the models from
the component schema names.
"""

import mi_interactions_api


def test_package_imports():
    assert mi_interactions_api.__name__ == "mi_interactions_api"


def test_core_client_symbols():
    from mi_interactions_api import ApiClient, ApiException, Configuration

    assert ApiClient is not None
    assert Configuration is not None
    assert ApiException is not None


def test_api_classes_exposed():
    # Tag "Interactions" -> InteractionsApi; "Authentication Details" ->
    # AuthenticationDetailsApi (re-exported from the top-level package).
    from mi_interactions_api import AuthenticationDetailsApi, InteractionsApi

    assert InteractionsApi is not None
    assert AuthenticationDetailsApi is not None


def test_key_models_exposed():
    from mi_interactions_api import (
        CommitteeDetails,
        InteractionDto,
        InteractionsBatchResultDto,
        InteractionsDto,
    )

    assert InteractionsDto is not None
    assert InteractionDto is not None
    assert CommitteeDetails is not None
    assert InteractionsBatchResultDto is not None
