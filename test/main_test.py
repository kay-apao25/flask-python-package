import pytest
from flask import Flask

from scripts.app import mod_app

application = Flask(__name__)
application.register_blueprint(app)


@pytest.fixture
def app():
    application.testing = True
    return application.test_client()


def test_index(app):
    r = app.get('/')
    assert r.status_code == 200
