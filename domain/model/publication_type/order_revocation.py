from .type_base import PublicationDetails

from dataclasses import dataclass


@dataclass
class OrderRevocation(PublicationDetails):
    """Revogacao de pedido"""
