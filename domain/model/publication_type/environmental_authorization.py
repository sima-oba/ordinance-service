from dataclasses import dataclass
from typing import Optional

from .type_base import PublicationDetails


@dataclass
class EnvironmentalAuthorization(PublicationDetails):
    observation: Optional[str]
