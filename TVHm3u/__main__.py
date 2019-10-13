#!/usr/bin/env python3
from http.server import HTTPServer
from .server import web_server


def main():
    serve = HTTPServer(('', 7878), web_server)
    serve.serve_forever()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('shutting down')
        exit(0)
