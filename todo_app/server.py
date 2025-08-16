import http.server
import socketserver
import os

port_str = os.getenv("PORT", "8080")
PORT = int(port_str)

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server started in port {PORT}")
    httpd.serve_forever()
