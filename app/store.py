"""A deliberately small persistence boundary for the sample resource.

Replace this class with a Record repository when the project gains a database;
the route contract stays the same.
"""

from __future__ import annotations

from .schemas import Widget, WidgetCreate, WidgetUpdate


class WidgetStore:
    """Store widgets in process for a runnable starter without infrastructure."""

    def __init__(self) -> None:
        self._next_id = 1
        self._widgets: dict[int, Widget] = {}

    def list(self) -> list[Widget]:
        return list(self._widgets.values())

    def get(self, widget_id: int) -> Widget | None:
        return self._widgets.get(widget_id)

    def create(self, payload: WidgetCreate) -> Widget:
        widget = Widget(id=self._next_id, **payload.model_dump())
        self._widgets[widget.id] = widget
        self._next_id += 1
        return widget

    def update(self, widget_id: int, payload: WidgetUpdate) -> Widget | None:
        widget = self.get(widget_id)
        if widget is None:
            return None
        updated = widget.model_copy(update=payload.model_dump(exclude_unset=True))
        self._widgets[widget_id] = updated
        return updated

    def delete(self, widget_id: int) -> bool:
        return self._widgets.pop(widget_id, None) is not None
