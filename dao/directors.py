from dao.model.directors import Directors, DirectorsSchema


class DirectorsDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        directors = Directors.query.all()
        return directors

    def get_one(self, did):
        director = Directors.query.get(did)
        return director