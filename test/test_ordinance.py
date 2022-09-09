from uuid import uuid1
import pytest
from flask import Flask
from domain.service.service import Service
from infrastructure.database import get_database
from infrastructure.repository import (
    Repository,
    SettingsRepository
)
from handlers.route_handlers import (
    configure_routes_ordinance,
    configure_routes_settings
)
from . import TestConfig as config


db = get_database(config.MONGODB_SETTINGS)
repository = Repository(db)
service = Service(repository)
settings_repo = SettingsRepository(db)


@pytest.fixture
def clientinstance():
    app = Flask(__name__)
    configure_routes_ordinance(app, service)
    configure_routes_settings(app, settings_repo)
    return app.test_client()


def _test_route_ordinance(clientinstance):
    url = '/'

    response = clientinstance.get(url)
    assert response.get_data() != b''
    assert response.status_code == 200


def _test_ordinance_id(clientinstance):
    url = '/'

    response = clientinstance.get(url)
    assert response.get_data() != b''
    assert response.status_code == 200


def _test_history_route(clientinstance):
    url = '/history'

    response = clientinstance.get(url)
    assert response.get_data() != b''
    assert response.status_code == 200


def _test_history_id(clientinstance):
    url = '/history'

    response = clientinstance.get(url)
    assert response.get_data() != b''
    assert response.status_code == 200


def _test_settings_route(clientinstance):
    url = '/settings'

    response = clientinstance.get(url)
    assert response.get_data() != b''
    assert response.status_code == 200


def _test_settings_post(clientinstance):
    url = '/settings'

    mjson = {
        'template_id': uuid1(),
        'subject': ""
    }

    response = clientinstance.post(url, json=mjson)
    assert response.status_code == 200
