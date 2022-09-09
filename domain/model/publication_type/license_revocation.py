from dataclasses import dataclass
from typing import Optional

from .type_base import PublicationDetails


@dataclass
class LicenseRevocation(PublicationDetails):
    origin_ordinance: str
    revocation_type: str
    lat: Optional[float]
    lon: Optional[float]
