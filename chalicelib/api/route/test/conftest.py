import pytest
from chalice.test import Client

from app import app as flask_app


@pytest.fixture()
def client():
    yield Client(flask_app)
