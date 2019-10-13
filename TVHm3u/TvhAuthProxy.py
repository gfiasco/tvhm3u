#!/usr/bin/env python3
import requests
from requests.auth import HTTPBasicAuth

from .config import *

def get_tvh_playlist():
    playlist_url=f'{TV_URL}/playlist/channels'
    auth=HTTPBasicAuth(TV_USER, TV_PASS)
    requests.get(TV_URL, auth=auth)