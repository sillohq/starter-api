"""Operational endpoints that sit beside the versioned API."""

from __future__ import annotations

from sillo import HttpContext, Router, json

from app.config import config

router = Router(tags=["operations"])


@router.get("/health", summary="Liveness probe")
async def health(ctx: HttpContext):
    """Confirm that this process can receive requests."""
    return json({"status": "ok", "environment": config.app_env})
