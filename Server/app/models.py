from mongoengine import *


class TodoModel(Document):
    meta = {
        'collections': 'todo-model'
    }
    content = StringField(required=True)
    isCheck = BooleanField(default=False)
    period = StringField(null=True)
    place = StringField(null=True)
