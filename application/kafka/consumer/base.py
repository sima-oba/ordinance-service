import logging
from abc import ABC, abstractmethod
from threading import Thread
from confluent_kafka import Consumer, KafkaError, KafkaException


class BaseConsumer(ABC):
    def __init__(self):
        self._running = False
        self._thread = None
        self._log = logging.getLogger(self.__class__.__name__)

    def start(self, config: dict, topic: str, timeout=1.0):
        if self._running:
            self._log.warning('Consumer is already running')
            return

        if topic is None:
            raise ValueError('"topic" must not be None')

        if len(topic) == 0 or topic.isspace():
            raise ValueError('"topic" must not be a blank string')

        args = (config, topic, timeout)
        self._thread = Thread(target=self._loop, args=args)
        self._thread.daemon = True
        self._thread.start()
        self._running = True

    def _loop(self, config: dict, topic: str, timeout: float):
        consumer = Consumer(config)
        consumer.subscribe([topic])

        self._log.info(f'Topic {topic} started')

        try:
            while self._running:
                msg = consumer.poll(timeout=timeout)

                if msg is None:
                    continue

                if msg.error():
                    self._handle_error(msg)
                    continue

                self.process(msg)
                consumer.commit(asynchronous=False)
        except Exception as e:
            self._log.exception(e)
        finally:
            consumer.close()
            self._running = False
            self._log.info(f'Topic {topic} finished')

    def _handle_error(self, msg):
        error = msg.error()

        if error.code() == KafkaError._PARTITION_EOF:
            waning = f'{msg.topic()} reached end at offset {msg.offset()}'
            self._log.warning(waning)
        elif error.code() == KafkaError.UNKNOWN_TOPIC_OR_PART:
            self._log.warn(error.str())
        else:
            raise KafkaException(error)

    def wait(self):
        if self._thread and self._thread.is_alive():
            self._thread.join()

    def shutdown(self):
        self._running = False
        self.wait()

    @abstractmethod
    def process(self, message: any):
        pass
