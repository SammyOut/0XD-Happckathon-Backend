from app.models import *
from app.models.account import AccountModel


class RentModel(Document):
    meta = {
        'collection': 'rent'
    }

    category = StringField(
        required=True
    )

    author = ReferenceField(
        document_type=AccountModel,
        required=True
    )

    hour_price = IntField()
    day_price = IntField()

    title = StringField(
        required=True,
        min_length=5
    )
    content = StringField(
        required=True
    )
    file = StringField(
        default=''
    )