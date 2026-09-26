"""Fixtures that exercise the application through its ASGI boundary."""

from __future__ import annotations

import sys

import pytest


@pytest.fixture(autouse=True)
def isolated_environment(monkeypatch: pytest.MonkeyPatch):
    """Keep a developer's shell settings from changing test configuration."""
    monkeypatch.setenv("APP_ENV", "testing")
    monkeypatch.setenv("DEBUG", "true")
    for name in list(sys.modules):
        if name == "app" or name.startswith("app.") or (
            name == "routes" or name.startswith("routes.")
        ):
            sys.modules.pop(name)
    yield


@pytest.fixture
def client():
    """Build one isolated application and enter its lifespan."""
    from sillo.testclient import TestClient

    from app.bootstrap import create_app

    with TestClient(create_app()) as test_client:
        yield test_client
