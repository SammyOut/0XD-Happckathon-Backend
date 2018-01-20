PARTY_LIST_GET = {
    'tags': ['party'],
    'description': '파티 리스트 가져오기',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
    ],
    'responses': {
        '200': {
            'description': 'get 성공',
            'examples': {
                'application/json': [
                    {
                        'id': '파티의 id',
                        'longitude': '경도    (type: Float)',
                        'latitude': '위도    (type: Float)',
                        'title': '파티의 title'
                    },
                    {
                        'id': '파티의 id',
                        'longitude': '경도    (type: Float)',
                        'latitude': '위도    (type: Float)',
                        'title': '파티의 title'
                    }
                ]
            }
        },
        '403': {
            'description': '권한 없음'
        },
        '204': {
            'description': '파티 없음'
        }
    }
}

PARTY_GET = {
    'tags': ['party'],
    'description': '파티 글 조회',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'party_id',
            'description': '조회할 파티 글의 id',
            'in': 'formData',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': 'get 성공',
            'examples': {
                'application/json': {
                    'id': '파티의 id',
                    'longitude': '파티의 경도    (type: Float)',
                    'latitude': '파티의 위도    (type: Float)',
                    'author_id': '주최자의 id',
                    'author_nickname': '주최자의 nickname',
                    'author_phone': '주최자의 phone',
                    'title': '파티의 제목',
                    'content': '파티의 내용',
                    'participants': [
                        {
                            'participant_id': '참가자1 id',
                            'participant_nickname': '참가자1 nickname',
                            'participant_phone': '참가자1 phone'
                        },
                        {
                            'participant_id': '참가자2 id',
                            'participant_nickname': '참가자2 nickname',
                            'participant_phone': '참가자2 phone'
                        }
                    ]
                }
            }
        }
    }
}

PARTY_POST = {
    'tags': ['party'],
    'description': '파티 글 작성',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'longitude',
            'description': '경도',
            'in': 'json',
            'type': 'float',
            'required': True
        },
        {
            'name': 'latitude',
            'description': '위도',
            'in': 'json',
            'type': 'float',
            'required': True
        },
        {
            'name': 'title',
            'description': '파티의 제목',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'content',
            'description': '파티의 내용',
            'in': 'json',
            'type': 'str',
            'required': True
        },
    ],
    'responses': {
        '201': {
            'description': 'post 성공'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

PARTY_DELETE = {
    'tags': ['party'],
    'description': '파티 글 작성',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'party_id',
            'description': '삭제할 파티의 id',
            'in': 'formData',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': 'delete 성공'
        },
        '204': {
            'description': 'party_id에 해당하는 파티 글 없음'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

PARTY_JOIN_POST = {
    'tags': ['party'],
    'description': '파티 참가',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'party_id',
            'description': '참가할 파티 id',
            'in': 'formData',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': 'post 성공'
        },
        '204': {
            'description': 'party_id에 해당하는 파티 글 없음',
        },
        '205': {
            'description': '이미 참가가 되어 있음'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}
