import os
import configparser


def parse_config(file_config='/etc/flask_market.conf'):
    # Берём данные из конфига (по умлочанию /etc/flask_market.conf)
    # что бы не коммитить пароли
    # Пример конфига в flask_market.conf
    if not os.path.isfile(file_config):
        return None

    config = configparser.ConfigParser()
    config.read(file_config)

    databeses = {}
    if config['FLASK_DB']:
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
    if config['IMAGE']:
        path_images = config['IMAGE'].get('PATCH', path_images)
    return {
        'DATABASES': databeses,
        'PATH_IMAGES': path_images,
    }


config = parse_config('/etc/flask_market.conf')
if not config:
    # если /etc/flask_market.conf не смогли прочитать, берём конфиг из примера
    config = parse_config('flask_market.conf')
