from dataclasses import dataclass
from typing import Optional

from .type_base import PublicationDetails


@dataclass
class RegularizationLicense(PublicationDetails):
    latitude: Optional[float]
    longitude: Optional[float]
    operation: Optional[str]
