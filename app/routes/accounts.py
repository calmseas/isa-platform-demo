"""Account read routes."""

from fastapi import APIRouter, HTTPException

from app import store
from app.config import OVERALL_ALLOWANCE
from app.isa_rules import remaining_overall_allowance
from app.models import Account, AllowanceStatus

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


@router.get("/{account_id}/allowance")
def get_allowance(account_id: str) -> AllowanceStatus:
    account = store.get_account(account_id)
    if account is None:
        raise HTTPException(status_code=404, detail="account not found")
    return AllowanceStatus(
        account_id=account.id,
        overall_allowance=OVERALL_ALLOWANCE,
        total_subscribed=account.cash_subscribed + account.stocks_subscribed,
        remaining=remaining_overall_allowance(account),
    )
