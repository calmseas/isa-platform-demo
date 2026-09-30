"""Platform fee calculation.

PLANTED BUG (for the /goal demo): the fee is computed with binary floating point
and rounded with the built-in round(), which mis-rounds values that land on a
half-penny boundary (e.g. 125 * 0.005 == 0.625 rounds to 0.62, not 0.63).
tests/test_fees.py fails because of this. The fix is to compute with Decimal and
round ROUND_HALF_UP. See PRESENTER.md.
"""

PLATFORM_FEE_RATE = 0.005  # 0.5% per year


def annual_platform_fee(balance: float) -> float:
    # BUG: float arithmetic + round() loses half-pennies.
    return round(balance * PLATFORM_FEE_RATE, 2)
