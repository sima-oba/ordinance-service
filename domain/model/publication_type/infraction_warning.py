from dataclasses import dataclass

from .type_base import PublicationDetails


@dataclass
class InfractionWarning(PublicationDetails):
    pass
