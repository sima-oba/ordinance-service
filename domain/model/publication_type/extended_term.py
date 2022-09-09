from dataclasses import dataclass

from .type_base import PublicationDetails


@dataclass
class ExtendedTerm(PublicationDetails):
    """Prorrogação do prazo de vencimento"""
    ordinance_number_extended: str
    extend_by: int
