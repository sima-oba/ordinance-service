import logging
from functools import wraps
from marshmallow import ValidationError
from json.decoder import JSONDecodeError

from domain.exception import EntityNotFound, EntityAlreadyExists
from .base import BaseConsumer


_log = logging.getLogger(__name__)
_errors = (
    ValidationError,
    EntityNotFound,
    EntityAlreadyExists,
    JSONDecodeError
)


def _is_process_method(method) -> bool:
    return hasattr(method, '__name__') and method.__name__ == 'process'


def _is_consumer_instance(args) -> bool:
    return len(args) > 0 and isinstance(args[0], BaseConsumer)


def error_handler(method):

    @wraps(method)
    def wrapper(*args, **kwargs):
        try:
            return method(*args, **kwargs)
        except _errors as e:
            if _is_consumer_instance(args) and _is_process_method(method):
                msg = args[1]
                topic = msg.topic()
                partition = msg.partition()
                key = msg.key().decode('utf8') if msg.key() else None
                value = msg.value().decode('utf8')

                _log.exception(
                    'Error occured while processing message: '
                    f'{topic} - {partition} - {key} - {value}'
                )
            else:
                _log.exception(e)

    return wrapper
