SIGNUP_POST = {
    'tags': ['계정'],
    'description': '회원 가입',
    'parameters': [
        {
            'name': 'id',
            'description': '회원 가입할 아이디',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'pw',
            'description': '회원 가입할 비밀번호',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'nickname',
            'description': '닉네임',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'phone',
            'description': '핸드폰 번호',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '회원가입 성공'
        },
        '205': {
            'description': '중복 ID'
        }
    }
}

AUTH_POST = {
    'tags': ['계정'],
    'description': '로그인',
    'parameters': [
        {
            'name': 'id',
            'description': '로그인할 아이디',
            'in': 'formData',
            'type': 'str',
            'required': True
        },
        {
            'name': 'pw',
            'description': '로그인할 비밀번호',
            'in': 'formData',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '로그인 성공',
            'examples': {
                'application/json': {
                    'access_token': '여기에 토큰이 담길 것이여'
                }
            }
        },
        '401': {
            'description': '로그인 실패'
        }
    }
}