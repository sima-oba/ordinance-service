from datetime import datetime
from dataclasses import dataclass

from .type_base import PublicationDetails


@dataclass
class DemolitionPenalty(PublicationDetails):
    infringement_date: datetime
    latitude: float
    longitude: float
