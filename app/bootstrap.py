"""Application assembly kept separate from the ASGI import target."""

from __future__ import annotations

from sillo import SilloApp

from app.config import config
from app.store import WidgetStore
from routes.health import router as health_router
from routes.widgets import router as widgets_router


def create_app() -> SilloApp:
    """Build the API and install its explicitly owned services."""
    application = SilloApp(
        debug=config.debug,
        title=config.app_name,
        version="0.1.0",
        description="A clean JSON API starter built with Sillo.",
    )
    application.state["widgets"] = WidgetStore()
    application.mount_router(health_router)
    application.mount_router(widgets_router)
    return application
