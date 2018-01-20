from flask import Response
from flask_restful import Resource, request
from flasgger import swag_from

from app.docs.sample import *


class Sample(Resource):
    @swag_from(SAMPLE_GET)
    def get(self):
        return Response('Get success')

    @swag_from(SAMPLE_POST)
    def post(self):
        name = request.form['name']
        return Response('Hello ' + name)