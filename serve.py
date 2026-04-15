#!/usr/bin/env python3
"""Simple HTTP server to serve static HTML site."""
import http.server
import os

PORT = int(os.environ.get('PORT', 8080))
SITE_DIR = '/app/site'

os.chdir(SITE_DIR)

handler = http.server.SimpleHTTPRequestHandler
handler.extensions_map.update({
    '.html': 'text/html; charset=utf-8',
    '.css': 'text/css; charset=utf-8',
    '.js': 'application/javascript; charset=utf-8',
})

print(f'Serving {SITE_DIR} on port {PORT}...')
server = http.server.HTTPServer(('0.0.0.0', PORT), handler)
server.serve_forever()
