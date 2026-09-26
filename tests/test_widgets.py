"""Tests for the sample JSON resource."""

from __future__ import annotations


def test_widgets_can_be_created_listed_and_fetched(client):
    created = client.post(
        "/api/v1/widgets",
        json={"name": "Telemetry", "description": "Collect useful signals."},
    )

    assert created.status_code == 201
    widget = created.json()["data"]
    assert widget["id"] == 1

    assert client.get("/api/v1/widgets").json()["data"] == [widget]
    assert client.get("/api/v1/widgets/1").json()["data"] == widget


def test_missing_widget_has_a_consistent_error_shape(client):
    response = client.get("/api/v1/widgets/404")

    assert response.status_code == 404
    assert response.json() == {"detail": "Widget 404 was not found.", "status": 404}
