import os
import configparser
import logging


def convert_str_to_logging_level(level_str=None):
    if not level_str:
        return logging.WARNING
    if level_str == 'DEBUG':
        return logging.DEBUG
    if level_str == 'INFO':
        return logging.INFO
    if level_str == 'WARNING':
        return logging.WARNING
    if level_str == 'ERROR':
        return logging.ERROR
    if level_str == 'CRITICAL':
        return logging.CRITICAL


def parse_config(file_config='/etc/flask_market.conf'):
    # Берём данные из конфига (по умлочанию /etc/flask_market.conf)
    # что бы не коммитить пароли
    # Пример конфига в flask_market.conf
    if not os.path.isfile(file_config):
        return None

    config = configparser.ConfigParser()
    config.read(file_config)

    databeses = {}
    if 'FLASK_DB' in config:
        databeses = {
            'default': {
                key.upper(): config['FLASK_DB'][key]
                for key in config['FLASK_DB']
            }
            # Можем тут объявить отдельные БД для TEST и PROD
            # 'test': {
            #     key.upper(): config['TEST_DB'][key]
            #     for key in config['TEST_DB']
            # }
        }

    path_images = 'images_product'  # Значение по-умолчанию
    if 'IMAGE' in config:
        path_images = config['IMAGE'].get('PATCH', path_images)

    logging_config = {}
    if 'LOGGING' in config:
        logging_config.update({
            'FILE': config['LOGGING'].get('FILE'),
        })
        # Если FILE не задано, то будет None - логи будут писаться в stdout
        logging_level = convert_str_to_logging_level(
            config['LOGGING'].get('LEVEL', logging.DEBUG)
        )
        logging_config.update({
            'LEVEL': logging_level,
        })

    return {
        'DATABASES': databeses,
        'PATH_IMAGES': path_images,
        'LOGGING': logging_config,
    }


file_config = '/etc/flask_market.conf'
config = parse_config(file_config)
if not config:
    # если /etc/flask_market.conf не смогли прочитать, берём конфиг из примера
    logging.error('config file "{}" not found'.format(file_config))
    config = parse_config('flask_market.conf')

# Мне показалось, что настроить logging в модуле settings логично
# Или я не прав?
logging_config = config.get('LOGGING')
if logging_config:
    logging.basicConfig(
        filename=logging_config.get('FILE'),
        level=logging_config.get('LEVEL'),
        format='%(asctime)s:%(levelname)s:%(message)s'
    )
