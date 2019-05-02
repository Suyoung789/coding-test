import os
from datetime import datetime


class Config:
    SERVICE_NAME = "TodoList"

    MONGODB_SETTINGS = {
        'host': 'localhost',
        'post': None,
        'db': SERVICE_NAME,
        'password': os.getenv('MONGODB_PWD', '12poalskdsafv0n')
    }