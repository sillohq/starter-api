"""A complete JSON CRUD resource to use as a starting point."""

from __future__ import annotations

from sillo import HttpContext, Router, json

from app.errors import not_found
from app.schemas import WidgetCreate, WidgetUpdate
from app.store import WidgetStore

router = Router(prefix="/api/v1", tags=["widgets"])


def store(ctx: HttpContext) -> WidgetStore:
    """Get the application's persistence boundary for this request."""
    return ctx.base_app.state["widgets"]


@router.get("/widgets", summary="List widgets")
async def list_widgets(ctx: HttpContext):
    """Return every widget currently known to the application."""
    return json({"data": [widget.model_dump() for widget in store(ctx).list()]})


@router.post("/widgets", request_model=WidgetCreate, summary="Create a widget")
async def create_widget(ctx: HttpContext, payload):
    """Validate and create one widget."""
    widget = store(ctx).create(payload)
    return json({"data": widget.model_dump()}, status_code=201)


@router.get("/widgets/{widget_id:int}", summary="Get a widget")
async def get_widget(ctx: HttpContext, widget_id: int):
    """Return one widget by its stable integer identifier."""
    widget = store(ctx).get(widget_id)
    if widget is None:
        return not_found("Widget", widget_id)
    return json({"data": widget.model_dump()})


@router.patch(
    "/widgets/{widget_id:int}", request_model=WidgetUpdate, summary="Update a widget"
)
async def update_widget(ctx: HttpContext, payload, widget_id: int):
    """Apply supplied fields without replacing omitted ones."""
    widget = store(ctx).update(widget_id, payload)
    if widget is None:
        return not_found("Widget", widget_id)
    return json({"data": widget.model_dump()})


@router.delete("/widgets/{widget_id:int}", summary="Delete a widget")
async def delete_widget(ctx: HttpContext, widget_id: int):
    """Delete one widget and acknowledge the deletion without a body."""
    if not store(ctx).delete(widget_id):
        return not_found("Widget", widget_id)
    return json({}, status_code=204)
