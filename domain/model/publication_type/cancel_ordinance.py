from dataclasses import dataclass

from .type_base import PublicationDetails


@dataclass
class CancelOrdinance(PublicationDetails):
    origin_ordinance: str
