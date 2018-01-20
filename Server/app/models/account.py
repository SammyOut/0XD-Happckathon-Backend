from app.models import *


class AccountModel(Document):
    meta = {
        'collection': 'account'
    }

    id = StringField(
        required=True,
        primary_key=True
    )
    pw = StringField(
        required=True
    )

    nickname = StringField(
        required=True
    )

    phone = StringField(
        required=True
    )

    point = IntField(
        required=True,
        default=0
    )

    level = IntField(
        required=True,
        default=0
    )
