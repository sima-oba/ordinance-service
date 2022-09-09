from dataclasses import dataclass

from .type_base import PublicationDetails


@dataclass
class LicenseRenewal(PublicationDetails):
    renovation_type: str
    operation: str
