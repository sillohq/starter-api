"""The ASGI application imported by Sillo development and production servers."""

from __future__ import annotations

from app.bootstrap import create_app

app = create_app()
