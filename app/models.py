"""Pydantic models for the demo API."""

from pydantic import BaseModel, Field


class Account(BaseModel):
    id: str
    holder: str
    age: int
    balance: float = 0.0
    cash_subscribed: float = 0.0
    stocks_subscribed: float = 0.0


class ContributionRequest(BaseModel):
    account_id: str
    kind: str = Field(description="'cash' or 'stocks'")
    amount: float = Field(gt=0)


class TransferRequest(BaseModel):
    from_account: str
    to_account: str
    amount: float = Field(gt=0)


class ContributionResult(BaseModel):
    account_id: str
    kind: str
    amount: float
    cash_subscribed: float
    stocks_subscribed: float
    total_subscribed: float


class AllowanceStatus(BaseModel):
    account_id: str
    overall_allowance: float
    total_subscribed: float
    remaining: float
