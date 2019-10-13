# config file for tvheadend
import os

TVH_HOST = os.getenv['TVH_HOST'] or 'localhost'
TVH_PORT = int(os.getenv['TV_HOST']) or 9981
TVH_USER = os.getenv['TVH_USER'] or 'test'
TVH_PASS = os.getenv['TVH_PASS'] or '123456'
