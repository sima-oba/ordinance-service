from dataclasses import dataclass
from typing import Optional

from .type_base import PublicationDetails


@dataclass
class ICMBioInfractionNotice(PublicationDetails):
    geometry: dict
    description: str
    infraction_type: str
    judging: Optional[str]
