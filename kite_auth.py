from kiteconnect import KiteConnect

API_KEY = "kx2db0cpkatmg6iz"
API_SECRET = "v7ere5zlfqqgqafuxroyeeq06ioaucp9"

kite = KiteConnect(api_key=API_KEY)

def get_login_url():
    return kite.login_url()

def generate_access_token(request_token):
    data = kite.generate_session(request_token, api_secret=API_SECRET)
    return data["access_token"]
