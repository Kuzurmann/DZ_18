from flask_restx import Resource, Namespace
from flask import request, jsonify
from dao.model.genres import GenresSchema
from implemented import genres_service

genres_ns = Namespace('genre')


@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        name = request.args.get('name')
        genre_id = request.args.get('genre_id')
        if name:
            genres = genres_service.get_by_genres(name)
        elif genre_id:
            genres = genres_service.get_by_genre(genre_id)
        else:
            genres = genres_service.get_all()
        result = GenresSchema(many=True).dump(genres)
        return result, 200


@genres_ns.route('/<int:gid>')
class GenresView(Resource):
    def get(self, gid):
        genre = genres_service.get_one(gid)
        result = GenresSchema().dump(genre)
        return result, 200

