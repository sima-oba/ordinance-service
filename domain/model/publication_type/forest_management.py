from dataclasses import dataclass

from .type_base import PublicationDetails


@dataclass
class ForestManagement(PublicationDetails):
    area: str
    latitude: float
    longitude: float
