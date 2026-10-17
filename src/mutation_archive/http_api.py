"""Minimal dependency-free HTTP API for local archive exploration.

This server is intentionally small and is not a substitute for a hardened
production API gateway. Put authentication, TLS, rate limiting, and an
application server in front of it for deployment.
"""
from __future__ import annotations
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from urllib.parse import urlparse, parse_qs
from .archive import MutationArchive
from .io import read_variants_json

class ArchiveHandler(BaseHTTPRequestHandler):
    archive = MutationArchive()

    def _send(self, status: int, payload: object) -> None:
        body = json.dumps(payload, sort_keys=True).encode("utf-8")
        self.send_response(status); self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body))); self.end_headers(); self.wfile.write(body)

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path == "/health": return self._send(200, {"status": "ok"})
        if parsed.path == "/api/v1/stats": return self._send(200, self.archive.stats())
        if parsed.path == "/api/v1/variants":
            q = parse_qs(parsed.query).get("q", [""])[0]
            rows = list(self.archive.variants.values()) if not q else self.archive.search(q)
            return self._send(200, {"count": len(rows), "variants": [v.to_dict() for v in rows]})
        if parsed.path.startswith("/api/v1/variants/"):
            key = parsed.path.rsplit("/", 1)[-1]
            variant = self.archive.get(key)
            return self._send(200, variant.to_dict()) if variant else self._send(404, {"error": "not found"})
        return self._send(404, {"error": "not found"})

def serve(archive: MutationArchive, host: str = "127.0.0.1", port: int = 8080) -> None:
    ArchiveHandler.archive = archive
    ThreadingHTTPServer((host, port), ArchiveHandler).serve_forever()

def load_archive(path: str) -> MutationArchive:
    archive = MutationArchive()
    for variant in read_variants_json(path): archive.add(variant)
    return archive
