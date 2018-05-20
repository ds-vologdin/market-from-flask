import os
import configparser

# Берём данные из конфига /etc/flask_market.conf (что бы не коммитить пароли)
# Пример конфига в flask_market.conf
file_config = '/etc/flask_market.conf'
if not os.path.isfile(file_config):
    # Если файл с конфигом отсутствует, то берём данные из примера
    file_config = 'flask_market.conf'

config = configparser.ConfigParser()
config.read(file_config)

DATABASES = {
    'default': {
        key.upper(): config['FLASK_DB'][key] for key in config['FLASK_DB']
    }
}
