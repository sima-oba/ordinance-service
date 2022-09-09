from abc import ABC, abstractmethod
from typing import Optional


class SettingsInterface(ABC):
    @abstractmethod
    def save(self, settings: dict) -> dict:
        pass

    @abstractmethod
    def load(self) -> Optional[dict]:
        pass
