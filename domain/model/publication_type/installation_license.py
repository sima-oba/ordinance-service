from dataclasses import dataclass
from typing import Optional

from .type_base import PublicationDetails


@dataclass
class InstallationLicense(PublicationDetails):
    objective: Optional[str]
    location: Optional[str]
