import pytest

from app import app as flask_app


@pytest.fixture()
def app():
    app = flask_app
    app.config.update(
        {
            "TESTING": True,
        }
    )
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()
