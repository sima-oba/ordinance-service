from flask import jsonify, Blueprint, request

from application.rest.security import Authorization, Role
from application.schema import PublicationQuery
from domain.service import Service
from utils import export_feature_collection


def get_blueprint(auth: Authorization, service: Service) -> Blueprint:  # noqa
    bp = Blueprint('ordinance', __name__)
    publication_query = PublicationQuery()

    def _search_publications():
        query = publication_query.load(request.args)

        user = auth.current_user

        if user and user.doc:
            query['owner_doc'] = user.doc

        return service.search_publications(query)

    @bp.get('/')
    @auth.require_role(Role.READ_ORDINANCES)
    def search_publications():
        ordinances = _search_publications()
        return jsonify(ordinances), 200

    @bp.get('/geojson')
    @auth.require_role(Role.READ_ORDINANCES)
    def search_publications_geojson():
        publications = _search_publications()
        publications_with_geometry = []

        for ordinance in publications:
            data = ordinance.asdict()
            details = data.pop('details', {})
            data['geometry'] = {
                'type': 'Point',
                'coordinates': [details.get('lon'), details.get('lat')]
            }
            publications_with_geometry.append(data)

        features = export_feature_collection(publications_with_geometry)
        return jsonify(features), 200

    @bp.get('/<string:id>')
    @auth.require_role(Role.READ_ORDINANCES)
    def find_publications(id: str):
        return jsonify(service.find_publication(id)), 200

    return bp
