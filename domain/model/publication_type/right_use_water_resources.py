from dataclasses import dataclass
from typing import Optional

from .type_base import PublicationDetails


@dataclass
class RightUseWaterResources(PublicationDetails):
    flow: str
    capture: Optional[str]
    area: Optional[float]
    latitude: Optional[float]
    longitude: Optional[float]
