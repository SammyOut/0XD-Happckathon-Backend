from flask import Response, abort
from flask_restful import Resource, request
from flasgger import swag_from
from flask_jwt_extended import create_access_token

from app.models.account import AccountModel
from app.docs.account import *


class SignUp(Resource):
    @swag_from(SIGNUP_POST)
    def post(self):
        """
        회원가입 
        """
        rq = request.json
        id = rq['id']
        pw = rq['pw']
        nickname = rq['nickname']
        phone = rq['phone']

        if AccountModel.objects(id=id).first():
            return Response('', 205)

        AccountModel(
            id=id,
            pw=pw,
            nickname=nickname,
            phone=phone
        ).save()

        return Response('', 201)


class Auth(Resource):
    @swag_from(AUTH_POST)
    def post(self):
        """
        로그인
        """
        id = request.form['id']
        pw = request.form['pw']
        user = AccountModel.objects(id=id, pw=pw).first()
        if user:
            return {
                'access_token': create_access_token(id)
            }, 200
        abort(401)