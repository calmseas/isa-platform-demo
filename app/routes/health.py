"""Health check. Public by design — a decoy for the auth-audit demo:
it looks unauthenticated because it is, and that is correct.
"""
from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
