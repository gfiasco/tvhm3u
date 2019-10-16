# config file for tvheadend
import os
import secrets

TVH_HOST = os.getenv('TVH_HOST') or 'localhost'
TVH_PORT = os.getenv('TVH_PORT') or 9981
TVH_USER = os.getenv('TVH_USER') or 'test'
TVH_PASS = os.getenv('TVH_PASS') or '123456'
TOKEN = os.getenv('TOKEN') or secrets.token_urlsafe(16)
NAT = eval(os.getenv('NAT'))
