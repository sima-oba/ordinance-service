from .type_base import PublicationDetails

from dataclasses import dataclass


@dataclass
class Rectification(PublicationDetails):
    """Retificacao de portaria"""
    ordinance_number_rectified: str
