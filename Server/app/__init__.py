from flask import Flask
from flask_cors import CORS
from mongoengine import connect
from app.views import Router

from Server.config import Config


def create_app(*config_cls):
    app_ = Flask(__name__)

    for config in config_cls:
        app_.config.from_object(config)

    CORS().init_app(app_)
    Router().init_app(app_)

    connect('TodoList')

    return app_
