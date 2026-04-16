from kiteconnect import KiteConnect
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("kx2db0cpkatmg6iz")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

kite = KiteConnect(api_key=API_KEY)
kite.set_access_token(ACCESS_TOKEN)

def get_kite():
    return kite
