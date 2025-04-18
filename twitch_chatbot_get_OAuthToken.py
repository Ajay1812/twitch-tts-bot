import requests
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

def get_oauth_token():
    url = "https://id.twitch.tv/oauth2/token"
    params = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "client_credentials",
        "scope": "chat:read chat:edit"
    }

    response = requests.post(url, params=params)
    data = response.json()

    if 'access_token' in data:
        token = data['access_token']
        print(f"✅ Token: oauth:{token}")
        return f"oauth:{token}"
    else:
        print("❌ Error:", data)
        return None

get_oauth_token()
