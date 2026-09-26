"""The framework validates request models before route handlers run."""

from __future__ import annotations

import pytest


@pytest.mark.parametrize(
    "payload",
    [
        {},
        {"name": ""},
        {"name": "valid", "unknown": True},
    ],
)
def test_invalid_widget_payloads_are_rejected(client, payload):
    response = client.post("/api/v1/widgets", json=payload)

    assert response.status_code == 422
