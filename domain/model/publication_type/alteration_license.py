from dataclasses import dataclass

from .type_base import PublicationDetails


@dataclass
class AlterationLicense(PublicationDetails):
    """Licenca ambiental de alteracao"""
