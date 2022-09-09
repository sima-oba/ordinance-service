from dataclasses import dataclass
from datetime import datetime

from .type_base import PublicationDetails


@dataclass
class PlantingAnticipation(PublicationDetails):
    crop: str
    seeding_harverst: str
    seeding_start: datetime
    seeding_end: datetime
    sanitary_void_harvest: str
    sanitary_void_start: datetime
    sanitary_void_end: datetime
