from dataclasses import dataclass
from datetime import datetime

from .type_base import PublicationDetails


@dataclass
class Erratum(PublicationDetails):
    origin_ordinance: str
    publish_date: datetime
    concession: str
