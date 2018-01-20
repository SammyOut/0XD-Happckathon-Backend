from app.models import *
from app.models.account import AccountModel


class PartyModel(Document):
    meta = {
        'collection': 'party'
    }

    longitude = FloatField(
        required=True
    )
    latitude = FloatField(
        required=True
    )

    author = ReferenceField(
        document_type=AccountModel,
        required=True
    )

    title = StringField(
        required=True
    )
    content = StringField(
        required=True
    )

    participants = ListField(
        field=ReferenceField(
            document_type=AccountModel
        ),
        default=[]
    )
