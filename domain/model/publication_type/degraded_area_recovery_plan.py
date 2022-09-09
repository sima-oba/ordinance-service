from dataclasses import dataclass

from .type_base import PublicationDetails


@dataclass
class DegradedAreaRecoveryPlan(PublicationDetails):
    prad: str
