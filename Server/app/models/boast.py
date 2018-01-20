from datetime import datetime

from app.models import *
from app.models.account import AccountModel


class BoastModel(Document):
    meta = {
        'collection': 'boast'
    }

    title = StringField(
        required=True
    )

    date = DateTimeField(
        required=True,
        default=datetime.now()
    )

    author = ReferenceField(
        document_type=AccountModel,
        required=True
    )

    content = StringField(
        required=True
    )