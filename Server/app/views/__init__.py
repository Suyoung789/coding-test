from flask import jsonify, after_this_request, request
from flask_restful import Resource
from functools import wraps
from werkzeug.exceptions import HTTPException


def after_request(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'deny'

    return response


def exception_handler(e):
    print(e)

    if isinstance(e, HTTPException):
        description = e.description
        code = e.code

    else:
        description = ''
        code = 500

    return jsonify({
        'msg': description
    }), code


def gzip(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        @after_this_request
        def zipper(response):
            if 'gzip' not in request.headers.get('Accept-Encoding', '') \
                    or not 200 <= response.status_code < 300 \
                    or 'Content-Encoding' in response.headers:
                return response

            response.data = gzip.compress(response.data)
            response.headers.update({
                'Content-Encoding': 'gzip',
                'Vary': 'Accept-Encoding',
                'Content-Length': len(response.data)
            })
            return response

        return fn(*args, **kwargs)

    return wrapper


class Router(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.after_request(after_request)
        app.register_error_handler(Exception, exception_handler)

        from app.views import post
        app.register_blueprint(post.api.blueprint)
