from unittest.mock import MagicMock

import pytest

from dao.model.movie import Movie
from dao.movie import MovieDAO
from service.movie import MovieService
from setup_db import db


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(db.session)

    doctor_sleep = Movie(
        id=1,
        title='doctor_sleep',
        description='Прошло много лет с тех пор, как мальчик с паранормальными способностями Дэнни Торранс пережил кошмарный сезон в отеле «Оверлук», где стал свидетелем безумия и гибели своего отца. Повзрослев, Дэн вёл жизнь маргинала-алкоголика, а теперь пытается завязать и даже устроился на работу в дом престарелых. Там он безошибочно определяет, кому из постояльцев подошла очередь покинуть этот мир, за что и получил прозвище Доктор Сон. Однажды с Дэном устанавливает связь невероятно одарённая «сияющая» девочка Абра. Вскоре ей потребуется его помощь, чтобы противостоять членам организации «Истинный узел» – группы охотников за особенными детьми.',
        trailer='https://www.youtube.com/watch?v=bkhjbv9UbPI',
        year=2019,
        rating=7.3,
        genre_id=1,
        director_id=1,
    )
    cheburashka = Movie(
        id=1,
        title='cheburashka',
        description='Иногда, чтобы вернуть солнце и улыбки в мир взрослых, нужен один маленький ушастый герой. Мохнатого непоседливого зверька из далекой апельсиновой страны ждут удивительные приключения в тихом приморском городке, где ему предстоит найти себе имя, друзей и дом',
        trailer='https://www.youtube.com/watch?v=x1qvJL7NF9s',
        year=2022,
        rating=7.4,
        genre_id=2,
        director_id=2,
    )
    cruella = Movie(
        id=1,
        title='cruella',
        description='Великобритания, 1960-е годы. Эстелла была необычным ребёнком, и особенно трудно ей было мириться со всякого рода несправедливостью. Вылетев из очередной школы, она с мамой отправляется в Лондон. По дороге они заезжают в особняк известной модельерши по имени Баронесса, где в результате ужасного несчастного случая мама погибает. Добравшись до Лондона, Эстелла знакомится с двумя мальчишками — уличными мошенниками Джаспером и Хорасом.',
        trailer='https://www.youtube.com/watch?v=9F2-eR2dfMY',
        year=2021,
        rating=7.6,
        genre_id=3,
        director_id=3,
    )


    movie_dao.get_one = MagicMock(return_value=doctor_sleep)
    movie_dao.get_all = MagicMock(return_value=[doctor_sleep, cheburashka, cruella])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.delete = MagicMock
    movie_dao.update = MagicMock
    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id == 1
        assert movie.title == 'doctor_sleep'

    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert len(movies) > 0

    def test_create(self):
        movie_data = {
            "title": "Nurnberg",
        }

        movie =self.movie_service.create(movie_data)

        assert movie.id is not None

    def test_delete(self):
        self.movie_service.delete(1)

    def test_update(self):
        movie_data = {
            "id": 3,
            "title": "nurnberg_get",
        }

        self.movie_service.update(movie_data)