from pymongo.database import Database
from typing import Optional
from uuid import uuid4

from domain.repository import SettingsInterface


class SettingsRepository(SettingsInterface):
    def __init__(self, db: Database):
        self._collection = db['settings']

    def save(self, settings) -> dict:
        current_settings = self.load()

        if current_settings:
            settings = {**current_settings, **settings}
            self._collection.replace_one({'_id': settings['_id']}, settings)
        else:
            settings['_id'] = str(uuid4())
            self._collection.insert_one(settings)

        return settings

    def load(self) -> Optional[dict]:
        result = self._collection.find(limit=1)
        return result[0] if result.count() > 0 else None
