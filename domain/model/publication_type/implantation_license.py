from dataclasses import dataclass
from typing import Optional

from .type_base import PublicationDetails


@dataclass
class ImplantationLicense(PublicationDetails):
    """Licenca de implantacao"""
    area: Optional[float]
    city: Optional[str]
    prod_volume: Optional[float]
