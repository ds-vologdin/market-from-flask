import configparser
import logging


def convert_str_to_logging_level(level_str=None):
    level_logging = {
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'WARNING': logging.WARNING,
        'ERROR': logging.ERROR,
        'CRITICAL': logging.CRITICAL,
    }
    return level_logging.get(level_str, logging.WARNING)


def parse_config_section_base(config=None):
    if 'FLASK_DB' not in config:
        return {}
    databases = {
        'default': {
            key.upper(): config['FLASK_DB'][key]
            for key in config['FLASK_DB']
        }
    }
    return databases


def parse_config_section_path_images(config=None):
    path_images = 'images_product'  # Значение по-умолчанию
    if 'IMAGE' in config:
        path_images = config['IMAGE'].get('PATCH', path_images)
    return path_images


def parse_config_section_logging(config=None):
    if 'LOGGING' not in config:
        return {}
    logging_config = {
        'FILE': config['LOGGING'].get('FILE'),
        'LEVEL': convert_str_to_logging_level(
            config['LOGGING'].get('LEVEL', logging.DEBUG)
        )
    }
    # Если FILE не задано, то будет None - логи будут писаться в stdout
    return logging_config


def parse_config(file_config='/etc/flask_market.conf'):
    # Берём данные из конфига (по умлочанию /etc/flask_market.conf)
    # что бы не коммитить пароли
    # Пример конфига в flask_market.conf
    try:
        config = configparser.ConfigParser()
        config.read(file_config)
    except IOError:
        return {}

    databases = parse_config_section_base(config)
    path_images = parse_config_section_path_images(config)
    logging_config = parse_config_section_logging(config)

    return {
        'DATABASES': databases,
        'PATH_IMAGES': path_images,
        'LOGGING': logging_config,
    }


file_config = '/etc/flask_market.conf'
config = parse_config(file_config)
if not config:
    # если /etc/flask_market.conf не смогли прочитать, берём конфиг из примера
    logging.error('config file "{}" not found'.format(file_config))
    config = parse_config('flask_market.conf')
