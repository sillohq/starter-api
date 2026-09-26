"""Fixtures that exercise the application through its ASGI boundary."""

from __future__ import annotations

import pytest


@pytest.fixture
def client():
    """Build one isolated application and enter its lifespan."""
    from sillo.testclient import TestClient

    from app.bootstrap import create_app

    with TestClient(create_app()) as test_client:
        yield test_client
