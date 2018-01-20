from flask import Flask
from flasgger import Swagger

from app.docs import TEMPLATE
from app.models import Mongo
from app.views import ViewInjector
from app.middleware import Logger

swagger = Swagger(template=TEMPLATE)
# To Swagger UI

db = Mongo()
# To Control MongoDB

view = ViewInjector()
# To Swagger Documentation

logger = Logger()
# To log in every context of Flask


def create_app(config_name):
    """
    Creates Flask instance & initialize

    :rtype: Flask
    """
    app_ = Flask(__name__)
    app_.config.from_pyfile(config_name)

    swagger.init_app(app_)
    db.init_app(app_)
    view.init_app(app_)
    logger.init_app(app_)

    return app_

app = create_app('../config/production.py')
