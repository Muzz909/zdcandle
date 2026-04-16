import streamlit as st
from kite_auth import get_login_url, generate_access_token
from kite_feed import KiteFeed
from candle_engine import CandleEngine
import time

API_KEY = "kx2db0cpkatmg6iz"

st.title("📊 Candle Engine (Zerodha)")

# STEP 1: HANDLE LOGIN
query_params = st.query_params
request_token = query_params.get("request_token")

if "access_token" not in st.session_state:

    if not request_token:
        login_url = get_login_url()
        st.markdown(f"[Login with Zerodha]({login_url})")
        st.stop()

    else:
        access_token = generate_access_token(request_token)
        st.session_state["access_token"] = access_token
        st.success("Login successful!")

# STEP 2: START FEED
if "feed" not in st.session_state:
    feed = KiteFeed(API_KEY, st.session_state["access_token"])
    feed.start()
    st.session_state["feed"] = feed
    st.session_state["engine"] = CandleEngine()

feed = st.session_state["feed"]
engine = st.session_state["engine"]

st.subheader("Live Data")

placeholder = st.empty()

# STEP 3: LOOP
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
