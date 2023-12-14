from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from starlette_authlib.middleware import AuthlibMiddleware as SessionMiddleware
from starlette.responses import HTMLResponse
from fastapi.testclient import TestClient
from app.settings import get_settings
import os

app = FastAPI()

app.add_middleware(
    SessionMiddleware,
    secret_key  = get_settings().SECRET_KEY,
    max_age = 60 * get_settings().ACCESS_TOKEN_EXPIRATION_MINUTES,
    session_cookie = "session_id",
    domain = get_settings().HOST
)

app.add_middleware(
    CORSMiddleware,
    allow_origins = [
        "http://localhost:3000",
        "http://localhost"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def main(request: Request):
    urls = [{"path": route.path, "name": route.name} for route in request.app.routes]
    return {
        "message": "Hello World",
        "env": os.getenv("ENVIROMENT", "development"),
        "urls": urls
    }

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()['env'] == 'development'
