from wsgiref.simple_server import make_server
from api.compare import app


if __name__ == "__main__":
    with make_server("", 8000, app) as server:
        print("Serving on http://localhost:8000")
        server.serve_forever()
