#!/usr/bin/env python3
from http.server import HTTPServer
from .server import web_server
from .config import TVH_HOST, TVH_USER, TVH_PORT, TVH_PASS, TOKEN
from .TVAuthProxy import TVHm3u
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def run():
    # setting up
    m3u = TVHm3u(TVH_HOST, TVH_PORT, TVH_USER, TVH_PASS)
    address, port = ('', 7878)
    logging.info(f'starting web server {address} {port}/tcp with {TOKEN}')
    serve = HTTPServer((
        address, port),
        lambda *args, **kwargs: web_server(m3u, *args, **kwargs)
    )
    try:
        serve.serve_forever()
    except KeyboardInterrupt:
        logging.info('shutting down...')
        serve.server_close()
        exit(0)


if __name__ == "__main__":
    run()
