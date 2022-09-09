from pymongo.database import Database
from typing import List, Optional

from domain.model import Publication, PublicationType, Owner
from domain.repository import RepositoryInterface


class Repository(RepositoryInterface):
    def __init__(self, database: Database):
        self._publications = database.get_collection('publications')
        self._owners = database.get_collection('owners')

    def create_ordinance(self, ordinance: Publication):
        doc = self._ordinance_to_doc(ordinance)
        self._publications.insert_one(doc)

    def update_ordinance(self, ordinance: Publication):
        doc = self._ordinance_to_doc(ordinance)
        self._publications.replace_one({'_id': ordinance._id}, doc)

    def _ordinance_to_doc(self, ordinance: Publication) -> dict:
        doc = ordinance.asdict()
        doc['ordinance_type'] = ordinance.ordinance_type.name
        return doc

    def find_ordinance_by_id(self, _id: str) -> Optional[Publication]:
        doc = self._publications.find_one({'_id': _id})
        return self._doc_to_ordinance(doc) if doc else None

    def find_ordinance_by_number(self, number: str) -> Optional[Publication]:
        doc = self._publications.find_one({'ordinance_number': number})
        return self._doc_to_ordinance(doc) if doc else None

    def ordinance_exists(self, number: str, issuer: str) -> bool:
        doc = self._publications.find_one({
            'ordinance_number': number,
            'issuer': issuer
        })
        return doc is not None

    def search_ordinances(self, query: dict) -> List[Publication]:
        _filter = {}

        if query.get('ordinance_type'):
            _filter['ordinance_type'] = query['ordinance_type'].name

        if query.get('publish_start') or query.get('publish_end'):
            _filter['publish_date'] = {}

            if query.get('publish_start'):
                _filter['publish_date']['$gte'] = query['publish_start']

            if query.get('publish_end'):
                _filter['publish_date']['$lte'] = query['publish_end']

        if query.get('owner_doc'):
            _filter['owner_doc'] = query['owner_doc']

        docs = self._publications.find(_filter)
        return [self._doc_to_ordinance(doc) for doc in docs]

    def _doc_to_ordinance(self, doc: dict) -> Publication:
        doc['ordinance_type'] = PublicationType[doc['ordinance_type']]
        return Publication.from_dict(doc)

    def create_owner(self, owner: Owner):
        self._owners.insert_one(owner.asdict())

    def update_owner(self, owner: Owner):
        self._owners.replace_one({'_id': owner._id}, owner.asdict())

    def find_owner_by_id(self, _id: str) -> Optional[Owner]:
        doc = self._owners.find_one({'_id': _id})
        return Owner.from_dict(doc) if doc else None

    def find_owner_by_doc(self, doc: str) -> Optional[Owner]:
        doc = self._owners.find_one({'doc': doc})
        return Owner.from_dict(doc) if doc else None
