from dataclasses import dataclass
from typing import Optional

from .type_base import PublicationDetails


@dataclass
class PreliminaryLicense(PublicationDetails):
    operation: Optional[str]
