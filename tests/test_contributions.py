"""Contribution + overall-allowance behaviour (passes on a fresh checkout).

There is deliberately NO test here for the £12,000 cash sub-limit — that is the
capstone feature. tests/test_isa_limit.py is written as part of the spec demo.
"""


def test_cash_contribution_succeeds(client):
    r = client.post("/contributions", json={"account_id": "ACC-003", "kind": "cash", "amount": 100.0})
    assert r.status_code == 200
    assert r.json()["cash_subscribed"] == 600.0


def test_overall_allowance_enforced(client):
    # ACC-001 has 12,000 subscribed; another 9,000 would exceed 20,000 overall.
    r = client.post("/contributions", json={"account_id": "ACC-001", "kind": "stocks", "amount": 9_000.0})
    assert r.status_code == 422
    assert "overall allowance" in r.json()["detail"]


def test_unknown_account_404(client):
    r = client.post("/contributions", json={"account_id": "NOPE", "kind": "cash", "amount": 1.0})
    assert r.status_code == 404
