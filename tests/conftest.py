from starlette.testclient import TestClient

from src.controllers.registrable_controller import app

import pytest


@pytest.fixture(scope="module")
def test_app() -> object:
    client = TestClient(app)
    yield client
