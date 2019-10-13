
from http.server import BaseHTTPRequestHandler, HTTPServer
from .TVAuthProxy import TVHm3u
from .config import *
import logging

M3U = TVHm3u(TVH_HOST, TVH_PORT, TVH_USER, TVH_PASS)


class web_server(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/playlist':
            try:
                response = M3U.get_m3u()
                self.send_response(200)
                self.send_header('Content-type', 'audio/x-mpegurl')
                self.end_headers()
                self.wfile.write(response)
                self.log_message('tvh m3u returned with success')
            except:
                self.log_message("FAILED TO OBTAIN M3U")
        elif self.path == '/xmltv':
            response = M3U.get_xmltv()
            self.send_response(200)
            self.send_header('Content-type', 'text/xml')
            self.end_headers()
            print(response)
            self.wfile.write(response)
        elif self.path == '/favicon.ico':
            #expected just do nothing no time for creating icon
            pass
        else:
            self.log_message("URL {} NOT FOUND".format(self.path))
            self.send_error(404,'Not found')

