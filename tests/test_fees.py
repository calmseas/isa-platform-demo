"""Fee rounding.

This test FAILS on a fresh checkout: annual_platform_fee(125) returns 0.62
because of float rounding, but the correct half-penny-up result is 0.63. Fixing
app/fees.py to use Decimal + ROUND_HALF_UP makes it pass. This is the target for
the /goal demo:

    /goal tests/test_fees.py passes, output shown; no other files change; or stop after 15 turns
"""
from app.fees import annual_platform_fee


def test_fee_rounds_half_penny_up():
    # 125 * 0.005 == 0.625 -> should round to 0.63
    assert annual_platform_fee(125.0) == 0.63


def test_fee_simple_case():
    assert annual_platform_fee(10_000.0) == 50.0
