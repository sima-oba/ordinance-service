from dataclasses import dataclass

from .type_base import PublicationDetails


@dataclass
class OwnerNameChange(PublicationDetails):
    from_name: str
    to_name: str
