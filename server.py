import http.server
import socketserver
import signal
import sys

PORT = 8003


class TCPServerReusableAddr(socketserver.TCPServer):
    allow_reuse_address = True


def signal_handler(sig, frame):
    print("\nShutting down server...")
    httpd.server_close()
    sys.exit(0)


Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map.update(
    {
        ".js": "application/javascript",
        ".css": "text/css",
    }
)

print(f"Server starting at http://localhost:{PORT}")
print("Press Ctrl+C to quit")

signal.signal(signal.SIGINT, signal_handler)

with TCPServerReusableAddr(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()
        print("\nServer stopped.")
