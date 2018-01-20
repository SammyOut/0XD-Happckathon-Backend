from flask import send_file
from flask_restful import Resource


class Image(Resource):
    def get(self, image_name):

        return send_file('../static/image' + image_name)