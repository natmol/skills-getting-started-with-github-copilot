import pytest
from fastapi.testclient import TestClient

from src.app import app


@pytest.fixture
def client():
    """Synchronous TestClient fixture for the ASGI app.

    Keeps tests simple and avoids requiring async test plugins in the environment.
    """
    with TestClient(app) as c:
        yield c
