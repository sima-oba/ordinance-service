from dataclasses import dataclass
from typing import Optional

from .type_base import PublicationDetails


@dataclass
class GrantWaiver(PublicationDetails):
    dismissal_process: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]
