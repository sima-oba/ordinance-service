from abc import ABC, abstractmethod
from typing import List, Optional

from domain.model import Publication, Owner


class RepositoryInterface(ABC):
    @abstractmethod
    def create_ordinance(self, ordinance: Publication):
        pass

    @abstractmethod
    def find_ordinance_by_id(self, _id: str) -> Publication:
        pass

    @abstractmethod
    def find_ordinance_by_number(self, ordinance_number: str) -> Publication:
        pass

    @abstractmethod
    def ordinance_exists(self, ordinance_number: str, issuer: str) -> bool:
        pass

    @abstractmethod
    def search_ordinances(self, _filter: dict) -> List[Publication]:
        pass

    @abstractmethod
    def create_owner(self, owner: Owner):
        pass

    @abstractmethod
    def update_owner(self, owner: Owner):
        pass

    @abstractmethod
    def find_owner_by_id(self, _id: str) -> Optional[Owner]:
        pass

    @abstractmethod
    def find_owner_by_doc(self, doc: str) -> Optional[Owner]:
        pass
