"""Account read routes."""
from fastapi import APIRouter, HTTPException

from app import store
from app.models import Account

router = APIRouter(prefix="/accounts", tags=["accounts"])


@router.get("")
def list_accounts() -> list[Account]:
    return store.all_accounts()


@router.get("/{account_id}")
def get_account(account_id: str) -> Account:
    account = store.get_account(account_id)
    if account is None:
        raise HTTPException(status_code=404, detail="account not found")
    return account
