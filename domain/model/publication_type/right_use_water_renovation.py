from dataclasses import dataclass
from typing import Optional

from .type_base import PublicationDetails


@dataclass
class RightUseWaterResourcesRenovation(PublicationDetails):
    flow: str
    capture: str
    area: Optional[float]
    latitude: Optional[float]
    longitude: Optional[float]
