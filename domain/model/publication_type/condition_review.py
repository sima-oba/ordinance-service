from dataclasses import dataclass

from .type_base import PublicationDetails


@dataclass
class ConditionReview(PublicationDetails):
    origin_ordinance: str
