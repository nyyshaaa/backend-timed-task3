
from fastapi import APIRouter, Depends, HTTPException, Query, Request
from fastapi.responses import RedirectResponse
from src.config import settings
from src.spotify.auth import get_access_token, refresh_access_token

