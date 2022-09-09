from dataclasses import dataclass

from .type_base import PublicationDetails


@dataclass
class DeadlineExtension(PublicationDetails):
    """Prorrogação do prazo de validade"""
    ordinance_number_extended: str
