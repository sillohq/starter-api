# Starter API

A clean, intentionally small JSON API starter for Sillo. It gives you a
versioned resource, validated JSON input, OpenAPI at /docs, tests, and a clear
persistence boundary without forcing a database on day one.

## Quick start

    uv sync --all-extras
    cp .env.example .env
    make dev

Open http://127.0.0.1:8000/docs. The development server reloads Python changes
and prints Sillo-formatted request logs.

## Included API

| Method | Path | Purpose |
| --- | --- | --- |
| GET | /health | Liveness probe |
| GET | /api/v1/widgets | List widgets |
| POST | /api/v1/widgets | Create a widget |
| GET | /api/v1/widgets/{id} | Fetch a widget |
| PATCH | /api/v1/widgets/{id} | Partially update a widget |
| DELETE | /api/v1/widgets/{id} | Delete a widget |

    curl -X POST http://127.0.0.1:8000/api/v1/widgets \
      -H 'content-type: application/json' \
      -d '{"name":"Telemetry","description":"Collect useful signals."}'

The sample store is in process on purpose, so the starter works immediately.
Replace app/store.py with a Record repository when data must persist; the
routes and JSON contract do not need to change.

## Quality checks

    make check
    make smoke  # while make dev is running

## Create it with Sillo Start

    uvx sillo-start create-app sillohq/starter-api myapi

The repository calls itself starter internally so Sillo Start can rename the
project, app title, environment file, and lockfile safely.

## License

BSD-3-Clause.
