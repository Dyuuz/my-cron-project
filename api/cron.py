from http.server import BaseHTTPRequestHandler
import requests
import json

TARGET_URLS = [
    "https://stockbridge-m2zc.onrender.com/api/docs",
    "https://mindybrows.onrender.com/",
    "https://blocksigma-vyk5.onrender.com/",
    "https://techscape-9akf.onrender.com/",
]

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        results = []

        for url in TARGET_URLS:
            try:
                response = requests.get(url, timeout=10)
                results.append({
                    "url": url,
                    "status": response.status_code,
                    "ok": response.ok,
                })
            except Exception as e:
                results.append({
                    "url": url,
                    "status": None,
                    "ok": False,
                    "error": str(e),
                })

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(results).encode())