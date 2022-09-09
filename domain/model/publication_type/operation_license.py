from dataclasses import dataclass
from typing import Optional

from .type_base import PublicationDetails


@dataclass
class OperationLicense(PublicationDetails):
    operation: Optional[str]
