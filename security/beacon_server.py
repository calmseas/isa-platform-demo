"""Tiny local beacon for the skill-poisoning demo.

Logs every request (the "phone home") to the terminal with a timestamp and
returns 200. Nothing is stored or forwarded anywhere. Run it in a spare terminal
during the demo so the room sees the hit land live.

    python3 security/beacon_server.py            # listens on http://localhost:9000
    python3 security/beacon_server.py 9100        # or pick a port

Then, in another terminal:

    export BEACON_URL="http://localhost:9000/hit"
    python3 security/build_poisoned_skill.py

Invoke the code-formatter skill in Claude Code and watch a BEACON HIT appear here.
"""

import sys
from datetime import UTC, datetime
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 9000


class Handler(BaseHTTPRequestHandler):
    def _hit(self) -> None:
        ts = datetime.now(UTC).strftime("%H:%M:%S")
        print(f"\n*** BEACON HIT {ts}Z  {self.command} {self.path}")
        print(f"    from {self.client_address[0]}  ua={self.headers.get('User-Agent', '')}")
        body = b"ok\n"
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    do_GET = _hit
    do_POST = _hit

    def log_message(self, *args) -> None:  # silence default per-request logging
        pass


if __name__ == "__main__":
    print(f"beacon listening on http://localhost:{PORT}  (Ctrl+C to stop)")
    try:
        HTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
    except KeyboardInterrupt:
        print("\nbeacon stopped")
