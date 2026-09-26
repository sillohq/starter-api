"""The published schema is part of the API contract."""

from __future__ import annotations


def test_openapi_documents_the_widget_resource(client):
    schema = client.get("/openapi.json").json()

    assert "/api/v1/widgets" in schema["paths"]
    assert "post" in schema["paths"]["/api/v1/widgets"]
