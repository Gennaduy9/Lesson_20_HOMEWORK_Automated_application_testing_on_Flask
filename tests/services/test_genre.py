from unittest.mock import MagicMock

import pytest

from dao.genre import GenreDAO
from dao.model.genre import Genre
from service.genre import GenreService

from setup_db import db


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(db.session)

    thriller = Genre(id=1, name='thriller')
    comedy = Genre(id=2, name='comedy')
    fantastic = Genre(id=3, name='fantastic')


    genre_dao.get_one = MagicMock(return_value=thriller)
    genre_dao.get_all = MagicMock(return_value=[thriller, comedy, fantastic])
    genre_dao.create = MagicMock(return_value=Genre(id=3))
    genre_dao.delete = MagicMock
    genre_dao.update = MagicMock
    return genre_dao


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)

        assert genre is not None
        assert genre.id == 1

    def test_get_all(self):
        genres = self.genre_service.get_all()

        assert len(genres) > 0

    def test_create(self):
        genre_data = {
            "name": "Max",
        }

        genre =self.genre_service.create(genre_data)

        assert genre.id is not None

    def test_delete(self):
        self.genre_service.delete(1)

    def test_update(self):
        genre_data = {
            "id": 3,
            "name": "Max",
        }

        self.genre_service.update(genre_data)