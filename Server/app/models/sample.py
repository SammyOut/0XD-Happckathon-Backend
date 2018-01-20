from app.models import *


class SampleModel(Document):
    """
    Sample Model
    """

    meta = {
        'collection': 'sample'
    }

    name = StringField(
        required=True
    )

    number = IntField(
        required=True
    )
