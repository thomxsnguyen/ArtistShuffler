import spotipy
import uvicorn
import os
import urllib.parse
import secrets

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth


#uvicorn main:app --reload

app = FastAPI()

SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")
SCOPE = os.getenv("SCOPE")

sp_oauth = SpotifyOAuth(
  client_id=SPOTIFY_CLIENT_ID,
  client_secret=SPOTIFY_CLIENT_ID,
  redirect_uri=REDIRECT_URI,
  scope=SCOPE
)

@app.get("/")
async def home():
  state = secrets.token_urlsafe(16)

  params = {'response_type': 'code', 'client_id':SPOTIFY_CLIENT_ID, 'scope': SCOPE, 'redirect_uri': REDIRECT_URI, 'state': state}
  url = 'https://accounts.spotify.com/authorize?' + urllib.parse.urlencode(params)
  return RedirectResponse(url=url)

if __name__ == "__main__":
  uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)