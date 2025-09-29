# Simple dev server to serve the generated site and dispatch events to Python callbacks.
import os, json
from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
from io import BytesIO

# import example builder
from examples.ultra_test import build_site

site = build_site()

INDEX_HTML = site.render()

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path in ['/', '/index.html']:
            self.send_response(200)
            self.send_header('Content-type','text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(INDEX_HTML.encode('utf-8'))
            return
        return super().do_GET()

    def do_POST(self):
        if self.path == '/event':
            length = int(self.headers.get('content-length', 0))
            body = self.rfile.read(length)
            try:
                payload = json.loads(body.decode('utf-8'))
            except:
                payload = {}
            ident = payload.get('id')
            action = payload.get('action')
            req = payload
            resp = {{'ok':True}}
            # dispatch to registered handler if exists
            cb = site.event_registry.get(ident)
            if cb:
                try:
                    out = cb(req, site)
                    if out: resp.update(out)
                except Exception as e:
                    resp.update({'ok':False, 'error':str(e)})
            else:
                resp.update({'ok':False, 'error':'no-handler'})
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()
            self.wfile.write(json.dumps(resp).encode('utf-8'))
            return
        self.send_response(404)
        self.end_headers()

def run(addr='127.0.0.1', port=8000):
    print(f'Running dev server at http://{{addr}}:{{port}} - ctrl+c to stop')
    httpd = HTTPServer((addr, port), Handler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Shutting down...')

if __name__ == '__main__':
    run()
