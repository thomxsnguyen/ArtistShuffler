import uvicorn
import os
import urllib.parse
import secrets
import httpx


from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, JSONResponse, HTMLResponse
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
from utils import token_utils


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
  return {'message': 'Backend API is running'}

@app.get('/login')
async def login(request: Request):
  state = secrets.token_urlsafe(16)

  params = {'response_type': 'code', 'client_id':SPOTIFY_CLIENT_ID, 'scope': SCOPE, 'redirect_uri': REDIRECT_URI, 'state': state}
  url = 'https://accounts.spotify.com/authorize?' + urllib.parse.urlencode(params)
  return RedirectResponse(url=url)

@app.get('/callback')
async def callback(request: Request):
  code = request.query_params.get('code')
  state = request.query_params.get('state')
  
  if not state:
    return JSONResponse(content={'error': 'state_mismatch'}, status_code=400)
  else:
    async with httpx.AsyncClient() as client:
      response = await client.post(
        "https://accounts.spotify.com/api/token"
      ,data={'code':code,
            'redirect_uri':REDIRECT_URI, 
            'grant_type': 'authorization_code'},
  
      headers={
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': token_utils.get_basic_auth_header(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)
              })
      
  token_data = response.json()
  access_token = token_data.get('access_token')

  return RedirectResponse(url=f'http://127.0.0.1:8000/#access_token={access_token}')
    
  

  



if __name__ == "__main__":
  uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)