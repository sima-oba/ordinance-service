from dataclasses import dataclass

from .type_base import PublicationDetails


@dataclass
class InterdictionInfraction(PublicationDetails):
    """Infracao de Interdicao"""
