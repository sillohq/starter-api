"""Typed application settings loaded from the environment."""

from __future__ import annotations

from typing import Literal

from sillo.config import Config


class AppConfig(Config):
    """Typed settings for Starter."""

    app_name: str = "Starter API"
    app_env: Literal["local", "testing", "staging", "production"] = "local"
    debug: bool = True
    host: str = "127.0.0.1"
    port: int = 8000


config = AppConfig(_env_file=".env")
