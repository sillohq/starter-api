"""Exercise a running local server without adding an HTTP client dependency."""

import json
from urllib.request import urlopen


with urlopen("http://127.0.0.1:8000/health", timeout=5) as response:
    body = json.loads(response.read())

assert response.status == 200, response.status
assert body["status"] == "ok", body
print("health check passed")
