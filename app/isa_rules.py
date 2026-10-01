"""ISA allowance rules.

Today this enforces only the overall subscription allowance. The capstone
feature (see specs/cash-isa-limit/) adds the cash ISA sub-limit for under-65s
that takes effect on 6 April 2027: cash subscriptions capped at £12,000 within
the unchanged £20,000 overall allowance.
"""

from app.config import OVERALL_ALLOWANCE
from app.models import Account


class AllowanceError(ValueError):
    """Raised when a contribution would breach an ISA allowance."""


def check_contribution(account: Account, kind: str, amount: float) -> None:
    """Raise AllowanceError if the contribution is not permitted.

    Currently enforces the overall allowance only.
    TODO (capstone): enforce the £12,000 cash sub-limit for holders under 65.
    """
    if kind not in ("cash", "stocks"):
        raise AllowanceError(f"unknown contribution kind: {kind!r}")

    total_after = account.cash_subscribed + account.stocks_subscribed + amount
    if total_after > OVERALL_ALLOWANCE:
        raise AllowanceError(
            f"overall allowance exceeded: {total_after:.2f} > {OVERALL_ALLOWANCE:.2f}"
        )


def remaining_overall_allowance(account: Account) -> float:
    """Return how much of the overall ISA allowance the account has left.

    Never negative. Mirrors the overall-allowance rule enforced by
    check_contribution; the cash sub-limit (capstone) is out of scope here.
    """
    subscribed = account.cash_subscribed + account.stocks_subscribed
    return max(OVERALL_ALLOWANCE - subscribed, 0.0)
