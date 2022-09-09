from dataclasses import dataclass

from .type_base import PublicationDetails


@dataclass
class SpecialProcedure(PublicationDetails):
    authorization_number: str
