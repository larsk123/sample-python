import os
import http.server
import socketserver

from http import HTTPStatus


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        msg = 'Hello Lars today is Thursday number 3 and also Friday! you requested %s' % (self.path)
        self.wfile.write(msg.encode())
        print('hullu lurz on friday')

port = int(os.getenv('PORT', 80))
print('Listening Lars on port %s' % (port))
httpd = socketserver.TCPServer(('', port), Handler)
httpd.serve_forever()
