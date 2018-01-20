from flask_restful import Api

from app.views.sample import Sample
from app.views.account import *
from app.views.rent import *
from app.views.image import *

class ViewInjector(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        api = Api(app)

        api.add_resource(Sample, '/sample')

        # 계정
        api.add_resource(SignUp, '/signup')
        api.add_resource(Auth, '/auth')

        # 대여
        api.add_resource(RentList, '/rentlist')
        api.add_resource(Rent, '/rent')

        # 이미지
        api.add_resource(Image, '/image/<image_name>')