from flask import Response, abort
from flask_restful import Resource, request
from flasgger import swag_from
from flask_jwt_extended import jwt_required, get_jwt_identity

import json

from app.models.account import AccountModel
from app.models.boast import BoastModel
from app.docs.boast import *


class Boast(Resource):
    @swag_from(BOAST_GET)
    @jwt_required
    def get(self):
        """
        자랑 글 리스트 불러오기
        """
        boasts = BoastModel.objects()

        if not boasts.first():
            return Response('', 204)

        response = [{
            'id': str(boast.id),
            'date': str(boast.date)[:10],
            'title': boast.title,
            'author_id': boast.author.id,
            'author_nickname': boast.author.nickname,
            'content': boast.content,
            'image': boast.image
        } for boast in boasts]

        return Response(json.dumps(response, ensure_ascii=False), 200, content_type='application/json; charset=utf8')

    @swag_from(BOAST_POST)
    @jwt_required
    def post(self):
        """
        자랑 글 작성
        """
        user = AccountModel.objects(id=get_jwt_identity()).first()
        if not user:
            abort(403)

        rq = request.form
        path = '../static/image/'

        if len(rq['title']) < 5:
            return Response('', 205)

        file = request.files['image']
        file.save(path + 'boast_' + file.filename)

        BoastModel(
            title=rq['title'],
            author=user,
            content=rq['content'],
            image='boast_' + file.filename
        ).save()

        return Response('', 201)

    @swag_from(BOAST_DELETE)
    @jwt_required
    def delete(self):
        """
        자랑 글 삭제
        """
        user = AccountModel.objects(id=get_jwt_identity()).first()
        if not user:
            abort(403)
        id = request.form['id']

        boast = BoastModel.objects(id=id).first()
        if boast.author.id != user.id:
            abort(403)

        boast.delete()

        return Response('', 201)
