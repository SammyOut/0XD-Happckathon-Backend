from flask import Flask
from flask_jwt_extended import JWTManager
from flasgger import Swagger

from app.docs import TEMPLATE
from app.models import Mongo
from app.views import ViewInjector
from app.middleware import Logger

swagger = Swagger(template=TEMPLATE)
db = Mongo()
view = ViewInjector()
logger = Logger()
jwt = JWTManager()


def create_app(config_name):
    """
    Creates Flask instance & initialize

    :rtype: Flask
    """
    app_ = Flask(__name__)
    app_.config.from_pyfile(config_name)

    jwt.init_app(app_)
    swagger.init_app(app_)
    db.init_app(app_)
    view.init_app(app_)
    logger.init_app(app_)

    return app_

app = create_app('../config/production.py')
