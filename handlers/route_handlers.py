from flask import jsonify, request
from domain.repository.settings_interface import SettingsInterface
from domain.service.service import Service
from application.schema import SettingsSchema
from utils import to_json


def configure_routes_ordinance(app, service: Service):

    @app.route('/')
    def search_ordinances():
        _filter = request.args.get('filter')
        _filter = to_json(_filter)
        return jsonify(service.search_publications(_filter)), 200

    @app.route('/<string:id>')
    def find_ordinance(id: str):
        return jsonify(service.find_publication(id)), 200

    @app.route('/history')
    def search_ordinances_history():
        _filter = request.args.get('filter')
        _filter = to_json(_filter)
        return jsonify(service.search_publications_history(_filter)), 200

    @app.route('/history/<string:id>')
    def find_ordinance_history(id: str):
        return jsonify(service.find_publication_history(id)), 200


def configure_routes_settings(app, repo: SettingsInterface):
    schema = SettingsSchema()

    @app.route('/settings')
    def get():
        return jsonify(repo.load())

    @app.route('/settings', methods=['POST', 'PUT'])
    def save():
        data = schema.load(request.json)
        return jsonify(repo.save(data))
