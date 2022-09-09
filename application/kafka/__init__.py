from domain.service import Service
from infrastructure.database import get_database
from infrastructure.repository import Repository

from application.schema import PublicationSchema, OwnerSchema
from .consumer import Consumer, ConsumerGroup


def start_consumer(config):
    db = get_database(config.MONGODB_SETTINGS)
    group = ConsumerGroup({
        'bootstrap.servers': config.KAFKA_SERVER,
        'group.id': 'ORDINANCE',
        'enable.auto.commit': False,
        'auto.offset.reset': 'earliest',
    })

    repository = Repository(db)
    service = Service(repository)

    pub_consumer = Consumer(PublicationSchema(), service.create_publication)
    owner_consumer = Consumer(OwnerSchema(), service.create_owner)

    group.add(pub_consumer, 'NEW_ORDINANCE')
    group.add(owner_consumer, 'NEW_OWNER')
    group.wait()
