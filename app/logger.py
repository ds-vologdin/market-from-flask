import logging

from .settings import config

# Логер app
logger = logging.getLogger('market-flask')


logging_config = config.get('LOGGING')
if logging_config:
    logging.basicConfig(
        filename=logging_config.get('FILE'),
        level=logging_config.get('LEVEL'),
        format='%(asctime)s:%(levelname)s:%(message)s'
    )
    logger.debug('Инициализация logging')
