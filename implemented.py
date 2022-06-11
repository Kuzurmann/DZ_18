from dao.movies import MoviesDAO
from dao.genres import GenresDAO
from dao.directors import DirectorsDAO

from service.movies import MoviesService
from service.genres import GenresService
from service.directors import DirectorsService

from setup_db import db

movies_dao = MoviesDAO(db.session)
movies_service = MoviesService(movies_dao=movies_dao)

genres_dao = GenresDAO(db.session)
genres_service = GenresService(genres_dao=genres_dao)

directors_dao = DirectorsDAO(db.session)
directors_service = DirectorsService(directors_dao=directors_dao)

# review_dao = ReviewDAO(db.session)
# review_service = ReviewService(dao=review_dao)