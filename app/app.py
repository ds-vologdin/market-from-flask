from flask import Flask
from . logger import logger

from app.main import blueprint as main_blueprint


def create_app():
    app = Flask(__name__)
    logger.debug('Создали app (app = Flask(__name__))')
    app.register_blueprint(main_blueprint.blueprint)
    logger.debug('Зарегистрировали main_blueprint')
    return app
