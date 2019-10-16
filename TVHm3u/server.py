
from http.server import BaseHTTPRequestHandler
from .config import TOKEN


class web_server(BaseHTTPRequestHandler):

    def __init__(self, m3u, request, client_address, server):
        self.M3U = m3u
        super().__init__(request, client_address, server)

    def usage(self):
        html = '<html><body>'
        html += f'<h1>TVHm3u HOME PAGE</h1>'
        html += '<h2>Entry Points:</h1>'
        html += '<p><b>/playlist</b> will return m3u file list of channels</p>'
        html += '<p><b>/xmltv</b> will return the EPG</p>'
        html += '<p><b>/</b> will print this message</p>'
        html += '</body></html>'
        return str.encode(html)

    def is_valid(self, token: str):
        self.log_message('Verifying Token')
        if len(token) < 6:
            return False
        return token == TOKEN

    def do_GET(self):

        try:
            uri, token = self.path.replace('token=', '').split('&')
        except ValueError:
            uri, token = (self.path, '')

        if uri == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(self.usage())
        elif (uri, self.is_valid(token)) == ('/playlist', True):
            try:
                response = self.M3U.get_m3u()
                self.send_response(200)
                self.send_header('Content-type', 'audio/x-mpegurl')
                self.end_headers()
                self.wfile.write(response)
                self.log_message('tvh m3u returned with success')
            except ConnectionRefusedError or ConnectionError:
                self.log_message("FAILED TO OBTAIN M3U")
                self.send_error(500)
        elif (uri, self.is_valid(token)) == ('/xmltv', True):
            response = self.M3U.get_xmltv()
            self.send_response(200)
            self.send_header('Content-type', 'text/xml')
            self.end_headers()
            self.log_message('xmltv epg returned with success')
            self.wfile.write(response)
        elif uri == '/favicon.ico':
            # expected just do nothing no time for creating icon
            pass
        else:
            self.log_message(f"URL {uri} NOT FOUND")
            self.send_error(404, 'Not found')
