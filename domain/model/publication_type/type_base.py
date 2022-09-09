from dataclasses import dataclass, asdict
from typing import Any


@dataclass
class PublicationDetails:
    def asdict(self) -> dict:
        return asdict(self)

    @classmethod
    def new(cls, **kwargs) -> Any:
        e = cls(**kwargs)
        return e
