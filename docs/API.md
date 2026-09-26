# API conventions

The public API begins at /api/v1. Keep an existing version stable; add a new
prefix when a change cannot be made backwards compatible.

Successful resource responses use a data envelope:

    {"data":{"id":1,"name":"Telemetry","description":null}}

Missing resources use the same JSON shape everywhere:

    {"detail":"Widget 404 was not found.","status":404}

Request models reject unknown fields and validate before a handler runs. Invalid
JSON or invalid fields therefore produce Sillo's standard 422 response. This
keeps the generated OpenAPI document and the running API aligned.
