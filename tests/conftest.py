import pytest
from fastapi.testclient import TestClient

from app import store
from app.config import ADMIN_KEY
from app.main import app


@pytest.fixture()
def client():
    store.reset()
    return TestClient(app)


@pytest.fixture()
def admin_headers():
    return {"x-api-key": ADMIN_KEY}
