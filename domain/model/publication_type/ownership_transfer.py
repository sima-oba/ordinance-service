
from dataclasses import dataclass
from typing import Optional

from .type_base import PublicationDetails


@dataclass
class OwnershipTransfer(PublicationDetails):
    transfer_type: Optional[str]
    to_doc_number: str
