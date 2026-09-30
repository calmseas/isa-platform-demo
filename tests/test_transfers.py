"""Transfer route auth + behaviour (passes on a fresh checkout).

Confirms the transfers router IS protected — the decoy in the auth-audit demo.
"""


def test_transfer_requires_admin(client):
    r = client.post("/transfers", json={"from_account": "ACC-002", "to_account": "ACC-003", "amount": 10.0})
    assert r.status_code == 401


def test_transfer_succeeds_with_admin(client, admin_headers):
    r = client.post(
        "/transfers",
        json={"from_account": "ACC-002", "to_account": "ACC-003", "amount": 10.0},
        headers=admin_headers,
    )
    assert r.status_code == 200
