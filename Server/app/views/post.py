from flask import Response, request, jsonify, Blueprint
from flask_restful import Api, Resource

from app.models import *

api = Api(Blueprint(__name__, __name__))


@api.resource('/')
class Todo(Resource):
    def post(self):
        content = request.json['content']
        period = request.json['period']
        place = request.json['place']

        todo = TodoModel(content=content, period=period, place=place).save()

        return jsonify({'todo_id': str(todo.id)})

    def get(self):
        return jsonify([{
            'todo_id': str(todo.id),
            'content': todo.content,
            'isCheck': todo.isCheck,
            'place': todo.place,
            'period': str(todo.period)
        } for todo in TodoModel.objects().all()])

@api.resource('/<todo_id>')
class TodoDetail(Resource):
    def delete(self, todo_id):
        todo = TodoModel.objects(id=todo_id).first()

        todo.delete()
        return Response('success', 200)

# @api.resource('/title')
# class Title(Resource):
#     def post(self):
#         title = request.json['title']
#
#         title = TodotitleModel(title=title).save()
#
#         return jsonify({'title_id': str(title.id)})
#
#     def get(self):
#         return jsonify([{
#             'title': title.title,
#             'title_id': str(title.id)
#         } for title in TodotitleModel.objects().all()])