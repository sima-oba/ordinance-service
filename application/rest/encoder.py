from datetime import datetime
from enum import Enum
from flask.json import JSONEncoder

from domain.model import PublicationType


class CustomJsonEncoder(JSONEncoder):
    def default(self, obj: any) -> str:
        if isinstance(obj, datetime):
            return obj.isoformat()

        if isinstance(obj, PublicationType):
            return obj.name

        if isinstance(obj, Enum):
            return obj.value

        return super().default(obj)
