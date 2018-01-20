from flask import Response, abort
from flask_restful import Resource, request
from flasgger import swag_from
from flask_jwt_extended import jwt_required, get_jwt_identity

import json
from app.models.account import AccountModel
from app.models.party import PartyModel


class PartyList(Resource):
    @swag_from()
    @jwt_required
    def get(self):
        """
        파티 리스트 불러오기
        """
        user = AccountModel.objects(id=get_jwt_identity()).first()
        if not user:
            abort(403)

        parties = PartyModel.objects()
        if not parties.first():
            return Response('', 204)

        response = [
            {
                'id': party.id,
                'latitude': party.latitude,
                'longitude': party.longitude,
                'title': party.title,
            } for party in parties]

        return Response(json.dumps(response, ensure_ascii=False), 200, content_type='application/json; charset=utf8')


class Party(Resource):
    @swag_from()
    @jwt_required
    def get(self):
        """
        파티 글 읽기
        """
        user = AccountModel.objects(id=get_jwt_identity()).first()
        if not user:
            abort(403)

        party_id = request.form['party_id']
        party = PartyModel.objects(id=party_id).first()
        if not party:
            return Response('', 204)

        response = {
            'id': party.id,
            'longitude': party.longitude,
            'latitude': party.latitude,
            'author_id': party.author.id,
            'author_nickname': party.author.nickname,
            'author_phone': party.author.phone,
            'title': party.title,
            'content': party.content,
            'participants': [
                {
                    'participant_id': participant.id,
                    'participant_nickname': participant.nickname,
                    'participant_phone': participant.phone
                } for participant in party.participants
            ]
        }

        return Response(json.dumps(response, ensure_ascii=False), 200, content_type='application/json; charset=utf8')

    @swag_from()
    @jwt_required
    def post(self):
        """
        파티 글 작성
        """
        user = AccountModel.objects(id=get_jwt_identity()).first()
        if not user:
            abort(403)

        rq = request.json

        PartyModel(
            longitude=rq['longitude'],
            latitude=rq['latitude'],
            author=user,
            title=rq['title'],
            content=rq['content']
        ).save()

        return Response('', 201)

    @swag_from()
    @jwt_required
    def delete(self):
        """
        파티 글 삭제
        """
        user = AccountModel.objects(id=get_jwt_identity()).first()
        if not user:
            abort(403)

        party_id = request.form['party_id']
        party = PartyModel.objects(id=party_id).first()
        if not party:
            return Response('', 204)

        if party.author.id != user.id:
            abort(403)

        party.delete()
        return Response('', 201)


class PartyJoin(Resource):
    @swag_from()
    @jwt_required
    def post(self):
        """
        파티 참가 신청
        """
        user = AccountModel.objects(id=get_jwt_identity()).first()
        if not user:
            abort(403)

        party_id = request.form['party_id']
        party = PartyModel.objects(id=party_id).first()
        if not party:
            return Response('', 204)
        for participant in party.participants:
            if participant.id == user.id:
                return Response('', 205)
        party.participants.append(user)
        party.save()
        return Response('', 201)
