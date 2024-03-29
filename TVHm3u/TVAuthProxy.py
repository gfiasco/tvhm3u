#!/usr/bin/env python3

import requests
from requests.auth import HTTPBasicAuth
from typing import Union


class TVHm3u:
    """ M3U formatter for tvheadend
        TV_HOST: hostname/ip tvh server
        TVH_PORT: tcp port tvh server
        TV_USER: username tvh
        TV_PASS: password tvh user
    """

    def __init__(
            self,
            TVH_HOST: str,
            TVH_PORT: Union[str, int],
            TVH_USER: str,
            TVH_PASS: str
    ) -> None:
        self.tvh_host = TVH_HOST
        self.tvh_port = TVH_PORT
        self.tvh_url = f'{TVH_HOST}:{TVH_PORT}'
        self.tvh_user = TVH_USER
        self.tvh_pass = TVH_PASS

    def error(self, response, target=None) -> None:
        if response.status_code not in (200, 300):
            raise ConnectionRefusedError(
                'TVH service seems unreachable: {target}')

    def get_m3u(self, nat_address=None) -> bytes:
        m3u = self._get_playlist()
        url = nat_address or self.tvh_url
        new_m3u = ""
        for line in m3u.split('\n'):
            if line.startswith(f'http://{self.tvh_url}'):
                new_m3u += line.replace(
                    f'http://{self.tvh_url}',
                    f'http://{self.tvh_user}:{self.tvh_pass}' +
                    f'@{url}:{self.tvh_port}'
                ) + '\n'
            else:
                new_m3u += line + '\n'

        return str.encode(new_m3u)

    def get_xmltv(self) -> bytes:
        playlist_url = f'http://{self.tvh_url}/xmltv'
        auth = HTTPBasicAuth(self.tvh_user, self.tvh_pass)
        response = requests.get(playlist_url, auth=auth)
        self.error(response, __name__)
        return response.content

    def _get_playlist(self) -> str:
        """ get default tvheadend playlist """
        playlist_url = f'http://{self.tvh_url}/playlist/channels.m3u'
        auth = HTTPBasicAuth(self.tvh_user, self.tvh_pass)
        response = requests.get(playlist_url, auth=auth)
        self.error(response, __name__)
        return response.text
