from flask import Response, abort
from flask_restful import Resource, request
from flasgger import swag_from
from flask_jwt_extended import jwt_required, get_jwt_identity

import json

from app.models.account import AccountModel
from app.models.rent import RentModel
from app.docs.rent import *


class RentList(Resource):
    @swag_from(RENT_LIST_GET)
    @jwt_required
    def get(self):
        """
        대여 글 리스트 불러오기
        """
        category = request.args['category']

        rents = RentModel.objects(category=category)

        if not rents.first():
            return Response('', 204)

        response = [{
            'id': rent.id,
            'category': rent.category,
            'title': rent.title
        } for rent in rents]

        return Response(json.dumps(response, ensure_ascii=False), 200, content_type='application/json; charset=utf8')


class Rent(Resource):
    @swag_from(RENT_GET)
    @jwt_required
    def get(self):
        """
        대여 글 읽기
        """
        id = request.args['id']

        rent = RentModel.objects(id=id).first()
        if not rent:
            return Response('', 204)

        response = {
            'id': rent.id,
            'category': rent.category,
            'title': rent.title,
            'author_id': rent.author.id,
            'author_nickname': rent.author.nickname,
            'hour_price': rent.hour_price or None,
            'day_price': rent.day_price or None
        }

        return Response(json.dumps(response, ensure_ascii=False), 200, content_type='application/json; charset=utf8')

    @swag_from(RENT_POST)
    @jwt_required
    def post(self):
        """
        대여 글 작성
        """
        user = AccountModel.objects(id=get_jwt_identity()).first()
        if not user:
            abort(403)
        rq = request.json

        RentModel(
            category=rq['category'],
            author=user,

            hour_price=rq.pop('hour_price', None),
            day_price=rq.pop('hour_price', None),

            title=rq['title'],
            content=rq['content']
        ).save()

        return Response('', 201)

    @swag_from(RENT_DELETE)
    @jwt_required
    def delete(self):
        """
        대여 글 삭제
        """
        user = AccountModel.objects(id=get_jwt_identity()).first()
        if not user:
            abort(403)
        id = request.form['id']

        rent = RentModel.objects(id=id).first()
        if rent.author.id != user.id:
            abort(403)

        rent.delete()

        return Response('', 201)
