"""Tests for operational endpoints."""

from __future__ import annotations


def test_health_reports_a_live_application(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"
