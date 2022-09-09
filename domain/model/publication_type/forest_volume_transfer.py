from dataclasses import dataclass

from .type_base import PublicationDetails


@dataclass
class ForestVolumeTransfer(PublicationDetails):
    to_doc_number: str
