"""Open the local route atlas in a browser until interrupted."""

from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Timer
import webbrowser


site_dir = Path(__file__).resolve().parent / "dist"
server = ThreadingHTTPServer(("127.0.0.1", 0), partial(SimpleHTTPRequestHandler, directory=str(site_dir)))
url = f"http://127.0.0.1:{server.server_port}/"
print(f"Route atlas: {url}\nPress Ctrl+C to stop.", flush=True)
Timer(0.5, lambda: webbrowser.open(url)).start()

try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
finally:
    server.server_close()
