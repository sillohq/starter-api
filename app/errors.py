"""Small, consistent JSON errors for resource routes."""

from __future__ import annotations

from sillo import json


def not_found(resource: str, identifier: int):
    """Return the standard response for a resource that does not exist."""
    return json(
        {
            "detail": f"{resource} {identifier} was not found.",
            "status": 404,
        },
        status_code=404,
    )
