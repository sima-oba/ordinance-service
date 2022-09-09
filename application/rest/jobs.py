import json
import logging
from datetime import datetime, timedelta

from domain.repository import SettingsInterface
from infrastructure.repository import Repository, Publisher


_log = logging.getLogger(__name__)


def get_ordinance_notifier(
    ordinances_repo: Repository,
    settings_repo: SettingsInterface,
    publisher: Publisher
):
    def notify_ordinances():
        settings = settings_repo.load()

        if settings is None:
            _log.warn('There is no settings. Skipping job...')
            return

        ordinances = ordinances_repo.search_ordinances({
            'notified_date': None,
            'term': {
                '$lte': datetime.utcnow() +
                timedelta(days=settings['alert_days_before'])
            }
        })

        _log.debug(f'Found {len(ordinances)} ordinances to notify')

        for ordinance in ordinances:
            owner = ordinances_repo.find_owner_by_doc(ordinance.owner_doc)
            publish_date = ordinance.publish_date.strftime('%d/%m/%Y')
            term_date = ordinance.term.strftime('%d/%m/%Y')

            payload = json.dumps({
                'email': {
                    'template_id': str(settings['template_id']),
                    'subject': settings['subject'],
                    'recipient': [owner.email],
                    'content': {
                        'ordinance_number': ordinance.ordinance_number,
                        'process': ordinance.process,
                        'publish_date': publish_date,
                        'term': term_date,
                        'link': ordinance.link,
                        'message': settings['alert_message']
                    }
                }
            }, ensure_ascii=False)

            publisher.send('NOTIFICATION', payload, ordinance._id)
            ordinance.notified_date = datetime.utcnow()
            ordinances_repo.update_ordinance(ordinance)
            _log.info(f'Sent ordinance NOTIFICATION:{ordinance._id}')

    return notify_ordinances
