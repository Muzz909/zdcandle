from kiteconnect import KiteTicker
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

class KiteFeed:
    def __init__(self):
        self.kws = KiteTicker(API_KEY, ACCESS_TOKEN)
        self.ltp = None

    def start(self):
        def on_ticks(ws, ticks):
            if ticks:
                self.ltp = ticks[0]['last_price']

        def on_connect(ws, response):
            ws.subscribe([256265])  # NIFTY
            ws.set_mode(ws.MODE_LTP, [256265])

        self.kws.on_ticks = on_ticks
        self.kws.on_connect = on_connect

        self.kws.connect(threaded=True)
