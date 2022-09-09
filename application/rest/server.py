from flask import Flask
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler

from infrastructure.database import get_database
from infrastructure.repository import Repository, SettingsRepository, Publisher
from domain.service import Service
from .encoder import CustomJsonEncoder
from .resources import publications, settings
from .jobs import get_ordinance_notifier
from .error import error_bp
from .security import Authorization, Role


API_PREFIX = '/api/v1/ordinances'


def create_server(config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.json_encoder = CustomJsonEncoder
    app.config['JSON_SORT_KEYS'] = False
    app.register_blueprint(error_bp)
    db = get_database(config.MONGODB_SETTINGS)

    CORS(app)

    auth = Authorization(config.INTROSPECTION_URI)
    auth.grant_role_for_any_request(Role.ADMIN)

    repository = Repository(db)
    service = Service(repository)
    bp = publications.get_blueprint(auth, service)
    app.register_blueprint(bp, url_prefix=API_PREFIX)

    settings_repo = SettingsRepository(db)
    settings_bp = settings.get_blueprint(settings_repo)
    auth.require_authorization_for_any_request(settings_bp)
    app.register_blueprint(settings_bp, url_prefix=API_PREFIX)

    publisher = Publisher({
        'bootstrap.servers': config.KAFKA_SERVER,
        'client.id': 'ORDINANCE',
        'message.max.bytes': 33554432
    })

    notifier = get_ordinance_notifier(repository, settings_repo, publisher)
    scheduler = BackgroundScheduler()
    scheduler.add_job(notifier, 'interval', seconds=config.SCHEDULE_INTERVAL)
    # scheduler.start()

    return app
