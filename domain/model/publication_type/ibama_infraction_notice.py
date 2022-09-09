from dataclasses import dataclass

from .type_base import PublicationDetails


@dataclass
class IbamaInfractionNotice(PublicationDetails):
    amount: float
    status: str
    sanctions: str
    city: str
    infraction: str
