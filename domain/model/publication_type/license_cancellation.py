from dataclasses import dataclass

from .type_base import PublicationDetails


@dataclass
class LicenseCancellation(PublicationDetails):
    origin_ordinance: str
