from dacite.core import from_dict
from dataclasses import dataclass, asdict
from datetime import datetime
from uuid import uuid4


@dataclass
class Model:
    _id: str
    created_at: datetime
    updated_at: datetime

    def asdict(self) -> dict:
        return asdict(self)

    def merge(self, data: dict):
        merged = {
            'updated_at': datetime.utcnow(),
            **self.asdict(),
            **data
        }

        return from_dict(self.__class__, merged)

    @classmethod
    def new(cls, data: dict):
        _id = data.pop('_id', None) or str(uuid4())
        now = datetime.utcnow()

        return cls(
            _id=_id,
            created_at=now,
            updated_at=now,
            **data
        )

    @classmethod
    def from_dict(cls, data: dict):
        return from_dict(cls, data)
