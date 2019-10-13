#!/usr/bin/env python3

import requests
from requests.auth import HTTPBasicAuth


class TVHm3u:
    """ M3U formatter for tvheadend
        TV_HOST: hostname/ip tvh server
        TVH_PORT: tcp port tvh server
        TV_USER: username tvh
        TV_PASS: password tvh user
    """

    def __init__(self, TVH_HOST: str, TVH_PORT: int, TVH_USER: str, TVH_PASS: str):
        self.tvh_host = TVH_HOST
        self.tvh_port = TVH_PORT
        self.tvh_url = f'http://{TVH_HOST}:{TVH_PORT}'
        self.tvh_user = TVH_USER
        self.tvh_pass = TVH_PASS

    def error(self, response, target=None) -> None:
        if response.status_code not in (200,300):
            raise ConnectionRefusedError('TVH service seems unreachable: {target}')

    def get_m3u(self) -> bytes:
        m3u = self._get_playlist()
        new_m3u = ""
        for line in m3u.split('\n'):
            if line.startswith(self.tvh_url):
                new_m3u += line.replace(
                    self.tvh_url,
                    f'http://{self.tvh_user}:{self.tvh_pass}@{self.tvh_host}:{self.tvh_port}'
                ) + '\n'
            else:
                new_m3u += line + '\n'

        return new_m3u

    def get_xmltv(self) -> bytes:
        playlist_url = f'{self.tvh_url}/xmltv'
        auth = HTTPBasicAuth(self.tvh_user, self.tvh_pass)
        response = requests.get(playlist_url, auth=auth)
        self.error(response, __name__)
        return response.content

    def _get_playlist(self):
        """
            get default tvheadend playlist
        """
        playlist_url = f'{self.tvh_url}/playlist/channels.m3u'
        auth = HTTPBasicAuth(self.tvh_user, self.tvh_pass)
        response = requests.get(playlist_url, auth=auth)
        self.error(response, __name__)
        return response.text


