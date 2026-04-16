from flask import Flask, request
from kiteconnect import KiteConnect
from dotenv import load_dotenv, set_key
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

app = Flask(__name__)
kite = KiteConnect(api_key=API_KEY)

@app.route("/")
def login():
    request_token = request.args.get("request_token")

    if not request_token:
        return f'<a href="{kite.login_url()}">Login with Zerodha</a>'

    try:
        data = kite.generate_session(request_token, api_secret=API_SECRET)
        access_token = data["access_token"]

        # Save token
        set_key(".env", "ACCESS_TOKEN", access_token)

        return "<h2>✅ Token saved. You can close this.</h2>"

    except Exception as e:
        return f"<h2>Error ❌</h2><p>{str(e)}</p>"

if __name__ == "__main__":
    app.run(port=8000)
