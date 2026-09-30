"""Transfer route.

DECOY for the auth-audit demo: the handler below has no auth check in its own
body, so a quick skim reads as unprotected. It is not — the router is created
with a router-level dependency, so require_admin runs before every route here.
A careful review (or the security-reviewer agent) should clear this, not flag it.
"""
from fastapi import APIRouter, Depends, HTTPException

from app import store
from app.auth import require_admin
from app.models import TransferRequest

router = APIRouter(
    prefix="/transfers",
    tags=["transfers"],
    dependencies=[Depends(require_admin)],  # guards every route in this router
)


@router.post("")
def transfer(req: TransferRequest) -> dict[str, str]:
    src = store.get_account(req.from_account)
    dst = store.get_account(req.to_account)
    if src is None or dst is None:
        raise HTTPException(status_code=404, detail="account not found")
    if src.balance < req.amount:
        raise HTTPException(status_code=422, detail="insufficient balance")
    src.balance -= req.amount
    dst.balance += req.amount
    store.upsert(src)
    store.upsert(dst)
    return {"status": "ok"}
