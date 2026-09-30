"""Minimal API-key auth for admin routes.

`require_admin` is a FastAPI dependency: attach it to a route (or a router) and
the request must carry a matching `x-api-key` header. The demo's planted
vulnerability is a route that forgets to attach it — see app/routes/admin.py.
"""
from fastapi import Header, HTTPException, status

from app.config import ADMIN_KEY


def require_admin(x_api_key: str = Header(default="")) -> None:
    if x_api_key != ADMIN_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="admin API key required",
        )
