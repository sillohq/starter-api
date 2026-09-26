"""The request and response shapes exposed by the API."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class WidgetCreate(BaseModel):
    """Fields accepted when a widget is created."""

    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    name: str = Field(min_length=1, max_length=120)
    description: str | None = Field(default=None, max_length=500)


class WidgetUpdate(BaseModel):
    """Fields that may be changed on a widget."""

    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    name: str | None = Field(default=None, min_length=1, max_length=120)
    description: str | None = Field(default=None, max_length=500)


class Widget(BaseModel):
    """A widget returned by the API."""

    id: int
    name: str
    description: str | None = None
