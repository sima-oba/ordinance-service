from dataclasses import dataclass
from typing import Optional

from .model import Model


@dataclass
class Owner(Model):
    doc: str
    email: str
    name: str
    enabled: Optional[str]
