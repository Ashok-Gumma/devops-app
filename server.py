import os
from http.server import HTTPServer, BaseHTTPRequestHandler

APP_NAME = os.getenv("APP_NAME", "Unknown App")
APP_VERSION = os.getenv("APP_VERSION", "Unknown Version")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        html = f"""
        <html>
        <body>
            <h1>{APP_NAME}</h1>
            <p>Version: {APP_VERSION}</p>
            <p>Running inside Docker</p>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())


server = HTTPServer(("0.0.0.0", 8000), Handler)

print(f"{APP_NAME} {APP_VERSION} started")

server.serve_forever()
