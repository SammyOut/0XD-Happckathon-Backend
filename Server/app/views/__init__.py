from flask_restful import Api

from app.views.sample import Sample
from app.views.account import SignUp, Auth

class ViewInjector(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        api = Api(app)

        api.add_resource(Sample, '/sample')
        api.add_resource(SignUp, '/signup')
        api.add_resource(Auth, '/auth')