import streamlit as st
from kite_feed import KiteFeed
from candle_engine import CandleEngine
import time

st.title("📊 Candle Engine")

feed = KiteFeed()
feed.start()

engine = CandleEngine()

placeholder = st.empty()

for _ in range(1000):
    if feed.ltp:
        closed = engine.update(feed.ltp)

        with placeholder.container():
            st.write("LTP:", feed.ltp)

            if engine.current:
                st.write("Current Candle:", engine.current)

            if closed:
                st.write("Closed Candle:", closed)

    time.sleep(1)
