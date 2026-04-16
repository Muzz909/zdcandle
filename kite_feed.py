from kiteconnect import KiteTicker

class KiteFeed:
    def __init__(self, api_key, access_token):
        self.kws = KiteTicker(api_key, access_token)
        self.ltp = None

    def start(self):
        def on_ticks(ws, ticks):
            if ticks:
                self.ltp = ticks[0]['last_price']

        def on_connect(ws, response):
            # NIFTY 50 token
            ws.subscribe([256265])
            ws.set_mode(ws.MODE_LTP, [256265])

        self.kws.on_ticks = on_ticks
        self.kws.on_connect = on_connect

        self.kws.connect(threaded=True)
