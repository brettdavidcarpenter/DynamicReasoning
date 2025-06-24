import json
from web_api import compare_agents


def app(environ, start_response):
    """WSGI application returning agent metrics as JSON."""
    if environ.get("REQUEST_METHOD") != "POST":
        start_response("405 Method Not Allowed", [("Content-Type", "text/plain")])
        return [b"Method Not Allowed"]

    try:
        length = int(environ.get("CONTENT_LENGTH", 0))
    except ValueError:
        length = 0
    body = environ["wsgi.input"].read(length).decode()
    try:
        data = json.loads(body) if body else {}
    except json.JSONDecodeError:
        data = {}
    script_text = data.get("script", "")
    script_lines = [line.strip() for line in script_text.splitlines() if line.strip()]

    result = compare_agents(script_lines)
    payload = json.dumps(result).encode()

    start_response("200 OK", [("Content-Type", "application/json")])
    return [payload]
