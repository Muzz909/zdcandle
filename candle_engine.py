import datetime

class CandleEngine:
    def __init__(self):
        self.current = None
        self.candles = []

    def update(self, price):
        now = datetime.datetime.now()
        minute = now.replace(second=0, microsecond=0)

        if not self.current:
            self.current = {
                "time": minute,
                "open": price,
                "high": price,
                "low": price,
                "close": price
            }
            return None

        if minute != self.current["time"]:
            closed = self.current
            self.candles.append(closed)

            self.current = {
                "time": minute,
                "open": price,
                "high": price,
                "low": price,
                "close": price
            }
            return closed

        self.current["high"] = max(self.current["high"], price)
        self.current["low"] = min(self.current["low"], price)
        self.current["close"] = price

        return None
