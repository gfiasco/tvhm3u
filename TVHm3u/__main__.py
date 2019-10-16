#!/usr/bin/env python3
from http.server import HTTPServer
from .server import web_server
from .config import TVH_HOST, TVH_USER, TVH_PORT, TVH_PASS, TOKEN
from .TVAuthProxy import TVHm3u
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    # setting up
    m3u = TVHm3u(TVH_HOST, TVH_PORT, TVH_USER, TVH_PASS)
    address, port = ('', 7878)
    logging.info(f'starting web server {address} {port}/tcp with {TOKEN}')
    serve = HTTPServer((
        address, port),
        lambda *args, **kwargs: web_server(m3u, *args, **kwargs)
    )
    serve.serve_forever()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('shutting down')
        exit(0)
