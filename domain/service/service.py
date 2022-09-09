import logging
from typing import List

from domain.exception import EntityNotFound
from domain.model import Publication, Owner
from domain.repository import RepositoryInterface


class Service:
    def __init__(self, repo: RepositoryInterface):
        self._repo = repo
        self._log = logging.getLogger(self.__class__.__name__)

    def create_publication(self, data: dict):
        owner = self._repo.find_owner_by_doc(data['owner_doc'])
        ord_number = data['ordinance_number']

        if owner is None:
            self._log.debug(f'Owner with doc {data["owner_doc"]} not found')
            return

        if self._repo.ordinance_exists(ord_number, data['issuer']):
            self._log.warn(f'Publication {ord_number} already exists')
            return

        data['title'] = data['ordinance_type'].value
        data['owner_name'] = owner.name
        ordinance = Publication.new(data)

        self._repo.create_ordinance(ordinance)
        self._log.debug(f'Added ordinance {ordinance.ordinance_number}')

    def find_publication(self, _id: str) -> Publication:
        publication = self._repo.find_ordinance_by_id(_id)

        if publication is None:
            raise EntityNotFound(f'Publication with id {_id} not found')

        return publication

    def search_publications(self, _filter: dict) -> List[Publication]:
        return self._repo.search_ordinances(_filter)

    def create_owner(self, data: dict):
        owner = self._repo.find_owner_by_id(data['_id'])

        if owner is None:
            owner = Owner.new(data)
            self._repo.create_owner(owner)
            self._log.debug(f'Added new owner with doc {owner.doc}')
        else:
            owner = owner.merge(data)
            self._repo.update_owner(owner)
            self._log.debug(f'Updated owner with doc {owner.doc}')
