"""Admin routes.

PLANTED VULNERABILITY (for the security-review / workflow-audit demo): the
`/admin/export` route dumps every account — including balances — but is missing
the `require_admin` dependency that the other admin routes carry. No test covers
it; a human review or the security-reviewer agent should catch it.

The fix is to add `dependencies=[Depends(require_admin)]` to the route (or the
router, like transfers.py does).
"""
from fastapi import APIRouter, Depends

from app import store
from app.auth import require_admin
from app.models import Account

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/summary", dependencies=[Depends(require_admin)])
def summary() -> dict[str, float]:
    accounts = store.all_accounts()
    return {
        "accounts": float(len(accounts)),
        "total_balance": sum(a.balance for a in accounts),
    }


@router.get("/export")  # BUG: no require_admin — leaks every account unauthenticated
def export_accounts() -> list[Account]:
    return store.all_accounts()


@router.post("/reset", dependencies=[Depends(require_admin)])
def reset() -> dict[str, str]:
    store.reset()
    return {"status": "reset"}
