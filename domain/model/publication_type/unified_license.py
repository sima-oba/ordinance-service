from dataclasses import dataclass

from .type_base import PublicationDetails


@dataclass
class UnifiedLicense(PublicationDetails):
    operation: str
