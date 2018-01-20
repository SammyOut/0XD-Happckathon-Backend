from datetime import timedelta

PORT = 3000

SECRET_KEY = 'idontcaresecurity'

JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)
JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=365)
JWT_HEADER_TYPE = 'JWT'

SERVICE_NAME = 'Hackathon Flask baseline'

SWAGGER = {
    'title': SERVICE_NAME,
    'specs_route': '/docs/',
    'uiversion': 3,

    'info': {
        'title': SERVICE_NAME + ' API',
        'version': '1.0',
        'description': '''
- Status Code 1xx : Informational
- Status Code 2xx : Success
- Status Code 3xx : Redirection
- Status Code 4xx : Client Error
- Status Code 5xx : Server Error

##### <a href="https://httpstatuses.com/">[All of HTTP status code]</a>
##### <a href="http://meetup.toast.com/posts/92">[About REST API]</a>
##### <a href="https://velopert.com/2389">[About JWT]</a>
'''
    },

    'basePath': '/ '
}
