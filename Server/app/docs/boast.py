BOAST_GET = {
    'tags': ['자랑'],
    'description': '자랑 글 불러오기',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': 'get 성공',
            'examples': {
                'application/json': [
                    {
                        'id': '자랑글1 id',
                        'date': '2018-04-20',
                        'title': '자랑글1 제목',
                        'author_id': '자랑글1 작성자 id',
                        'author_nickname': '자랑글1 작성자 nickname',
                        'content': '자랑글1 내용',
                        'image': '자랑글1 사진'
                    },
                    {
                        'id': '자랑글2 id',
                        'date': '2018-04-20',
                        'title': '자랑글2 제목',
                        'author_id': '자랑글2 작성자 id',
                        'author_nickname': '자랑글2 작성자 nickname',
                        'content': '자랑글2 내용',
                        'image': '자랑글2 사진'
                    }
                ]
            }
        },
        '204': {
            'description': '글 없음'
        }
    }
}


BOAST_POST = {
    'tags': ['자랑'],
    'description': '자랑글 쓰기',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'title',
            'description': '글의 제목',
            'in': 'formData',
            'type': 'str',
            'required': True
        },
        {
            'name': 'content',
            'description': '글의 내용',
            'in': 'formData',
            'type': 'str',
            'required': True
        },
        {
            'name': 'image',
            'description': '이미지',
            'in': 'file',
            'type': 'file',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '글 작성 성공'
        },
        '205': {
            'description': '글 제목의 길이가 짧음 (5글자 이상)'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

BOAST_DELETE = {
    'tags': ['자랑'],
    'description': '자랑 글 삭제',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'id',
            'description': '삭제할 자랑글의 id',
            'in': 'formData',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '글 삭제 성공'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}