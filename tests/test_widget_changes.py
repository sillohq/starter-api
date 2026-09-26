"""Mutation behaviour for the sample resource."""

from __future__ import annotations


def create(client) -> int:
    response = client.post("/api/v1/widgets", json={"name": "Original"})
    return response.json()["data"]["id"]


def test_widget_can_be_partially_updated(client):
    widget_id = create(client)

    response = client.patch(
        f"/api/v1/widgets/{widget_id}",
        json={"description": "Only this field changed."},
    )

    assert response.status_code == 200
    assert response.json()["data"] == {
        "id": widget_id,
        "name": "Original",
        "description": "Only this field changed.",
    }


def test_widget_can_be_deleted(client):
    widget_id = create(client)

    assert client.delete(f"/api/v1/widgets/{widget_id}").status_code == 204
    assert client.get(f"/api/v1/widgets/{widget_id}").status_code == 404
