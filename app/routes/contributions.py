"""Contribution route — applies ISA allowance rules."""
from fastapi import APIRouter, HTTPException

from app import store
from app.isa_rules import AllowanceError, check_contribution
from app.models import ContributionRequest, ContributionResult

router = APIRouter(prefix="/contributions", tags=["contributions"])


@router.post("")
def contribute(req: ContributionRequest) -> ContributionResult:
    account = store.get_account(req.account_id)
    if account is None:
        raise HTTPException(status_code=404, detail="account not found")

    try:
        check_contribution(account, req.kind, req.amount)
    except AllowanceError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc

    if req.kind == "cash":
        account.cash_subscribed += req.amount
    else:
        account.stocks_subscribed += req.amount
    account.balance += req.amount
    store.upsert(account)

    return ContributionResult(
        account_id=account.id,
        kind=req.kind,
        amount=req.amount,
        cash_subscribed=account.cash_subscribed,
        stocks_subscribed=account.stocks_subscribed,
        total_subscribed=account.cash_subscribed + account.stocks_subscribed,
    )
