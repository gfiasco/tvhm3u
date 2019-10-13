
from http.server import BaseHTTPRequestHandler
from .TVAuthProxy import TVHm3u
from .config import TVH_HOST, TVH_USER, TVH_PORT, TVH_PASS

M3U = TVHm3u(TVH_HOST, TVH_PORT, TVH_USER, TVH_PASS)


class web_server(BaseHTTPRequestHandler):

    def usage(self):
        html = '<html><body>'
        html += f'<h1>TVHm3u HOME PAGE {TVH_HOST} on {TVH_PORT}/tcp</h1>'
        html += '<h2>Entry Points:</h1>'
        html += '<p><b>/playlist</b> will return m3u file list of channels</p>'
        html += '<p><b>/xmltv</b> will return the EPG</p>'
        html += '<p><b>/</b> will print this message</p>'
        html += '</body></html>'
        return str.encode(html)

    def do_GET(self):

        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(self.usage())
        elif self.path == '/playlist':
            try:
                response = M3U.get_m3u()
                self.send_response(200)
                self.send_header('Content-type', 'audio/x-mpegurl')
                self.end_headers()
                self.wfile.write(response)
                self.log_message('tvh m3u returned with success')
            except ConnectionRefusedError:
                self.log_message("FAILED TO OBTAIN M3U")
        elif self.path == '/xmltv':
            response = M3U.get_xmltv()
            self.send_response(200)
            self.send_header('Content-type', 'text/xml')
            self.end_headers()
            print(response)
            self.wfile.write(response)
        elif self.path == '/favicon.ico':
            # expected just do nothing no time for creating icon
            pass
        else:
            self.log_message(f"URL {self.path} NOT FOUND")
            self.send_error(404, 'Not found')
