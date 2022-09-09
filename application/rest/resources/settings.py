from flask import Blueprint, request
from flask.json import jsonify

from domain.repository import SettingsInterface
from ...schema import SettingsSchema


def get_blueprint(repo: SettingsInterface) -> Blueprint:
    bp = Blueprint('Settings', __name__)
    schema = SettingsSchema()

    @bp.get('/settings')
    def get():
        return jsonify(repo.load())

    @bp.route('/settings', methods=['POST', 'PUT'])
    def save():
        data = schema.load(request.json)
        return jsonify(repo.save(data))

    return bp
