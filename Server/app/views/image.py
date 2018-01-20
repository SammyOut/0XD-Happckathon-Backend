from flask import send_file
from flask_restful import Resource
from flasgger import swag_from


class Image(Resource):
    @swag_from()
    def get(self, image_name):

        return send_file('../static/image' + image_name)