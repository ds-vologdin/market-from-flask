import os
import configparser
import logging


def convert_str_to_logging_level(level_str=None):
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
    # Значение по умолчанию
    return logging.WARNING


def parse_config_section_base(config=None):
    if not config:
        return None
    if 'FLASK_DB' not in config:
        return None

    databases = {
        'default': {
            key.upper(): config['FLASK_DB'][key]
            for key in config['FLASK_DB']
        }
    }
    # Эта секция приведена для примера, как расширять конфиг
    # Можно разделить TEST БД и PROD БД
    # if 'TEST_DB' not in config:
    #     databases.update({
    #         'test': {
    #             key.upper(): config['TEST_DB'][key]
    #             for key in config['TEST_DB']
    #         }
    #     })
    return databases


def parse_config_section_path_images(config=None):
    if not config:
        return None
    path_images = 'images_product'  # Значение по-умолчанию
    if 'IMAGE' in config:
        path_images = config['IMAGE'].get('PATCH', path_images)
    return path_images


def parse_config_section_logging(config=None):
    if not config:
        return None
    logging_config = {}
    if 'LOGGING' in config:
        logging_config['FILE'] = config['LOGGING'].get('FILE'),
        # Если FILE не задано, то будет None - логи будут писаться в stdout
        logging_level = convert_str_to_logging_level(
            config['LOGGING'].get('LEVEL', logging.DEBUG)
        )
        logging_config['LEVEL'] = logging_level
    return logging_config


def parse_config(file_config='/etc/flask_market.conf'):
    # Берём данные из конфига (по умлочанию /etc/flask_market.conf)
    # что бы не коммитить пароли
    # Пример конфига в flask_market.conf
    if not os.path.isfile(file_config):
        return None

    config = configparser.ConfigParser()
    try:
        config.read(file_config)
    except:
        return None

    databeses = parse_config_section_base(config)
    path_images = parse_config_section_path_images(config)
    logging_config = parse_config_section_logging(config)

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
# Или я не прав? надо об этом подумать
logging_config = config.get('LOGGING')
if logging_config:
    logging.basicConfig(
        filename=logging_config.get('FILE'),
        level=logging_config.get('LEVEL'),
        format='%(asctime)s:%(levelname)s:%(message)s'
    )
    logging.debug('Инициализация logging')
