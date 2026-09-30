"""In-memory account store with seed data. Resets on process restart."""
from app.models import Account

_ACCOUNTS: dict[str, Account] = {}


def _seed() -> None:
    _ACCOUNTS.clear()
    for acc in [
        Account(id="ACC-001", holder="Ada Vaughan", age=41, balance=18_400.0,
                cash_subscribed=9_000.0, stocks_subscribed=3_000.0),
        Account(id="ACC-002", holder="Bram Ellison", age=68, balance=52_100.0,
                cash_subscribed=11_500.0, stocks_subscribed=0.0),
        Account(id="ACC-003", holder="Chidi Okonjo", age=29, balance=535.0,
                cash_subscribed=500.0, stocks_subscribed=0.0),
    ]:
        _ACCOUNTS[acc.id] = acc


_seed()


def all_accounts() -> list[Account]:
    return list(_ACCOUNTS.values())


def get_account(account_id: str) -> Account | None:
    return _ACCOUNTS.get(account_id)


def upsert(account: Account) -> None:
    _ACCOUNTS[account.id] = account


def reset() -> None:
    _seed()
