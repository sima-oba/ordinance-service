from confluent_kafka import Producer
from uuid import uuid4


class Publisher:
    def __init__(self, config: dict):
        self._producer = Producer(config)

    def send(self, dest: str, data: any, key: str = str(uuid4())) -> str:
        self._producer.produce(dest, key=key, value=data)
        self._producer.flush()
        return key
