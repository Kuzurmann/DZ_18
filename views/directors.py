from flask_restx import Resource, Namespace
from flask import request, jsonify
from dao.model.directors import DirectorsSchema
from implemented import directors_service

directors_ns = Namespace('director')


@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        name = request.args.get('year')
        director_id = request.args.get('director_id')
        if name:
            directors = directors_service.get_by_year(name)
        elif director_id:
            directors = directors_service.get_by_director(director_id)
        else:
            directors = directors_service.get_all()
        result = DirectorsSchema(many=True).dump(directors)
        return result, 200


@directors_ns.route('/<int:did>')
class DirectorsView(Resource):
    def get(self, did):
        director = directors_service.get_one(did)
        result = DirectorsSchema().dump(director)
        return result, 200

